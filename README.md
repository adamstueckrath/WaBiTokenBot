# WaBiTokenBot
I was tired of Reddit crypto FUD (fear, uncertainity, and doubt) about WaBi. So I created a bot to upvote submissions, and to reply to comments with information about the company (Walimai). If a user on reddit writes !WaBi in a comment, the bot will reply with the following information:

>> ##### About WaBi Token
>>
>>Walimai, the company behind WaBi, is a company that develops solutions to ensure product authenticity. It places secure anti-counterfeit labels on consumer products in China and internationally.
>>
>>Walimai’s operations are mainly in China, which suffers from counterfeit in products such as baby formula, cosmetics, and alcohol. In order to solve this problem and provide confidence for consumers, the company has developed RFID labels with anti-reuse design, as well as mobile Apps that integrate with the labels.
>>
>>Walimai label is applied to the product at the point of origin and is scanned throughout the supply chain. After consumers purchase the products, they can scan the items with Walimai app, which would then show whether the product is original and the product’s previous locations and timestamp along the supply chain.
>>
>> * Company Website: https://www.walimai.com/
>> * Token Website: https://www.wacoin.io/
>> * Whitepaper: http://resources.wacoin.io/WaBI_Whitepaper_ENG.pdf
>>
>>I am a bot | Feedback | Github




## Requirements
The bot uses the Praw python library to access and parse reddit. 


## Set Up 
1. Download requirements 
2. Create reddit account
3. Create reddit developer app
4. Edit praw.ini file with reddit account information, app client id and secret, user agent, and host account
5. Run! 


## Next Steps
Host the script on a Raspberry Pi to run continously
