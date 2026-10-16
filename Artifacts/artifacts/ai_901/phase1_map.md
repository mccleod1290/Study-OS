topic: Microsoft Azure AI Fundamentals, exam AI-901
slug: ai_901
target: phase1_target.md (course, 16 transcripts in user-input-learning-text/ai-901/, plus the official study guide)
study_mode: course
size: 10 domains, 52 topics, 20 anchors (7 exam skill groups X1 to X7, 13 lab checks L1 to L13). Above the 50 node guide. Phase 2 splits by domain (rule: .rules/phase-order-and-coverage.md, section 3). He decides.

domains (module order of the course; exam area in brackets):
  1. AI concepts and responsible AI (identify AI concepts, 40 to 45 percent). Exam shape, AI and ML, workloads, assistant versus agent, six principles, principles as controls.
  2. Azure, Entra and Foundry (prerequisite for the implement area). Tenant, subscription, resource group, Foundry resource and project, portal map.
  3. How generative AI models work (model components). LLM and SLM, tokens, system and user prompt, parameters, embeddings and attention, multimodal versus multimodel.
  4. Models, deployment and guardrails (model components and configurations). Catalog, deploy, deployment types, PTU and priority, guardrails, agent guardrails.
  5. Calling Foundry from code (implement, 55 to 60 percent). Endpoint and REST, SDK, chat client code, Completions versus Responses, keys, Entra tokens, managed identity, switching keys off.
  6. Agents (implement). Prompt versus hosted, tools and MCP, knowledge and Azure AI Search, portal to client app, approval and identity, multi-agent.
  7. NLP and Azure Language (workloads, then implement text). Tasks, model versus Language, features and code, preprocessing.
  8. Speech (workloads, then implement speech). STT and TTS, Azure Speech three ways, Voice Live, pipelines.
  9. Computer vision and generation (workloads, then implement vision). Vision tasks, multimodal prompts, image and video generation, diffusion, CNN versus ViT.
  10. Information extraction (workloads, then implement extraction). OCR, field extraction, Content Understanding analyzers, audio and video.

prerequisites (stated by him in the spawn prompt, not drilled, so not acquired):
  - Cloud basics, HTTP, REST, JSON, auth. Stated.
  - Python at reading level. Assumed (A2 in phase1_context.md). The study guide asks for Python syntax.
  - An Azure subscription or trial for the labs. Assumed (A3).
  - A modern browser, ideally with a GPU, for the browser labs L1, L3, L5, L7, L9, L11. Assumed (A5).

acquired: (empty. He was not drilled. Doing a lab by clicking is exposure, not skill.)

order:
  - foundation: d1a d1b d1c, d2a d2b, d3a d3b, d4a d4b, d5a, d6a, d7a, d8a, d9a, d10a
  - core: the rest, in domain order. Do L2 first: the project, the endpoint, the key and the Entra switch are the base of every later lab.
  - dive: d1e, d4f, d5h, d6e, d6f, d7d, d8d, d9e, d10d

anchors (gold badge in the map): see controls in phase1_mindmap.json.
  - X1 to X7 are the seven skill groups of the study guide (official).
  - L1 to L13 are hands-on checks. L1 to L12 come from the course labs (episodes 2 to 13). L13 comes from the cram demo. The Learn exercise pages were not opened. The steps come from the videos.

grade rule: node grade = grade of its main claim (.rules/grounding-and-confidence.md). A weaker side claim is named in the note. The tally: grade 5 = 11 nodes, grade 4 = 22, grade 3 = 18, grade 2 = 0, grade 1 = 1 (d10d, an open question).

