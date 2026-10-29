# IAShots Ultimate

Version 1.0.0 — Visual Reference to Photorealistic JSON Prompt.

Transform photographic references into English JSON prompts while preserving composition, pose, wardrobe, setting and light independently from the original person's physical identity.

## Preserved behaviour
Image or accessible link in; raw JSON out. Exactly ten ordered string fields: Subject, Clothing, Pose, Setting, Camera Settings, Lighting, Effects, Background, Details and Quality. The default output has no Markdown fence, title, comments, introduction or extra keys.

Do not transfer the scene person's face, hair, skin tone, ethnicity or other identifying physical traits. A designated separate identity reference supplies identity; without one, keep it neutral. Exclude unrequested overlays, captions and watermarks; relevant text physically on objects may remain.

## Five modes
Reference Mirror, Multi-Reference Fusion, Precision Photography, Controlled Variation and Prompt QA. Multi-reference, layered lighting, conflict detection and QA are proposed improvements, not empirically demonstrated parity with an original agent.

## Use and installation
Send an actual photograph and request “Reconstruct this scene as JSON”. Assign A as scene and B as identity when applicable. For a controlled variation, specify what changes and what remains fixed. Missing or inaccessible visual input triggers a request for a usable reference.

Copy `.agents/skills/iashots-ultimate/` to the host-supported discovery directory. See [installation](docs/INSTALLATION.md). Publishing to GitHub does not automatically install in ChatGPT.

## Package
[Self-contained nucleus](.agents/skills/iashots-ultimate/SKILL.md), five technique references, four JSON examples, source specification, audit, twelve planned comparative cases, schema, strict validator, regression tests and CI. [Example provenance](examples/README.md).

## Validate
```bash
python -m pip install -r tests/requirements.txt
python tests/validate.py
python tests/test_validator.py
python .agents/skills/iashots-ultimate/scripts/validate_json.py .agents/skills/iashots-ultimate/examples/portrait.json
```
Python 3.9+, PyYAML 6.x and jsonschema 4.x. Initial dependency installation may need network access; validation itself is local and credential-free. The portable output validator uses the Python standard library only. It rejects wrong order, duplicates, extra/missing keys, non-string values, comments and invalid JSON.

## Compatibility and evidence
Nano Banana Pro (Gemini 3 Pro Image) is the target named in the brief, not a claim of current API/version compatibility. The JSON is an instruction format, not an official provider payload. Actual analysis requires host vision and reference access; rendering needs a separate generator and is not automatic.

Structural tests do not prove English fluency, photographic accuracy or identity fidelity. The twelve behavioural comparisons remain not executed. See [audit](docs/AUDIT.md) and [comparison](tests/comparison-matrix.md). The complete supplied brief is preserved in [source specification](docs/SOURCE_SPECIFICATION.md).

## Maintenance and license
Read [CHANGELOG](CHANGELOG.md) and [CONTRIBUTING](CONTRIBUTING.md). MIT, copyright 2026 mxcapellani. Independent implementation with no vendor endorsement.

Em português: reconstruir a fotografia sem copiar a identidade física da pessoa da cena; entregar somente JSON em inglês, com dez campos na ordem definida.
