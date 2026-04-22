from __future__ import annotations
import json
import sys
from pathlib import Path
from collections import defaultdict, deque

STATE_COLORS = {
    'baseline': '#5B8DEF',
    'promising': '#2BAE66',
    'branch-trigger': '#F2A93B',
    'dead-end': '#D64545',
    'parked': '#8B7CF6',
    'production-candidate': '#1F8EFA',
}

BOX_W = 220
BOX_H = 64
X_GAP = 70
Y_GAP = 90
MARGIN = 40


def esc(text: str) -> str:
    return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;'))


def wrap(text: str, width: int = 26):
    words = text.split()
    lines = []
    cur = []
    cur_len = 0
    for w in words:
        if cur_len + len(w) + (1 if cur else 0) <= width:
            cur.append(w)
            cur_len += len(w) + (1 if cur_len else 0)
        else:
            lines.append(' '.join(cur))
            cur = [w]
            cur_len = len(w)
    if cur:
        lines.append(' '.join(cur))
    return lines[:3]


def main(inp: str, out: str):
    data = json.loads(Path(inp).read_text(encoding='utf-8'))
    nodes = {n['id']: n for n in data.get('nodes', [])}
    edges = data.get('edges', [])
    children = defaultdict(list)
    indeg = defaultdict(int)
    for e in edges:
        children[e['from']].append(e)
        indeg[e['to']] += 1
        indeg[e['from']] += 0

    roots = [nid for nid in nodes if indeg[nid] == 0] or list(nodes.keys())[:1]

    level = {}
    q = deque((r, 0) for r in roots)
    seen = set()
    while q:
        nid, d = q.popleft()
        if nid in seen:
            continue
        seen.add(nid)
        level[nid] = d
        for e in children.get(nid, []):
            q.append((e['to'], d + 1))

    cols = defaultdict(list)
    for nid, d in level.items():
        cols[d].append(nid)
    for d in cols:
        cols[d].sort()

    positions = {}
    max_col = max(cols) if cols else 0
    max_rows = max((len(v) for v in cols.values()), default=1)
    width = MARGIN * 2 + (max_col + 1) * BOX_W + max_col * X_GAP
    height = MARGIN * 2 + max_rows * BOX_H + (max_rows - 1) * Y_GAP + 80

    for d in sorted(cols):
        for r, nid in enumerate(cols[d]):
            x = MARGIN + d * (BOX_W + X_GAP)
            y = MARGIN + r * (BOX_H + Y_GAP) + 40
            positions[nid] = (x, y)

    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    parts.append('<style>text{font-family:Segoe UI,Arial,sans-serif}.title{font-size:20px;font-weight:700}.label{font-size:14px;font-weight:600}.note{font-size:11px;fill:#333}.edge{font-size:11px;fill:#555}</style>')
    title = esc(data.get('title', 'Prototype Branch Map'))
    parts.append(f'<text x="{MARGIN}" y="28" class="title">{title}</text>')

    for e in edges:
        if e['from'] not in positions or e['to'] not in positions:
            continue
        x1, y1 = positions[e['from']]
        x2, y2 = positions[e['to']]
        sx = x1 + BOX_W
        sy = y1 + BOX_H / 2
        tx = x2
        ty = y2 + BOX_H / 2
        mx = (sx + tx) / 2
        parts.append(f'<path d="M {sx} {sy} C {mx} {sy}, {mx} {ty}, {tx} {ty}" fill="none" stroke="#999" stroke-width="2"/>')
        label = esc(e.get('label', ''))
        if label:
            parts.append(f'<text x="{mx}" y="{(sy + ty) / 2 - 6}" class="edge" text-anchor="middle">{label}</text>')

    for nid, node in nodes.items():
        if nid not in positions:
            continue
        x, y = positions[nid]
        color = STATE_COLORS.get(node.get('state', ''), '#888')
        parts.append(f'<rect x="{x}" y="{y}" width="{BOX_W}" height="{BOX_H}" rx="10" ry="10" fill="#fff" stroke="{color}" stroke-width="3"/>')
        parts.append(f'<text x="{x + 10}" y="{y + 18}" class="note">{esc(nid)} • {esc(node.get("state", ""))}</text>')
        for i, line in enumerate(wrap(node.get('label', ''), 24)):
            parts.append(f'<text x="{x + 10}" y="{y + 38 + i * 16}" class="label">{esc(line)}</text>')

    parts.append('</svg>')
    Path(out).write_text('\n'.join(parts), encoding='utf-8')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python branch_map_svg.py <input.json> <output.svg>')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