| id | node | grade | note |
|---|---|---|---|
| d1a | Exam shape and weights | 5 | weights and pass mark: study guide. Multiple choice and no penalty: video only (3) |
| d1b | AI, ML and workloads | 4 | workload names: study guide. Definitions: videos |
| d1c | Assistant versus agent | 4 | study guide names the pair. Contrast: videos |
| d1d | Six responsible AI principles | 4 | names: study guide (5). Examples: Ep 2 (3) |
| d1e | Principles become controls | 4 | joins guardrails, architecture and approval passages. My step |
| d2a | Tenant and Entra ID | 4 | identity types: managed identity page. "Subscription trusts one tenant": cram only (3) |
| d2b | Subscription and resource group | 4 | scope levels and one group per resource: ARM page. "Do not nest": read from four scope levels, plus cram |
| d2c | Foundry resource and project | 5 | architecture page |
| d2d | Portal map and lab hygiene | 3 | video tour only. The portal changes |
| d3a | LLM and SLM | 3 | cram and Ep 4 only |
| d3b | Tokens | 3 | videos only |
| d3c | System and user prompt | 4 | videos plus Responses page example (the page does not define the fields) |
| d3d | Sampling parameters | 3 | videos only. "Newer models may hide temperature": one cram remark |
| d3e | Embeddings and attention | 4 | embedding: Learn page (5). Attention: Transformer abstract (5). Next-token loop: Ep 4 (3) |
| d3f | Multimodal versus multimodel | 3 | cram and Ep 11 only |
| d4a | Model catalog and choice | 3 | "over 10,000 models" is a cram figure |
| d4b | Deploy before use | 4 | deployments exist: deployment page. Name-as-model: videos |
| d4c | Deployment types | 5 | deployment types page |
| d4d | PTU and priority | 5 | same page. See stuck 2 |
| d4e | Guardrails | 5 | guardrails page |
| d4f | Agent guardrails | 5 | guardrails page (preview parts marked in the page) |
| d5a | Endpoint and REST | 4 | Responses page shows REST. The rest: Ep 3 |
| d5b | The SDK | 3 | package names come from videos |
| d5c | Chat client code | 3 | code walk-through from videos. Study guide names the skill |
| d5d | Completions versus Responses API | 4 | Responses page (read 100k of 151k characters) plus Ep 5 |
| d5e | API keys | 4 | keyless page and Responses example (api-key header). Rotation: Ep 3 |
| d5f | Entra ID tokens | 5 | keyless page: role, scope, DefaultAzureCredential |
| d5g | Managed identity | 5 | managed identity page and keyless page |
| d5h | Switch keys off | 3 | Ep 3 only. I did not find the setting name in an opened page, so I do not name it |
| d6a | Prompt versus hosted agent | 5 | agent overview |
| d6b | Tools and MCP | 5 | agent overview and MCP intro |
| d6c | Knowledge and Azure AI Search | 4 | AI Search page. Foundry file-search steps: Ep 5 |
| d6d | Portal to client app | 4 | study guide and agent overview. YAML and code: Ep 5 |
| d6e | Approval and agent identity | 4 | agent overview (identity). Approval choices: Ep 3 and Ep 7 |
| d6f | Multi-agent workflows | 3 | videos only |
| d7a | Text analysis tasks | 4 | task names: study guide. Definitions: Ep 6 |
| d7b | Prompted model or Azure Language | 4 | "preconfigured": Language page. "Deterministic" and "cheaper": videos (3) |
| d7c | Azure Language features and code | 4 | features and legacy label: Language page. Method names: Ep 7 |
| d7d | Preprocessing and statistics | 3 | Ep 6 and cram only |
| d8a | STT and TTS | 4 | Speech page plus Ep 8 |
| d8b | Azure Speech three ways | 4 | Speech page, SDK flow from Ep 9 |
| d8c | Voice Live | 4 | Speech and agent pages plus Ep 9 |
| d8d | Speech pipelines | 3 | Ep 8 only |
| d9a | Vision tasks | 3 | Ep 10 and cram only |
| d9b | Multimodal prompts | 3 | Ep 11 only |
| d9c | Image and video generation | 3 | Ep 11 and cram. Model names are not opened |
| d9d | Diffusion models | 3 | videos agree. The abstract gives the name only |
| d9e | CNN versus vision transformer | 4 | ViT abstract: patches and transformer. CNN detail: Ep 10 |
| d10a | OCR | 3 | Ep 12 and cram |
| d10b | Field extraction | 3 | Ep 12 |
| d10c | Content Understanding analyzers | 5 | overview page |
| d10d | Audio and video extraction | 1 | audio and video support: overview page (5). "More deterministic than an LLM": conflict, see stuck 10 |

