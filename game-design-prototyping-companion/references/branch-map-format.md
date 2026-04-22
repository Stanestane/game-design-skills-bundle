# Branch Map Format

Use a simple JSON object with `nodes` and `edges`.

## Structure

```json
{
  "title": "Prototype branch map",
  "nodes": [
    {
      "id": "P0",
      "label": "Grouped request board",
      "state": "baseline",
      "note": "Initial prototype to test readability"
    },
    {
      "id": "P1",
      "label": "Conflict-based board",
      "state": "promising",
      "note": "Players noticed tradeoffs faster"
    }
  ],
  "edges": [
    {
      "from": "P0",
      "to": "P1",
      "label": "What if requests compete?"
    }
  ]
}
```

## Node fields
- `id`: short unique ID
- `label`: visible node title
- `state`: baseline | promising | branch-trigger | dead-end | parked | production-candidate
- `note`: optional short explanation

## Edge fields
- `from`: source node ID
- `to`: target node ID
- `label`: short branch reason or question

## Layout note
The bundled script uses a simple top-to-bottom tree-like layout.
It is not a full graph engine. Keep maps small to medium for readability.
