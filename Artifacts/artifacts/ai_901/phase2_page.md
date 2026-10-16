# AI-901: Introduction to AI in Azure, read for Foundry app code

> tally: g5 **230** · g4 **12** · g3 **157** · g2 **4** · g1 **3** (claim badges, count of `[gN]` marks in the ten sections)
> words per section, outside code, chips badges and cites counted as words: 1 **1,229** · 2 **737** · 3 **1,188** · 4 **2,016** · 5 **2,173** · 6 **1,314** · 7 **993** · 8 **895** · 9 **1,026** · 10 **1,081**. Ceiling per section: 2,500. Total 12,652. No page ceiling (`.rules/brevity.md` rule 10).
> pages per section at 500 words a page: 2.5, 1.5, 2.4, 4.0, 4.3, 2.6, 2.0, 1.8, 2.1, 2.2.

**Scope.** Labs in your own Azure subscription or trial only. Delete each lab resource after use. Nothing here targets a system you do not own.

**How to read.** Each section runs parts, condition, when it does not apply, then how. A badge from 5 to 1 grades each claim: 5 verified in an official or primary source, 4 sourced by joining two, 3 only a transcript or secondary source says it, 2 not verified, 1 conflict or unknown. Cites: [n] is a web source in the last section. [C] is the cram transcript. [E3 16:56] is a course episode (file header number) and a time.

**Framing lines.** The Parts, Condition, Not when and Failure lines that open each section are my framing. They restate facts cited below them. They add no new claim.

**Conflicts shown with both sides.** S2 and S3 (section 4), S5 and the token-provider forms, resolved from the SDK source (section 5), S8 (section 3), S9 (section 7), S10 (section 10), S11 and S12 (section 1), the guardrail severity labels, which look reversed (section 4).

**Not verified (grade 2 or 1).** The Entra single-page-app lab pattern. Text in an image as an attack path. The contract example for LLMs. Which role an agent call needs. What "regional" means in the exam.

## 1. AI concepts and responsible AI {d1}

**Exam area.** Identify AI concepts and capabilities: 40 to 45 percent of the exam. It includes the six responsible AI skills [1] [g5].

**Parts:** a workload (the kind of task), a model or service that does it, and rules that limit harm. **Condition:** you can name the workload before you pick a tool. **Not when:** one real task chains several workloads. Name each link. **Failure:** pick "a generative model" for every task, then miss the question that wants Azure Language or Content Understanding.

### Exam shape and weights {d1a}

- Two areas: identify AI concepts and capabilities (40 to 45 percent), implement AI solutions by using Microsoft Foundry (55 to 60 percent). Pass mark: 700 of 1000 [1][2] [g5].
- The exam expects Python syntax, Azure resource knowledge, and "REST APIs, SDKs, and CLIs". Most questions use general availability features. Preview features can appear when they are commonly used [1] [g5].
- The format is multiple choice. A wrong answer costs no points [E1 3:53-4:26][E14 2:41-4:12] [g3].
- Depth: read simple Python. Do not write complex code [C Study resources] [g3].
- The practice assessment sits on AI Skills Navigator. It needs a sign-in [1] [g5]. The Learn path is "Get started with AI applications and agents on Azure", 7 modules [31] [g5].

> **Conflict S11.** The study guide says 40 to 45 and 55 to 60 percent [1] [g5]. Ep 14 says "about 40" and "60" [E14 3:22-3:33] [g3]. Use the study guide.

> **Conflict S12.** The exam page blurb still lists machine learning principles, computer vision, NLP and generative AI workloads. The "Assessed on this exam" list on the same page, and the study guide, give the two areas above [2][1] [g5]. Use the skills list. The blurb is stale.

### AI, ML and workloads {d1b}

**Exam skill group {X3}:** identify AI workloads and their techniques [1] [g5].

AI is software that imitates a human ability: predict, see, hear, speak, create [C What is AI] [g3]. Machine learning is how it learns: from data and patterns, not from fixed rules [E2 3:56-4:15] [g3].

| Workload | In, out | Azure service in this course | Section |
|---|---|---|---|
| Generative and agentic AI | prompt in, new content or actions out | models and agents in Foundry | 3 to 6 |
| Text analysis | text in, key terms, entities, sentiment, summary out | Azure Language, or a prompted model | 7 |
| Speech | audio to text, text to audio | Azure Speech, Voice Live | 8 |
| Computer vision | image in, label, box, pixels or description out | multimodal models, image models | 9 |
| Information extraction | document, image, audio or video in, structured fields out | Content Understanding | 10 |

The workload names come from the study guide [1] [g5]. The service names come from the product pages [16][18][8] [g5].

One task chains workloads. Example: "Help me prepare for tomorrow's meeting." Speech turns the voice to text. Language AI reads the request. An agent finds files. Vision reads scanned pages. A generative model writes the summary [E2 5:09-5:55] [g3]. Name each link and you name the workloads.

When it does not apply: the page does not teach machine learning training. The exam moved to the skills above (S12).

> **Lab {L1}** (Ep 2, browser). Open the computer-history agent. A small Phi model runs inside your browser. Run one text prompt, one speech prompt, one image prompt and one blocked prompt. Each prompt shows one workload [E2 10:00-23:34] [g3].

> **Note S13.** The browser labs run a small local model. Answers can be wrong. The Language app in the browser is not the Azure service. Ep 7 repeats the same tasks on real Foundry [E4 25:43-25:56][E6 23:35-23:43] [g3].

### Assistant versus agent {d1c}

| | Assistant | Agent |
|---|---|---|
| Starts on | a user request | an event, a schedule or a goal |
| Control | the human steers each turn | works toward a goal, plans steps, acts |
| Aim | productivity | end-to-end automation |
| Parts | model and prompt | model, instructions and tools |

The contrast is from the cram and Ep 4 [C Assistants and agents][E4 5:49-6:51][E4 11:43-12:53] [g3]. The study guide names "generative and agentic AI" but not the pair [1] [g5]. Foundry configures an agent from instructions, a model and tools, then runs it [6] [g5]. "Without tools, AI only talks" [E3 9:21-9:27] [g3].

Example: "Summarize this document" is an assistant task. One request, one answer. "Prepare the weekly project report and email my manager" is an agent task. It reads, decides, writes and acts [E4 10:49-11:38] [g3].

### Six responsible AI principles {d1d}

**Exam skill group {X1}:** describe considerations for fairness, reliability and safety, privacy and security, inclusiveness, transparency and accountability. The study guide lists each as its own skill [1] [g5].

| Principle | What it asks [11] [g5] | A test, with an example [E2 6:38-9:54] [g3] |
|---|---|---|
| Fairness | treat similar people and cases the same; test to reduce bias | a job-screening model tested across profiles |
| Reliability and safety | perform consistently, fail safely, resist manipulation | a medical model that signals doubt and lets a human decide |
| Privacy and security | protect data across its life, least privilege, purpose limits | summaries stay protected, access is controlled |
| Inclusiveness | design for diverse needs, test with a broad set of users | voice input, text input, screen readers, many languages |
| Transparency | explain how it works, what it uses, where it fails | users know the text is AI-generated |
| Accountability | clear owners, people stay answerable, humans are not out of the loop | a named person answers for the decision |

The Foundry responsible AI page does not list the six. It frames the work as Discover, Protect and Govern [10] [g5]. The two frames fit: the principles say what to protect; Discover, Protect and Govern say when to act.

### Principles become controls {d1e}

My step, joined from the sources named in each row [g4]. A principle is six words until it is a setting you can audit.

