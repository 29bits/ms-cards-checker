# Cards Checker

Checks CSV file to find users with active accounts that had not picked up their cards by given CSV file

## Usage

As script requires no special dependencies you can run it directly in python3 interpreter. 
You can also leverage docker. 

### Python from terminal

`$ python cards_checker.py CSV_FILE`

results in:

> Użytkownik, Status konta, odebrał karty?\
> Nieodbierający Użytkownik, aktywne, nie

See also `$ python cards_checker.py --help` for expected CSV file structure 

### Docker


1. Run `$ dockerBuildAndRun.sh` once
2. Continue using `$ dockerRun.sh` for future runs


`$ dockerRun.sh CSV_FILE` results in:
> Użytkownik, Status konta, odebrał karty?\
> Nieodbierający Użytkownik, aktywne, nie

See also `$ dockerRun.sh --help` for expected CSV file structure


## Troubleshooting

### Windows + WSL line endings issue

1. After running `./dockerBuildAndRun.sh` user encountered the following issue: 
```
unable to prepare context: path ".\r" not found
./dockerRun.sh: line 4: syntax error near unexpected token `elif'
'/dockerRun.sh: line 4: `elif [ "$1" = "" ]
```
2. Using `dos2unix` solved the issue