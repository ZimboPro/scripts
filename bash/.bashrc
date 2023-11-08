# Ingore duplicates, commands that start with a space and removes duplicates from history
export HISTCONTROL=ignoreboth:erasedups
# Deletes local branches if they have been deleted on the remote
alias gitdel='git fetch --prune && git branch -r | awk "{print \$1}" | egrep -v -f /dev/fd/0 <(git branch -vv | grep origin) | awk "{print \$1}" | xargs git branch -d'