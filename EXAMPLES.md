# Slash Detailed Examples 

## Website Examples
#### 1. Searching
The search bar accepts the product you wanted to search and uses it to search and scrape the requested products on 
the available e-commerce websites. The results of the search will be available when scrolled below

Example:
<p align="center"><img width="700" src="./assets/slash_web_demo_1.gif"></p>

#### 2. Result length
The maximum number of results that are scraped from each website can be set in the second text bar. It accepts
a positive integer value from 1 to 15 number of results per each website. Incase of an invalid input, the results default this value to 3. 

Example: In this example, The user searches for the same product with two different result lengths (2 and 4).
<p align="center"><img width="700" src="assets/slash_web_demo_2.gif"></p>


#### 3. Email Notification
There is an option to send emails to customers using a parameter that accepts an email address. 

Example:
<p align="center"><img width="700" src="./assets/slash_web_demo_3.gif"></p>


## REST API Examples
#### 1. Searching

The ```search``` parameter accepts one  string which it uses to search and scrape the requested products on 
the e-commerce websites. This is a **mandatory field** for the REST API.
The search string should be in double quotes if it has two or more words and you are using a web browser.It is not required in Postman. 

Example:
<p align="center"><img width="700" src="./assets/slash_rest_demo_1.gif"></p>

If we want to search an item 'toy', the results can also be obtained at:

```https://slash-app.herokuapp.com/slash/?search=toy```

#### 2. Result length
The ```num``` parameter defines the maximum number of results that are scraped from each website can be set in the second text bar. It accepts
a positive integer value from 1 to 15 number of results per each website. Incase of an invalid input, the results default this value to 3. This is a **mandatory field** for the REST API.

Example: In this example, The user searches for the same product with two different result lengths (2 and 4).
<p align="center"><img width="700" src="./assets/slash_rest_demo_2.gif"></p>
If we want to search an item 'toy' where this product can be scraped 5 times from each website, the results can be obtained at: 

```https://slash-app.herokuapp.com/slash/?search=toy&num=5```

#### 3. Email Notification
The ```email``` parameter can be used to send a copy of the results. You can send the same email to multiple senders by seperating the emails by commas

Example:
<p align="center"><img width="700" src="./assets/slash_rest_demo_3.gif"></p>
If we want to send results to several people on email, we can just used the argument email, with values of list of comma separated emails. we want to send notifications to people 'sbuchan2@ncsu.edu' and 'vperoll@ncsu.edu', the results can be seen at:

```https://slash-app.herokuapp.com/slash/?search=toy&num=5&email="sbuchan2@ncsu.edu,vperoll@ncsu.edu"```


## CLI Tool Examples
#### 1. Searching
```--search```  accepts one argument string which it uses to search and scrape the requested products on 
the e-commerce websites. So, to use this, run the python script followed by the --search argument and the 
search string. The search string should be in double quotes if it have two or more words. Example:
```
For Mac
python3 slash.py --search "philips hue"

For Windows
python slash.py --search "philips hue"
```
```
| timestamp                     | title                                       | price      | website   | rating   |
|-------------------------------|---------------------------------------------|------------|-----------|----------|
| 01/10/2022 13:56:08 EDT -0400 | Amazon Basics 60W Equivalent, Soft White... | $14.99     | amazon    | 4.6      |
| 01/10/2022 13:56:08 EDT -0400 | Philips Hue White & Color Ambiance White... | $119.99    | amazon    | 4.7      |
| 01/10/2022 13:56:08 EDT -0400 | PHILIPS Hue 2pk A19 LED Starter Kit with... | $69.99     | amazon    | 4.7      |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue Smart Stand Alone Bridge, Hu... | $49.68     | walmart   | N.A      |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue 3-Pack 60W White Bluetooth S... | $69.00     | walmart   | N.A      |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue LED 60-Watt White A19 Dimmab... | $52.99     | walmart   | N.A      |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue A19 75W Smart LED Bulb White    | $15.99     | target    | 4.44     |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue 4pk White and Color Ambiance... | $199.99    | target    | 4.63     |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue A19 75W Smart LED Bulb          | $54.99     | target    | 4.3      |
```
#### 2. Sorting
```--sort``` accepts one or more arguments that determine how the tool sorts and filters the requested products
after scraping. The first value is used to initially sort and filter the results of the scraping. The arguments
following the first one are not required but will be used to further sort the filtered results. Example:
```
For Mac
python3 slash.py --search "philips hue" --sort pr

For Windows
python slash.py --search "philips hue" --sort pr
```
```
| timestamp                     | title                                       | price      | website   | rating   |
|-------------------------------|---------------------------------------------|------------|-----------|----------|
| 01/10/2022 13:57:59 EDT -0400 | Philips Hue Econic Outdoor White & Color... | N.A        | amazon    | 4.8      |
| 01/10/2022 13:57:59 EDT -0400 | Amazon Basics 60W Equivalent, Soft White... | $14.99     | amazon    | 4.6      |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue A19 75W Smart LED Bulb White    | $15.99     | target    | 4.44     |
| 01/10/2022 13:57:59 EDT -0400 | Outdoor Low voltage Extension Cable for ... | $19.98     | amazon    | 4.7      |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue White Ambiance A19 LED 60-Wa... | $21.88     | walmart   | N.A      |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue White Ambiance A19 LED 60-Wa... | $21.97     | walmart   | N.A      |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue White and Color Ambiance Blu... | $39.99     | target    | 3.42     |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue Smart Stand Alone Bridge, Hu... | $49.68     | walmart   | N.A      |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue 2pk BR30 Warm-To-Cool LED Sm... | $49.99     | target    | 4.73     |
```
#### 3. Sort Order
The ```--des``` flag can be set to sort the requested products in a non-increasing order. This flag will be 
actually used when coupled with ```--sort``` and the default value taken is true. Example:
```
For Mac
python3 slash.py --search "philips hue" --sort pr --des

For Windows
python slash.py --search "philips hue" --sort pr --des
```
```
| timestamp                     | title                                       | price   | website   | rating   |
|-------------------------------|---------------------------------------------|---------|-----------|----------|
| 01/10/2022 13:59:09 EDT -0400 | 75" Gradient TV Lightstrip Entertainment... | $541.77 | amazon    | 4.3      |
| 01/10/2022 13:59:09 EDT -0400 | Philips Hue 2-Pack Bluetooth Gradient Am... | $324.99 | amazon    | N.A      |
| 01/10/2022 13:59:09 EDT -0400 | Philips Hue White and Color Ambiance Ext... | $323.95 | amazon    | N.A      |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue White and Color Ambiance A19... | $199.99 | walmart   | N.A      |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue 4pk White and Color Ambiance... | $199.99 | target    | 4.63     |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue White &#38; Color Ambiance D... | $179.99 | target    | 3.7      |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue 4-Pack White and Color A19 M... | $159.99 | walmart   | N.A      |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue White & Color Ambiance Calla... | $149.99 | target    | 5.0      |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue White A19 Smart Light Starte... | $81.86  | walmart   | N.A      |
```