| Principle | A control you can set or check | Source |
|---|---|---|
| Fairness | evaluations in Foundry, plus human review of results | [11][E3 26:40-27:06] [g3] |
| Reliability and safety | guardrails: risks, severity, block or annotate; a fixed model version | [7] [g5] [E5 4:54-5:32] [g3] |
| Privacy and security | Entra (Microsoft's identity service) roles, managed identity, private networking, data zone deployment, customer-managed keys, detection of personally identifiable information (PII) | [4][13][15][3][16] [g5] |
| Inclusiveness | speech in and out, many languages, accessible modes | [E2 8:24-8:55] [g3] |
| Transparency | traces and evaluations; answers that cite their knowledge source | [6] [g5] |
| Accountability | approval of tool calls, a dedicated agent identity, audit logs | [6][13] [g5] |

Condition: a control exists only if someone sets it. Models get the guardrail Microsoft.DefaultV2 by default [7] [g5]. A control you never opened is a default you accepted.

> **Lab {L1}** again: the blocked prompt is a guardrail firing. Read the refusal text. Find which control produced it [E2 22:36-23:34] [g3].

## 2. Azure, Entra and Foundry {d2}

**Parts:** an identity directory (tenant), a cost and access boundary (subscription), a lifecycle container (resource group), the resources. **Condition:** every resource sits in one group, in one subscription. **Not when:** a few resource types deploy at subscription, management group or tenant scope [14] [g5]. **Failure:** treat Foundry as one box. It is a resource, with projects inside it, and roles that attach at each level.

You know cloud. Read this section for the Foundry names.

### Tenant and Entra ID {d2a}

A tenant is your organization's Entra directory. Users, groups, apps, managed identities and agents get identities there [E3 3:16-3:46][C Azure and Entra] [g3]. Workload identities in Entra are applications, service principals and managed identities [13] [g5]. Each agent can also have its own Entra identity [6] [g5].

A subscription trusts one tenant. Only identities from that tenant can be given permission on its resources [C Azure and Entra] [g3].

Why it matters here: identity decides who may call a model. Entra is the keyless way in (section 5).

### Subscription and resource group {d2b}

```diagram-hierarchy
tenant (Entra directory: users, groups, apps, identities)
  |  a subscription trusts one tenant
  v
[management group: optional level]
  |
subscription (cost and access boundary; roles and policy flow down)
  |
  +-- resource group "rg-ai-lab" (one lifecycle: delete it, all goes)
        |
        +-- Foundry resource (Microsoft.CognitiveServices/accounts, kind AIServices)
        |     +-- model deployments, networking, security, connections
        |     +-- project "demo" (agents, files, evaluations)
        +-- Storage, Key Vault, AI Search (own governance)
```

Azure has four management scopes: management groups, subscriptions, resource groups, resources. Lower levels inherit settings from higher ones [14] [g5]. Example: a policy on the subscription applies to every group and resource under it. A policy on one group does not reach another group [14] [g5].

Resource group rules [14] [g5]:

- Each resource is in exactly one group.
- Resources in a group should share a lifecycle. Delete the group and you delete all of them.
- A group has a location. It stores the group's metadata.
- Tags on a group are not inherited by its resources.

Groups do not nest. The page lists four levels and no group inside a group; the cram says it outright [14] [C Azure and Entra] [g4]. A subscription is the cost boundary [E3 3:46-4:09] [g3].

> **Security.** A role assigned at the subscription reaches every group under it. Assign at the lowest scope that works. The keyless guide assigns Cognitive Services User at the Foundry resource, not the subscription [4] [g5].

### Foundry resource and project {d2c}

| Level | Holds | Who works here |
|---|---|---|
| Foundry resource (`Microsoft.CognitiveServices/accounts`, kind `AIServices`) | governance: networking, security settings, model deployments, connections | platform and security team |
| Project (`.../accounts/projects`, a subresource) | files, agents, evaluations, and reuse of the resource's deployments | one team, one app |
| Connected resources (Storage, Key Vault, AI Search) | their own data and rules | managed separately |

All rows from the architecture page [15] [g5].

Roles split the same way. Control-plane actions (create a deployment or a project) are separate from data-plane actions (build an agent, run an evaluation, upload a file). You can assign roles at the resource or at one project [15] [g5]. A starter assignment: Foundry User for each developer at the resource scope [15] [g5]. Most new APIs sit at project scope. Some, like Translator, only exist at resource level [15] [g5].

When not: one developer exploring needs one resource and one project. A standalone Azure OpenAI resource can be enough if you only need completions [15] [g5].

> **Lab {L2}** (Ep 3, Foundry). Create a project: pick a subscription, a resource group and a region. Find the project endpoint and the key. Deploy gpt-4.1-mini and chat. Then switch keys off and use Entra only. Delete everything after [E3 14:13-18:00; 36:00-39:40] [g3]. Use your own subscription or a trial.

### Portal map and lab hygiene {d2d}

The portal is ai.azure.com. The Ep 3 tour [E3 21:34-31:00] [g3]:

| Menu | Holds |
|---|---|
| Discover | model catalog, tools, solution templates |
| Build | agents, workflows, models, AI services, fine-tune, tools, knowledge, data, evaluation, guardrails |
| Operate | assets, compliance, quota, provisioned throughput |
| Admin | projects, AI gateway |

The portal changes. A playground is a test page in the portal where you try a model with no code [E5 6:35-7:49] [g3]. Docs mark which pages apply to the "Foundry (classic) portal" and which to the new one. The embeddings page says it applies to classic only [21] [g5]. Learn the idea, not the menu.

The Azure portal shows the endpoint and, under Resource Management, Keys and Endpoints [4] [g5]. Lab hygiene: delete the resource group when you finish. It removes every resource in it [14] [g5][E3 51:21-51:40] [g3].

## 3. How generative AI models work {d3}

**Exam skill group {X2}:** describe how generative models work, pick a model by capability, pick deployment options and parameters [1] [g5].

**Parts:** tokens in, embeddings, attention, a next-token prediction, and a loop. **Condition:** the model predicts one token at a time from the tokens before it [22] [g5]. **Not when:** image and video generation (diffusion) and vision classifiers (CNN) work differently. See section 9. **Failure:** treat the model as a database that looks answers up. It generates them.

```diagram-tokens
text:        "I heard a dog bark"
  -> tokens      [I] [heard] [a] [dog] [bark]            tokenizer
  -> embeddings  each token = a vector (position = meaning)
  -> attention   weights: which tokens matter to which   transformer
  -> next token  "loudly" is the most likely one
  -> append it and repeat until the reply is done        loop
```

### LLM and SLM {d3a}

| | Large language model (LLM) | Small language model (SLM) |
|---|---|---|
| Size | billions of parameters, maybe more | millions, often distilled from a larger model |
| Cost and speed | more capable, slower, dearer | lighter, faster, cheaper |
| Fits | understands language, context, tone and intent from huge training text | lower cost, faster replies, or running cloud to device |

Table rows [C Generative AI][E4 3:39-4:50] [g3]. Both are generative: they create a response; they do not pick from a list [E4 4:42-4:51] [g3]. A parameter is a number that sets the strength of a connection inside the model. Inference is the model producing output from input [C Generative AI] [g3].

Example: an HR help assistant that answers simple policy questions quickly can use an SLM [E4 4:15-4:42] [g3]. A summary of a 40-page contract suits an LLM. That second half is my example, not a sourced rule [g2].

Not every model in Foundry is an LLM [C Generative AI] [g3].

### Tokens {d3b}

A token is a unit a tokenizer cuts text into: a word, a part of a word, a character set, or punctuation [22] [g5]. Three methods exist: word, character, subword. GPT models use a subword method, byte-pair encoding [22] [g5].

Input tokens and output tokens share one limit, the context window. Tokens set price and the tokens-per-minute rate limit [22] [g5]. Chat history adds input tokens each turn: the playground shows the input count grow [E5 17:58-18:40] [g3].

Worked example [22] [g5]. Text: "I heard a dog bark loudly at a cat". Context window: 100 tokens.

| Method | Input tokens | Left for output |
|---|---|---|
| Word | 9 | 91 |
| Character | 34 | 66 |

> **Conflict S8.** Ep 4 says a token is a word, part of a word or punctuation [E4 7:22-7:52]. Ep 6 says "think of each word as a token" [E6 7:45-7:57]. Both fit [22]: Ep 6 describes word tokenization, one of three methods [g4]. Real LLMs use subwords.

### System and user prompt {d3c}

**Exam skill group {X4}:** create effective system and user prompts [1] [g5].

The system prompt (instructions) sets role, format and limits. The user prompt (input) is the request. In Chat Completions the system message is the first item in `messages`. It is optional, but the docs say to include at least a basic one [24] [g5]. The Responses API takes `instructions` and `input`. The page uses both fields in examples and does not define them. Reading `instructions` as the system role is my join [23] [g4].

Agents keep their instructions as a standing job description [E5 11:20-12:41] [g3].

Example, and the same call with one change [E4 15:48-18:38][C Custom AI app] [g3]:

| System prompt | User prompt | Result |
|---|---|---|
| "You are an AI assistant that helps people find information." | What is expense management? | long, general answer |
| "You are an AI agent that provides short, concise answers to expense-related questions." | What is expense management? | a few words |
| "You are a helpful assistant, but always answer like a pirate." | What is the capital of England? | London, in pirate voice |

> **Security.** A system prompt is an instruction, not a lock. A user prompt can try to override it. User prompt attacks are malicious prompts that try to bypass system instructions [34] [g5]. Foundry lists them as a guardrail risk [7] [g5]. So do not rely on the system prompt alone to hold secrets or access rules. That conclusion is my reading of those two sources [g4].

> **Lab {L3}** (Ep 4, browser). Change the system prompt and watch the reply change. Read the Python at the end: endpoint, key, model, instructions, input [E4 23:40-25:30] [g3]. The same demo in real Python is {L13} in section 5.

### Sampling parameters {d3d}

| Parameter | Effect |
|---|---|
| Temperature | randomness: low is focused and repeatable, high is varied |
| Top P | diversity of word choice; similar to temperature, a different method |
| Max tokens | maximum length of the reply |
| Repetition penalty | higher value, less repeated text |

Source: playground text in Ep 4 and Ep 5 [E4 21:23-21:58][E5 9:16-10:10; 29:59-30:34] [g3].

Example: a legal summary wants low temperature. Marketing copy wants high [E5 9:53-10:10] [g3].

When it does not apply: reasoning models. On the Chat Completions page, GPT-5 series reasoning models "use `max_completion_tokens` instead of `max_tokens`, and they don't support `temperature`, `top_p`, or the penalty parameters" [24] [g5]. The cram says the same in softer words: older models let you change temperature [C Custom AI app] [g3].

> **Lab {L3}**: change temperature, top P and max tokens. Ask the same question three times at each setting [E4 21:23-22:06] [g3].

### Embeddings and attention {d3e}

An embedding is a vector of floating-point numbers that holds the meaning of a piece of text. The distance between two embeddings tracks how similar the meanings are [21] [g5]. Cosine similarity measures the angle between two vectors [21] [g5]. Embeddings power vector similarity search in Azure AI Search [21][20] [g5].

Example: dog and puppy sit close. Dog and skateboard sit far apart [E4 8:09-8:34] [g3]. The famous "dog plus young is puppy" is not real arithmetic. "Young" is a direction. You move from dog along it and land near puppy [E6 15:12-15:57] [g3].

Attention weighs which tokens matter to each other in context. The Transformer is "based solely on attention mechanisms" [28] [g5]. In "I heard a dog bark", to predict "bark" the tokens dog and heard weigh more than I and a [E4 8:55-9:24] [g3].

The loop: the model predicts the next token, appends it, and repeats [22][E4 9:54-10:15] [g5].

### Multimodal versus multimodel {d3f}

| | Multimodal | Multimodel |
|---|---|---|
| Meaning | one model takes or gives more than one modality | one app uses more than one model |
| Modality | text, audio, image, video, code | not the point |
| Example | a model that takes text and an image and answers in text | speech to text, then a reasoning model, then text to speech |

The terms are from the cram and Ep 11 [C Generative AI][E11 2:10-2:30] [g3]. The word "multimodel" is not in the docs I opened. The pattern is. Voice-based agents run either as native speech-to-speech (one realtime model) or as a cascade: recognition, a text model, synthesis [6][15] [g4]. Each cascade stage adds latency [6] [g5].

One letter apart. Two ideas.

## 4. Models, deployment and guardrails {d4}

**Parts:** a catalog entry, a deployment (a name, a type, a version, limits) and a guardrail. **Condition:** a model must be deployed before an app can call it. **Not when:** an instant access model (preview). You call it by name and no deployment exists [3][25] [g5]. Open-source and custom models on managed compute also skip these deployment types [3] [g5]. **Failure:** read "global", "data zone" and "regional" as three sizes. They are three answers to one question: where is my prompt processed?

### Model catalog and choice {d4a}

The catalog has two groups. Models sold directly by Azure are hosted by Microsoft, billed through your subscription, with enterprise support and service-level agreements (SLAs). Partner and community models come under the partner's terms [E5 2:35-4:14] [g3]. You filter by collection, capability, source, inference task, fine-tune method and industry [E3 22:17-22:53] [g3]. The cram counts "over 10,000 models". That figure changes [C Microsoft Foundry] [g3]. Agent Service works with many catalog models, for example GPT-4o, Llama and DeepSeek [6] [g5].

Choose by task, quality, cost and latency. Do not choose by name [E11 5:34-8:33] [g3]. Names move (S15): gpt-4.1-mini, GPT image, FLUX, sora-2 and GPT-5.4 are what the videos show. The catalog today differs. Learn the task, not the name.

Example: a text-to-image job. Filter by inference task "text to image". Compare two models on quality and latency. A quick prototype takes speed. A campaign takes quality [E11 7:34-8:11] [g3].

The cram also shows a model router. It picks a model by the complexity of the request [C Looking at an agent] [g3].

### Deploy before use {d4b}

**Exam skill group {X4}:** deploy a model and interact with it in the portal [1] [g5].

A deployment is a named instance of a model in your project, with a type, a version and limits. Quick deploy takes defaults. Custom deploy shows version, deployment type, tokens-per-minute rate, upgrade policy and guardrail [E3 37:29-37:59][C Models] [g3]. Deployments are Azure resources (`Microsoft.CognitiveServices/accounts/deployments`) [3] [g5].

**S1: the deployment name is not the model name.** Code passes the deployment name as `model`. The docs comment says "Replace with your model deployment name" [24] [g5]. The image guide says the same: set `model` to the name of your deployment [26] [g5]. The quickstart says to change the model name in the sample if you used a different deployment name [25] [g5].

Example: you deploy `gpt-4.1-mini` and name the deployment `chat-prod`. The code says `model="chat-prod"` [E5 21:25-22:29] [g3]. If you leave `gpt-4.1-mini` there, no deployment has that name. I did not run the failing call, so I do not quote its error [g2].

> **Security.** Deployments are resources, so role-based access control (RBAC) and Azure Policy apply. The docs show a policy that denies one deployment type by its SKU name, the type's code name. Replace `GlobalStandard` with the type you want to block [3] [g5]. That is how you enforce a data residency rule.

> **Lab {L2}**: deploy with default settings, then open the custom option and read each field before you cancel [E3 37:29-38:12] [g3].

### Deployment types {d4c}

**Exam skill group {X2}** includes picking deployment options [1] [g5].

Data at rest stays in the designated Azure geography. Where the prompt is processed depends on the type [3] [g5]:

- **Global:** any Azure region.
- **Data Zone:** only inside the zone: US, EU or Asia Pacific.
- **Standard and Regional Provisioned:** inside the geography you choose. The service may move it between regions of that geography.

| Type | Data processed | You pay | Pick it when [3] [g5] |
|---|---|---|---|
| Global Standard | any region | per token | default; newest models, lowest price, widest regions |
| Global Provisioned | any region | reserved PTU | steady high throughput |
| Global Batch | any region | 50% off, 24-hour target | large async jobs |
| Data Zone Standard | inside the data zone | per token | EU, US or APAC data zone rules |
| Data Zone Provisioned | inside the data zone | reserved PTU | zone rules and steady throughput |
| Data Zone Batch | inside the data zone | 50% off | async jobs with zone rules |
| Standard | inside the geography | per token | geography rules, low volume |
| Regional Provisioned | inside the geography | reserved PTU | geography rules and throughput |
| Developer | any region | per token | evaluating a fine-tuned model only; 24-hour life; no SLA |

Start with Global Standard. Move only for a reason: data residency, reserved throughput or batch [3] [g5]. New types appear in order: global, then data zone, then geography [3] [g5]. Not every model supports every type [3] [g5].

Example, then one change. A support chatbot with EU customers and a rule that prompts stay in the EU: pick Data Zone Standard, EU. Same app, now with steady heavy traffic and a latency target: pick Data Zone Provisioned [3] [g4] (my join of two rows).

The EU Data Zone follows the Azure EU Data Boundary, which can include European Free Trade Association countries such as Norway and Switzerland [3] [g5]. Microsoft can add regions to a zone without notice [3] [g5].

> **Conflict S3.** The course says "regional" and means one region [C Models] [g3]. The deployment types page says Standard processes "within Azure geography" and may move data between regions of that geography [3] [g5]. The architecture page table says "Single region" for the same type [15] [g5]. The same page, in its data residency section, says "standard or regional deployments process in the deployment region" [15] [g5]. Two official pages disagree; the term "regional" in an answer option is the cram's word. Open question for the exam wording [g1].

### PTU and priority {d4d}

**PTU** means provisioned throughput unit. You buy a fixed number of PTUs. They guarantee a level of capacity, so latency is lower and steadier than on Standard [3] [g5]. Each model and version needs a different number of PTUs, and each has a minimum [3] [g5].

**Priority processing** is a request-level tier on Standard types. It gives faster responses on pay-as-you-go. Global Standard and Data Zone Standard support it [3] [g5]. **Flex processing** is the cheap, delay-tolerant tier on Global Standard [3] [g5].

| | PTU | Priority | Flex | Batch |
|---|---|---|---|---|
| What it is | a deployment type with reserved capacity | a tier on a Standard type | a tier on Global Standard | a deployment type |
| Pay | reserved capacity | per token, higher rate | per token, lower rate | 50% off |
| You get | steady latency | faster responses | slower, cheaper | results within 24 hours |

All rows [3] [g5], except "higher rate" and "lower rate", which are my reading of "pay-as-you-go" and "lower-cost" [g4].

> **Conflict S2.** The cram shows "priority processing" as an option next to PTU in the custom deploy dialog [C Models] [g3]. The docs table does not list Priority as a deployment type. They call it a processing tier [3] [g5]. Treat Priority as a tier. PTU is the type.

Quota and PTU appear under Operate in the portal [E3 29:59-30:47] [g3].

### Guardrails {d4e}

**Exam skill groups {X1} and {X2}** cover this [1] [g5].

A guardrail is a named collection of controls. A control names a risk, the intervention points to scan, and the action when the risk fires [7] [g5].

| Part | Values for a model [7] [g5] |
|---|---|
| Risks | hate, sexual, self-harm, violence, user prompt attacks, indirect attacks, protected material (code, text); in preview: spotlighting, groundedness, PII, task adherence |
| Intervention points | user input, output |
| Actions | annotate; annotate and block |
| Severity (content risks) | off (approved customers only), low, medium, high |

Three preview terms in that row. Spotlighting tags a document as lower-trust and base64-encodes it, so the model treats it as less trusted than the user and system prompts [34] [g5]. Groundedness detection checks that a reply rests on the source material you gave it, and flags made-up content [35] [g5]. Task adherence checks that an agent's tool call matches what the user asked for [36] [g5].

Models get Microsoft.DefaultV2 by default [7] [g5]. Foundry runs classification models from Azure AI Content Safety. Variations in API setup and app design can change filtering, so a guardrail is a control, not a guarantee [7] [g5]. The guardrail applies to Foundry Models sold by Azure, except audio transcription models [7] [g5]. Content Understanding inherits the guardrail of its model deployment [8] [g5].

The portal shows Microsoft Default and Microsoft Default V2, blocklists (terms by hand, regex, or CSV upload) and trusted integrations [E3 27:08-27:57] [g3]. The cram shows jailbreak protection, content safety and protected material in the default guardrail [C Models] [g3].

Example: a clinic app needs to discuss violence in medical cases. Set the violence threshold to High for that deployment, so only the most severe content is flagged. Keep the other controls. The cram talks of a "higher tolerance", which is ambiguous [C Models] [g3]. The threshold rule is from [7][32] [g5].

> **Security.** Prompt Shields covers two attacks [34] [g5]. User prompt attacks are malicious prompts that try to bypass system instructions or safety training. The page says this shield was previously called jailbreak risk detection. Document attacks (the "indirect attacks" risk) are hidden instructions in third-party content such as documents, emails and web pages. They are scanned at user input and at tool response. The agent page calls the same family cross-prompt injection attacks (XPIA) [6] [g5].

> **Severity direction.** [7] and the severity-levels page [32] both say Low "flags content at low severity and higher" and call it "least restrictive". They say High "flags only the most severe content" and call it "most restrictive". The classic page says the default Medium threshold filters medium and high content and does not filter low [33]. Content at the Safe level is always annotated and never blocked [32]. Read the rule, not the label: a lower threshold flags more. The labels "least" and "most restrictive" look reversed. Test it in the lab before you trust either [g4].

> **Lab {L1} and {L2}**: open the default guardrail on your deployment. Read each control. Send a blocked prompt and match the refusal to a control [C Models][E2 22:36-23:34] [g3].

### Agent guardrails {d4f}

**Exam skill group {X1}.** Agent guardrails are in preview [7] [g5].

Parts: one guardrail, a set of controls, and now two more intervention points. Tool call is the action and data an agent sends to a tool. Tool response is what the tool returns to the agent. Both apply to agents only [7] [g5].

| | Model | Agent (preview) |
|---|---|---|
| Intervention points | user input, output | user input, tool call, tool response, output |
| Actions | annotate; annotate and block | annotate and block only |
| Spotlighting, groundedness | supported | not supported |

All rows [7] [g5].

**Override rule.** An agent's guardrail fully replaces the model's guardrail [7] [g5]. Example from the docs: the model has Violence at High for input and output. The agent has Violence at Low for input and output and no control for tool calls. Result: user input and final output are scanned at Low. Tool calls and tool responses are not scanned for violence [7] [g5].

If you assign no guardrail to an agent, it inherits the guardrail of its model deployment. It uses Microsoft.DefaultV2 only if the model does, or you assign it [7] [g5]. Hosted agents add network egress controls (preview) in the same guardrail. They limit where the agent may connect [7] [g5].

> **Security.** A tool response is untrusted input to the agent. Treat it like a form field from the internet. Prompt Shields scans for document attacks at the tool response point [34] [g5]. My step: if your agent guardrail has no tool-response control, nothing checks what tools send back.

## 5. Calling Foundry from code {d5}

**Exam skill group {X4}:** create a chat client with the Foundry SDK, a single agent, and a client for that agent [1] [g5]. Python syntax is part of the exam [1] [g5].

**Parts:** an endpoint (where), a credential (who), a client (the SDK object), a request (deployment name plus messages or input), and a response (what you read). **Condition:** you have a deployment and a permission. **Not when:** an instant model needs no deployment, and an agent is called by agent name (section 6). **Failure:** copy the sample, paste a key into it and commit it.

### Endpoint and REST {d5a}

An endpoint is an HTTPS address. Your app is the client. Foundry is the server. Calls are REST with JSON bodies [E3 10:21-13:01][C Endpoints, keys and Entra auth] [g3]. You know this. The new part is the address forms [25][23][24] [g5]:

| Endpoint | Form | Used by |
|---|---|---|
| Project endpoint | `https://<resource>.services.ai.azure.com/api/projects/<project>` | `AIProjectClient` in `azure-ai-projects` [25] |
| OpenAI-compatible endpoint | `https://<resource>.openai.azure.com/openai/v1/` | the plain `openai` client [24][23] |

> **Note S4.** A project shows both endpoints. The Ep 3 lab app uses the project endpoint, not the Azure OpenAI one [E3 16:56-17:12; 40:20-40:41] [g3].

A raw call, with a key and with an Entra token [23] [g5]:

```bash
curl -X POST https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/responses \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{"model": "MODEL_NAME", "input": "This is a test."}'
# Entra: replace the api-key header with
#   -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN"
```

Reading the call: the path `/openai/v1/responses` names the operation. `model` is your deployment name. `input` is the user prompt. The header carries who you are. The threat model is the one you know: TLS, a secret in a header, authorization at the resource.

### The SDK {d5b}

An SDK wraps the REST call, the JSON and often the sign-in [E3 13:05-13:43][C App integration with Foundry] [g3]. You read a flow: import, configure, create a client, call, read the result.

| Package | For | Source |
|---|---|---|
| `openai` | chat, responses and images against the OpenAI-compatible endpoint | [24][23] [g5] |
| `azure-identity` | `DefaultAzureCredential`, `get_bearer_token_provider` | [4] [g5] |
| `azure-ai-projects` | `AIProjectClient`, agents (needs 2.x: `pip install "azure-ai-projects>=2.3.0" azure-identity`) | [25] [g5] |
| `azure-ai-textanalytics` | `TextAnalyticsClient` for Azure Language | [17] [g5] |
| `azure-cognitiveservices-speech` | the Speech SDK | [19] [g5] |
| `azure-ai-contentunderstanding` | `ContentUnderstandingClient` | [9] [g5] |

SDK versions break code. The quickstart warns that Azure AI Projects 2.x is incompatible with 1.x [25] [g5].

### Chat client code {d5c}

**Exam skill group {X4}** reads this code. Here is the smallest useful version, with a key first [24][E4 23:40-25:30] [g5].

```python
import os                                                    # 1
from openai import OpenAI                                    # 2

client = OpenAI(                                             # 3
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),               # 4
    base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",  # 5
)

response = client.chat.completions.create(                   # 6
    model="YOUR-DEPLOYMENT-NAME",                            # 7
    messages=[                                               # 8
        {"role": "system", "content": "You are a helpful assistant. Always answer like a pirate."},  # 9
        {"role": "user", "content": "What is the capital of England?"},                              # 10
    ],
)

print(response.choices[0].message.content)                   # 11
```

Shape from the Chat Completions page [24] [g5]. The prompts are from the cram demo [C Custom AI app] [g3].

| Line | What it does | Why a reviewer cares |
|---|---|---|
| 1 | `os` reads environment variables | the key stays out of source |
| 2 | imports the client class | the same class serves any OpenAI-compatible endpoint |
| 3 | builds the client: holds endpoint and credential | no network call happens yet |
| 4 | reads the key from `AZURE_OPENAI_API_KEY` | a literal key here goes into git |
| 5 | the endpoint: your resource name is in the host | check the host is the resource you mean |
| 6 | sends a POST and returns a response object | this is the only network call |
| 7 | the deployment name, not the model family | S1 |
| 8 to 10 | a list of role and content: system first, then user | the system message sets behavior, the user message asks |
| 11 | `choices` is a list; `[0]` is the first; `.message.content` is the text | the object also carries tool calls, a refusal field and safety annotations |

All rows from the code and page [24] [g5]. The extra fields in the response object are from the cram demo [C Custom AI app] [g3]. Print the whole object once. You will see content-safety results such as self-harm and violence [C Custom AI app] [g3].

Now the same call with Entra. Only the credential lines change [4][24] [g5]:

```python
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(                      # a
    DefaultAzureCredential(), "https://ai.azure.com/.default"    # b
)

client = OpenAI(
    base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",
    api_key=token_provider,                                      # c
)
# the rest is identical: client.chat.completions.create(...)
```

| Line | Meaning |
|---|---|
| b | `DefaultAzureCredential()` tries credentials in order until one yields a token. On a laptop: environment variables for a service principal, or developer tools. In Azure: managed identity [4] [g5]. The scope `https://ai.azure.com/.default` names the audience [4] [g5] |
| a | `get_bearer_token_provider` wraps the credential in a function that returns a bearer token [4] [g5] |
| c | the function goes where the key went. No secret is in the code |

> **Pass the function.** The keyless page [4] and the chat page [24] pass the function: `api_key=token_provider`. The Responses page [23] shows both forms: `token_provider()` in one snippet, `token_provider` in two. The `openai` Python client types `api_key` as `str | Callable[[], str]` and calls the function again before each request, so the token refreshes [38] [g5]. `token_provider()` returns one string. It stops working when that token expires, about 60 to 90 minutes [25] [g5].

The Foundry-generated code in key mode leaves the key out. You set an environment variable yourself (S14) [C Foundry generated code] [g3].

> **Lab {L3} and {L13}** (cram demo). Run the basic script with the key in an environment variable. Run it again with Entra. Add a system message. Print only `.choices[0].message.content` [C Custom AI app] [g3]. Use your own resource.

### Completions versus Responses API {d5d}

**S6: two call shapes for one job.** [24][23] [g5]

| | Chat Completions | Responses |
|---|---|---|
| Call | `client.chat.completions.create(model=..., messages=[{role, content}])` | `client.responses.create(model=..., instructions=..., input=...)` |
| Read the text | `response.choices[0].message.content` | `response.output_text` |
| History | you resend it in `messages` | stateful: chain with `previous_response_id`; responses stored 30 days by default |
| Structured output | `response_format` | `text.format` |
| For new apps | still supported | Microsoft says to consider it first |

The Responses API "brings together capabilities from chat completions and the Assistants API" [23] [g5]. For reasoning models, the chat page says to use the Responses API for tool calling [24] [g5]. In the portal the Code tab switches between the two. The course describes Completions as the widely used syntax and Responses as the newer one for models and agents [E5 20:13-21:01] [g3].

> **Security.** Stored responses stay for 30 days by default and can be fetched or deleted by ID [23] [g5]. Know that before you send personal data.

> **Lab {L4}** (Ep 5, Foundry). Read the input and output tokens. Open the Code tab. Switch Completions to Responses, key to Entra, Python to REST. Watch each line change [E5 17:58-24:21] [g3].

### API keys {d5e}

A key in a header is a shared secret. Whoever holds it can call your resource [23] [g5]. Where it lives:

- An environment variable. All the docs samples read `os.getenv(...)` or `os.environ[...]` [23][17][19] [g5].
- Key Vault. Foundry stores key-based connection secrets in a managed Key Vault. You can connect your own [15] [g5].
- Never in code. Never in a git repo [C Endpoints, keys and Entra auth] [g3]. Standard practice; the docs samples follow it.

The Azure portal shows two keys, Key 1 and Key 2, under Resource Management, Keys and Endpoints. You can regenerate each [4] [g5]. Why two: regenerate one and the app keeps using the other, so you lose no access [C App integration with Foundry] [g3]. If you think a key leaked, regenerate it [C App integration with Foundry] [g3].

> **Security.** Setting up Entra does not turn keys off. The keyless page says key access still works for anyone who already has a key. To revoke, regenerate Key 1 and Key 2 [4] [g5]. To block keys for good, see "Switch keys off".

Language, Speech and Content Understanding samples use a key by default: `AzureKeyCredential`, `SPEECH_KEY`, the `Ocp-Apim-Subscription-Key` header [17][19][9] [g5].

> **Lab {L2}**: find Key 1 and Key 2 in the portal. Regenerate Key 1 on a lab resource. Confirm an old script with Key 1 now fails [C App integration with Foundry] [g3]. Use a lab resource only.

### Entra ID tokens {d5f}

Condition: the caller needs a role. Assign **Cognitive Services User** at the scope of the Foundry resource [4] [g5]. You need Owner or User Access Administrator to assign it. A role assignment can take up to 5 minutes to propagate. Group membership changes apply at once [4] [g5].

The token scope is `https://ai.azure.com/.default`. It is sent as `Authorization: Bearer <token>` [4][23] [g5]. To test by hand: `az login`, then `az account get-access-token --resource https://ai.azure.com` [4] [g5].

Why it is better: access becomes a role you grant and revoke. There is no secret to leak. In production, the keyless page says to move from `DefaultAzureCredential` to a deterministic credential such as `ManagedIdentityCredential`, or to a short `ChainedTokenCredential` [4] [g5].

> **Conflict S5.** The keyless page names Cognitive Services User for inference [4] [g5]. The architecture and guardrails pages say Foundry User, Owner, Account Owner and Project Manager are renamed from Azure AI User, Owner, Account Owner and Project Manager, with the same role IDs [15][7] [g5]. The architecture page suggests Foundry User for developers at resource scope [15] [g5]. Which role an agent call needs: I did not open the Foundry RBAC page. Open question [g1].

> **Note.** The Ep 3 lab registers an Entra app for a single-page app. It sets a redirect URI, enables implicit and hybrid flow, and adds the Cognitive Services delegated permission [E3 41:55-45:45] [g3]. Whether that is a pattern to copy: not verified [g2]. You know OAuth. Judge it. The trainer says this is not an application security course.

> **Lab {L2} and {L13}**: run the Entra script. If the call is refused, check the role on the resource first. The role is the condition [4] [g4].

### Managed identity {d5g}

A managed identity is an identity assigned to an Azure compute resource: a VM, a scale set, a Kubernetes cluster or a supported app platform. Once assigned, it can be authorized to reach other resources. It replaces secrets such as keys and passwords. Credentials "aren't even accessible to you". It costs nothing extra [13] [g5].

| | System-assigned | User-assigned |
|---|---|---|
| Created | with the Azure resource | as a stand-alone resource |
| Life | dies with the resource | independent; you delete it |
| Shared | one resource only | many resources |
| Use | one workload on one resource | many VMs, recycled resources, same permissions |

All rows [13] [g5]. In code, the same `DefaultAzureCredential` call finds the managed identity when the code runs in Azure [4] [g5]. Foundry also lists system- and user-assigned identities on the resource [E3 21:11-21:16] [g3]. Tool connections to MCP servers (section 6) can use the agent's or the project's managed identity [6] [g5].

**Choose:**

| | API key | Entra user or service principal | Managed identity |
|---|---|---|---|
| Proves | possession of a secret | who you are, via a token | which Azure resource you are, via a token |
| Secret to store | yes | a credential for the service principal; none for a signed-in user | none |
| Runs where | anywhere | laptop, CI, anywhere with a login | only on Azure compute |
| Revoke | regenerate the key | remove the role | remove the role or delete the identity |
| Audit | weak: the key has no name | sign-in and role logs | sign-in logs and Activity log [13] |
| Use when | a service has no Entra option; a quick lab | developing on your laptop | the app runs in Azure |

Rows on managed identity [13] [g5]. Other rows follow from [4][13] [g4].

```diagram-auth
Where does the code run?
  on your laptop                -> Entra user: az login. DefaultAzureCredential finds it.
  inside Azure (VM, container app, hosted agent) -> managed identity. No secret.
  anywhere else, no Entra option -> API key from an env var or Key Vault. Rotate with Key 1 and Key 2.
Then: grant Cognitive Services User at the Foundry resource. Later: switch keys off.
```

### Switch keys off {d5h}

Keyless is a resource setting as well as a code choice. The setting is `disableLocalAuth` [5][4] [g5].

```powershell
Set-AzCognitiveServicesAccount -ResourceGroupName "my-resource-group" -Name "my-resource-name" -DisableLocalAuth $true
```

- **Bicep or ARM:** set `disableLocalAuth` to `true` when you create the account [5] [g5].
- **Azure Policy:** "Azure AI Services resources should have key access disabled (disable local authentication)", at subscription or group scope [5] [g5].
- **Check:** `Get-AzCognitiveServicesAccount` and read `DisableLocalAuth`. Then send a data-plane request (a call to the service itself, not to Azure management) with the old key. You want HTTP 401 [5] [g5].
- **Reverse:** `-DisableLocalAuth $false` [5] [g5].

> **Security.** The change is immediate on the control plane. The gateway that enforces it can accept old keys until its cache refreshes. That takes minutes, and up to several hours. Do not rely on an instant cutoff when you rotate or audit [5] [g5].

When to do it: after Entra works in every app that calls the service [4] [g5]. In the Ep 3 lab the portal greys out Key 1 and Key 2 with "disabled by the resource owner" [E3 17:47-18:00; 20:14-20:32] [g3].

> **Lab {L2}**: on a lab resource, switch keys off, then confirm the key script fails and the Entra script works. Delete the resource after.

## 6. Agents {d6}

**Parts:** a model (the brain), instructions (the job description), tools (to act), knowledge (to ground answers) and an identity. **Condition:** the job needs action or data the model was not trained on. **Not when:** one prompt in, one answer out. A plain model call does that. **Failure:** give an agent every tool "to be safe". Each tool is a thing it can do in your name.

### Prompt versus hosted agent {d6a}

**Exam skill group {X4}:** create and test a single agent in the portal [1] [g5].

| | Prompt agent | Voice-based prompt agent | Hosted agent |
|---|---|---|---|
| You write | instructions, a model, tools | the same, plus audio settings | your own code, in a framework |
| Code to maintain | none | none | yes |
| Compute to manage | none | none | a container, run by Foundry |
| Endpoint | managed | managed; real-time WebSocket (a long-lived two-way connection) | managed |
| Entra identity | yes | yes | dedicated, automatic |
| Best for | fast start, no custom logic | spoken conversations | custom code and orchestration |

All rows [6] [g5]. Hosted agents use Agent Framework, LangGraph, the OpenAI Agents SDK and others. You ship a container image or a zip [6] [g5]. Private networking works for prompt agents. Hosted agents can join your own virtual network [6] [g5].

A fourth way: call the Responses API from your own code. The agent definition lives in your app. Nothing is stored in Foundry. The docs call it an ephemeral agent [6] [g5].

The cram says the same in its own words: prompt-based is no code, hosted is pro code that you package as an image [C Agents] [g3].

Choose: least to manage means a prompt agent. Full control means a hosted agent [6] [g5].

### Tools and MCP {d6b}

**Exam skill group {X4}.** Built-in tools: web search, file search, code interpreter, memory. You can add custom functions, OpenAPI specs and MCP servers [6] [g5]. A toolbox groups tools behind one managed MCP-compatible endpoint, with central authentication, governance and versioning [6] [g5]. Tools give an agent hands: knowledge tools find information, action tools do tasks [E4 12:52-13:21] [g3].

**MCP** is the Model Context Protocol, an open-source standard for connecting AI applications to data sources, tools and workflows. Think of a USB-C port for AI apps [12] [g5].

Authentication options for MCP servers and other tool connections [6] [g5]:

- key-based access
- Microsoft Entra, using the agent's or the project's managed identity
- OAuth identity passthrough (on-behalf-of)
- unauthenticated, where appropriate

> **Security.** A tool is code that acts in your name. Give the agent the narrow tool. For the Azure DevOps MCP server, the docs say you can configure a subset of tools to control which actions the agent may perform [6] [g5].

> **Lab {L4}**: add a tool to your lab agent. Read its connection settings. Note which of the four auth options it uses [E3 23:12-24:12][6] [g3].

### Knowledge and Azure AI Search {d6c}

Knowledge grounds answers in your data, not in the training data. A model alone does not know your files or your policy [E3 9:27-10:06] [g3].

Azure AI Search is a managed service that connects your data to AI. It has two engines [20] [g5]:

| | Classic search | Agentic retrieval |
|---|---|---|
| Target | one index | a knowledge base of one or more knowledge sources |
| Query | one request, no plan | an LLM plans and splits subqueries |
| Returns | ranked documents | an answer or raw data, with references |

Grounding answers on retrieved data is called retrieval-augmented generation (RAG) [20] [g5]. Queries can be full-text, vector, hybrid or multimodal [20] [g5]. Vector search uses embeddings (section 3) [21] [g5]. The docs add: LLMs and agents do not need vectors. Use them if you need similarity search [20] [g5]. Foundry IQ builds on Azure AI Search as a managed, permission-aware knowledge layer for agents [20] [g5].

In the Ep 5 lab you upload a file. Foundry builds a vector index and attaches it as a file search tool [E5 31:19-33:45] [g3]. The cram connects an agent to Azure AI Search and a knowledge base of several sources [C Looking at an agent] [g3].

Example, then one change. Ask "How much can I claim for a taxi?" with no file: the agent says it depends on company policy. Upload the policy file and ask again: the answer comes from the file [E5 29:19-34:02] [g3].

> **Security.** Azure AI Search supports Entra ID, Private Link and document-level access control [20] [g5]. A grounded agent answers from what it can read. Index only what every asker may see, or use the permission features.

> **Lab {L3} and {L4}**: add a text file as knowledge. Ask a question only the file can answer. Remove the file and ask again [E4 19:55-21:21][E5 31:19-34:02] [g3].

### Portal to client app {d6d}

The study-guide path is: create, test, call [1] [g5].

1. Test the model in the playground.
2. Save the setup as a named agent. A YAML tab appears. It holds `kind: prompt`, the model, instructions, temperature, top P and tools [E5 27:55-30:34] [g3].
3. Add a tool. File search shows `vector_store_ids` in the YAML [E5 31:48-33:41] [g3].
4. Preview the agent in the browser [E5 34:26-35:02] [g3].
5. Call it from code with the project client.

```yaml
# Illustrative shape of the Ep 5 YAML tab. Not from a doc.
kind: prompt
model: gpt-4.1-mini
instructions: You are a helpful AI assistant for employee expense claims.
temperature: ...
top_p: ...
tools:
  - type: file_search
    vector_store_ids: [ ... ]
```

The call, from the quickstart [25] [g5]:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project = AIProjectClient(                                   # 1
    endpoint="https://<resource>.services.ai.azure.com/api/projects/<project>",
    credential=DefaultAzureCredential(),
)
project.agents.create_version(                               # 2
    agent_name="MyAgent",
    definition=PromptAgentDefinition(
        model="gpt-5-mini",
        instructions="You are a helpful assistant that answers general questions",
    ),
)
openai = project.get_openai_client(agent_name="MyAgent")     # 3
conversation = openai.conversations.create()                 # 4
response = openai.responses.create(                          # 5
    conversation=conversation.id,
    input="What is the size of France in square miles?",
)
print(response.output_text)                                  # 6
```

| Line | Meaning |
|---|---|
| 1 | a project client: the project endpoint plus an Entra credential. No key |
| 2 | defines the agent as a new version: a model and instructions |
| 3 | an OpenAI client bound to the agent by name |
| 4 | a conversation holds the turns, so the agent keeps history |
| 5 | one turn; `input` is the user prompt, `conversation` links the history |
| 6 | the reply text |

The Ep 5 Python reads differently: it references the agent by name and version in the call [E5 36:15-36:57] [g3]. SDK code moves with versions (section 5). Agents are versioned, and you can publish one to a stable endpoint [6] [g5].

> **Lab {L4}**: save your setup as an agent, read the YAML, run the agent from a Python script [E5 28:07-39:41] [g3]. Delete the agent and the project after.

### Approval and agent identity {d6e}

**Approval.** In Ep 7 each tool call needs approval. The choices: approve once, always allow this tool, or always allow all tools for the agent [E7 20:11-20:48] [g3]. Ep 3 shows a different menu: the portal's "Ask AI" helper has no action, manual approval, system access and data access [E3 33:51-35:36] [g3]. They are two menus. Do not mix them.

**Identity.** Each agent can have a dedicated Microsoft Entra identity, with scoped access and no shared credentials. Agent identities can authenticate to external MCP servers. Hosted agents get one automatically [6] [g5]. An agent without a user behind it needs its own identity, so you can audit it and limit it [C Azure and Entra] [g3].

> **Security.** An acting agent is a service account. Give it least privilege. "Always allow all tools" removes the human check, so use it only on a lab agent. This is my step, from the approval choices and the RBAC rules [6][13] [g4].

### Multi-agent workflows {d6f}

Several agents can split one job. One gathers data, one summarizes, one acts [E4 13:52-14:15] [g3]. Foundry's Build menu offers workflows: sequential, human in the loop, group chat [E3 25:10-25:22] [g3]. Foundry supports the A2A protocol for agent-to-agent talk. A2A v1.0 is generally available, and v0.3 is preview [6] [g5]. Hosted agents suit multi-agent systems [6] [g5].

Know the idea. The study guide tests a single-agent solution [1] [g5].

## 7. NLP and Azure Language {d7}

**Parts:** text, a task, and an engine: a prompted model or Azure Language. **Condition:** you pick by how much you need repeatable, structured output. **Not when:** the job is a conversation about the text. That wants a model. **Failure:** answer "use GPT" to every text question.

### Text analysis tasks {d7a}

**Exam skill group {X3}:** key phrase extraction, entity detection, sentiment analysis and summarization [1] [g5].

Take one paragraph: "Alex and I attended a Microsoft AI conference. It was in Las Vegas on September 21st. The advances in AI technology are amazing." [E6 1:56-6:01] [g3]

| Task | Gives | On the paragraph |
|---|---|---|
| Key term extraction | topics | "Microsoft AI conference", "AI technology" |
| Named entity recognition (NER) | who, where, when | Alex (person), Microsoft (organization), Las Vegas (location), September 21st (date) |
| Sentiment analysis | tone | positive |
| Text classification | a category | technology; event recap |
| Summarization | the core message | "Alex attended a Microsoft AI conference in Las Vegas" |

The Language docs define the same tasks: key phrase extraction returns the main concepts as a list; sentiment finds positive or negative; named entity recognition sorts entries into predefined types; summarization is extractive (selects key sentences) or abstractive (writes new sentences) [16] [g5].

> **Lab {L5}** (Ep 6, browser). Run sentiment, entities and a summary with the small local model. Then run language detection and PII in the Language app [E6 16:39-25:12] [g3]. Same note as S13: local, small, can be wrong.

### Prompted model or Azure Language {d7b}

**Exam skill groups {X3} and {X5}** [1] [g5].

| | Prompted general model | Azure Language |
|---|---|---|
| How | one model, many tasks, one prompt | purpose-built, preconfigured features |
| Setup | none; you only ask | the models "can't be changed. You just send your data" [16] [g5] |
| Output | free text; can vary between calls | structured; repeatable |
| Cost | tokens | the cram says cheaper [C Natural Language Processing] [g3] |
| Fits | explore text, combine tasks, chat, human in the loop | automated pipelines, regulated or sensitive data |
| Code | the `openai` client | `azure-ai-textanalytics` [17] [g5] |

Rows without a cite: [E7 1:37-9:19; 14:00-14:20] [g3]. The word "deterministic" comes from the cram and Ep 7. It means: the same input gives the same output. The Language page does not use the word. Treat it as a course claim, not a documented guarantee [C Natural Language Processing][E7 8:00-8:07] [g3].

A single app can use both: a model to help people read text, Azure Language to automate decisions [E7 11:18-11:34] [g3].

Example, then one change. A support inbox: ask a model "summarize, give the sentiment, and explain the intent" in one prompt. Fine for a human reader. Now the same inbox feeds a compliance pipeline that must redact personal data in thousands of messages. Use Azure Language PII detection. You want precision, not creative variation [E7 8:12-8:34] [g3].

> **Lab {L6}** (Ep 7, Foundry). Do sentiment, entities and a summary by prompt with gpt-4.1. Then run language detection and PII redaction (text, document, conversation) with Azure Language. Read the `TextAnalyticsClient` code [E7 22:17-41:37] [g3].

### Azure Language features and code {d7c}

**Exam skill group {X5}** [1] [g5].

| Group | Features [16] [g5] |
|---|---|
| Core (recommended for new work) | PII detection, language detection, named entity recognition (prebuilt and custom), text analytics for health |
| Legacy (supported for existing use) | conversational language understanding, custom text classification, entity linking, key phrase extraction, orchestration workflow, question answering, sentiment and opinion mining, summarization |

> **Conflict S9.** The study guide names keyword extraction, sentiment and summarization as skills [1] [g5]. The Language page labels all three legacy [16] [g5]. The Ep 7 portal lab lists only language detection and PII tools under Language [E7 29:58-30:26] [g3]. The cram lists five tools: language detection, PII redaction, document PII redaction, text analytics for health, conversational PII redaction [C Natural Language Processing] [g3]. Know both views. Legacy does not mean removed: the page says "supported for existing implementations" [16] [g5].

The code, from the NER quickstart [17] [g5]:

```python
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

language_key = os.environ.get('LANGUAGE_KEY')               # 1
language_endpoint = os.environ.get('LANGUAGE_ENDPOINT')     # 2

client = TextAnalyticsClient(                               # 3
    endpoint=language_endpoint,
    credential=AzureKeyCredential(language_key),
)

documents = ["I had a wonderful trip to Seattle last week."]   # 4
result = client.recognize_entities(documents=documents)[0]     # 5
for entity in result.entities:                                 # 6
    print(entity.text, entity.category, entity.subcategory, round(entity.confidence_score, 2))
```

| Line | Meaning |
|---|---|
| 1, 2 | key and endpoint from environment variables, not literals |
| 3 | the client: the Language endpoint plus a key credential |
| 4 | a list of documents; the service takes many at once [E7 16:11-16:21] [g3] |
| 5 | runs named entity recognition; `[0]` is the result for the first document |
| 6 | each entity has text, category, subcategory and a confidence score |

Same client, other methods: `detect_language` for language detection, and a PII method for sensitive data [E7 17:11-18:14] [g3]. The quickstart authenticates with a key. Entra works for all Foundry Tools resources [5] [g5]. Agents reach Azure Language through the Azure Language MCP server, remote in the Foundry Tool Catalog or local [16] [g5].

### Preprocessing and statistics {d7d}

**Exam skill group {X3}.** Classic text pipeline [E6 6:54-10:15] [g3]:

1. Tokenize: cut text into pieces.
2. Normalize: lowercase, drop punctuation.
3. Drop stop words (the, a, it, to).
4. Stem or lemmatize: group related words (power, powered, powerful).
5. Tag part of speech (verb, noun).

Example: "We choose to go to the moon" becomes choose, go, moon [E6 9:04-9:59] [g3].

Statistical methods count words. Term frequency counts one word. TF-IDF weighs a word by how rare it is across documents. Bag of words ignores order. TextRank ranks sentences by similarity and picks the top ones for an extractive summary [E6 11:09-14:11] [g3]. Semantic models use embeddings and capture meaning [E6 14:17-16:05] [g3]. Embeddings are defined in [21] [g5].

Managed services do preprocessing for you. You need only the vocabulary [E6 10:15-10:47] [g3]. A token here means a word (see S8 in section 3) [22] [g5].

## 8. Speech {d8}

**Parts:** audio, text, and a direction. **Condition:** name the direction. Audio to text is speech recognition. Text to audio is speech synthesis. **Not when:** you need a live conversation with interruptions. That is Voice Live. **Failure:** chain recognition and synthesis yourself for a voice bot, then wonder why it feels slow.

### Speech to text and text to speech {d8a}

**Exam skill group {X3}:** features of speech recognition and synthesis [1] [g5].

| | Speech to text (recognition) | Text to speech (synthesis) |
|---|---|---|
| Direction | audio in, text out | text in, audio out |
| Modes or options | real-time (streaming), fast transcription (pre-recorded), batch (large volume, async) | standard voices, custom voices, SSML (Speech Synthesis Markup Language) to tune pitch, pronunciation, rate, volume |
| Uses | transcripts, captions, call centers, dictation | assistants, accessibility, hands-free use |

Modes and options [18] [g5]. Uses [E8 2:37-4:34] [g3]. Other Azure Speech features: speech translation, language identification, pronunciation assessment, a text-to-speech avatar [18] [g5].

Name the direction and you have named the workload [E8 2:37-4:34] [g3]. A voice assistant uses both: it listens, understands, answers aloud.

> **Lab {L7}** (Ep 8, browser). Turn voice mode on. Ask by voice. Hear the answer. The two steps are speech to text, then text to speech [E8 12:17-16:33] [g3].

### Azure Speech three ways {d8b}

**Exam skill group {X5}:** build a lightweight app with Azure Speech [1] [g5].

| Entry point | What | Use it to |
|---|---|---|
| Playground (Foundry portal) | no code; upload a file or use the microphone | explore |
| Speech SDK | config with endpoint and key, an audio config, a recognizer or synthesizer | build |
| Agent tool through MCP | the agent calls speech as a tool | automate |

Course framing [E9 1:45-4:12] [g3]. The official page lists Speech Studio (no code), the Speech SDK, the Speech CLI and REST APIs. REST suits batch transcription. MCP is not on that page [18] [g5]. Both lists are true. Know the course's three and the page's four.

Speech to text from a microphone, from the quickstart [19] [g5]:

```python
import os
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(                       # 1
    subscription=os.environ.get('SPEECH_KEY'),
    endpoint=os.environ.get('ENDPOINT'))
speech_config.speech_recognition_language = "en-US"

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)   # 2
# a file instead: speechsdk.audio.AudioConfig(filename="YourAudioFile.wav")

