# 📍 Google Local API: Local Pack Business Listings in Clean JSON

> The efficient, reliable, and developer-friendly way to use the Google Local API.

**Actor page:** [apify.com/johnvc/google-local-api](https://apify.com/johnvc/google-local-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/google-local-api/input-schema](https://apify.com/johnvc/google-local-api/input-schema?fpr=9n7kx3)

The Google Local API returns the businesses Google shows in the local pack of its Search results for a query and location, as clean, structured JSON: title, rating, review count, price level, address, GPS coordinates, business type, and a stable `place_id`. Target by city-level location, country, language, and Google domain, and page through results. Built for local SEO, lead lists, market research, and AI agent workflows.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-Local-API.git
   cd Apify-Google-Local-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python google-local-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-local-api-example.py
```

## Why Use This Google Local API?

**The local pack, structured.** Get the ranked businesses Google shows for a local query, with rating, reviews, price, address, and GPS, as clean JSON.

**Stable place IDs.** Every listing carries a `place_id` you can store, dedupe on, or feed into other place lookups.

**Geo-targeted.** Target by city-level `location` (or an advanced `uule`), country (`gl`), language (`hl`), and Google domain.

**Device-aware.** Emulate desktop (about 20 results per page) or mobile (about 10) and control depth with `max_pages`.

**Predictable, pay-per-use pricing.** Billing is per page processed, with a small per-run fee and no subscription.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can run local searches for you on demand.

## Features

### Core Capabilities
- Local-pack business listings for any query and location
- City-level location targeting, plus advanced `uule` and `ludocid`
- Country, language, and Google-domain localization
- Device emulation (desktop, tablet, mobile)
- Pagination with a configurable page cap

### Data Quality
- One item per page, each with a `local_results` array
- Title, rating, review count, price level, type, address, and GPS per business
- Stable `place_id` on every listing
- Search parameters and result counts echoed on every item

## Usage Examples

### Basic local search
```json
{
  "q": "coffee",
  "location": "Austin, Texas, United States",
  "max_pages": 1
}
```

### Localized search (UK)
```json
{
  "q": "plumbers",
  "location": "London, United Kingdom",
  "google_domain": "google.co.uk",
  "gl": "uk",
  "hl": "en"
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `q` | `str` | Yes | - | Local search query, e.g. `coffee`, `dentists near me`. |
| `location` | `str` | No | - | City-level location, e.g. `Austin, Texas, United States`. Cannot combine with `uule`. |
| `uule` | `str` | No | - | Advanced Google-encoded location for precise targeting. |
| `google_domain` | `str` | No | `google.com` | Google domain, e.g. `google.co.uk`. |
| `gl` | `str` | No | `us` | Country code (ISO 3166-1 alpha-2). |
| `hl` | `str` | No | `en` | Language code (ISO 639-1). |
| `ludocid` | `str` | No | - | Advanced: place CID to narrow around one business. |
| `tbs` | `str` | No | - | Advanced Google filter string. |
| `device` | `str` | No | `desktop` | `desktop` (~20/page), `tablet`, or `mobile` (~10/page). |
| `max_pages` | `int` | No | `1` | Pages to fetch; `0` = unlimited (safety-capped). Each page is billed. |

## Output Format

A real `coffee` search in Austin returns one item per page, each with a `local_results` array (trimmed to a single business here).

```json
{
  "search_parameters": { "q": "coffee", "location": "Austin, Texas, United States", "max_pages": 1 },
  "search_metadata": { "pages_processed": 1, "max_pages_set": 1, "pagination_limit_reached": true, "total_results_estimate": null },
  "page_number": 1,
  "local_results": [
    {
      "position": 1,
      "title": "Black Fox Coffee",
      "type": "Coffee shop",
      "rating": 4.7,
      "reviews": 23,
      "price": "$1-10",
      "address": "323 W 6th St",
      "place_id": "4198181583016835484",
      "gps_coordinates": { "latitude": 30.268645, "longitude": -97.746054 }
    }
  ],
  "ads_results": [],
  "local_map": { "gps_coordinates": { "latitude": 30.268645, "longitude": -97.746054 } }
}
```

Each page item echoes the `search_parameters`, reports `search_metadata` (pages processed and result estimate), and lists every local-pack business in `local_results` with its position, title, type, rating, review count, price level, address, `place_id`, and GPS coordinates. A `local_map` center and any `ads_results` are returned alongside.

---

## Use as an MCP tool

You can load the Google Local API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/google-local-api
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Google Local API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/google-local-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google Local API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-local-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-local-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google Local API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/google-local-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/google-local-api`, using OAuth when prompted.
5. Ask Claude to run the Google Local API.

Open Claude on the web: https://claude.ai/referral/uIlpa7nPLg

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-local-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-local-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google Local API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/google-local-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

## Use it from n8n

There is a free, ready-made n8n template built on this API: [Track Google local pack rankings in Google Sheets](https://n8n.io/workflows/17523-track-google-local-pack-rankings-in-google-sheets-with-apify/). Put your keywords, city, and business name in one node, and every week it appends the full local pack for each keyword to a sheet: position, business, category, rating, review count, and address, with your own listing flagged YES. It uses the official Apify node, so it works on n8n Cloud with a live preview.

Because it logs the whole pack rather than only your own rank, the sheet doubles as a competitor watch: you can see who moved above you and what their review count looks like. No rank tracker subscription and no SERP API key.

Self-hosting n8n? There is also a dedicated community node: [`n8n-nodes-google-local-api`](https://www.npmjs.com/package/n8n-nodes-google-local-api) on npm.

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google Local API to power local SEO, lead generation, and market research with reliable, structured results.*

## Featured Tasks

Ready-to-run examples on the Apify Store.

- [Export Google Local Results to CSV](https://apify.com/johnvc/google-local-api/examples/export-google-local-results-to-csv?fpr=9n7kx3)

Last Updated: 2026.08.10
