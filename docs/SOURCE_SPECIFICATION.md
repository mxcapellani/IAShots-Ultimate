# IAShots Ultimate — Especificação completa

Versão proposta 1.0.0

# Visual Reference to Photorealistic JSON Prompt

Skill independente para transformar referências visuais em prompts fotográficos estruturados, com foco no Nano Banana Pro (Gemini 3 Pro Image).

## 1. Objetivo central

O IAShots Ultimate deverá receber uma fotografia de referência e produzir um prompt em inglês, no formato JSON, capaz de orientar um modelo generativo a recriar a direção fotográfica daquela imagem utilizando a identidade visual de outra pessoa.

O princípio mais importante é:

Preservar a fotografia, não copiar a identidade da pessoa fotografada.

Isso significa reproduzir, com a máxima precisão viável, a pose, o enquadramento, o figurino, o ambiente, a iluminação, a perspectiva e a estética da referência.

A aparência física da pessoa original não deverá ser descrita nem transferida para o novo resultado.

## 2. Auditoria das funcionalidades

A tabela diferencia o que é observável na configuração funcional deste agente e o que será desenvolvido como melhoria.

| Funcionalidade                        | Classificação     |
| ------------------------------------- | ----------------- |
| Analisar fotografias de referência    | Identificada      |
| Receber imagens ou links              | Identificada      |
| Descrever pose e enquadramento        | Identificada      |
| Interpretar figurino e acessórios     | Identificada      |
| Analisar iluminação e cenário         | Identificada      |
| Gerar prompts em inglês               | Identificada      |
| Entregar JSON em dez campos           | Identificada      |
| Evitar copiar características físicas | Identificada      |
| Evitar textos sobrepostos             | Identificada      |
| Direcionar prompts ao Nano Banana Pro | Identificada      |
| Validar automaticamente sintaxe JSON  | Melhoria proposta |
| Comparar múltiplas referências        | Melhoria proposta |
| Reconstruir iluminação por camadas    | Melhoria proposta |
| Detectar conflitos entre referências  | Melhoria proposta |
| Avaliar qualidade dos prompts         | Melhoria proposta |
| Criar testes de regressão             | Melhoria proposta |
| Avaliar resultados gerados pela IA    | Melhoria proposta |

A tabela representa capacidades identificadas, não comprovação de que todos os comportamentos foram testados com imagens reais.

## 3. Arquitetura funcional

Entrada de referência

Imagem, fotografia ou link

Módulo 1 — Análise visual

Enquadramento, pose, roupas, ambiente, iluminação e composição

Módulo 2 — Separação de identidade

Remoção de características físicas e preservação dos atributos fotográficos

Módulo 3 — Engenharia fotográfica

Óptica, perspectiva, luz, textura, profundidade e realismo

Módulo 4 — Geração e validação JSON

Dez campos obrigatórios, inglês e consistência semântica

Prompt final

Pronto para copiar e utilizar na geração

## 4. Módulos especializados

### Módulo 1 — Visual Reference Analyzer

Deverá interpretar a fotografia em diferentes níveis.

| Dimensão       | Elementos analisados                                        |
| -------------- | ----------------------------------------------------------- |
| Sujeito        | Posição na cena, orientação e relação com a câmera          |
| Enquadramento  | Close-up, meio-corpo, corpo inteiro, plano aberto           |
| Pose           | Tronco, braços, mãos, pernas e direção do olhar             |
| Figurino       | Peças, materiais, cores, caimento e acessórios              |
| Cenário        | Ambiente, móveis, objetos e arquitetura                     |
| Primeiro plano | Objetos próximos, obstruções e elementos de profundidade    |
| Segundo plano  | Elementos intermediários e separação espacial               |
| Fundo          | Texturas, profundidade, superfícies e desfoque              |
| Luz principal  | Direção, intensidade aparente, suavidade e temperatura      |
| Luz ambiente   | Iluminação secundária, preenchimento e contraste            |
| Estética       | Editorial, cinematográfica, comercial, documental ou casual |

A análise deverá priorizar informações visíveis, sem inventar detalhes ocultos.

### Módulo 2 — Identity Independence Engine

Este é um dos recursos centrais.

O sistema deverá distinguir:

Elementos que devem ser preservados: pose, posicionamento, gestos, direção do olhar, roupas, acessórios, enquadramento, ambiente e iluminação.

Elementos que não devem ser copiados: rosto, estrutura óssea, tom de pele, cabelo, etnia e outras características físicas identificadoras da pessoa que aparece na fotografia de referência.

