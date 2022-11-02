# Songcrud

Songcrud app contains a simple REST API to list all songs in the database and all the artists. The API is also able to fetch a particular song, delete and update a particular song.

## Table of Contents

* [About](#Songcrud)
* [Required Features](#required-features)
* [Routes Test with Django REST Framework](#routes-test-with-django-rest-framework).
* [Techonologies Used](#technologies-used)
* [Author](#author)
* [Acknowledgements](#acknowledgements)

## Required Features

* Build a simple REST API to list all the songs in the database and all the artists. 
* The API should also be able to fetch a particular song, delete and update a particular song.
* When you delete a particular song in the API, All lyrics of that song should be deleted. 
* Also, updating a song simply means updating the song title or the date it was published.

## Routes Test with Django REST Framework

```shell
    {
        "title": "Oghene dooo",
        "date_released": "2022-11-01",
        "likes": "Football",
        "artiste": 'Frank Edwards'
    }
```

| METHOD | DESCRIPTION                                  | ENDPOINTS
| ------ | ---------------------------------------------|--------------------------
| GET    | Get all songs and artistes in the database   | `http://localhost:8000/songs/`
| GET    | Fetch a particular song                      | `http://localhost:8000/details/:pk/`
| POST   | Store data in the database                   | `http://localhost:8000/songs/`
| PUT    | Update a particular song                     | `http://localhost:8000/details/:pk/`
| DELETE | Delete a particular song                     | `http://localhost:8000/details/:pk/`

## Technologies Used

* [Django](https://www.djangoproject.com/)
* [DjangoRestFramework](https://www.django-rest-framework.org/#requirements)
* [Thunder Client](https://www.thunderclient.com/)

## Acknowledgements

* [Zuri](https://zuri.com/)

## Author

* [Alabi Tosin](https://github.com/alatos2)
