# Simulating-Inventory-System

This project is to simulate the stocking level of one product: Awnet Umbrella, inside an inventory management system in an Australian firm. The firm provides this product to its distributors together with a recommended retail price (RRP). 

**Information regarding the product and firm:**

1. The Australian firm was established in January 1st, 2000. For the past 20 years, there have been no changes to the inventory management system. There was also no change in product model in the past 20 years as it is quite robust design, the product model will not change in the future either. 
On January 1st, 2000, when the firm was first open for business, there were 1000 Awnet umbrellas in stock, the distribution number of the Awnet umbrella on that day to the distributors was 36, and each Awnet umbrella’s RRP was $705 AUD (This date has taken the peak season, which causes increase in sales quantity and increase in price. 
Please note when the inventory stock drops to 400, the firm will restock 600 Awnet umbrellas back to the warehouse (We do not consider any cost related to restocking fee).

2. Awnet Umbrella has a peak selling season. It is from 1st November to end of February each year (Number of days in February is decided by whether that year is a leap year or not). 
During the peak season, the company is expected to have a 35% increase in quantity for distribution (Which means the number of Awnet umbrellas that goes out of the inventory system is increased by 35%, rounded up to an integer). 
It is also expected to have 20% increase in RRP (Recommended Retail Price, contains 2 decimal places, it will be the same for the rest of the document) during peak season as it is hard to supply enough umbrellas to meet the demand. 

3. The stocking system is updated daily at 11:59 pm. This number has been consistent every day until the beginning of a new financial year. 
At the beginning of the new financial year each year (1st July), the company will impose a 10% increase in the supply of Awnet umbrellas to its distributors (rounded up) and 5% increase of the RRP due to inflation. 

4. Based on statistics, global financial crisis happens every 9 years, and lasts for another 2 years, the number of Awnet umbrella distributed to distributors will drop by 20% in the first year when global financial crisis hit the market, the number will continue to drop by 10% and 5% for the next 2 years when the economy is recovering. 
To make up the losses, during the year that a global financial crisis starts, the company will add an additional 10% increase in RRP to the product, the increase of the product RRP will become 5% in the next year, and 3% the year after to make up the loss. 

**CRISIS**

During the crisis, the price inflation and increase in quantity for distribution are still valid and applicable. 
Note: the crisis will start on 1st Jan on the 9th year, and end on 31st Dec the 11th year. In this example, it will start on 1st January, 2009 and ends on 31st Dec, 2011. And there will be another crisis start on 1st January, 2020 etc. 
> Example of price increase to make up the loss during crisis is: the price increase will start on 1st January, 2009, and it will have another increase on 1st January, 2010, etc. 

5. It is expected that 5% of items will be defective and returned to warehouse every month. (Which means the inventory number will increase by 5%). 

Defective items will be refurbished and redistributed at 80% of original price (original price is the RRP at the time the product is returned) in the following months. 

> This firm assesses the quantity of product distributed and total revenue earned from distributors every year (The most basic formula for revenue is: Revenue = RRP x total quantity. But please bear in mind you also need to consider the defective items as well as global financial crisis and inflation and increase over the supply of Awnet umbrella).

- The firm also runs predictions 20 years in advance. (We are currently in year 2020, the company will have a prediction of this information to year 2040) 

**Text file Explaination:**

This Consist of two text files:
1. AU_INV_START.txt
2. AU_INV_END.txt

- The starting information will need to be read from a file called “AU_INV_START.txt”. 
- After operation of this  program, the information will be saved to a file called “AU_INV_END.txt”. 