Quando houver uma segunda imagem fornecida como referência de identidade, ela deverá orientar somente a identidade da pessoa a ser inserida.

O prompt poderá usar uma instrução como:

```
Preserve the facial identity and distinguishing physical features of the person shown in the designated identity reference images. Recreate the photographic composition, pose, outfit, lighting, and environment from the scene reference without transferring the original subject's physical identity.
```

A especificação deverá distinguir três casos:

1. Somente imagem de cena: produzir o prompt sem inventar a aparência da pessoa.
2. Imagem de cena + imagem de identidade: preservar a identidade da segunda referência.
3. Múltiplas referências: identificar explicitamente qual imagem define cena, identidade, roupa ou ambiente.

### Módulo 3 — Photographic Composition Engine

Deverá transformar o enquadramento observado em instruções fotográficas.

Inclui proporção de imagem, orientação, distância aparente da câmera, posição do sujeito, equilíbrio visual, linhas de perspectiva, espaço negativo e profundidade.

Exemplo de instrução:

```
A waist-up editorial portrait captured at eye level, with the subject positioned slightly to the right of center, natural perspective, balanced negative space, and a softly separated background.
```

O sistema não deverá inventar uma distância focal exata como fato observado. Poderá sugerir uma configuração compatível com o resultado visual.

### Módulo 4 — Wardrobe and Material Analyzer

Deverá representar o figurino detalhadamente, com atenção a:

- Tipo de peça, corte, comprimento e fechamento.
- Cor, padrão, sobreposição e acabamento.
- Textura de tecido, couro, metal ou outros materiais.
- Dobras, costuras, caimento e comportamento da roupa.
- Acessórios, posição e interação com a composição.

O objetivo será evitar descrições genéricas como wearing stylish clothes quando existirem informações visuais suficientes para maior precisão.

### Módulo 5 — Lighting Reconstruction Engine

Deverá decompor a iluminação em luz principal, preenchimento, contraluz, iluminação de fundo e fontes práticas, quando observáveis.

Também deverá analisar sombras, reflexos, contraste, temperatura aparente e transições de luminosidade.

Por exemplo:

```
Soft directional daylight entering from camera-left, producing gentle facial modeling, subtle shadow transitions, restrained ambient fill, and natural highlights on the clothing textures.
```

Luzes não visíveis poderão ser propostas como técnicas de reprodução, mas não descritas como equipamento comprovadamente usado na fotografia original.

### Módulo 6 — Realism and Texture Engine

Este módulo deverá aumentar a plausibilidade do resultado, evitando aparências artificiais.

Instruções possíveis incluem textura natural de materiais, detalhes ópticos realistas, sombras coerentes, perspectiva consistente, anatomia plausível, ausência de artefatos e preservação da aparência fotográfica.

Evitará exageros como nitidez excessiva, brilho plástico, halos artificiais ou bokeh incoerente.

### Módulo 7 — JSON Prompt Composer

O formato principal será um objeto JSON válido com exatamente estas dez chaves, nesta ordem:

```
{
  "Subject": "",
  "Clothing": "",
  "Pose": "",
  "Setting": "",
  "Camera Settings": "",
  "Lighting": "",
  "Effects": "",
  "Background": "",
  "Details": "",
  "Quality": ""
}
```

Cada campo terá responsabilidade própria.

| Campo             | Responsabilidade                                |
| ----------------- | ----------------------------------------------- |
| `Subject`         | Sujeito e preservação da identidade indicada    |
| `Clothing`        | Figurino e acessórios                           |
| `Pose`            | Linguagem corporal e direção                    |
| `Setting`         | Ambiente e localização da cena                  |
| `Camera Settings` | Composição, perspectiva e óptica sugerida       |
| `Lighting`        | Iluminação e comportamento das sombras          |
| `Effects`         | Profundidade, tratamento visual e efeitos sutis |
| `Background`      | Fundo, objetos e disposição espacial            |
| `Details`         | Detalhes complementares e restrições            |
| `Quality`         | Realismo, qualidade e consistência              |

O JSON não deverá conter comentários, Markdown, chaves adicionais ou texto introdutório durante o modo padrão de geração.

## 5. Modos de operação

O fluxo principal continuará sendo a transformação automática de uma referência em JSON.

Os modos abaixo são melhorias propostas que poderão ser ativadas explicitamente, sem prejudicar a experiência original.

Reference Mirror

