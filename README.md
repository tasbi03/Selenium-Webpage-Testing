# 🌐 Selenium WebPage Testing 

Welcome to our comprehensive 📚 testing documentation for the web application project. This repository is your gateway to all the test scripts 📝, results 📊, and analyses 🧐 from our extensive testing efforts. Our primary goal is to ensure the application's functionality, performance under stress, and scalability across various scenarios.
## 🎯 Functional Tests

We perform functional tests by checking the functionalities outlined in the requirements table. "Must have" and "should have" functional requirements are listed as RE-01 through RE-14, while "could have" requirements are RE-15 through RE-17.

### Key Tests

- **`test_display()`**: Checks if the webpage correctly displays all required elements. **Validates RE-01 and RE-06.**
- **`test_navigation_buttons()`**: Ensures that previous and next buttons navigate correctly. **Validates RE-02 and RE-03.**
- **`test_wrap_around()`**: Tests if navigation wraps around correctly at the boundaries. **Validates RE-04 and RE-05.**
- **`test_comment_submission()`**: Submits comments and checks for correctness and field clearance. **Validates RE-07, RE-08, and RE-11.**
- **`test_comments_persistence()`**: Ensures comments persist when navigating away and back. **Validates RE-09.**
- **`test_1000_comments()`**: Confirms the page can handle at least 1000 comments and that these are scrollable. **Validates RE-10 and RE-12.**

**Validates RE-09.**

test_1000_comments() function checks if each webpage can accommodate at least 1000 comments, and if the comments are scrollable. **Validates RE-10 and RE-12.**

In the same test, we added a time delay of 60 seconds and by using CMD-F we searched 750 to check if we can search for any comment by finding it on the page. Although it can be searched on the page, there is no built-in functionality in our real estate predictor to search the comment. So, in a way, we can say that the comments, if they are searched by a unique key present in them, then that comment can be searched by using CMD-F. However, there is no functionality implemented to search for instance all comments of a particular user. Thus, we can say **that the RE-13 is not implemented.**

These requirements are not implemented!


<table>
  <tr>
   <td>RE-13
   </td>
   <td>The comments should be searchable.
   </td>
   <td>M
   </td>
  </tr>
  <tr>
   <td>RE-14
   </td>
   <td>In any discussion, the real estate agent should be identifiable as such.
   </td>
   <td>M
   </td>
  </tr>
  <tr>
   <td>RE-15
   </td>
   <td>The comments could have a like button
   </td>
   <td>L
   </td>
  </tr>
  <tr>
   <td>RE-16
   </td>
   <td>The comments could keep track of the number of likes for each comment
   </td>
   <td>L
   </td>
  </tr>
  <tr>
   <td>RE-17
   </td>
   <td>The comments could have spell check.
   </td>
   <td>L
   </td>
  </tr>
</table>



<img width="470" alt="image" src="https://github.com/MohammedAerafKhan/SeleniumWebpageTesting/assets/97615236/12f6f554-04a3-4f14-aa77-d97d7fd95c8d">

Raw output of functional test:

......

----------------------------------------------------------------------

Ran 6 tests in 274.647s

OK



**Stress and Scalability Test Report:**

Stress and Scalability test were conducted on a mac 2019 with intel i9, 16 GB ram. For stress test, the webpage was overloaded with 1500 of comments being entered on each of the pages. Time taken to enter each 100 comments were recorded for comparison, and resources usage was tracked. For Scalability Test, in similar way to Stress test, 1500 comments were added iteratively by 1, 5 and 10 threads in parallel and time was recorded completion of each thread. 

Stress Test:

Here is the raw output of the stress test:

 \
**Submitted 100 comments on page 0, time taken: 17.031492233276367 seconds**

**Submitted 200 comments on page 0, time taken: 17.964168071746826 seconds**

**Submitted 300 comments on page 0, time taken: 18.95777988433838 seconds**

**Submitted 400 comments on page 0, time taken: 22.160690307617188 seconds**

**Submitted 500 comments on page 0, time taken: 24.021145820617676 seconds**

**Submitted 600 comments on page 0, time taken: 29.330840826034546 seconds**