stuck (where people stick on this order; each has a source):
  - S1 Deployment name is not the model name. Code passes the deployment name as the model value. Source: Ep 5 21:25-22:29, Ep 3 40:15-40:29. Node d4b.
  - S2 "Priority" is not in the deployment type table of the docs. The cram shows it as an option next to PTU in the custom deploy dialog. The docs call Priority and Flex request-level processing tiers on Standard types. Source: deployment types page, cram "Models". Node d4d.
  - S3 The course says "regional". The docs table says Standard (one geography) and Regional Provisioned. Source: same page. Node d4c.
  - S4 A project shows two endpoints. The Ep 3 lab app uses the project endpoint, not the Azure OpenAI one. Source: Ep 3 16:56-17:12 and 40:20-40:41. Node d5a.
  - S5 Three ways to authenticate, one role name that changed. The keyless page names Cognitive Services User at the Foundry resource. Two other official pages say the roles Foundry User, Owner, Account Owner and Project Manager were renamed from Azure AI User, Owner and so on, with the same role IDs. Which role a given agent call needs: open question, RBAC page not opened (grade 1). Source: keyless page, guardrails page, architecture page. Nodes d5f, d5h.
  - S6 Two call shapes for one job. Completions uses messages with role and content. Responses uses instructions and input. Source: Ep 5 20:13-23:07, Responses page. Node d5d.
  - S7 Multimodal is not multimodel. Source: cram "Generative AI". Node d3f.
  - S8 "Token" appears twice. Ep 4 says a token is a word, part of a word or punctuation. Ep 6 says think of one word as a token for the NLP preprocessing step. Source: Ep 4 7:22-7:52, Ep 6 7:45-7:57. Nodes d3b, d7d.
  - S9 Names versus the portal. The study guide names sentiment, key phrase extraction and summarization as skills. The Language page labels them legacy. The Ep 7 portal lab lists only language detection and PII tools under Language. Source: study guide, Language page, Ep 7 29:58-30:26. Node d7c.
  - S10 Content Understanding "deterministic". The cram says purpose-built models are more deterministic than an LLM. The Content Understanding page says the service uses generative AI. Show both. Not settled. Source: cram "Information extraction", overview page. Node d10d.
  - S11 Exam weights. Study guide: 40 to 45 and 55 to 60 percent. Ep 14: about 40 and 60. Use the study guide. Source: study guide, Ep 14 3:22-3:33. Node d1a.
  - S12 The exam page blurb still lists old topics (machine learning principles, computer vision, NLP, generative AI workloads). The skills measured list is different. Use the skills list. Source: exam page, study guide. Node d1a.
  - S13 Browser labs run a small local model (Phi) in the page. Answers can be wrong, and the Language app there is not the Azure service. Ep 7 repeats the same tasks on real Foundry. Source: Ep 4 25:43-25:56, Ep 6 23:35-23:43. Anchors L1, L3, L5, L7, L9, L11.
  - S14 Foundry-generated code in key mode leaves the key out. You set an environment variable. Source: cram "Foundry generated code". Node d5c.
  - S15 Model names move. gpt-4.1-mini, GPT image, FLUX, sora-2 and GPT-5.4 are what the videos show. The catalog changes. Learn the task, not the name. Source: Ep 3 36:00-38:12, Ep 11 16:20-24:03.

conflicts, both sides shown: S2, S3, S5, S9, S10, S11, S12.

