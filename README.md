
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

### Programs
https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/programs/
