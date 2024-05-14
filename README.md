# sast-validator
Script to help validate SAST and check more vulnerabilities.


## Run
```python3 sast.py -d PATH -l Language (optional) ``` 
```
  _____          _____ _______  __      __   _ _     _       _             
 / ____|  /\    / ____|__   __| \ \    / /  | (_)   | |     | |            
| (___   /  \  | (___    | |     \ \  / /_ _| |_  __| | __ _| |_ ___  _ __ 
 \___ \ / /\ \  \___ \   | |      \ \/ / _` | | |/ _` |/ _` | __/ _ \| '__|
 ____) / ____ \ ____) |  | |       \  / (_| | | | (_| | (_| | || (_) | |   
|_____/_/    \_\_____/   |_|        \/ \__,_|_|_|\__,_|\__,_|\__\___/|_| 

```

## Workflow's example

```
on:
  push:
    branches:
    - main

jobs:
  sast_job:
    runs-on: ubuntu-latest
    name: SAST Validator
    steps:
      - name: Checkout repository content
        uses: actions/checkout@v2 

      - name: SAST validator
        uses: michelleamesquita/sast-validator@v40
        with:
          options: -v $PWD/:/app
          path: .
          language: python
```


Enjoy it 💜