caption errors fixed in my wording (speech-to-text noise in the files):
  - "Savile", "boundaries" in the cram = Savill, Foundry. "AI-91" and "AI 91" = AI-901. "text PEE redaction" = text PII redaction. "language redaction" (Ep 7) = language detection. "express agent" = expense agent. "appreciation card" = purchasing card. "top T" = top P. "porosity" = prosody. "nodule file" = audio file. "general-purque" = general-purpose.
  - Ep numbers follow the file headers. Inside the videos the trainer says other session numbers. Ep 1 says 12 sessions. The playlist has 14 episodes.

sources (claim | url | grounded | grade). All opened 2026-10-12. Types: official, primary.

| claim used for | url | grounded | grade |
|---|---|---|---|
| skills measured, weights, 700 pass mark, Python and REST SDK CLI note | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901 | yes | 5 |
| exam page, stale blurb, weights repeated | https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-901/ | yes | 5 |
| deployment types, data residency, PTU, priority, flex, batch | https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types | yes | 5 |
| Entra keyless, Cognitive Services User, scope ai.azure.com/.default, DefaultAzureCredential | https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/configure-entra-id | yes | 5 |
| agent types, tools, MCP auth options, agent identity, guardrails link | https://learn.microsoft.com/en-us/azure/foundry/agents/overview | yes | 5 |
| guardrails, controls, intervention points, DefaultV2, agent override, role rename | https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview | yes | 5 |
| Content Understanding: analyzers, modalities, JSON or Markdown, confidence, uses generative AI | https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview | yes | 5 |
| Discover, Protect, Govern. No list of six principles on this page | https://learn.microsoft.com/en-us/azure/foundry/responsible-use-of-ai-overview | yes | 5 |
| MCP definition | https://modelcontextprotocol.io/docs/getting-started/intro | yes | 5 |
| managed identity, system and user assigned | https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview | yes | 5 |
| scope levels, resource group rules | https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview | yes | 5 |
| Foundry resource, project, RBAC split, deployment types table | https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture | yes | 5 |
| Azure Language features, legacy label, preconfigured, MCP server | https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview | yes | 5 |
| Azure Speech: STT, TTS, Voice Live, SDK, CLI, REST | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview | yes | 5 |
| Azure AI Search, vector, hybrid, agentic retrieval | https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search | yes | 5 |
| embedding definition, cosine similarity (classic portal page) | https://learn.microsoft.com/en-us/azure/foundry-classic/openai/concepts/understand-embeddings | yes | 5 |
| Responses API: stateful, instructions and input in examples, REST path | https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses | partly (100k of 151k characters) | 4 |
| Transformer built on attention alone | https://arxiv.org/abs/1706.03762 | yes (abstract) | 5 |
| ViT: transformer on image patches versus CNNs | https://arxiv.org/abs/2010.11929 | yes (abstract) | 5 |
| diffusion model name only | https://arxiv.org/abs/2006.11239 | yes (abstract, no detail) | 5 for the name |

ungrounded (no source opened, or opinion):
  - Not in the tree. Ep 3 lab step: the Entra app registration for a single-page app sets redirect URI and implicit and hybrid flow (Ep 3 41:55-42:01). Whether that is a pattern to copy: not verified, grade 2. He knows OAuth, so he can judge it. Do not copy it into real code on the video's word.
  - Not opened: the Microsoft Learn exercise pages for L1 to L12 and their aka.ms links, the Learn AI-901 learning path, the practice assessment (sign-in needed), the Foundry RBAC page, model availability pages, the exact setting that turns keys off. Each is grade 3 or lower where it appears.
  - Prices, quotas, model lifecycles, region lists: not covered. They change.
  - No node carries ungrounded: true. Every node cites at least one opened source. Transcript-only nodes are grade 3.

failure to avoid: a fake acquired skill. Watching 14 episodes and clicking the labs is exposure. A lab passes only when he can say, line by line, what the code does without the video.

handoff: explainer not run