**Submitted 700 comments on page 0, time taken: 35.16910791397095 seconds**

**Submitted 800 comments on page 0, time taken: 42.491716146469116 seconds**

**Submitted 900 comments on page 0, time taken: 48.729485750198364 seconds**

**Submitted 1000 comments on page 0, time taken: 56.29409193992615 seconds**

**Submitted 1100 comments on page 0, time taken: 66.24230194091797 seconds**

**Submitted 1200 comments on page 0, time taken: 79.10155487060547 seconds**

**Submitted 1300 comments on page 0, time taken: 90.14845085144043 seconds**

**Submitted 1400 comments on page 0, time taken: 102.60793113708496 seconds**

**Submitted 1500 comments on page 0, time taken: 116.48570203781128 seconds**

Submitted 100 comments on page 1, time taken: 13.808525085449219 seconds

Submitted 200 comments on page 1, time taken: 15.44584608078003 seconds

Submitted 300 comments on page 1, time taken: 17.822314977645874 seconds

Submitted 400 comments on page 1, time taken: 21.198618173599243 seconds

Submitted 500 comments on page 1, time taken: 26.248559951782227 seconds

Submitted 600 comments on page 1, time taken: 31.009228944778442 seconds

Submitted 700 comments on page 1, time taken: 36.576435804367065 seconds

Submitted 800 comments on page 1, time taken: 43.62559103965759 seconds

Submitted 900 comments on page 1, time taken: 52.291404008865356 seconds

Submitted 1000 comments on page 1, time taken: 60.331857204437256 seconds

Submitted 1100 comments on page 1, time taken: 70.84150075912476 seconds

Submitted 1200 comments on page 1, time taken: 83.18100500106812 seconds

Submitted 1300 comments on page 1, time taken: 96.58001208305359 seconds

Submitted 1400 comments on page 1, time taken: 110.30696320533752 seconds

Submitted 1500 comments on page 1, time taken: 124.4517879486084 seconds

Submitted 100 comments on page 2, time taken: 14.21062707901001 seconds

Submitted 200 comments on page 2, time taken: 15.576992988586426 seconds

Submitted 300 comments on page 2, time taken: 18.097819089889526 seconds

Submitted 400 comments on page 2, time taken: 21.80224108695984 seconds

Submitted 500 comments on page 2, time taken: 28.638401746749878 seconds

Submitted 600 comments on page 2, time taken: 34.645166873931885 seconds

Submitted 700 comments on page 2, time taken: 40.04827404022217 seconds

Submitted 800 comments on page 2, time taken: 46.77599787712097 seconds

Submitted 900 comments on page 2, time taken: 53.82850885391235 seconds

Submitted 1000 comments on page 2, time taken: 63.56348991394043 seconds

Submitted 1100 comments on page 2, time taken: 73.96190810203552 seconds

Submitted 1200 comments on page 2, time taken: 86.9245400428772 seconds

Submitted 1300 comments on page 2, time taken: 100.55238389968872 seconds

Submitted 1400 comments on page 2, time taken: 115.02224516868591 seconds

Submitted 1500 comments on page 2, time taken: 131.87899327278137 seconds

Submitted 100 comments on page 3, time taken: 14.213139772415161 seconds

Submitted 200 comments on page 3, time taken: 16.50778603553772 seconds

Submitted 300 comments on page 3, time taken: 22.971533060073853 seconds

Submitted 400 comments on page 3, time taken: 24.900105953216553 seconds

Submitted 500 comments on page 3, time taken: 31.173030138015747 seconds

Submitted 600 comments on page 3, time taken: 34.29809617996216 seconds

Submitted 700 comments on page 3, time taken: 40.17784905433655 seconds

Submitted 800 comments on page 3, time taken: 48.63104701042175 seconds

Submitted 900 comments on page 3, time taken: 56.27932691574097 seconds

Submitted 1000 comments on page 3, time taken: 67.29518103599548 seconds

Submitted 1100 comments on page 3, time taken: 77.90213584899902 seconds

Submitted 1200 comments on page 3, time taken: 90.40666317939758 seconds

