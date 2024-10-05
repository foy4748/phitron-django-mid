**Mid Term Exam**

**What You Need to Submit :**   
     Sample :   
1\.  Practice 18.5 : github link  
2\. Practice 19.5 : github link  
3\. Doc File or Video Link : doc/video file drive link  
4\. Mid Term Exam link : github link

**Instructions: Watch the video sincerely**

**Mid Term Exam**

Create a fully functional **car sales website** that facilitates car listings for users and allows the users to filter cars by brand, create account, login, logout and also to buy a car. Each car will have an image, title, description, price, and a "Buy Now" button. Users can place orders, view their order history, and manage their account.   
The platform should consist of the following features:

**User-Facing Features:**  
**1\. Car Listings: (35 Marks)**

* There must be a navbar where an authenticated user can see home, profile, logout menu and an unauthenticated user will see home, signup, login.  
* In the home page, at first show some text and a single picture on the home page. Then the user can see the car list with image, price, and can filter cars by brand name.   
* There will be two models: Car Model and Brand Model. Make a relationship between them so that A brand has multiple cars but a car must have only one brand. You can add additional apps/models if you need.  
* In the car details page there will be a car image, name, description, quantity,price, brand name and a button named Buy Now will be shown for an authenticated user to buy a product.  
* Anyone can comment on any cars with their name, comment.  

**2\. User Registration and Authentication: (10 Marks)**

* Implement a user registration and login system.  
* User can also edit their profile details

**3\. Placing Orders: (20 Marks)**

* An authenticated user can only buy cars.   
* An unauthorized user cannot see the buy now button.  
* When an authenticated user clicks the buy now button this item will be purchased by that user and the total quantity of that car will be reduced by one.

**4\. Order History: (15 Marks)**

* In the profile page users can see the bought cars lists.

**N:B : There must be at least 3 class based views.**  
