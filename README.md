
# Automation Bot for Hotel Booking on Booking.com

## 1. Introduction
This report presents the development of an automated booking bot that logs into booking.com, searches for hotels in Bangalore, and retrieves the top 10 hotels based on a specified check-in and check-out date. The bot was developed using Selenium WebDriver and Python, focusing on streamlining the process of hotel search and selection.

## 2. Objective
The primary goal of this bot is to automate the manual process of logging into booking.com, entering search criteria such as location and date, and fetching relevant hotel options. This bot eliminates the need for human intervention and automates the search and retrieval process, potentially aiding users in fast-tracking hotel bookings.

## 3. Technologies Used
**Programming Language:**  Python

**Automation Tool:** Selenium WebDriver

**Web Browser:** Google Chrome (or another supported browser)

## 4. Workflow of the Bot
**Step 1:** Launch Browser and Navigate to Booking.com

The bot initiates a new browser session using Selenium WebDriver and navigates to the login page of booking.com.

**Step 2:** Log In

The bot enters predefined credentials (email ID and password) into the corresponding input fields on the booking.com login page.

**Step 3:** Enter Search Criteria

Once logged in, the bot navigates to the hotel search page:

It enters Bangalore in the location input field.
It specifies the check-in and check-out dates.
Step 4: Retrieve Hotel Listings
The bot executes a search query based on the criteria mentioned. After the results are displayed, the bot scrapes the names and details of the top 10 hotels listed on the results page.

**Step 5:** Display Results

The scraped hotel data, including the name, price, and ratings (if available), is then printed or stored for further processing.

## 5. Conclusion
This automated booking bot successfully demonstrates the capability of Selenium WebDriver to handle web automation tasks. It significantly reduces manual effort in hotel searching, logging in, and fetching results. The bot can be extended to cover additional features such as hotel sorting based on user preferences, filtering by price range, or automating actual bookings.

## Authors

- [@Sahil-Singh-312](https://github.com/Sahil-Singh-312)
- Email: sahil312003@gmail.com

