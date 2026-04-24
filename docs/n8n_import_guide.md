# n8n Import Guide

1. Open n8n
2. Import `n8n/antigravity_auto_pipeline.json`
3. Set environment variables:
   - ANTIGRAVITY_LLM_ENDPOINT
   - YOUTUBE_API_KEY
   - ANTIGRAVITY_TOPIC_SEED
4. Connect your LLM endpoint
5. Connect your publishing and analytics endpoints
6. Run on a cron schedule

Workflow overview:
CRON -> YouTube Search -> Prompt Builder -> LLM Call -> Brief Output