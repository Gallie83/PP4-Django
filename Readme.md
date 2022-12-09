# **_Shannon Muay Thai Academy_**

Shannon Muay Thai Academy is a muay thai kickboxing gym located in Shannon, Co. Clare. This website is designed users information about both the gym and the sport, and for users to be able to request private training sessions at times that suit them. 

Welcome to the <a href="https://pp4-django-bookings.herokuapp.com/" target="_blank" rel="noopener">Shannon Muay Thai Academy</a> Website.

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    *  [User Stories](<#user-stories>)
    * [Design Choices](<#design-choices>)
    *  [Typography](<#typography>)
    *  [Colour Scheme](<#colour-scheme>)
* [**Features**](<#features>)
    * [**Existing Features**](<#existing-features>)
         * [How To Play](<#how-to-play>)
         * [Dealer Cards](<#dealer-cards>)
         * [Player Cards](<#player-cards>)
         * [Game Buttons](<#game-buttons>)
         * [Responsiveness](<#responsiveness>)
    * [**Future Features**](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
* [**Debugging**](<#debugging>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
*  [**Acknowledgements**](<#acknowledgements>)


# User Experience (UX)

## User Stories

* As a user I want to clearly see information about class times.
* As a user I want to see information about the background of the club and sport.
* As a user I want to be able to book training sessions easily on the website.
* As a user I want to have access to all my currently booked private sessions.
* As a user I want to be able to delete any currently booked private session.
* As a user I want to be able to register for an account.
* As a user I want to be able to easily log in and log out.


[Back to top](<#contents>)
## Design Choices

 * ### Typography
      The font I chose for the title in the navbar was 'Lobster', which I found on <a href="https://fonts.google.com/" target="_blank" rel="noopener">Google Fonts</a>.
      I chose this font as it was close to the style of the gyms actual logo title font.
    ![Font image](readme-images/lobster.png)

      For the remainder of the website I left the font as the default boostrap font, as it hsa a clean, legible look.

 * ### Colour Scheme
      The colour scheme eventually chosen is mostly black with a secondary color of light grey as that is the color of the gyms clothing items. I added red to the navbar links and the users bookings to make them stand out and prevent the website from having a two tone color palette.


[Back to top](<#contents>)
# Features

The gyms website is designed to be easy for users to navigate and simple for users to make bookings.

## Existing Features  
  * ### User accounts

    * Users are able to create accounts quickly, with cleary laid out steps.
    ![Register Page image](readme-images/register-page.png)

    * If the user already has an account, there is a login page where the user only has to provide their username and password. If the user logs in correctly they are brought to the homepage with a message confirming they logged in.
    ![Login Page image](readme-images/login-page.png)
    ![Login Confirm image](readme-images/login-confirm.png)

    * Both login and register pages have messages to say if there was an error and asking the user to try again.
    ![Login Page image](readme-images/login-page.png)

    * Once logged in, the login and register pages become hidden in the navbar and instead there is a logout option. The View bookings page also now becomes available.
    ![Logged in navbar image](readme-images/logged-in-nav.png)

    * When logging out, the user the then redirected to the login page with a message to confirm logout has been carried out successfully.
    ![Logout image](readme-images/logout.png)

[Back to top](<#contents>)

  * ### Bookings

      * If logged in, the user is able book private training sessions through the bookings page. First the user if brought a page where they select the date they want to make the booking.
      ![Date picker image](readme-images/date-pick.png)

      * If the user tried to pick a date that has already passed they receive an invalid date message.
      ![Invalid date image](readme-images/invalid-date.png)      

      * The user is then brought to a page where they can pick what time they would like to book the session for. The user is only given the option for times that have not been booked yet.
      ![Available times image](readme-images/times.png)

      * If there is no available times left on the date chosen the user is asked to choose a different date with a link back to the date picker page.
      ![No available times image](readme-images/full.png)
