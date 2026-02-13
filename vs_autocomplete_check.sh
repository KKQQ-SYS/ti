#!/bin/bash
# vs_autocomplete_check.sh
# 用于快速排查 VS Code 补齐问题

echo "=== VS Code 自动补全排查工具 ==="
echo ""

# 1️⃣ 检查 VS Code 版本
if command -v code &> /dev/null
then
    CODE_VER=$(code --version | head -n1)
    echo "[1] VS Code 版本: $CODE_VER"
else
    echo "[1] VS Code 未安装或命令行未配置"
fi
echo ""

# 2️⃣ 检查 Node.js 版本（TS Server 依赖）
if command -v node &> /dev/null
then
    NODE_VER=$(node -v)
    echo "[2] Node.js 版本: $NODE_VER"
else
    echo "[2] Node.js 未安装"
fi
echo ""

# 3️⃣ 检查项目配置文件
if [ -f tsconfig.json ]; then
    echo "[3] 找到 tsconfig.json ✅"
else
    echo "[3] tsconfig.json 未找到 ❌"
fi

if [ -f jsconfig.json ]; then
    echo "[3] 找到 jsconfig.json ✅"
else
    echo "[3] jsconfig.json 未找到 ❌"
fi
echo ""

# 4️⃣ 检查 node_modules 是否存在
if [ -d node_modules ]; then
    echo "[4] node_modules 存在 ✅"
else
    echo "[4] node_modules 不存在 ❌"
    echo "   建议运行: npm install 或 yarn install"
fi
echo ""

# 5️⃣ 检查 TS Server 日志路径（方便定位错误）
TS_LOG="$HOME/tsserver.log"
if [ -f "$TS_LOG" ]; then
    echo "[5] TS Server 日志: $TS_LOG"
else
    echo "[5] TS Server 日志不存在，打开 VS Code 并在命令面板执行 'TypeScript: Open TS Server log' 会生成日志"
fi
echo ""

# 6️⃣ 建议操作
echo "=== 建议操作 ==="
echo "1. 在 VS Code 命令面板运行: TypeScript: Restart TS Server"
echo "2. 确认项目中 tsconfig.json/jsconfig.json 配置正确"
echo "3. 删除 VS Code 缓存并重启: "
echo "   Windows: %APPDATA%\\Code\\CachedData"
echo "   macOS: ~/Library/Application Support/Code/CachedData"
echo "   Linux: ~/.config/Code/CachedData"
echo "4. 如果问题仍未解决，尝试禁用其他扩展，排查冲突"