speech_recognizer = speechsdk.SpeechRecognizer(               # 3
    speech_config=speech_config, audio_config=audio_config)

result = speech_recognizer.recognize_once_async().get()       # 4
if result.reason == speechsdk.ResultReason.RecognizedSpeech:  # 5
    print("Recognized: {}".format(result.text))
```

| Line | Meaning |
|---|---|
| 1 | config: who you are (key) and where to connect (endpoint). Nothing is heard yet |
| 2 | audio config: where the audio comes from, a microphone or a file |
| 3 | the recognizer joins the config and the audio source |
| 4 | listen once, recognize, return the result |
| 5 | the result reason says what happened: `RecognizedSpeech`, `NoMatch` or `Canceled`; the text is in `result.text` |

Speech synthesis follows the same shape in reverse. The config adds a voice name. There is no audio config, because nothing is heard. A synthesizer takes text and returns audio [E9 11:29-13:57] [g3]. I did not open a Python synthesis sample, so I show no code for it.

> **Security.** The quickstart says to prefer Microsoft Entra ID with managed identities over stored keys in production. If you use keys, store them in Azure Key Vault [19] [g5].

### Voice Live {d8c}

Voice Live runs a real-time spoken conversation with a generative model that has instructions and tools. It handles continuous listening, speaking, background noise and interruptions [E9 15:13-17:42] [g3]. The Speech page says Voice Live provides fast, reliable interaction between a human and an agent [18] [g5]. A voice-based prompt agent uses Voice Live for recognition, turn taking, model interaction and synthesis. You connect by a real-time WebSocket [6] [g5].

| Architecture | Path | Trade-off [6] [g5] |
|---|---|---|
| Native speech-to-speech | caller audio, a realtime speech model, spoken reply | low latency, natural |
| Cascaded text model | recognition, a text model, synthesis | broader model and voice choice, more control, each stage adds latency |

Why not chain the two steps yourself: it feels clunky, with pauses and delays [E9 14:58-15:08] [g3]. The cascaded option shows that chaining is still a valid design when you need control.

Voice-based agents are in preview. Preview capabilities have no service-level agreement [6] [g5]. The Ep 9 voice-mode settings: language auto-detect, end-of-turn detection (lets natural pauses pass without ending the turn [37] [g5]; the video calls it end of utterance and semantic VAD [g3]), audio enhancement, phrase list, voice temperature from 0 to 1, playback speed, custom lexicon, interim responses, proactive engagement, avatar [E9 20:44-24:00] [g3].

> **Lab {L8}** (Ep 9, Foundry). Create a speech agent. Turn on voice mode. Pick a voice. Read the YAML and the Voice Live code [E9 17:48-28:35] [g3].

### Speech pipelines {d8d}

**Exam skill group {X3}.** Both pipelines are from Ep 8 [E8 5:50-11:46] [g3].

| Recognition (audio to text) | Synthesis (text to audio) |
|---|---|
| capture audio as a digital waveform | normalize the text ("Dr." becomes "doctor"; times and numbers are made speakable) |
| featurize: compact set of features | map words to phonemes (the smallest sound units) |
| acoustic model: features to phonemes | prosody: pitch, rhythm, stress, pauses |
| language model: pick the likely words in context | generate the audio waveform |
| post-process: capitals, punctuation, numbers | |

Example: "cat" has three phonemes. Two words can sound the same. The language model picks the one that fits the context [E8 7:23-8:18] [g3].

## 9. Computer vision and generation {d9}

**Parts:** an image or video, a question about it, and a model. **Condition:** pick the task by the question. **Not when:** you need to create pixels. That is generation (diffusion), not recognition. **Failure:** use object detection when you need one label, or classification when you need a box.

### Vision tasks {d9a}

**Exam skill group {X3}.**

| Task | Question it answers | Output | Example |
|---|---|---|---|
| Image classification | what is this? | one label for the whole image | apple or orange; damaged or normal product |
| Object detection | what and where? | a label and a box for each object | bananas on a shelf |
| Semantic segmentation | exactly which pixels? | a label for every pixel | organs in a scan; roads and buildings in satellite images |
| Contextual image analysis | what is happening? | a caption or tags | "a person eating an apple" |

Rows on segmentation and contextual analysis [E10 1:21-5:28][C Computer vision] [g3]. For classification and detection the docs agree: classification applies labels to an entire image, and detection returns the coordinates where the labels are found [27] [g5].

> **Note.** The Custom Vision page announces retirement, with full support until 25 September 2028. It points to Azure Machine Learning AutoML, Foundry models, or Content Understanding for custom classification [27] [g5]. The exam tests the concepts, not that service.

> **Lab {L9}** (Ep 10, browser). Enable image analysis. Ask a question about a photo. Your question maps to one of the four tasks [E10 12:52-16:20] [g3].

### Multimodal prompts {d9b}

**Exam skill group {X6}:** interpret visual input in prompts with a deployed multimodal model [1] [g5].

A multimodal chat model takes text and an image in one prompt and answers in text. It reads both together [E11 2:10-4:41] [g3]. The image goes in as a URL, or as base64: the image converted to text that the API can send [E11 3:27-3:55] [g3]. The code, from the Responses page [23] [g5]:

```python
import base64, os
from openai import OpenAI

