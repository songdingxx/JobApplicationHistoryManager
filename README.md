# Job application history manager :)
## Introduction
>I'm looking for a job now. However, I always forgot what jobs that I've applied for. So I wrote this simple Python-MongoDB-based program. 

## Usage
>### How to use
>- Change the parameters in the AppHistory.py to connect to your own database. If you need to connect to a remote database, just change / re-implement the getConnection() function in ConnDB.py
>- Run python AppHistory.py
>### Data structure<br>
>Example:<br>
><pre>{<br>
>      company name:       test<br>
>             jobID:       testString<br>
>          position:       software engineer<br>
>         timestamp:       16/02/2021 03:51:45<br>
>            status:       pending<br>
>}</pre><br>
>
>### Supported funcitons
>- Insert a new application history.
>- Update application status (pending, rejected, passed, ...).
>- Find all jobs by some parameters.
>- Find a specific job by Company name and JobID / Position.
>- Get the total number of jobs that you have applied.
>
## I hope we all can find our dream jobs! :)

