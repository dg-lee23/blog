hugo server -D --bind 0.0.0.0 --baseURL "https://$CODESPACE_NAME-1313.app.github.dev/" --appendPort=false

hugo server -D --bind 0.0.0.0 --port 1314 --baseURL "https://$CODESPACE_NAME-1314.app.github.dev/" --appendPort=false