client = OpenAI(
    base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

with open("path_to_your_image.jpg", "rb") as image_file:                  # 1
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

response = client.responses.create(
    model="MODEL_NAME",                                                    # 2
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "What is in this image?"},     # 3
            {"type": "input_image",
             "image_url": f"data:image/jpeg;base64,{base64_image}"},       # 4
        ],
    }],
)
print(response.output_text)                                                # 5
```

| Line | Meaning |
|---|---|
| 1 | read the file as bytes and encode it as base64 text |
| 2 | your deployment name; the model must accept images |
| 3 | one content part: the text instruction |
| 4 | the second part: the image, as a data URI. With a URL, put `"<image_url>"` here |
| 5 | the text reply |

The prompt has several parts: a structured prompt [E11 4:18-4:22] [g3]. Uses: screenshots of errors, product images, charts and scans [E11 4:47-5:19] [g3].

> **Security.** Text inside an image is input the model reads. Treat it as untrusted, like a tool response. I found no source that says this; it follows from the indirect-attack risk (section 4) [g2]. Not verified.

> **Labs {L9} and {L10}**: in Foundry, send text and an image to gpt-4.1-mini. Read the base64 code [E11 8:39-15:10] [g3].

### Image and video generation {d9c}

Search the catalog by task, not by model name: text to image, image to image, video [E11 5:34-6:30] [g3]. The course uses GPT image, FLUX.2-pro, FLUX.1-Kontext-pro and sora-2. Sora made a four-second clip, in 16:9 or 9:16 [E11 16:20-24:03] [g3]. I did not open pages for FLUX or sora-2.

Names change (S15). The image docs say `dall-e-3` was retired on 4 March 2026. Use a `gpt-image-` series model instead [26] [g5]. Choose by task, quality, and cost with latency: a quick draft or a production visual [E11 7:34-8:11] [g3].

The image guide builds the client with `AzureOpenAI(api_version="2025-04-01-preview", azure_endpoint=...)`. The `OpenAI(base_url=.../openai/v1/)` client from section 5 also works for its streaming sample [26] [g5]. The call:

```python
import base64, os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2025-04-01-preview",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

