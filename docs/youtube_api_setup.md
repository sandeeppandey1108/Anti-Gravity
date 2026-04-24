# YouTube API Setup

1. Create a Google Cloud project
2. Enable:
   - YouTube Data API v3
   - YouTube Analytics API
3. Create OAuth consent screen
4. Create OAuth Client ID for Desktop App
5. Download credentials JSON
6. Store it in:
   `credentials/youtube_oauth.json`

Environment variables:
- YOUTUBE_API_KEY
- YOUTUBE_CLIENT_SECRETS

Recommended packages:
- google-api-python-client
- google-auth
- google-auth-oauthlib
- google-auth-httplib2