#!/usr/bin/env bash
HOME=
global_script_dir=
workspace=


# 今日 leetcode 格式化 note
today_question="$global_script_dir/,today_question"
cat <<EOF > "$today_question"
PYTHONPATH=$workspace /usr/local/bin/python3.9 $workspace/leetcode/today_question.py
EOF
chmod +x "$today_question"


