# 🚀 Multi-Agent Career Tracker Engine

An enterprise-grade, zero-cost autonomous career pipeline engineered in n8n. This system uses multi-agent orchestration to scrape job listings, run objective semantic alignment gap analyses against a master profile, and instantly generate highly tailored application assets.

---

## 🏗️ Execution Pipeline Architecture

*   [Step 1] Chat Trigger Link Input ➔ Receives raw job posting URL string payloads.
*   [Step 2] Input Filter Guard ➔ Executes strict Regex syntax verification checks to isolate URLs.
*   [Step 3] 60s Throttling Delay ➔ Pauses pipeline execution loops to shape traffic and protect API limits.
*   [Step 4] Job Scraper AI Node ➔ Extracts core title, description, and instruction elements via Apify automation.
*   [Step 5] Airtable Staging Nodes ➔ Maps, relates, and updates staging records across Companies and Jobs tables.
*   [Step 6] Analyst Gatekeeper Node ➔ Computes non-inflated mathematical alignment matrix match scoring.
*   [Step 7] n8n Conditional IF Gate ➔ Directs path routing based on the target score parameters:
    *   TRUE Path (Score >= 80%) ➔ Instantiates tailored Google Doc resume copies and builds platform outreach pitches.
    *   FALSE Path (Score < 80%) ➔ Drops asset creation, logging keyword deficits to Airtable 3 and pushing Telegram alert cards.

---

## 🤖 AI Agent Configuration Matrix

| Agent Component | Core Production Model | Fallback Model | Operating Temp | Execution Mandate |
| :--- | :--- | :--- | :--- | :--- |
| Agent 1: Job Scraper | openrouter/free | Native Scraping Webhooks | 0.0 | Parse web markup into rigid paragraph schemas without markdown artifacts. |
| Agent 2: Job Analyst | nvidia/nemotron-3-super-120b-a12b:free | gemini-2.5-flash | 0.0 | Compute strict, non-inflated mathematical alignment match indexing. |
| Agent 3: Resume Writer | qwen/qwen3-coder:free | groq/llama-3.3-70b-versatile | 0.4 | Reframe background roles using clean engineering metrics and active voice verbs. |
| Agent 4: Proposal Writer | meta-llama/llama-3.3-70b-instruct:free | gemini-2.5-flash | 0.5 | Compose natural, platform-native outreach pitches matching the user's authentic tone. |

---

## 🛠️ Relational Database Schema (Airtable)

The database framework enforces clean data states, ensuring missing data attributes resolve directly to safe JavaScript null indicators rather than static placeholder string blocks like "None".

*   Table 1: Companies ➔ Aggregates historic hiring entities tracking continuous corporate applicant pipelines via unique primary indexes.
*   Table 2: Jobs ➔ Manages structural job metadata records, linking scraped tracking properties back to specific Company profile entries.
*   Table 3: Resumes & Analysis ➔ The primary relational ledger tracking individual pipeline attempts. Generates conditional web view links for successful resume files on the True Path, while logging arrays of missing competencies on the False Path.

---

## 🚀 Setup & Environment Deployment

### Prerequisites
* A running n8n instance (Cloud or self-hosted)
* API accounts and credential arrays configured for: OpenRouter, Groq, Google Drive, Google Docs, Airtable, and Telegram.

### Installation & Import
1. Clone this repository to your local architecture workstation directory.
2. Download your sanitized JSON configuration asset file.
3. Open your n8n workspace dashboard, select Import from File..., and choose the file.
4. Open the node configuration windows to connect your secure authentication vaults to the respective API integrations.
5. Update the variable parameters in your "Get my knowledge base" and database nodes to target your specific workspace IDs.
