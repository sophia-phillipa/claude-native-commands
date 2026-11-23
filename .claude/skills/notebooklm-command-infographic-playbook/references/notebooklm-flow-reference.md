# NotebookLM Studio infographic spec for command infographics

How to write the content of one infographic's `blueprint.json` (contract section 3) and how the Studio prompt is built from the recipe. The contract holds the field names and the validation rules; this file says what to write in each field.

## 1. The four zones

| Zone | Blueprint fields | What it shows |
| --- | --- | --- |
| 1 Identidade e gatilho | `command`, `category`, `ui.zone1`, `identity.purpose` | The command as typed, its category on the guide page, and what it is for. |
| 2 Fluxo de execução | `flow.steps` (3 to 5), `flow.edges` | What the command does inside the prompt-and-engine flow, step by step. |
| 3 Conexões e variações | `connections.flags`, `connections.files`, `connections.related`, `ui.zone3` | Arguments, impacted files, related commands from the page. |
| 4 Contraste prático | `contrast.when`, `contrast.pitfalls`, `contrast.example`, `ui.when`, `ui.pitfalls`, `ui.example` | When to use it, the common traps, one literal invocation. |

Zone 4 has no title of its own. The three cards carry the zone: "Quando usar", "Armadilhas comuns", "Exemplo". The contract's `ui` object has no zone 4 key, so the text "Contraste prático" is not in the closed list and is not rendered.

## 2. Zone 1: identity

- `command`: `"/" + slug`, exactly as the card id.
- `category`: the `name` of the `CATEGORIES` entry whose `ids` array holds the slug.
- `identity.purpose`: at most 12 words, one sentence, says what the command gives the user in the flow. It is not a copy of the card's `short`; it can reuse its key terms.

## 3. Zone 2: the flow

Zone 2 explains what the command does inside the flow of the prompt and the engine. It is not the card text. Read the card's `what` and `note` to learn the mechanism, then write the steps as the engine's moves.

| Card says (source) | Flow step says (blueprint) |
| --- | --- |
| "Resume a conversa até aqui e segue com o resumo no lugar do histórico completo." (`what`) | "O motor escreve resumo fiel" (processing) |
| "Libera espaço na janela de contexto" (`why`) | "Sessão segue mais leve" (result) |

Rules:
- 3 to 5 steps. The first step is `layer: input`, the last is `layer: result`; in between, `processing` steps only.
- Each step is one state or one move, with a subject the reader can see: the user's action, the engine's move, the resulting state.
- Edges form a single chain: one edge from each step to the next, `steps.length - 1` edges in total.
- Verbs: one or two lowercase words in the infinitive or 3rd-person present, from what the step does: `motiva`, `executa`, `lê`, `gera`, `reduz`, `injeta`, `zera`, `grava`, `carrega`, `mantém`, `aplica`, `bloqueia`. A new verb is fine if it names the move exactly.
- Do not invent engine behaviour. If a step needs a fact the card and the doc do not show, drop the step or mark the claim UNVERIFIED and keep it out of the blueprint.

## 4. Zone 3: connections and variations

