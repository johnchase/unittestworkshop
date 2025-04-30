#!/usr/bin/env bash
set -e

echo "📦 Creating virtual environment..."
python3 -m venv .venv

echo "📥 Activating virtual environment..."
source .venv/bin/activate

echo "⚡ Installing uv if needed..."
python -m pip install --upgrade pip
pip install uv

echo "📚 Installing requirements from requirements.txt..."
uv pip install -e .

echo ""
echo "✅ Setup complete!"
echo "➡️  Run \`source .venv/bin/activate\` to start coding."
