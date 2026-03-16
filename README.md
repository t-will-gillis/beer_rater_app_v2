# BeerRater App

Full-stack web app for reviewing beers and breweries.

## Stack

- **Backend:** Python 3.13 / Django 5.2
- **Database:** PostgreSQL 17
- **Auth:** django-allauth — username/password + GitHub OAuth (SSO)
- **Containerization:** Docker / Docker Compose
- **Static files:** WhiteNoise
- **Image processing:** Pillow
- **Configuration:** 12-factor via environment variables (environs)

## Features

- Browse and search beers and breweries
- User accounts with GitHub OAuth login
- Submit beers, breweries, and reviews (admin approval required)
- Beer label image uploads with automatic resizing
- Ratings and review counts are stored on the Beer model and updated automatically when reviews are added or removed, using Django signals.

    <br>
    <details><summary>Home Page example</summary> 

    <img src="staticfiles\images\homepage_screen.png">

    </details>  
    <br>

    <details><summary>Beer Page example</summary> 

    <img src="staticfiles\images\item_screen.png">

    </details>  

## Running locally

```bash
docker compose up --build
```

App runs at `http://localhost:8000`

## Environment variables

| Variable | Description |
|---|---|
| `DJANGO_SECRET_KEY` | Django secret key |
| `DJANGO_DEBUG` | Debug mode (`True` / `False`) |
| `GITHUB_CLIENT_ID` | GitHub OAuth app client ID |
| `GITHUB_SECRET` | GitHub OAuth app secret |

## To do

- Deployment (AWS / Railway / Render TBD)
