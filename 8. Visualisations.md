# Visualisations  

## Matplotlib  
-	Data visualization package in Python  
-	The subpackage is pyplot  

## Import statement  

        import matplotlib.pyplot as plt  
        plt.plot(x,y) - line graph  
        plt.show()  

## Labels  

        plt.xlabel(‘x label’)  
> x axis label  
        plt.ylabel(‘y label’) - y axis label
        plt.title(‘title’) - title label
        plt.yticks([0,2,4,6,8]) - allows you to set the intervals on the y axis

VISUALIZING YOUR DATA

dog_pack[‘height_cm’].hist(bins = 20) - creates a histogram with 20 bins of the height data

avg_weight_by_breed.plot(kind = ‘bar’, title = ‘Bar plot’) - creates a bar graph of the data (dog breed vs weight) with the title “Bar plot”.

sully.plot(x = ‘date’, y = ‘weight_kg’, kind = ‘line’, rot = 45) - creates a line plot of (years vs weight) and rotates the x labels by 45 degrees

dog_pack.plot(x = height_cm, y = ‘weight_kg’, kind = scatter) - scatter plot of (height vs weight) of dogs

Plotting two plots on top of one another. Use alpha for transparency
dog_pack[dog_pack[‘sex’] == ‘F’][‘height_cm].hist(alpha = 0.7)
dog_pack[dog_pack[‘sex’] == ‘M’][‘height_cm].hist(alpha = 0.7)
plt.legend([‘F’, ‘M’]) - creates a key on the graph	
plt.show()

Missing values

dogs.isna() - identifies missing values as booleans
dogs.isna().any() - identifies whether there are any missing values in a column by outputting a boolean of True to say there is at least one missing value in that column
dogs.isna().sum() OR dogs.isnull().sum() - calculates the sum of the booleans of missing values i.e. tells you how many missing values there are in each column

dogs.drop(columns = ‘Name’, inplace = True)
dogs.dropna() - drops all rows with missing data
dogs.fillna(0) - replaces all missing data with 0

### Example  

Seaborn is a data visualisation library built on top of matplotlib and closely integrated with Pandas data structures.  

        %matplotlib inline  
        import seaborn as sns  
        sns.set_style("darkgrid")  

> Select rows where both 'Rating' and 'Size' values are present (ie. the two values are not null)  

        apps_with_size_and_rating_present = apps[(apps["Rating"] != 0) & (apps['Size'] != 0)]  

> Subset for categories with at least 250 apps  

        large_categories = apps_with_size_and_rating_present.groupby("Category").filter(lambda x: len(x) >= 250)

>  Plot size vs. rating  

        plt1 = sns.jointplot(x = large_categories["Rating"], y = large_categories["Size"])

> Select apps whose 'Type' is 'Paid'  

        paid_apps = apps[apps['Type']=='Paid']

> Plot price vs. rating  
        plt2 = sns.jointplot(x = paid_apps["Rating"], y = paid_apps["Price"])