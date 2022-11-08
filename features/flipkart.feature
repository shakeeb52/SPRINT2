# We will automate the Login page of FlipKart Account
  # As the number of rows present in EXAMPLE keyword, Feature file will run those number of times
Feature: login flipkart
    Scenario Outline: login data
      Given we navigate to flipkart homepage
      #Then we click on close button
      When we click on the login button
      Then we type in the "<username>" edit box
      And we type in the "<password>" field
      Then we click on the sign in button
      Then type "<searchTEXT>" in search bar
      And Click on search button
      Then Check on Relevance is clickable
      Then Check on popularity is clickable
      Then Check on Price low-high is clickable
      Then Check on Price high-low is clickable
      Then Check on newest first is clickable
      Then we validate filter text is present or not
      And  select the dropdown
      And type "<brand>" in the search bar
      And click on the checkbox
      And click on the assured checkbox
     # And click on the checkbox
      And Click on ratings checkbox 4* above and 3* above
      And Open GST link
      And ram checkbox clicked
      And internal storage checkbox clicked
      And battery link is opened
      And Get the first element on the page
      Examples:
           | username | | password | | searchTEXT | | brand |
           | 9606242790 | | 9608506036 | | mobiles | | realme |