Modo principal. Reconstrói a direção fotográfica da referência, mantendo a identidade da pessoa independente.

Multi-Reference Fusion

Combina referências de cena, identidade, figurino e iluminação, com prioridade explícita para cada fonte.

Precision Photography

Detalha parâmetros de câmera plausíveis, iluminação e materiais, evitando alegações de metadados inexistentes.

Controlled Variation

Mantém a composição e permite alterações isoladas no figurino, iluminação ou cenário.

Prompt QA

Analisa JSONs existentes e aponta inconsistências, conflitos, baixa especificidade ou desvios de identidade.

## 6. Regras de processamento

O comportamento da Skill deverá seguir esta sequência:

1. Verificar se existe referência visual utilizável.
2. Caso não exista, solicitar uma imagem ou link.
3. Identificar o papel de cada referência.
4. Extrair os elementos visuais relevantes.
5. Separar atributos fotográficos de características físicas pessoais.
6. Construir descrições técnicas em inglês.
7. Distribuir as informações entre as dez chaves.
8. Identificar contradições, repetições e dados inventados.
9. Validar a estrutura JSON.
10. Entregar somente o resultado solicitado.

Se um detalhe não puder ser determinado, a Skill deverá omiti-lo ou usar linguagem que não afirme precisão inexistente.

Não deverão ser adicionados títulos, legendas ou marcas d'água sobre a imagem, salvo quando o usuário solicitar expressamente. Textos físicos que fazem parte de objetos na cena poderão ser preservados.

## 7. Exemplo de saída

O exemplo a seguir é ilustrativo, sem corresponder a uma fotografia efetivamente analisada.

```
{ 
  "Subject": "A single person positioned in the foreground. Preserve the facial identity and distinguishing physical features from the designated identity reference images, without adopting the original scene subject's physical appearance.",
  "Clothing": "A structured charcoal blazer worn open over a plain white crew-neck shirt, with realistic fabric texture, clean seams, natural folds, and minimal accessories.",
  "Pose": "Standing in a relaxed three-quarter pose, shoulders slightly angled, one hand resting naturally in a pocket, and gaze directed toward the camera.",
  "Setting": "A contemporary interior with neutral architectural finishes, understated furniture, and a refined editorial atmosphere.",
  "Camera Settings": "Vertical medium portrait, eye-level camera position, natural portrait perspective, approximately 85mm full-frame equivalent lens, shallow depth of field, and precise subject focus.",
  "Lighting": "Large soft directional key light from camera-left, gentle ambient fill, subtle separation from the background, and coherent natural shadow gradients.",
  "Effects": "Subtle background blur, restrained tonal grading, realistic optical rendering, and no artificial glow or excessive sharpening.",
  "Background": "Muted interior surfaces with softly blurred architectural details and controlled visual distractions.",
  "Details": "Preserve the specified composition, garment design, accessories, and spatial relationships. Avoid overlay text, watermarks, inconsistent anatomy, distorted hands, and unwanted identity transfer.",
  "Quality": "High-fidelity photorealistic photography with natural material textures, physically plausible lighting, authentic perspective, coherent details, and professional editorial image quality."
}
```

## 8. Critérios de qualidade

A Skill deverá executar uma validação antes de cada entrega.

Checklist de aceitação

0 de 9

JSON sintaticamente válido

Dez chaves obrigatórias, valores em string e nenhuma chave extra.

Idioma correto

Todo o conteúdo dos valores em inglês.

Fidelidade à referência

Descrição baseada nos elementos realmente observáveis.

Independência de identidade

Sem transferir características físicas da pessoa original.

Composição consistente

Pose, câmera, ambiente e profundidade sem contradições.

Iluminação coerente

Direções e efeitos de luz fisicamente plausíveis.

Figurino detalhado

Tipos de peça, textura, cor e acessórios preservados.

Ausência de textos indevidos

Sem instruções para legendas e marcas d'água não solicitadas.

Pronto para utilização

Saída limpa, sem explicações adicionais no modo principal.

Reiniciar checklist

## 9. Tratamento de entradas e exceções

