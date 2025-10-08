#!/bin/bash
# Auto-activate virtual environment
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
    echo "✅ Virtual environment activated: $(which python)"
else
    echo "❌ Virtual environment not found at .venv/bin/activate"
fi
