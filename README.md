[Dictionaries]

# General

This app integrates various online dictionary APIs to fetch and store words in a local database.
There are rate limit checks in place to ensure we don't exceed APIs rate limits. (e.g. 2500 requests/day)

# Currently integrated APIs :

## WordsAPI

rate-limit : 2500 requests/day


# Technicals

## How to use

- mysql -> docker-compose 
- run script

## Rate limits

Rate limitation is currently handlded through files.
API clients are instantiated on script execution, they're able to keep track of how many requests they've sent since their instantiation,
However, that information is lost once the class instance is garbage collected, which happens when the script stops running for whichever reason.
As a result, we must ensure that the amount of requests sent by a client is stored locally and persistently.
There are many ways to achieve so, since requests are currently sent linearly (no concurrence, we can only send a new request once the response from the
previous request has been dealt with), we don't have a need for a more complex system like Redis, at the moment.
We currently store the amount of request sent over a time period in files, each API client has its own file where it writes the amount of
requests it has sent over a time period.