result = client.images.generate(
    model="gpt-image-1",        # the name of your GPT-image series deployment
    prompt="a close-up of a bear walking through the forest",
    n=1, size="1024x1024", quality="high", output_format="png",
)
image_bytes = base64.b64decode(result.data[0].b64_json)   # gpt-image models return base64
```

`model` is again the deployment name (S1). The response carries base64 data, not a URL [26] [g5]. Ep 11 shows the same call with model, prompt and size [E11 20:52-21:08] [g3]. The cram lists the options of a GPT image deployment: resolution, quality, compression, format, number of variations and an optional source image. A source image makes the call multimodal [C Image and video generation] [g3].

> **Lab {L10}**: generate images with two models and a short video. Compare. Read the `images.generate` code [E11 16:20-24:03] [g3].

### Diffusion models {d9d}

**Exam skill group {X6}.**

```diagram-diffusion
training:    photo -> +noise -> +noise -> +noise -> ... -> pure noise
                      the model learns to undo each step
generation:  pure noise -> less noise -> less noise -> ... -> image
                      each step is guided by the prompt
video:       the same, over a sequence of frames, kept consistent in time
```

Training adds noise to an image in steps until only noise is left. The model learns to reverse each step [E10 10:09-11:05][C Image and video generation] [g3]. Generation starts from pure noise. The model removes noise step by step. The prompt guides which features to keep [E10 11:05-11:54] [g3]. Video repeats this across frames and keeps motion consistent [E10 11:58-12:14] [g3].

Example: the prompt "a dog carrying a stick in a park". Each step favors dog shapes, fur texture, grass and trees [E10 11:40-11:54] [g3].

The name: "Denoising Diffusion Probabilistic Models" describes a class of latent variable models inspired by nonequilibrium thermodynamics. The abstract gives the name and results. It does not teach the training story [30] [g5]. The name is verbatim; nothing else on the page covers training.

Why it matters: many small steps cost time. Video takes longer than a still [E11 22:51-22:59] [g3].

### CNN versus vision transformer {d9e}

**Exam skill group {X3}.**

| | CNN | Vision transformer (ViT) |
|---|---|---|
| Idea | slide filters over the image; detect edges, shapes, texture | cut the image into patches; turn each into a vector; use attention |
| Middle | feature maps, flattened into a fully connected network | patch vectors related to each other by attention |
| Output | probabilities, such as 80% water bottle | the same kind of prediction, with global context |
| Sees | local patterns | relations across the whole image |
| Learns from | thousands of labeled images | the same, at large scale |

CNN and ViT detail [E10 5:32-9:35] [g3]. The ViT paper: "a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks" [29] [g5]. It reports results competitive with convolutional networks [29] [g5].

Remember one contrast: local patterns versus global context [E10 9:15-9:25] [g3]. ViT uses attention, the same idea as section 3 [28][29] [g5].

## 10. Information extraction {d10}

**Parts:** content (document, image, audio, video), a reading step (OCR or transcription), a schema of fields, and structured output. **Condition:** you need data a system can store, not text a person reads. **Not when:** you want a free-form chat answer from a document. A model does that. **Failure:** stop at OCR and call the job done. OCR gives text, not meaning.

### OCR {d10a}

**Exam skill groups {X3} and {X7}** [1] [g5].

OCR (optical character recognition) reads text from images, scans, screenshots and video frames. It gives text, not meaning. It does not know that 23.50 is a total. It just reads it [E12 4:23-8:37] [g3]. It is the first step of most document flows.

In Content Understanding, content extraction reads text with OCR, finds selection marks and barcodes, detects formulas, and recognizes layout: paragraphs, sections, tables [8] [g5].

OCR process [E12 6:33-7:35] [g3]: capture the image; clean it (noise, contrast, rotation, blur); locate where text sits; recognize characters; assemble words and sentences.

Example: a business card. OCR returns a name, a number and an email as raw text. It does not know which one is the phone [E12 7:49-8:06] [g3].

> **Lab {L11}** (Ep 12, browser). Run the receipt extractor. The receipt shows OCR first, then field extraction [E12 12:57-16:17] [g3]. Same note as S13: a local model, not the Azure service.

### Field extraction {d10b}

**Exam skill group {X7}.** OCR says what text exists. Field extraction says what it means [E12 8:43-9:10] [g3].

Example: OCR gives "Contoso Coffee, 15 August, 6.97". Field extraction gives vendor = Contoso Coffee, date = 15 August, total = $6.97 [E12 9:10-9:47] [g3].

The five steps [E12 10:01-12:09] [g3]:

1. Take the OCR output: the text, its position and confidence scores.
2. Detect candidate fields by pattern and position.
3. Map candidates to named fields, using context and position.
4. Normalize: one date format, standard currency.
5. Send to a business system: a database, accounting, a workflow.

Position matters. The number 12345 can be an invoice number, a customer ID or a phone number, depending on where it sits [E12 10:20-10:33] [g3].

In Content Understanding, field extraction "generates structured key-value pairs based on your defined schema". A field is made by one of three methods [8] [g5]:

| Method | What it does | Example |
|---|---|---|
| Extract | takes the value as it appears; documents only | a date from a receipt |
| Classify | picks from a fixed set of categories | call sentiment, chart type |
| Generate | writes a value from the input | a summary of a call, a scene description |

### Content Understanding analyzers {d10c}

**Exam skill group {X7}:** extract from documents, images, audio and video, and build a client app [1] [g5].

Content Understanding is a Foundry Tool inside the Foundry resource. It uses generative AI to turn documents, images, video and audio into a user-defined output format [8] [g5]. The **analyzer** is the core: it sets the extraction settings, the field schema and the model deployments [8] [g5].

| | Prebuilt analyzer | Custom analyzer |
|---|---|---|
| For | common content: invoices, receipts, forms, call center, media | your own forms and reports |
| You do | upload and run | define a schema and give samples |
| Example | `prebuilt-invoice`, `prebuilt-imageSearch`, `prebuilt-audioSearch`, `prebuilt-videoSearch` [9] [g5] | project name, approval status, budget [E13 3:04-3:41] [g3] |

Output is Markdown or JSON that matches your schema. Each field can carry a confidence score from 0 to 1, and grounding: the region of the source where the value was found [8] [g5].

The REST call is asynchronous. A POST returns 202 with an `Operation-Location` header. You poll that URL until `status` is `Succeeded` [9] [g5]:

```bash
curl -i -X POST "{endpoint}/contentunderstanding/analyzers/prebuilt-invoice:analyze?api-version=2025-11-01" \
  -H "Ocp-Apim-Subscription-Key: {key}" \
  -H "Content-Type: application/json" \
  -d '{"inputs":[{"url": "https://example.test/invoice.pdf"}]}'
