# Crypto Net

Crypto Net is a social networking platform designed specifically for individuals interested in cryptocurrencies, blockchain technology, and the rapidly evolving world of digital finance. This platform is tailored to those who want to stay updated with the latest trends, news, and discussions related to various crypto assets and projects. It is a hub where users can share their insights, articles, and commentary, as well as engage in conversations about all things crypto.

[Here is the live version of my project](https://cryptonet-0fc8d0019661.herokuapp.com/)

![screenshot of Crypto Net from i am responsive](static/images/readme/resp-header.jpg)

## User Story
**New User**
- I want to know what the site is for
- I want to easily use the platform, so that I can quickly start interacting
- I want to be able to look through content with minimal effort
- I want to be able to see content clearly and see the discussions in the comments
- I want to be able to see what channels are most popular with the most content and activity

**Returning User**
- I want to come back and see new content
- I want to be able to keep up to date with my favorite crypto currencies
- I want to add a post for new content
- I want to view comments on my post and join in with the discussions
- I want to see if there are any new channels
- I want to add a new channel for my favorite crypto currency

**Other Customer Scenarios**

**Site Adminstrator**
- As a site administrator, the platform should run smoothly and remain secure.
- As a site administrator, that the site remain.

## Features

### Fonts

- **The site uses the following fonts:**
  - Base: [Ubuntu](https://fonts.google.com/specimen/Ubuntu)
  - Headers: [Kanit](https://fonts.google.com/specimen/Kanit)

The fonts were imported from [Google Fonts](https://fonts.google.com/)

### Color Scheme

- **The site uses the following colors:**
  - Jet: rgb(53, 53, 53)
  - Caribbean Current: rgb(60, 110, 113)
  - White: rgb(255, 255, 255)
  - Platinum: rgb(217, 217, 217)
  - Indigo Dye: #rgb(40, 75, 99)

![screenshot of color pallets taken from coolors.co](static/images/readme/color-pallet.jpg)

This color pallet was made in [Coolors](https://coolors.co)

- **Additional colors**
  - Black from [Bootstraps](https://getbootstrap.com/docs/5.3/utilities/background/) default colors


- **Input message return**


## Bugs
### Solved Bugs
- **Get attribute icon issue**

- **Displaying comment count of a individual post**

- **Returning True or False for a liked post**

- **Cloudinary http/https mixed content**

### Remaing Bugs
- **aria-hidden="true"**

## Testing
### Manual Testing
- Vigorous manual testing to ensure everything functions as expected


### Validator Testing
#### HTML
#### CSS
#### JavaScript
#### PEP8
  - There were errors in the [PEP8 Validator](https://pep8ci.herokuapp.com/), mainly related to whitespace and excessive line lengths. I had to reduce some lines in Django settings.py also.  
    ![screenshot of pep8 errors](static/images/readme/pep8-errors.jpg)
    ![screenshot of pep8 errors](static/images/readme/pep8-django-error.jpg)

  - All errors have been fixed
    ![screenshot of pep8 errors](static/images/readme/pep8-django-fix.jpg)
    ![screenshot of pep8 errors](static/images/readme/pep8-django-fix.jpg)

#### Lighthouse Testing

## Deployment
This project was deployed using Heroku.
- **Steps for deployment**
  - Fork or clone this [repository](https://github.com/AndyV773/pp4)
  - Create a new Heroku app
  - Add Config Var in Heroku's settings. Here is [.env.example](https://github.com/AndyV773/pp4/blob/main/.env.example)
  - Link the Heroku app to the repository
  - Click on **Deploy**

## Credits
### Content

- Code Institute for [Code Institute Blog](https://github.com/Code-Institute-Solutions/blog/) and deployment to Heroku
- [Django Project](https://www.djangoproject.com/)
- [Boot Strap](https://getbootstrap.com/docs/)
- [W3S](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Stack Overflow](https://stackoverflow.com/)
- The icons used were taken from [Font Awesome](https://fontawesome.com/)
- Animated 404 .svg was from [Loading](https://loading.io/)

### Media

- Images were created using Grok from [X](https://x.com/)
