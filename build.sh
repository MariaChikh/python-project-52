#!/usr/bin/env bash

curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="/opt/render/.local/bin:$PATH"

make install