# 202 Accepted + Operation-Location -> GET that URL until status is Succeeded
```

The Python SDK hides the polling [9] [g5]:

```python
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput
from azure.core.credentials import AzureKeyCredential

client = ContentUnderstandingClient(endpoint=endpoint, credential=AzureKeyCredential(key))   # 1
poller = client.begin_analyze(analyzer_id="prebuilt-invoice",
                              inputs=[AnalysisInput(url=invoice_url)])                        # 2
result = poller.result()                                                                      # 3
```

| Line | Meaning |
|---|---|
| 1 | a client: the endpoint and a key |
| 2 | starts the analysis with a chosen analyzer; returns a poller, not the answer |
| 3 | waits for the job, then gives the result: fields, confidence, markdown |

Use API version `2025-11-01` (GA) for production. `2026-06-01-preview` is for new features [8] [g5]. In the Foundry portal you see Content Understanding, Read and Layout under AI Services [E13 8:41-12:23] [g3].

| | Content Understanding | A prompted generative model |
|---|---|---|
| Output | JSON by your schema, with confidence and grounding | free text unless you force a format |
| Setup | prebuilt analyzer, or a schema | a prompt |
| Checks | confidence scores let you skip manual review | you check each answer |

Output and setup [8] [g5]. The cram adds that a generative model "could" do the job, but consistency and accuracy vary [C Information extraction] [g3].

> **Security.** The analyzer calls a generative model deployment. That deployment's guardrail applies. Blocking can limit field extraction, and a run can succeed with warnings even when some fields are missing. Read the warnings before you use results in an automated flow [8] [g5].

> **Lab {L12}** (Ep 13, Foundry). Open Content Understanding. Run Read and Layout on a sample. Read the JSON. Run an audio analyzer. Read the code [E13 7:27-15:25] [g3].

### Audio and video extraction {d10d}

**Exam skill group {X7}:** extract from audio and video [1] [g5].

Same platform, same analyzer idea. Only the input changes [E13 5:41-5:56] [g3].

| Input | Typical output |
|---|---|
| Audio | transcript, key topics, summary |
| Video | key moments, spoken content, activity segments |

Examples and use [E13 4:44-7:00] [g3]. The docs: for audio and video, content extraction transcribes speech and identifies key visual elements. Segmentation can split a video into scenes [8] [g5]. Output is structured JSON [E13 6:57-7:00] [g3].

> **Open question S10.** The cram says purpose-built models are "more deterministic" than an LLM [C Information extraction] [g3]. The Content Understanding page says the service "uses generative AI". It also says it uses multiple models that "cross-validate" the result [8] [g5]. Both are shown. They are not settled. Treat the cram's claim as unverified [g1].

> **Note.** The Custom Vision page calls Content Understanding "currently in public preview" [27] [g5]. [27] is the stale page: its front matter is dated 2025-03-26. [8] is current and lists `2025-11-01` as GA [g5].

> **Lab {L12}**: run an audio analyzer on a sample call recording. Find the transcript and the topics in the JSON [E12 13:25-13:49] [g3].


## References

Every link below was opened on 2026-10-12 in this run. Each line gives the title, publisher, URL, the part read, the date accessed, the source type, and what it settles. "Partly" means the fetch cut off the page, and I name what I read.

### Web sources

- [1] Study guide for Exam AI-901. Microsoft Learn. https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901 . Section "Skills measured as of April 15, 2026". Accessed 2026-10-12. Type: official. Settles: skills list, 40 to 45 and 55 to 60 percent, 700 pass mark, REST, SDK and CLI note, practice assessment.
- [2] Exam AI-901: Microsoft Azure AI Fundamentals. Microsoft Learn. https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-901/ . Accessed 2026-10-12. Type: official. Settles: the stale blurb, the "Assessed on this exam" list, passing score.
- [3] Understanding deployment types in Microsoft Foundry Models. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types . Whole page. Accessed 2026-10-12. Type: official. Settles: the type table, data residency, PTU, Priority and Flex, batch, instant access, the Azure Policy example.
- [4] Configure keyless authentication with Microsoft Entra ID. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/configure-entra-id . Partly (Python, portal and CLI pivots, role section, disable section; not the C#, Java or JavaScript tabs). Accessed 2026-10-12. Type: official. Settles: Cognitive Services User role, scope `https://ai.azure.com/.default`, `DefaultAzureCredential` code, regenerate keys, disable key auth.
- [5] Disable local authentication in Foundry Tools. Microsoft Learn. https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth . Whole page. Accessed 2026-10-12. Type: official. Settles: `disableLocalAuth`, the PowerShell cmdlet, the Azure Policy name, the propagation delay, the 401 check.
- [6] What is Microsoft Foundry Agent Service? Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/agents/overview . Accessed 2026-10-12. Type: official. Settles: agent types, tools, toolbox, MCP auth options, agent identity, A2A, voice agents, Responses API as ephemeral agent.
- [7] Guardrails and controls overview in Microsoft Foundry. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview . Whole page. Accessed 2026-10-12. Type: official. Settles: controls, risks, intervention points, actions, severity, DefaultV2, agent override, role rename.
- [8] What is Azure Content Understanding in Foundry Tools? Microsoft Learn. https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview . Whole page. Accessed 2026-10-12. Type: official. Settles: analyzers, modalities, field extraction methods, confidence, grounding, generative AI use, API versions, guardrails.
- [9] Content Understanding REST API quickstart. Microsoft Learn. https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/quickstart/use-rest-api . Partly (100k of 141k characters; document, image, audio and video tabs, Python and REST). Accessed 2026-10-12. Type: official. Settles: the analyze call, analyzer IDs, async polling, the Python client.
- [10] Responsible AI for Microsoft Foundry. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/responsible-use-of-ai-overview . Whole page. Accessed 2026-10-12. Type: official. Settles: Discover, Protect, Govern. It does not list the six principles.
- [11] Identify guiding principles for responsible AI. Microsoft Learn training unit. https://learn.microsoft.com/training/modules/embrace-responsible-ai-principles-practices/3-identify-guiding-principles-responsible-ai . Whole unit. Accessed 2026-10-12. Type: official. Settles: the six principles and what each asks.
- [12] What is the Model Context Protocol (MCP)? modelcontextprotocol.io. https://modelcontextprotocol.io/docs/getting-started/intro . Whole page. Accessed 2026-10-12. Type: primary. Settles: the MCP definition and the USB-C analogy.
- [13] Managed identities for Azure resources. Microsoft Entra docs. https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview . Whole page. Accessed 2026-10-12. Type: official. Settles: definition, system-assigned and user-assigned table, no credentials to manage.
- [14] What is Azure Resource Manager? Microsoft Learn. https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview . Sections "Understand scope", "What is a resource group?". Accessed 2026-10-12. Type: official. Settles: four scopes, inheritance, resource group rules.
- [15] Microsoft Foundry architecture. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture . Whole page. Accessed 2026-10-12. Type: official. Settles: resource and project split, RBAC split, resource types, Key Vault, the "single region" wording, role rename.
- [16] What is Azure Language in Foundry Tools. Microsoft Learn. https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview . Whole page. Accessed 2026-10-12. Type: official. Settles: core and legacy features, preconfigured, task definitions, MCP server.
- [17] Quickstart: Use the NER client library. Microsoft Learn. https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/quickstart?pivots=programming-language-python . Python pivot only. Accessed 2026-10-12. Type: official. Settles: `TextAnalyticsClient` code, package name, `LANGUAGE_KEY` and `LANGUAGE_ENDPOINT`.
- [18] What is Azure Speech? Microsoft Learn. https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview . Whole page. Accessed 2026-10-12. Type: official. Settles: speech to text modes, text to speech, SSML, Voice Live, SDK, CLI and REST.
- [19] Speech to text quickstart, Python. Microsoft Learn. https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text?pivots=programming-language-python . Partly (the text-to-speech part was cut off). Accessed 2026-10-12. Type: official. Settles: the recognizer code, key and Entra advice.
- [20] Introduction to Azure AI Search. Microsoft Learn. https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search . Whole page. Accessed 2026-10-12. Type: official. Settles: classic search, agentic retrieval, query types, security features, Foundry IQ.
- [21] Azure OpenAI embeddings (classic portal page). Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry-classic/openai/concepts/understand-embeddings . Whole page. Accessed 2026-10-12. Type: official. Settles: embedding definition, cosine similarity, classic-only note.
- [22] Understanding tokens. Microsoft Learn, .NET docs. https://learn.microsoft.com/en-us/dotnet/ai/conceptual/understanding-tokens . Whole page. Accessed 2026-10-12. Type: official. Settles: token definition, tokenization methods, context window, next-token loop, pricing and rate limits.
- [23] Responses API in Foundry. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses . Partly (first 100k of 151k characters, plus a second read for image input). Accessed 2026-10-12. Type: official. Settles: Responses code, REST path, `api-key` header, stateful design, 30-day retention, image input code.
- [24] Work with chat completion models. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/chatgpt . Partly (the Python code, system role, reasoning-model note and Responses tip; I did not read the whole page). Accessed 2026-10-12. Type: official. Settles: Chat Completions code, `response.choices[0].message.content`, roles, deployment name, reasoning models skip temperature.
- [25] Quickstart: Get started with Microsoft Foundry SDK. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code . Whole page, Python tabs read. Accessed 2026-10-12. Type: official. Settles: project endpoint form, `AIProjectClient`, agent create and chat code, 2.x versus 1.x.
- [26] How to use image generation models from OpenAI. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/dall-e . Partly (visible text up to 100k characters). Accessed 2026-10-12. Type: official. Settles: dall-e-3 retired, gpt-image models, `images.generate` code, base64 result.
- [27] What is Custom Vision? Microsoft Learn. https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview . Whole page. Accessed 2026-10-12. Type: official. Settles: classification versus detection, the retirement notice, the stale "public preview" line.
- [28] Attention Is All You Need. Vaswani et al. https://arxiv.org/abs/1706.03762 . Abstract only. Accessed 2026-10-12. Type: primary. Settles: the Transformer is based solely on attention.
- [29] An Image is Worth 16x16 Words. Dosovitskiy et al. https://arxiv.org/abs/2010.11929 . Abstract only. Accessed 2026-10-12. Type: primary. Settles: a pure transformer on image patches, competitive with CNNs.
- [30] Denoising Diffusion Probabilistic Models. Ho, Jain, Abbeel. https://arxiv.org/abs/2006.11239 . Abstract only. Accessed 2026-10-12. Type: primary. Settles: the name and the class of model. It does not teach the training story.
- [31] Get started with AI applications and agents on Azure. Microsoft Learn learning path. https://learn.microsoft.com/en-us/training/paths/get-started-ai-apps-agents/ . Whole page. Accessed 2026-10-12. Type: official. Settles: the seven modules.

