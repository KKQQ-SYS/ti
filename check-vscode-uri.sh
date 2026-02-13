#!/usr/bin/env bash

echo "🚀 VSCode URI 格式检测"

# 1. 全局 settings.json 路径
USER_CFG="$HOME/.config/Code/User/settings.json"
echo "👉 检查全局 VS Code 设置: $USER_CFG"
if [ ! -f "$USER_CFG" ]; then
  echo "⚠️ settings.json 不存在"
else
  jq -r '
    path(..|strings) as $p
    | select(getpath($p) | test("file:") )
    | (getpath($p), getpath($p))
  ' "$USER_CFG" \
  | while read -r key; do
        val=$(jq -r "getpath($key)" "$USER_CFG")
        echo "✳️ 检查 URI: $val"
        if python3 -c "from urllib.parse import urlparse; u = urlparse('$val'); \
            (u.scheme and (not u.path.startswith('/'))) and exit(1)" 2>/dev/null; then
            echo "❌ 非法 URI 可能导致 UriError: $val"
        else
            echo "✔️ 合法 URI"
        fi
      done
fi

echo "🧾 检查完毕"
