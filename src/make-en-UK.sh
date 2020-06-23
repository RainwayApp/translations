jq '.[] |= (gsub("((?<=[Ii]nitial)|(?<=[Ll]ocal)|(?<=[Mm]inim))iz";"is") | gsub("(?<=[Ll]icen)se";"ce"))' < en-US.json > en-UK.json