Submitted 1300 comments on page 3, time taken: 106.00745701789856 seconds

Submitted 1400 comments on page 3, time taken: 121.53048491477966 seconds

Submitted 1500 comments on page 3, time taken: 137.84068298339844 seconds

Submitted 100 comments on page 4, time taken: 14.268728256225586 seconds

Submitted 200 comments on page 4, time taken: 16.133392095565796 seconds

Submitted 300 comments on page 4, time taken: 19.283796787261963 seconds

Submitted 400 comments on page 4, time taken: 23.83200216293335 seconds

Submitted 500 comments on page 4, time taken: 30.70002508163452 seconds

Submitted 600 comments on page 4, time taken: 34.97180914878845 seconds

Submitted 700 comments on page 4, time taken: 41.85740399360657 seconds

Submitted 800 comments on page 4, time taken: 51.23526668548584 seconds

Submitted 900 comments on page 4, time taken: 59.730507612228394 seconds

Submitted 1000 comments on page 4, time taken: 69.99820709228516 seconds

Submitted 1100 comments on page 4, time taken: 81.72521996498108 seconds

Submitted 1200 comments on page 4, time taken: 94.8781008720398 seconds

Submitted 1300 comments on page 4, time taken: 109.15100526809692 seconds

Submitted 1400 comments on page 4, time taken: 126.6663978099823 seconds

Submitted 1500 comments on page 4, time taken: 143.85952305793762 seconds

.

----------------------------------------------------------------------

Ran 1 test in 4227.673s

OK

Let’s analyze the first set of output, which is bolded. The time to enter 100 comments were recorded to see if more time would be required as number of comments will keep increasing. What we can see from the implementation of the webpage is that the comments are all just one string concatenated and bolded to appear like how they do on the web page. So, as the size of the string will keep increasing the time required to add more characters into it would increase. However, we saw no peculiar increment in memory consumption from beginning to end of each batch (1500 comments on one page). 

To summarize the data in the output, here is graph: 

<img width="468" alt="image" src="https://github.com/MohammedAerafKhan/SeleniumWebpageTesting/assets/97615236/a1641e32-4048-4426-bf3a-eeebc6502e93">

At first look it would seem Like, as the number of comments is increasing the time required to enter the comment is increasing. But that’s not the case, the tie which was recorded was just to enter 15 times 100 comments on each page. What we need to notice is that the first 100 to 200 comments took less 20 seconds only on all the webpages. However, the last 100 comments on each webpage took more than 115 seconds to be entered. This indicates that as the number of comments on each house in our application increases, the time to add newer comments will drastically increase. 

Another important thing to note is that there is a gradual increase in time required to enter every 100 comments from the first house to the last house. All the pages took somewhat same time for their first 800 comments, but after that the higher the page the more time was required to enter same number of comments. For instance, when 1100 comments were already posted on the first page, the next 100 comments took around 80 seconds to be posted. In contrast to the last page when 1100 comments were already posted, the next 100 comments took 94 seconds. Why these 94 seconds stand out so much is because the first hundred comments on any page only took about 15 – 20 seconds, but the 11<sup>th</sup> hundred comments took almost 6 times more time than that. This kept getting more and more worse, with the last 100 comments on the first page being posted in 116 seconds to last 100 comments being posted on the last page in 143 seconds. 

Bottom line hear is, that successive comments on same page exponentially increases the time required to add newer comments. Higher number of comments on any page would lead to slower processing of newer comment on any page.


<img width="468" alt="image" src="https://github.com/MohammedAerafKhan/SeleniumWebpageTesting/assets/97615236/bbd09e3b-4d03-4bc3-8afd-dc2f910d601d">


Below is a screen shot when the last 100 comments out of 1500 comments on the last page were being entered. As we can see their memory consumption by all the instances of Google Chrome and Visual studio code is all less then Microsoft word which was just existing in the background. Apart from the main instance of Google Chrome which is above word, however that instance was not the test instance created by selenium, that window had youtube, lear@seneca, stackoverflow, outlooks and whatsapp web. 


Scalability test:

