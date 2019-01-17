#!/bin/bash
RED='\033[0;32m'
NC='\033[0m'
SPACE=' '
echo -ne "${RED}Time: $(date)${NC}" "$SPACE" && ./network_check.py