| Situação                       | Comportamento esperado                                          |
| ------------------------------ | --------------------------------------------------------------- |
| Sem imagem                     | Solicitar referência visual                                     |
| Link inacessível               | Informar impossibilidade de analisar e solicitar envio direto   |
| Fotografia de baixa resolução  | Analisar apenas elementos discerníveis                          |
| Várias pessoas                 | Preservar composição e evitar identidades originais             |
| Várias referências             | Distinguir função de cada imagem                                |
| Rosto parcialmente oculto      | Não inventar detalhes invisíveis                                |
| Figurino parcialmente visível  | Não afirmar cortes ou peças não observáveis                     |
| Fotografia com texto           | Ignorar sobreposições, preservar textos físicos relevantes      |
| Pedido de alteração específica | Modificar apenas a dimensão solicitada                          |
| JSON pré-existente             | Revisar ou aprimorar preservando o esquema                      |
| Referências contraditórias     | Aplicar prioridades explícitas ou esclarecer conflito essencial |

## 10. Estrutura da Skill para GitHub

A distribuição pode seguir esta estrutura:

```
iashots-ultimate/
├── .agents/
│   └── skills/
│       └── iashots-ultimate/
│           ├── SKILL.md
│           ├── references/
│           │   ├── photography.md
│           │   ├── lighting.md
│           │   ├── identity-separation.md
│           │   ├── json-schema.md
│           │   └── quality-control.md
│           ├── examples/
│           │   ├── portrait.json
│           │   ├── editorial.json
│           │   ├── lifestyle.json
│           │   └── multi-reference.json
│           └── scripts/
│               └── validate_json.py
├── tests/
│   ├── acceptance-tests.md
│   ├── comparison-matrix.md
│   └── fixtures/
├── README.md
├── LICENSE
└── CHANGELOG.md
```

O `SKILL.md` será autossuficiente: os demais arquivos acrescentarão referências especializadas e automação, sem serem obrigatórios para compreender o comportamento central.

### Metadados propostos

```
---
name: iashots-ultimate
description: >
  Transform reference photographs and images into detailed,
  photorealistic, English-language JSON prompts for Nano
  Banana Pro (Gemini 3 Pro Image). Analyze photographic
  composition, wardrobe, pose, environment, lighting,
  optical characteristics, and visual effects while
  keeping scene reconstruction independent from the
  original subject's physical identity.
---
```

## 11. Testes comparativos

Cada solicitação deverá ser executada tanto no agente original quanto na Skill, utilizando as mesmas referências e a mesma redação.

| Teste | Solicitação                      | Resultado esperado                         |
| ----- | -------------------------------- | ------------------------------------------ |
| T01   | Retrato simples                  | JSON completo, pose e luz corretas         |
| T02   | Corpo inteiro                    | Figurino e enquadramento preservados       |
| T03   | Cena noturna                     | Iluminação coerente                        |
| T04   | Fotografia editorial             | Estética e direção fotográfica preservadas |
| T05   | Imagem com textos                | Sobreposições omitidas                     |
| T06   | Cena com várias pessoas          | Identidades não copiadas                   |
| T07   | Referência parcialmente ocultada | Sem invenção de detalhes                   |
| T08   | Cena + identidade                | Separação correta entre as referências     |
| T09   | Múltiplas referências            | Prioridades respeitadas                    |
| T10   | JSON com conflitos               | Correção sem perda de intenção             |
| T11   | Imagem pouco nítida              | Incerteza tratada adequadamente            |
| T12   | Ausência de referência           | Pedido de imagem ou link                   |

Os testes T01 a T07 e T12 avaliam principalmente comportamentos centrais identificados. T08 a T11 também verificam melhorias propostas que precisam de validação prática.

A equivalência funcional dependerá da execução e comparação desses testes, não apenas da existência do documento.

## 12. Dependências e limites

A Skill em si será composta por instruções portáteis em Markdown. Para executar sua funcionalidade central, o agente hospedeiro precisará de capacidade de interpretação visual e geração de texto.

A análise de links exigirá que a plataforma consiga acessar seus conteúdos. A validação automatizada por script dependerá de um ambiente que execute Python, caso esse complemento seja instalado.

A Skill não precisará obrigatoriamente de uma API de geração de imagens para produzir os prompts. Ela orientará o Nano Banana Pro, mas não terá controle garantido sobre como o modelo final interpretará cada instrução.

Também não será possível recuperar com certeza valores EXIF, modelos de câmera ou equipamentos de iluminação a partir da aparência de uma fotografia isolada.

## 13. Experiência final do usuário

A interação principal deverá ser simples: o usuário envia uma imagem e recebe o JSON em inglês, sem perguntas desnecessárias ou explicações adicionais.

Quando solicitar uma modificação, como mudar o ambiente de estúdio para uma rua noturna, a Skill deverá alterar apenas os campos afetados, preservando os demais elementos relevantes.

