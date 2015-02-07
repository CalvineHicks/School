#!/bin/bash
#Calvin Hicks 

grep [1-9]$ $1 | wc -l
grep -v ^[a,e,i,o,u] $1| wc -l
grep '^[a-zA-Z]\{12\}$' $1 | wc -l
grep '[0-9]\{3\}[ -]\?[0-9]\{3\}[ -]\?[0-9]\{4\}' $1 | wc -l
grep '[303]\{3\}[ -]\?[441]\{3\}[ -]\?[0-9]\{4\}' $1 | wc -l
grep '[a-zA-Z0-9][@][a-zA-Z0-9.-]' $1 | wc -l
grep '[a-zA-Z0-9][@][a-zA-Z0-9.-].*gov$' $1 | wc -l
