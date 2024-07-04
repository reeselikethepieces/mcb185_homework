gunzip -c ~/Code/MCB185/data/dictionary.gz | grep  -v "[^zirconia]" | grep "r" | grep -E ".{4,}"
