if [ -n "$CODESPACE_NAME" ]; then
  BASE_URL="https://$CODESPACE_NAME-1314.app.github.dev/"
else
  BASE_URL="http://localhost:1314/"
fi

hugo server -D --bind 0.0.0.0 --port 1314 --baseURL "$BASE_URL" --appendPort=false