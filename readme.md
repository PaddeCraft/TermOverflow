# TermOverflow

> A command-line StackOverflow client.

> Not affiliated with StackOverflow in any way.

## What is it?

TermOverflow is a command-line StackOverflow client, that uses the StackExchange api.
It searches the best matching question to your query and displays the answers sorted by upvotes.

## Installation

```shell
# Latest release
python3 -m pip install https://api.github.com/repos/PaddeCraft/TermOverflow/zipball

# Developement version
python3 -m pip install git+https://github.com/PaddeCraft/TermOverflow.git
```

## Usage

```shell
# Search
python3 -m termoverflow s "Your query"

# Get version
python3 -m termoverflow version
```

## Feature list

[x] Query StackOverflow
[ ] Show authors and question owner
[ ] Show tags

If you have a feature request, open a issue.
Please note: I do not work on *that* often, so maybe it takes a bit for me to respond. 

## Troubleshooting

If you get errors (especially KeyError), it´s most likely that your daily api-limit is reached.