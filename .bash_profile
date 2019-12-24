
# Setting PATH for Python 3.8
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.8/bin:${PATH}"
export PATH

# ignore capitalization for auto-complete
bind "set completion-ignore-case on"

# git aliases
alias gs="git status"
alias ga="git add"
alias gaa="git add --all"
alias gcmsg="git commit -m"
alias gp="git push"
alias gpsu="git push --set-upstream"
alias gb="git branch"
alias gchk="git checkout"
alias gd="git diff"

# run the daily readings script
python3 ./daily_readings.py