#### 4. Result length
The maximum number of results that are scraped from each website can be set using the ```--num``` argument. It accepts
an integer value ```n``` and then returns ```n``` results from each website. Note that tool returns a maximum of 
the value of ```n``` and the number of results on the webiste. By default this value is set to 3. Example:
```
For Mac
python3 slash.py --search "philips hue" --num 5

For Windows
python slash.py --search "philips hue" --num 5
```
```
| timestamp                     | title                                       | price      | website   | rating   |
|-------------------------------|---------------------------------------------|------------|-----------|----------|
| 01/10/2022 13:59:54 EDT -0400 | Amazon Basics 60W Equivalent, Soft White... | $14.99     | amazon    | 4.6      |
| 01/10/2022 13:59:54 EDT -0400 | Philips Hue White & Color Ambiance White... | $119.99    | amazon    | 4.7      |
| 01/10/2022 13:59:54 EDT -0400 | PHILIPS Hue 2pk A19 LED Starter Kit with... | $69.99     | amazon    | 4.7      |
| 01/10/2022 13:59:54 EDT -0400 | Philips Hue White Filament Globe G25 LED... | $32.94     | amazon    | 4.7      |
| 01/10/2022 13:59:54 EDT -0400 | Philips Hue White and Color Ambiance A19... | $99.99     | amazon    | 4.7      |
| 01/10/2022 13:59:56 EDT -0400 | Philips Hue Smart Stand Alone Bridge, Hu... | $49.68     | walmart   | N.A      |
| 01/10/2022 13:59:56 EDT -0400 | Philips Hue 3-Pack 60W White Bluetooth S... | $69.00     | walmart   | N.A      |
| 01/10/2022 13:59:56 EDT -0400 | Philips Hue LED 60-Watt White A19 Dimmab... | $52.99     | walmart   | N.A      |
| 01/10/2022 13:59:56 EDT -0400 | Philips Hue White A19 Smart Light Starte... | $81.86     | walmart   | N.A      |
| 01/10/2022 13:59:56 EDT -0400 | Philips Hue White and Color Ambiance Sma... | $69.99     | walmart   | N.A      |
| 01/10/2022 13:59:57 EDT -0400 | Philips Hue A19 75W Smart LED Bulb White    | $15.99     | target    | 4.44     |
| 01/10/2022 13:59:57 EDT -0400 | Philips Hue 4pk White and Color Ambiance... | $199.99    | target    | 4.63     |
| 01/10/2022 13:59:57 EDT -0400 | Philips Hue A19 75W Smart LED Bulb          | $54.99     | target    | 4.3      |
| 01/10/2022 13:59:57 EDT -0400 | Philips Hue 2pk A19 LED Starter Kit with... | $69.99     | target    | 4.35     |
| 01/10/2022 13:59:57 EDT -0400 | Philips Hue White &#38; Color Ambiance D... | $179.99    | target    | 3.7      |
```