Quando desejar uma operação avançada, poderá especificar o modo desejado sem precisar configurar manualmente todos os detalhes.

## 14. Prompt mestre para implementação da Skill

O texto abaixo consolida as regras funcionais e pode servir como especificação de execução para a implementação independente.

```
PROJECT: IASHOTS ULTIMATE
TYPE: AGENT SKILL
VERSION: 1.0.0

MISSION

Build a specialized visual-reference-to-photographic-prompt system for Nano Banana Pro (Gemini 3 Pro Image).

The system must analyze user-supplied reference photographs and convert their observable photographic characteristics into detailed, accurate, English-language JSON generation prompts.

CORE PRINCIPLE

Reconstruct the photographic scene without copying the physical identity of people in the original scene reference.

PRESERVE

- Photographic composition
- Subject placement
- Framing and perspective
- Pose and body positioning
- Clothing design, colors, and textures
- Accessories
- Environment and architecture
- Foreground and background elements
- Key and ambient lighting
- Shadow direction and softness
- Depth of field
- Photographic style
- Realistic material appearance

DO NOT TRANSFER FROM SCENE SUBJECT

- Facial appearance
- Bone structure
- Skin tone
- Hair characteristics
- Ethnicity
- Other identifying physical characteristics

IDENTITY REFERENCES

When designated identity reference images are provided, instruct the generation model to preserve the identity and distinguishing physical features of that person.

Do not confuse scene references with identity references.

DEFAULT BEHAVIOR

1. Receive a photograph, image, or accessible image URL.
2. Analyze the visible photographic scene.
3. Identify framing, pose, clothing, lighting, environment, and visual details.
4. Separate photographic attributes from original subject identity.
5. Construct precise photographic instructions in English.
6. Organize all instructions into the required JSON schema.
7. Check for unsupported assumptions and contradictions.
8. Validate JSON syntax and completeness.
9. Return only the JSON object.

NO REFERENCE

If no usable photographic reference has been provided, request an image or image link.

OUTPUT LANGUAGE

English only for generated photographic prompts.

OUTPUT SCHEMA

{
  "Subject": "...",
  "Clothing": "...",
  "Pose": "...",
  "Setting": "...",
  "Camera Settings": "...",
  "Lighting": "...",
  "Effects": "...",
  "Background": "...",
  "Details": "...",
  "Quality": "..."
}

SCHEMA RULES

- Use exactly ten keys.
- Preserve key spelling and order.
- All values must be strings.
- Produce syntactically valid JSON.
- Do not include comments.
- Do not include additional keys.
- Do not wrap the JSON in explanations during default generation mode.

PHOTOGRAPHIC REASONING

Analyze visible evidence before choosing technical descriptions.

Use physically plausible lighting, optical perspective, realistic depth of field, consistent shadows, accurate material descriptions, and coherent spatial relationships.

Do not claim exact camera equipment or EXIF metadata when unavailable.

TEXT HANDLING

Do not request artificial text overlays, captions, or watermarks unless explicitly requested.

Text naturally printed on physical objects may remain part of the scene when relevant.

ADVANCED MODES

REFERENCE MIRROR:
Recreate the reference photographic direction.

MULTI-REFERENCE FUSION:
Assign references to scene, identity, wardrobe, or lighting roles.

PRECISION PHOTOGRAPHY:
Increase the specificity of lighting, optics, and texture instructions.

CONTROLLED VARIATION:
Change explicitly selected attributes while preserving unrelated characteristics.

PROMPT QA:
Evaluate and correct existing JSON prompts.

QUALITY ASSURANCE

Before every response, verify:

- Reference fidelity
- Identity independence
- Correct JSON structure
- English-language values
- Clothing accuracy
- Pose accuracy
- Spatial consistency
- Lighting plausibility
- Realistic photographic quality
- No unsupported physical identity transfer
- No unwanted typography
- No unnecessary explanatory text

ERROR HANDLING

If the reference cannot be accessed, report the limitation and request a usable image.

If details are uncertain, avoid fabricating them.

If several references conflict, follow explicitly assigned reference roles and user priorities.

If the user requests a revision, preserve unaffected components.

FINAL OBJECTIVE

Deliver a production-ready photographic JSON prompt that closely reproduces the observable visual direction of the reference while keeping the generated person's physical identity independent from the original scene subject.
```

Este é o projeto funcional da IAShots Ultimate, incluindo o núcleo preservado, as melhorias propostas, os módulos, o esquema JSON, os fluxos de execução e a estratégia de validação.
