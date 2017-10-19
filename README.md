# Crime Log Parser README

Continually request and parse through Lehigh's crime logs, save the data to a database, and provide a way to analyze and review it.

## Usage Notes


## Branches
* Master
* Database
* Parser
* Internal Web Viewer
* Backend



### Database
#### Schema
```
CREATE TABLE logs (
    report_number INTEGER PRIMARY KEY,
    report_time TIMESTAMP,
    incident_time TIMESTAMP,
    disposition TEXT,
    incident_type TEXT,
    suspect_name TEXT,
    incident_location TEXT,
    description TEXT
)
```

#### Interface
##### `newEntry(Report): int`
Used to add an entry to the database.
Returns:
1. Success
2. Duplicate
3. Connection Error
4. Other

In the event of a failure, also writes to an error log (tbd).


## Change Log