- [32] Harm categories and severity levels in Microsoft Foundry. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-severity-levels . Severity table and the Safe-level sentence. Accessed 2026-10-12. Type: official. Settles: Low flags at low and higher, labelled least restrictive; Safe is annotated, never blocked.
- [33] How to configure content filters (classic). Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry-classic/foundry-models/how-to/configure-content-filters . Intro and default filtering paragraph. Accessed 2026-10-12. Type: official. Settles: default Medium threshold filters medium and high, not low.
- [34] Prompt Shields in Microsoft Foundry. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields . Whole page. Accessed 2026-10-12. Type: official. Settles: user prompt attacks, document attacks and where they are scanned, spotlighting.
- [35] Groundedness Detection Filter. Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-groundedness . Whole page. Accessed 2026-10-12. Type: official. Settles: the groundedness definition.
- [36] Agentic Workflows Task Adherence (preview). Microsoft Learn. https://learn.microsoft.com/en-us/azure/foundry/guardrails/task-adherence . Whole page. Accessed 2026-10-12. Type: official. Settles: what task adherence detects.
- [37] Voice Live API Overview. Microsoft Learn. https://learn.microsoft.com/en-us/azure/ai-services/speech-service/voice-live . Whole page. Accessed 2026-10-12. Type: official. Settles: advanced end-of-turn detection, WebSocket events. It does not define semantic VAD.
- [38] openai-python, `_client.py`. GitHub. https://github.com/openai/openai-python/blob/main/src/openai/_client.py . The `api_key` annotation and `_refresh_api_key`. Accessed 2026-10-12. Type: primary. Settles: `api_key` accepts a function that is called before each request.

