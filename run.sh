BASE_URL="https://$CODESPACE_NAME-1315.app.github.dev/"
hugo server -D --bind 0.0.0.0 --port 1315 --baseURL "$BASE_URL" --appendPort=false