- `connections.flags`: `text` is the literal from the card's `params` (for example `[instruções]`), `label` says what it changes (3 to 7 words). Empty when the card has no params.
- `connections.files`: `text` is a literal file name the command reads or writes, from the card or the doc (`CLAUDE.md`, `.claude/settings.json`); `label` says what changes there. Empty when the card names no file. Never invent a file.
- `connections.related`: `command` is `"/" + <a card id that exists>` (`check-blueprint` enforces it), `label` says how it relates (3 to 7 words). 1 to 3 items, always at least one: every guide command relates to another card. Use the commands the card or the page names; do not add a related command only to fill the zone. Source order (decision E8, 2026-11-23): commands named by the card, its CONTEXTS row or its DOCS row; else another card that names this one (label from that card's text); else the first other id of the same category in `CATEGORIES` order whose card `short` has 3 to 7 words, with that `short` verbatim as the label. Never link by a concept the card only alludes to.

## 5. Zone 4: contrast

- `contrast.when`: 1 to 3 items, each 3 to 7 words, each a situation in which the command helps.
- `contrast.pitfalls`: 1 to 3 items, each 3 to 7 words, each a trap the card's `note` or the doc names.
- `contrast.example`: a literal invocation that starts with the command, copied from the card's `examples` (for example `/compact mantenha testes e decisões`). It is exempt from the word limit.

## 6. Word limits and literal identifiers

Counted on whitespace-separated tokens (contract section 3):

| Field | Limit |
| --- | --- |
| every box label: `flow.steps[].label`, `connections.*[].label`, `contrast.when[]`, `contrast.pitfalls[]` | 3 to 7 words |
| `flow.steps[].label` at 16:9 | at most 5 words recommended (6 or 7 give a `check-blueprint` warning and smaller step text) |
| `identity.purpose` | at most 12 words |
| `contrast.when`, `contrast.pitfalls` | 1 to 3 items each |
| `flow.edges[].verb` | 1 or 2 lowercase words |

Literal identifiers are matched exactly and are exempt from the word limits: `command`, `connections.flags[].text`, `connections.files[].text`, `connections.related[].command`, `contrast.example`. Copy them from the card or the doc, never retype them from memory: a flag `[instruções]` keeps its accent and brackets.

## 7. Language rules

- Infographic text is PT-BR under the current orthographic agreement. The spelling of the agreement in force in Brazil is the reference; this skill did not fetch its text, so the rule is marked UNVERIFIED for its source. When a spelling is in doubt, leave the word out or ask Sophia; do not guess.
- Only terminal syntax stays in English: commands, flags, file names, environment variables and code identifiers (`/compact`, `--model`, `CLAUDE.md`, `.claude/settings.json`).
- No Spanish words and no "portunhol" (mixed Spanish and Portuguese).
- The audit (section 8) checks accents á é í ó ú â ê ô ã õ à, cedilla ç, crase (`à` before a feminine noun where the preposition `a` meets the article `a`, for example "à conversa"), hyphens and agreement of gender and number.

## 8. Barrier 1: the audit before `check-blueprint`

Claude reads every string of the blueprint, one by one, and checks:

1. PT-BR spelling as in section 7.
2. Technical accuracy: each claim matches the card (`what`, `why`, `how`, `params`, `note`, `examples`) and, where the claim depends on behaviour, the doc link (`DOCS[<slug>].url`, with its `note` if present). Read the doc with WebFetch and cite the section; a claim the doc does not show is marked UNVERIFIED and removed from the blueprint.
3. Literal identifiers equal the card's spelling.
4. Limits of section 6 hold.

Fix the strings, then run `check-blueprint <slug>` and confirm exit 0. Then the blueprint is frozen: no later step changes its strings. A string found wrong after this point ends the run: report it to Sophia, then restart from step 2 with a new Barrier 1.

## 9. Worked example: the reviewed `/compact` blueprint

This is the seed from the contract, reviewed. Use it to see the shape, not as a template to copy text from.

```json
{
  "version": 1,
  "slug": "compact",
  "command": "/compact",
  "category": "Contexto e memória",
  "aspect": "16:9",
  "ui": {
    "zone1": "Identidade e gatilho",
    "zone2": "Fluxo de execução",
    "zone3": "Conexões e variações",
    "when": "Quando usar",
    "pitfalls": "Armadilhas comuns",
    "example": "Exemplo"
  },
  "identity": { "purpose": "Resume a conversa e libera contexto." },
  "flow": {
    "steps": [
      { "id": "s1", "layer": "input", "label": "A conversa enche a janela" },
      { "id": "s2", "layer": "input", "label": "Você digita /compact com instruções" },
      { "id": "s3", "layer": "processing", "label": "O motor lê o histórico" },
      { "id": "s4", "layer": "processing", "label": "O motor escreve resumo fiel" },
      { "id": "s5", "layer": "result", "label": "Sessão segue mais leve" }
    ],
    "edges": [
      { "from": "s1", "to": "s2", "verb": "motiva" },
      { "from": "s2", "to": "s3", "verb": "executa" },
      { "from": "s3", "to": "s4", "verb": "gera" },
      { "from": "s4", "to": "s5", "verb": "reduz" }
    ]
  },
  "connections": {
    "flags": [ { "text": "[instruções]", "label": "Diz o que o resumo preserva" } ],
    "files": [],
    "related": [
      { "command": "/context", "label": "Mede quanto contexto sobrou" },
      { "command": "/autocompact", "label": "Ajusta a compactação automática" },
      { "command": "/clear", "label": "Recomeça com contexto vazio" }
    ]
  },
  "contrast": {
    "when": [ "Perto do limite da sessão", "Antes da compactação automática" ],
    "pitfalls": [ "Sem instruções, detalhes podem sumir", "Mensagens exatas viram resumo" ],
    "example": "/compact mantenha testes e decisões"
  }
}
```

Why it passes the rules: the flow starts at `input` and ends at `result`; four edges chain five steps; every label has 3 to 7 words (the shortest, "Sessão segue mais leve", has 4); `identity.purpose` has 6 words; the flag and the related commands exist in the card data; the example starts with `/compact`.

## 10. Studio prompt and later attempts

Recipe of record (D9): NotebookLM Studio, Infográfico, idioma português (Brasil), Paisagem, Instrutivo, Conciso, and only the two notes `nota.md` and `roteiro.md` as sources. The prompt is the one below, from the /compact pilot runs (their log stays local under `work/notebooklm-tests/`), with the command name replaced by `<slug>`. Paste it unchanged. Its note titles must match the notes written in `SKILL.md` step 3 (`Roteiro /<slug>` and `/<slug>: descrição completa`).

```
Infográfico para o comando /<slug> usando EXCLUSIVAMENTE os textos curtos e ortograficamente revisados da nota "Roteiro /<slug>", sem adicionar frases longas nem alterar a grafia das palavras em PT-BR. A ideia do infográfico é explicar a ação do comando dentro do fluxo de prompt e do motor além de repetir os dados do cartão. Use o visual mais técnico possível: as cinco etapas do fluxo em ordem, da entrada ao resultado, com os verbos entre elas. Telas e painéis ilustrados não mostram valores de exemplo (números de versão, nomes de modelo, contas, IDs ou estados): use só textos da nota "Roteiro /<slug>" ou nenhum texto. Não escreva palavras que não estejam na nota "Roteiro /<slug>", em inglês ou em português: escalas, relatórios e etiquetas de status nos desenhos ficam sem texto.
```

- The prompt says "as cinco etapas" for a five-step flow. For a blueprint with 3 or 4 steps, replace only that number word with "três" or "quatro" (decision E7, 2026-11-23, batch progress dossier); every other word stays unchanged.
- The second-to-last sentence (decision E13) stops Studio from filling mock screens with invented values; without it, /status attempt 1 showed a made-up version, model and account.
- The last sentence (decision E15) was the /code-review attempt-2 fix ("REPORT", "BAIXO MÉDIO ALTO" and "PENDENTE" on attempt 1); since the pilot approval it is part of attempt 1 for every command.
- Build the prompt by script from the blueprint (slug and step-count word), and read it back from the Studio box by length and hash before generating.

### 10.1 Attempts 2 and 3: a fresh generation with one more sentence

A Studio output has no correction input: its ⋮ menu offers only Compartilhar, Renomear, Baixar, Ver comando e fontes, Abrir em uma nova guia and Excluir (observed 2026-11-23). So attempts 2 and 3 are fresh generations with the same notes and recipe, and the new output lists as the first row.

For attempt 2, append one more sentence to the prompt above that names the class of the audit errors still seen, not each wrong word: for example, "Não escreva títulos, legendas nem etiquetas em inglês." or "Os desenhos não levam números, nomes de arquivo nem nomes de modelo."

For attempt 3, tighten that sentence once more for what attempt 2 still shows. Labels are not shortened or rewritten in these runs: blueprint version 1 has no field that allows it. A label that still fails after attempt 3 ends the run (`SKILL.md` step 8).
