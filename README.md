
# Nero - UCalgary Spider

## Development

Pip is needed to install the packages in `requirements.txt`

```
pip install -r requirements.txt
```

## Run

Run a crawler

`scrapy crawl <crawler-name>`

List of crawlers are under directory `nero/spiders`


## Endpoints

Coursedog Curriculum API: https://coursedogcurriculum.docs.apiary.io/#reference/programs/get-all-programs

### Departments
https://app.coursedog.com/api/v1/ucalgary_peoplesoft/departments

### Courses
https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/courses/
https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/courses/1604171-2018-07-01?includeDependents=true&formatDependents=true

### Programs
https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/programs/
https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/courseSets/

AOS - Area of Study


Requisites example (simple): 
- https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/courses/1072711-2020-07-01?includeDependents=true&formatDependents=true
- https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/courses/1072161-2020-07-01?includeDependents=true&formatDependents=true
