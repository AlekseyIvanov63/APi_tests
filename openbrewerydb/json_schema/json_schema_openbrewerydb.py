SCHEMA_META = {
    "type": "object",
    'properties':
        {"total": {"type": 'string'},
         "page": {"type": 'string'},
         "per_page": {"type": 'string'}
         },
    "required": ["total", "page", "per_page"],
    "additionalProperties": False
}