Here is the raw output of a number of runs which was conducted one after another (after 5 10 minutes) in the sae environment to test scalability:

10 users inserting 500 comments in parallel

User 7 completed 500 actions in 435.967866897583 seconds.

User 4 completed 500 actions in 436.85020184516907 seconds.

User 6 completed 500 actions in 436.9159417152405 seconds.

User 8 completed 500 actions in 437.83718609809875 seconds.

User 0 completed 500 actions in 437.9104881286621 seconds.

User 9 completed 500 actions in 438.5692939758301 seconds.

User 1 completed 500 actions in 438.619637966156 seconds.

User 2 completed 500 actions in 438.6181888580322 seconds.

User 3 completed 500 actions in 439.20077681541443 seconds.

User 5 completed 500 actions in 439.2075879573822 seconds.

5 users inserting 500 comments in parallel

User 2 completed 500 actions in 253.79927611351013 seconds.

User 0 completed 500 actions in 254.36794114112854 seconds.

User 3 completed 500 actions in 254.36635518074036 seconds.

User 1 completed 500 actions in 254.67795395851135 seconds.

User 4 completed 500 actions in 254.67131805419922 seconds.

10 users inserting 1000 comments in parallel

User 2 completed 1000 actions in 1090.8130779266357 seconds.

User 3 completed 1000 actions in 1090.7135581970215 seconds.

User 9 completed 1000 actions in 1090.7853329181671 seconds.

User 0 completed 1000 actions in 1092.3844101428986 seconds.

User 7 completed 1000 actions in 1093.4479048252106 seconds.

User 1 completed 1000 actions in 1093.9694321155548 seconds.

User 4 completed 1000 actions in 1094.8543281555176 seconds.

User 5 completed 1000 actions in 1095.7774310112 seconds.

User 8 completed 1000 actions in 1096.0047438144684 seconds.

User 6 completed 1000 actions in 1095.867789030075 seconds.

5 users inserting 1000 comments in parallel

User 3 completed 1000 actions in 714.4226140975952 seconds.

User 1 completed 1000 actions in 715.6942782402039 seconds.

User 4 completed 1000 actions in 715.6531059741974 seconds.

User 0 completed 1000 actions in 717.490602016449 seconds.

User 2 completed 1000 actions in 717.4894409179688 seconds.

10 users inserting 1500 comments in parallel

User 1 completed 1500 actions in 2478.954972267151 seconds.

User 8 completed 1500 actions in 2485.22540807724 seconds.

User 5 completed 1500 actions in 2488.208236694336 seconds.

User 7 completed 1500 actions in 2488.1926708221436 seconds.

User 9 completed 1500 actions in 2488.1977791786194 seconds.

User 6 completed 1500 actions in 2488.2094299793243 seconds.

User 3 completed 1500 actions in 2490.4012799263 seconds.

User 2 completed 1500 actions in 2493.9364380836487 seconds.

User 4 completed 1500 actions in 2493.8909888267517 seconds.

User 0 completed 1500 actions in 2494.0865919589996 seconds.

5 users inserting 1500 comments in parallel

User 3 completed 1500 actions in 1634.2463738918304 seconds.

User 0 completed 1500 actions in 1634.1093497276306 seconds.

User 2 completed 1500 actions in 1635.9946057796478 seconds.

User 4 completed 1500 actions in 1638.3100340366364 seconds.

User 1 completed 1500 actions in 1639.6163139343262 seconds.

The output shows the time it required by 5 and 10 threads each to enter 500, 1000 and 1500 comments each in parallel. We already have the output of entering 500, 1000 and 1500 comments when entered by a single user in our stress test. To summarize the analysis here is a graph which shows the average time required for different scalability scenarios as mentioned: \

<img width="600" alt="image" src="https://github.com/MohammedAerafKhan/SeleniumWebpageTesting/assets/97615236/03507f55-bc52-4311-813e-4b9b705f44cb">