### Course transcripts (case documents, his own files, read only)

Type: case. The transcripts are auto-captions. Where a claim rests on one alone, it carries grade 3. Episode numbers follow the file headers. The times are the video times.

- [C] `00_ai_901_cram_exam_transcript.md`. The exam cram. Cited with its section heading.
- [E1] `02_...course_introduction_ep_1.md`. [E2] `03_...ai_concepts_ep_2.md`. [E3] `04_...get_started_with_ai_in_azure_ep_3.md`. [E4] `05_...generative_ai_and_agents_ep_4.md`. [E5] `06_...get_started_with_generative_ai_and_agents_in_azure_ep.md`. [E6] `07_...natural_language_processing_concepts_.md`. [E7] `08_...text_analysis_in_azure_ep_7.md`. [E8] `09_...ai_speech_concepts_ep_8.md`. [E9] `10_...speech_in_azure_ep_9.md`. [E10] `11_...computer_vision_concepts_ep_10.md`. [E11] `12_...computer_vision_in_azure_ep_11.md`. [E12] `13_...information_extraction_concepts_ep_12.md`. [E13] `14_...information_extraction_in_azure_ep_1.md`. [E14] `15_...course_closing_ep_14.md`.
- `01_...course_preview.md` was read. It is not cited.

### Not opened, so not claimed

The Learn exercise pages for L1 to L12 (the steps come from the videos). The Foundry RBAC page (S5 stays open). The practice assessment (sign-in needed). The Python SDK source for token refresh. A Python text-to-speech sample. Prices, quotas, model lifecycles and region lists. FLUX and sora-2 model pages.
