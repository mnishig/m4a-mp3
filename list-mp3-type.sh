#!/bin/sh

if [$1 -eq '']; then
  echo 'list-type.sh: list .mp3 file and which result of [file] command'
  echo 'Usage: $ ./list-type.sh SEARCHPATH'
  echo ''
  echo 'script search begin from SEARCHPATH with fild commnad.'
  echo 'and each file is checked by file command'
  exit 1
fi

#filePattern="$1"
filePattern="*.mp3"

target="$1"

find $target -name "$filePattern" | while read -r fname
do
  file "$fname"
done
exit $?