As we can see from the graph, if there is only one user interacting with our website, the performance is very good. The time required to enter 500, 1000 and even 1500 comments by one user only at a time is comparatively very less than the time require when 5 users were entering only 500 comments. As users get even more higher to 10, the time required to enter 500 comments went even higher to almost 500 seconds. In the second scenario when 1, 5 and 10 users were entering 1000 comments, it took only about 50 seconds when only 1 user was entering 1000 comments, but when number of users grew to 5, with each entering 1000 comments the time required. Increased exponentially all the way from just about 50 to almost 700. When got even worse when 10 users were entering 1000 comments as it took about 400 more seconds compared to th time 5 users took to enter same number of comments. 

The bottom line here is, as number of users increases the amount of time to post comments gradually increases.

During the process, Apple Spell (keyboard process) was severally lagging, I couldn’t type anything on my laptop. As we can see here, Apple Spell was consuming the most CPU usage, but of course it would as virtually 5 users were using it at that point. It only gone worse when I run the test for 10 users after that.

<img width="468" alt="image" src="https://github.com/MohammedAerafKhan/SeleniumWebpageTesting/assets/97615236/280927e3-f9cf-44c2-b051-d878051c8db0">

Also interestingly to be noted, that the amount of CPU usage was more when only one user was interacting with the website, however when 5 users were interacting, the CPU usage for each was almost 50%, which dropped to about 15% when 10 users were interacting:

<img width="468" alt="image" src="https://github.com/MohammedAerafKhan/SeleniumWebpageTesting/assets/97615236/c2fd60a3-3e3a-4ab8-800d-be280966724b">

Regardless, the memory consumption for all of the process was very less. As we saw previously when there was only 1 user the memory consumption was less than Microsoft word. This time, the memory consumption even when 10 users were interacting with the website at the same time was still less than Microsoft word. Infect it was just a little more than finder (file explorer equivalent of mac).

<img width="468" alt="image" src="https://github.com/MohammedAerafKhan/SeleniumWebpageTesting/assets/97615236/758c50ad-9b74-43de-bf07-7d8ec38daddb">

We can definitely forcefully provide the processes more CPU and memory, but as for testing purposes, in the same environment we decided to keep it fair.



Performance test report: \
1 users with 100.0 comments on each page:

Total time taken: 97.80700182914734 seconds

Average time taken by each user: 97.80700182914734 seconds

Average navigation time per user: 0.05697564506530762 seconds

Average comment submission time per user: 0.0427470850944519 seconds

5 users with 100.0 comments on each page:

Total time taken: 746.2191870212555 seconds

Average time taken by each user: 149.2438374042511 seconds

Average navigation time per user: 0.0995269416809082 seconds

Average comment submission time per user: 0.058340497493743905 seconds

10 users with 100.0 comments on each page:

Total time taken: 2793.3585352897644 seconds

Average time taken by each user: 279.33585352897643 seconds

Average navigation time per user: 0.18359161009788513 seconds

Average comment submission time per user: 0.1040536286830902 seconds

1 users with 200.0 comments on each page:

Total time taken: 171.61964678764343 seconds

Average time taken by each user: 171.61964678764343 seconds

Average navigation time per user: 0.05731476378440857 seconds

Average comment submission time per user: 0.0369250795841217 seconds

5 users with 200.0 comments on each page:

Total time taken: 1607.0972318649292 seconds

Average time taken by each user: 321.4194463729858 seconds

Average navigation time per user: 0.11077855215072634 seconds

Average comment submission time per user: 0.06921019182205199 seconds

10 users with 200.0 comments on each page:

Total time taken: 6112.1850616931915 seconds

Average time taken by each user: 611.2185061693192 seconds

Average navigation time per user: 0.21046369240283966 seconds

Average comment submission time per user: 0.12476666247844696 seconds

1 users with 300.0 comments on each page:

Total time taken: 282.0951118469238 seconds

Average time taken by each user: 282.0951118469238 seconds

Average navigation time per user: 0.06512971560160319 seconds

Average comment submission time per user: 0.04461323006947835 seconds

5 users with 300.0 comments on each page:

Total time taken: 2640.189147233963 seconds

Average time taken by each user: 528.0378294467926 seconds

Average navigation time per user: 0.12585064061482748 seconds

Average comment submission time per user: 0.08562619466781615 seconds

