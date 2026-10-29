# JSON contract

Exactly ten keys in order: Subject, Clothing, Pose, Setting, Camera Settings, Lighting, Effects, Background, Details, Quality. Every value is a string. No comments, trailing commas, duplicate keys, NaN, extra keys, explanatory text or Markdown wrapper in default generation.

Subject controls role and identity source; Clothing garments; Pose body orientation/action; Setting environment; Camera Settings framing/perspective/optical suggestions; Lighting key/ambient/shadows; Effects restrained treatment; Background spatial context; Details remaining constraints; Quality physical and photographic goals.

Use scripts/validate_json.py to parse a saved raw object. JSON Schema checks property/type constraints, while the Python validator additionally checks insertion order and duplicates. Neither proves English fluency, visual fidelity, factual accuracy or facial identity.