#### 5. Link
There is an option to display links int the output. Example:
```
For Mac
python3 slash.py --search "philips hue" --link

For Windows
python slash.py --search "philips hue" --link
```
```
| timestamp                     | title                                       | price   | website   |   rating | link                         |
|-------------------------------|---------------------------------------------|---------|-----------|----------|------------------------------|
| 07/10/2022 16:57:17 EDT -0400 | mens Performance Cotton Cushioned Athlet... | $13.50  | amazon    |     4.5  | https://tinyurl.com/2hf4nm8l |
| 07/10/2022 16:57:35 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $3.59   | target    |     4.79 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:57:17 EDT -0400 | mens Performance Cotton Cushioned Athlet... | $13.50  | amazon    |     4.5  | https://tinyurl.com/2hf4nm8l |
| 07/10/2022 16:57:35 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $3.59   | target    |     4.79 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:57:18 EDT -0400 | Mens Socks, 6 Pairs Anti-Blister Cushion... | $15.99  | amazon    |     4.6  | https://tinyurl.com/2qjv6k8w |
| 07/10/2022 16:57:35 EDT -0400 | Pair of Thieves Men&#39;s Solid Crew Soc... | $7.79   | target    |     4.71 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:57:18 EDT -0400 | Mens Socks, 6 Pairs Anti-Blister Cushion... | $15.99  | amazon    |     4.6  | https://tinyurl.com/2qjv6k8w |
| 07/10/2022 16:57:35 EDT -0400 | Pair of Thieves Men&#39;s Solid Crew Soc... | $7.79   | target    |     4.71 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:57:18 EDT -0400 | No Show Socks Women Low Socks Non Slip F... | $15.89  | amazon    |     4.5  | https://tinyurl.com/2khadfy2 |
| 07/10/2022 16:57:35 EDT -0400 | Signature Gold by GOLDTOE Men&#39;s Mode... | $9.35   | target    |     4.67 | https://tinyurl.com/2m5ec5nt |
| 07/10/2022 16:57:18 EDT -0400 | No Show Socks Women Low Socks Non Slip F... | $15.89  | amazon    |     4.5  | https://tinyurl.com/2khadfy2 |
| 07/10/2022 16:57:35 EDT -0400 | Signature Gold by GOLDTOE Men&#39;s Mode... | $9.35   | target    |     4.67 | https://tinyurl.com/2m5ec5nt |

Trying to send email notification to the customers if there are any...

No email to send data. Hence not sending the email
Done :)
```

#### 6. Email Notification
There is an option to send emails to customers using a parameter that accepts a comma separated list of emails. Example:
```
For Mac
python3 slash.py --search "philips hue" --link --email "vchalla2@ncsu.edu,sponnur@ncsu.edu"

For Windows
python slash.py --search "philips hue" --link --email "vchalla2@ncsu.edu,sponnur@ncsu.edu"
```
```
| timestamp                     | title                                       | price   | website   |   rating | link                         |
|-------------------------------|---------------------------------------------|---------|-----------|----------|------------------------------|
| 07/10/2022 16:47:58 EDT -0400 | mens Performance Cotton Cushioned Athlet... | $13.50  | amazon    |     4.5  | https://tinyurl.com/2outdp6f |
| 07/10/2022 16:48:15 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $3.59   | target    |     4.79 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:47:58 EDT -0400 | mens Performance Cotton Cushioned Athlet... | $13.50  | amazon    |     4.5  | https://tinyurl.com/2outdp6f |
| 07/10/2022 16:48:15 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $3.59   | target    |     4.79 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:47:58 EDT -0400 | Mens Socks, 6 Pairs Anti-Blister Cushion... | $15.99  | amazon    |     4.6  | https://tinyurl.com/2dsl5uyc |
| 07/10/2022 16:48:15 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $8.99   | target    |     4.65 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:47:58 EDT -0400 | Mens Socks, 6 Pairs Anti-Blister Cushion... | $15.99  | amazon    |     4.6  | https://tinyurl.com/2dsl5uyc |
| 07/10/2022 16:48:15 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $8.99   | target    |     4.65 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:47:59 EDT -0400 | CelerSport Ankle Athletic Running Socks ... | $15.95  | amazon    |     4.7  | https://tinyurl.com/2en2jbsd |
| 07/10/2022 16:48:15 EDT -0400 | Signature Gold by GOLDTOE Men&#39;s Mode... | $9.35   | target    |     4.67 | https://tinyurl.com/2m5ec5nt |
| 07/10/2022 16:47:59 EDT -0400 | CelerSport Ankle Athletic Running Socks ... | $15.95  | amazon    |     4.7  | https://tinyurl.com/2en2jbsd |
| 07/10/2022 16:48:15 EDT -0400 | Signature Gold by GOLDTOE Men&#39;s Mode... | $9.35   | target    |     4.67 | https://tinyurl.com/2m5ec5nt |

Trying to send email notification to the customers if there are any...

Done :)
```