10 users with 300.0 comments on each page:

Total time taken: 10158.096586942673 seconds

Average time taken by each user: 1015.8096586942672 seconds

Average navigation time per user: 0.2413754865487417 seconds

Average comment submission time per user: 0.160799994913737 seconds

Comparing the performance test report with a baseline test:

1 users with 2.0 comments on each page:

Total time taken: 2.09378981590271 seconds

Average time taken by each user: 2.09378981590271 seconds

Average navigation time per user: 0.054038262367248534 seconds

Average comment submission time per user: 0.0420513391494751 seconds

The performance test which we decided to conduct focuses on the workability of the webpage in different conditions. We analyzed the time required to go to the next page, we included an implicit wait until the next page loads completely. We recorded the time it took for clicking the next button and the next page to load successfully. We did this repeatedly in a loop, and then averaged the time taken to go to next page in different conditions such as with low load, medium load and high load per page, and with different number of users. We also did the same for submitting a comment and waiting until the blog reappears on the screen after clicking submit.

Like how we’ve did previously, let’s analyze the output using a graph. With no surprises as of now, we know that the comment submission time increases when either stress or scalability is increased. In the performance test that got validated once more.

<img width="468" alt="image" src="https://github.com/MohammedAerafKhan/SeleniumWebpageTesting/assets/97615236/62d38604-9742-42c5-bf7d-202e333f1cf8">

The following graph shows the average time taken per user to submit 100, 200 and 300 comments on each page by different number of users compared to a baseline. The baseline is 1 user submitting only 2 comments on each page. All the values are averages and thus they can be compared.

In the left section of the graph, we see that the Average time required for 1, 5 and 10 users to post 100 comments on each page. So basically, posting 500 comments on the webpage, during this the page was changed at every iteration and there was an explicit wait until the next page would load properly. As we can see for 1 user the time taken was about 100 seconds, comparing this with our stress test report, during stress test we were posting all the comments on the same picture at one time, so there was no next before each comment. Also, we were not waiting for the whole page to load during stress test, we were only waiting for the username and comment section to appear and the submit button to become clickable again. Thus, in our stress test 1 user didn’t even take 50 seconds to post 100 comments on one page.

Now comparing with the baseline test, 1 user was submitting 2 comments on each page iteratively and waiting for the page to load completely. Thus, for 1 user with 100 comments on each page the average time will be higher, which we can see from the graph is true, as the number of users increases the time to post comments also increases. The conclusion here is same that as the number of users and comments per page increases, adding newer comments take more and more time. Just the way of performing this test was different. (stress test post “x” comments on one page and then goes to the next page, performance test post “x” comments in total, with “x/5” comment on each page, changing page “x” time.) 

Now let’s analyze the average time taken to change page as load and scalability increased.

<img width="468" alt="image" src="https://github.com/MohammedAerafKhan/SeleniumWebpageTesting/assets/97615236/c1cacb85-06f4-472a-a0fc-390416ce172c">

As we can see from the graph, for similar load condition, the average time taken to click next and wait for the page to load took more time as number of users kept increasing. For 1 user when they were soliciting on our website, they experienced top notch responsiveness. However, when 4 more users came on the website, each user started experiencing almost half the responsiveness the first one was experiencing when alone. And when 5 more users came and a total of 10 users were using the website, the responsiveness decreased more than three folds from when there was only 1 user. Interestingly, the responsiveness kept decreasing as the users kept posting more and more comments.

Bottom line here is, the time taken for page to load after when next was clicked, kept increasing as number of users, and number for comments on each page kept increasing. However, The website was very responsive throughout, there were no crashes, and even the highest average time to load the next page was still only under 0.25 seconds, but overall the performance still degraded. 

Now the average single comment submission time.

<img width="468" alt="image" src="https://github.com/MohammedAerafKhan/SeleniumWebpageTesting/assets/97615236/72ad81d7-15ad-4a5e-92eb-f6a3f166d734">

This graph shows how the average time required to submit a comment in different circumstances of load and scalability. As we can see from the graph, the average time to post a single comment kept increasing gradually as the number of users kept increasing.



