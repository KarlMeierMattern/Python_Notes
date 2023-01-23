# Python Notes  

## Pandas DataFrames
- Pandas is built on top of Numpy and Matplotlib.
- Better than Numpy array as DataFrames can contain multiple data types.
You can think of DataFrame columns as single-dimension arrays called Series.
Pandas is for dataframes
-	We convert a dictionary to a dataframe
-	DataFrames are the most common way to work with tabular data in Python.

To convert a dictionary dict into a dataframe:
import pandas as pd
brics = pd.DataFrame(dict)

To change the index numbers in the far left column:
brics = [‘BR’, ‘CH’, ‘DU’]

Import and read a csv file into a DataFrame:
import pandas as pd
brics = pd.read_csv(“brics.csv”, index_col = 0)
index_col = 0 shifts the DataFrame a column left

Select column with type DataFrame:
brics[[‘country’]] 
brics.loc[ :, [‘country’, ‘capital’]] - selects the country and capital columns
brice.loc[ :, ‘country’: ‘capital’] - selects columns from country to capital
brics.iloc[ :, [0,1]]

Row access (and all columns):
brics[1:4] - can only get row access through slicing if you don’t use loc
brics.loc[[‘RU’, ‘IN’, ‘CH’]]
brics.iloc[[1]]
brics.iloc[[1,2,3]]

Row and column access:
brics.loc[[‘RU’, ‘IN’, ‘CH’], [‘country’, ‘capital’]]
brics.iloc[[1,2,3], [0,1]]

loc - label based
iloc - integer based location

Creating a data frame
In a pandas DataFrame missing data is indicated by NaN (Not-a-Number)

First create a list/s
years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103,101,99,100,100,95,95,96,93,90]

Then create a dictionary of those lists
movie_dict = {'years':years,'durations':durations}

Then convert that dictionary to a DataFrame
durations_df = pd.DataFrame(movie_dict)  

---













### Lists
Lists are mutable i.e. the object can be modified after it has been created
This is unlike strings, integers, floats, tuples and dictionaries
Collection of values, order matters

Select, update and remove: [ ]
Indexed by range of numbers
Can select entire subsets
fam = [‘cat’, 1.58, 2.1, ’house, ’Liz’, 1.89, ’Jack’]

List slicing is exclusive
[start:end]
[inclusive:exclusive]
Fam[1:4]
Output is exclusive of 4
[1.58, 2.1,’ house’]


### Functions

max() is a function as you can call it on a list

fam = [4,6,10,3,9]
I.e. max(fam)

round(number, decimal places) 
By default it rounds to zero decimal places

len() - can call on a string or list (will count number of elements in the list)


### Methods
These are functions that are specific to Python objects
Objects have methods associated, depending on the type (i.e. list, float, string etc.) of the object
Methods call functions on objects

.capitalize() - capitalizes the first letter in a word
.replace() - input an element for replacement, but cannot be called on a list on a single string object
.count()
.index() - gets the index number of an element in a list
.append() - adds inputted element into a list


### Packages
Directory of Python scripts
Each script is a module which specify functions, methods, types


## Numpy
-	Numeric Python
-	Alternative to the list
-	Can perform calculations over entire arrays unlike lists
-	Type pip3 install numpy at the command line to install
-	Numpy arrays must contain only one type

bmi > 23
Returns an array of booleans

bmi[bmi > 23]
Returns an array of the values that are greater than 23
Calling the shape attribute (N.B. no brackets after an attribute call) on an array will output the number of rows and columns in the array


### 2D Numpy array

np_2d[0][2] is the same as np_2d[0,2]
 
np_2d[ : , 1:3]
-	Outputs both rows and columns 1-3


### Numpy statistics

np.mean(np_city[ :, 0]) calculates the mean of the first column
np.median(np_city[ :, 0]) calculates the median of the first column
np.corrcoef(np_city[ :, 0], np_city[ :, 1]) calculates the correlation of the first and second columns
np.std(np_city[ :, 0] calculates the standard deviation of the first column
Also: 
np.sum() 
np.sort()
np.round()
np.random.normal(distribution mean, distribution std., number of samples)


## Matplotlib
-	Data visualization package in Python
-	The subpackage is pyplot

import matplotlib.pyplot as plt
plt.plot(x,y) - line graph
plt.show()

s = [2,4,5,6,7,8,9]
plt.hist(values, bins =3) - histogram that places the values list into 3 bins

plt.xlabel(‘x label’) - x axis label
plt.ylabel(‘y label’) - y axis label
plt.title(‘title’) - title label
plt.yticks([0,2,4,6,8]) - allows you to set the intervals on the y axis


Dictionary
Keys are immutable objects
Select, update and remove: [ ]
Indexed by range of unique keys
Lookup table with unique keys

world = {‘key1’:value1, ‘key2’:value2}
world[‘key1’] - outputs value1

world[‘key3’] = value3 - adds this ‘key’:value pair to the end of the dictionary
‘value3’ in world - returns the boolean True as the key ‘value3’ is in the world dictionary
world[‘key3’] = value4 - edits the value of ‘key3’ to value4
del(world[‘key3’] - deletes the ‘key3’:value4 pair from the world dictionary



Comparison operators in Numpy
Comparison operators: <, >, <=, >=, ==, !=
Boolean operators: and, or, not
Conditional statements: if, else, elif

import numpy as np
np.logical_and
np.logical_or 

np.logical_and(bmi > 21, bmi < 23) - output will be an array of booleans
bmi[np.logical_and(bmi > 21, bmi < 23)] - output will be the actual values in the array


If, elif, else

if: condition
	print()
elif: condition
	print()
else:
	print()


Filtering Pandas DataFrames

brics[brics[“area”] > 8] - first checks the column “area” for values that exceed 8 and then outputs all the rows where that condition is met

brics[np.logical_and(brics[“area”] > 8, brics[“area”] < 10)] - searches the “area” column for values exceeding 8 and less than 10 and outputs the rows in the DataFrame which meet these conditions


While loops
While loop creates a repeated if statement.
Repeats an action until a condition is met.

while condition:
	expression

For loops
For each variable in a sequence execute an expression.
I.e. can iterate through a list or an array.

for var in seq:
	expression

To control how many times the for loop iterates use the range() function:
for x in range(10):
	expression

world = {‘key1’:value1, ‘key2’:value2}

Calling the .items() method when iterating over a dictionary:
for key, value in world.items():
	print(key + “--” + str(value))

Calling the nditer() function when iterating over a multidimensional Numpy array:
for val in np.nditer(meas):
	print(val)

Calling the .iterrows() method when iterating over a Pandas DataFrame:
Used to iterate over a pandas Data frame rows in the form of (index, series) pair. This function iterates over the data frame column, it will return a tuple with the column name and content in the form of a series.   

for lab, row in brics.iterrows():
	print(lab +  “: “ + row[“capital”])

On each iteration this for loop generates two pieces of data: the ‘label’ in the row and then the actual data in the row as a series.

row is a bit of a misnomer as it refers to the row data in the specified column name.


Random numbers

import numpy as np

np.random.seed(123) - starting from a seed number
np.random.rand() - generates pseudo random numbers based on the seed number
np.randint(0,2) - randomly generates a 0 or a 1 based on the seed number


Pandas
.head() - prints first 5 rows of a DataFrame
.tail() - prints last 5 rows of a DataFrame
.info() - displays info about the data such as type and non-null items
.dtypes - returns the data types in the DataFrame
.shape - this attribute displays the number of rows and columns in a DataFrame
.describe() - computes summary stats for columns with numeric values
.values - prints the data in the DataFrame
.columns - prints column names
.index - prints the number of rows

Sorting and subsetting DataFrames

.sort_values(“weight_kg”) - sorts the column “weight-kg” in ascending order
.sort_values(“weight_kg”, ascending = False) - sorts by descending order
.sort_values([“weight_kg”, “height_cm”], ascending = [True, False]) - sorts “weight_kg” by ascending order and then sorts “height_cm” by descending order


dogs[[“breed”, “height_cm”]] - inner brackets create a list of column names to subset and outer brackets subset the DataFrame
dogs[dogs[“date_of_birth”] > “2015 - 10 - 25”] - outputs all rows in the DataFrame which have a “date_of_birth” that exceeds “2015 - 10 - 25”
dogs[dogs[“color”].isin([“Black”, “Brown”])] - outputs all rows which have a “color” equal to black or brown
dogs[“height_m”] = [45,52,61,39] - creates a new column with the heading “height_m” with the data in the list






























DATA MANIPULATION WITH PANDAS


Summary statistics in DataFrames

Methods in DataFrames

dogs[“height_cm”].mean() - calculates the mean of the “height_cm” column
.median()
.mode()
.min()
.max()
.var()
.std()
.sum()
.quantile()
.agg(function) - allows you to pass a defined function into the .agg method. This method allows for non-standard methods to be run on DataFrames based on what the function is
.cumsum() - calculates the cumulative sum
.cummax() - shows the maximum value seen so far
.cummin()
.cumprod()


Counting in DataFrames

.drop_duplicates(subset = ‘name’) - drop duplicates in the name column
.drop_duplicates(subset = [‘name’, ‘breed’]) - drop elements where name and breed are duplicated
dogs[‘breed’].value_counts(sort = True, normalize = True) - counts the number of dogs of each type of breed. Normalize argument turns count into proportion of the total.


Grouped summary stats in DataFrames

dogs.groupby(‘color’)[“weight_kg”].mean() - group by color, select the weight column and calculate the mean for each colour group.
dogs.groupby(‘color’)[“weight_kg”].agg([min, max, sum]) - groups data by color and calculates the min, max and sum of the weight for each group.
dogs.groupby([‘color’, ‘breed’])[“weight_kg”].mean() - groups data by color and then by breed (for each colour) and calculates the mean of the weight for each group.



Pivot tables in DataFrames
A pivot table is a DataFrame with sorted indexes

dogs.groupby(‘color’)[“weight_kg”].mean()  
OR
dogs.pivot_table(values = ‘weight_kg’, index = ‘color’) - groups data by color and calculates the mean of the weight for each colour group. By default the pivot table calculates the mean value for each group.

dogs.pivot_table(values = ‘weight_kg’, index = ‘color’, aggfunc = [np.mean, np.median]) - groups data by color and calculates the mean and median weight for each colour group

dogs.groupby([‘color’, ‘breed’])[“weight_kg”].mean() - groups data by color and then by breed (for each colour) and calculates the mean of the weight for each group. 
OR
dogs.pivot_table(values = ‘weight_kg’, index = ‘color’, columns = ‘breed’) - produces the same result although it looks a bit different. The index argument is the column to group by and display in rows. The column argument is the column to group by and display in columns. 

dogs.pivot_table(values = ‘weight_kg’, index = ‘color’, columns = ‘breed’, fill_value = 0, margins = True) - fill_value fills all missing values with 0. Margins calculates the mean for all rows and columns

You can slice pivot tables in the same way you normally would a DataFrame

.mean(axis = ‘index’) - calling the mean function on a pivot table calculates the mean on the index values i.e. by row
.mean(axis = ‘columns’) - calling the mean function on a pivot table calculates the mean on the column values i.e. by column


Explicit indexes
Setting indexes violates the ‘tidy’ data principle of Python as there is separate syntax.
DataFrames are composed of three parts:
1.	Numpy array for data
2.	Index to store row details
3.	Index to store column details

dogs.set_index(‘name’) - sets the ‘name’ column as the index i.e. the far left column. This column is indented to the left, unlike the date in the DataFrame which is indented to the right.
dogs.reset_index(inplace=True) - resets the DataFrame to its original
dogs.reset_index(drop = True) - deletes the data in the index column

dogs[dogs[‘name’].isin([‘Bella’, ‘Stella’])
OR if you subsetted the ‘name’ column and called this new object dogs_ind
dogs_ind.loc[[‘Bella’, ‘Stella’]]

REMEMBER: when subsetting multiple columns you need to use double square brackets because the inner square brackets generate a list and the outer brackets do the subsetting.

dogs.set_index([‘breed’, ‘color’]] - the inner index ‘color’ is nested inside the outer index ‘breed’

dogs.loc[[‘Labrador’,’Chihuahua’]] - subset outer index
dogs.loc[[(‘Labrador’, ‘brown’),(‘Chihuahua’, ‘black’)]] - subset inner index with tuples. The result must match both conditions

dogs.sort_index() - sorts from outer to inner (in ascending order by default)
dogs.sort_index(level = [‘color’, ‘breed’], ascending = [‘True’, ‘False’]) - controlling the sort index

dogs.set_index(‘name’).sort_index() - sets and sorts the index

dogs.loc[(‘Labrador’, ‘brown’):(‘Schnauzer’, ‘grey)] - slicing the inner index using tuples. Only use one set of square brackets when slicing (as opposed to subsetting).

dogs.iloc[2:5, 1:4] - unlike .loc the end value is exclusive





















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


Creating DataFrames
DataFrames can be constructed in two ways:
1.	A list of dictionaries i.e. row by row
a.	list_of_dics = [{‘name’: ‘Karl’, ‘age’: ‘24’}, {‘name’: Jack, ‘age’: ‘26’}]
2.	A dictionary of lists i.e. column by column
a.	dict_of_lists = {‘name’: [‘Karl’, ‘Jack’], ‘age’: [‘24’, ‘26’]}
Option 2 is more efficient


Reading and writing CSVs

new_dogs = pd.read_csv(“new_dogs.csv”) - imports csv file
new_dogs.to_csv(“new_dogs_with_bmi.csv”) - writes to a new csv file
THE ANDROID APP MARKET ON GOOGLE PLAY

Read more about lambda expressions:
https://realpython.com/python-lambda/#lambda-calculus


Task 2
# List of characters to remove
chars_to_remove = ['+',",","$"]
# List of column names to clean
cols_to_clean = ["Installs","Price"]

# Loop for each column in cols_to_clean
for col in cols_to_clean:
    # Loop for each char in chars_to_remove
    for char in chars_to_remove:   
        # Replace the character with an empty string
        apps[col] = apps[col].apply(lambda x: x.replace(char, ''))


Task 3
# Convert Installs to float data type
apps['Installs'] = apps['Installs'].astype(float)

# Convert Price to float data type
apps['Price'] = apps['Price'].astype(float)

# Checking dtypes of the apps dataframe
print(apps.dtypes)


Task 4
# Print the total number of unique categories
num_categories = len(apps["Category"].unique())
print('Number of categories = ', num_categories)

# Count the number of apps in each 'Category'. 
num_apps_in_category = apps['Category'].value_counts()

# Sort num_apps_in_category in descending order based on the count of apps in each category
sorted_num_apps_in_category = num_apps_in_category.sort_values(ascending = False)



Task 6

# seaborn is a data visualisation library built on top of matplotlib and closely integrated with Pandas data structures

%matplotlib inline
import seaborn as sns
sns.set_style("darkgrid")

# Select rows where both 'Rating' and 'Size' values are present (ie. the two values are not null)
apps_with_size_and_rating_present = apps[(apps["Rating"] != 0) & (apps['Size'] != 0)]

# Subset for categories with at least 250 apps
large_categories = apps_with_size_and_rating_present.groupby("Category").filter(lambda x: len(x) >= 250)

# Plot size vs. rating
plt1 = sns.jointplot(x = large_categories["Rating"], y = large_categories["Size"])

# Select apps whose 'Type' is 'Paid'
paid_apps = apps[apps['Type']=='Paid']

# Plot price vs. rating
plt2 = sns.jointplot(x = paid_apps["Rating"], y = paid_apps["Price"])


Task 10
# Load user_reviews.csv
reviews_df = pd.read_csv('datasets/user_reviews.csv')

# Join the two dataframes
merged_df = pd.merge(apps, reviews_df, on = "App")

# Drop NA values from Sentiment and Review columns
merged_df = merged_df.dropna(subset = ['Sentiment', 'Review'])









JOINING DATA WITH PANDAS

Inner Joins

Data merging basics

ward_licenses = ward.merge(licenses, on = ‘ward’, suffixes = (‘_ward’, ‘_lic’) - matching the ward table and the licenses table based on values in the ward column in each table. The new table ward_licenses will include column names with suffixes where there are multiple columns with the same name

Code
-	The agg function counts the number of accounts by title
# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on = 'account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values('account', ascending = False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())


Output
                     			account
    title                   
    PRESIDENT           	6259
    SECRETARY          	5205
    SOLE PROPRIETOR     	1658
    OTHER               		1200
    VICE PRESIDENT       	970


Merging multiple DataFrames

Total riders in a month
-	Notice the loc call in the print statement - we filter row data by calling the variable filter_criteria (that specifies specific row data) and then we call the ‘rides’ column. We then sum this column
# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
                           .merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7)
                 & (ridership_cal_stations['day_type'] == 'Weekday')
                  & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria,'rides'].sum())


Three table merge
-	Notice the agg function finds the median income by alderman 
# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
                       .merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))


alderman                            	income                           
    
Ameya Pawar                 	66246.0
Anthony A. Beale            	38206.0
Anthony V. Napolitano       	82226.0
Ariel E. Reyboras           	41307.0
Brendan Reilly             	110215.0
Brian Hopkins               	87143.0
Carlos Ramirez-Rosa         	66246.0


Left Join
If your goal is to enhance or enrich a dataset, then you do not want to lose any of your original data. A left join will do that by returning all of the rows of your left table, while using an inner join may result in lost data if it does not exist in both tables.

movies_financials = movies.merge(financials, on = ‘id’, how = ‘left’) - the default value for how is inner. As such for an inner join we don’t have to specify this argument, but for a left join we must specify the argument. Match the movies and financials DataFrames/tables on id

If those rows in the left table match multiple rows in the right table, then all of those rows will be returned. The returned rows must be equal to if not greater than the left table.

Right Join

tv_movies = movies.merge(tv_genre, how = ‘right’, left_on = ‘id’, right_on = ‘movie_id’) - if we want to merge data on id but the column names, where the id values are held, have different names in each table, then we must specify the arguments left_on and right_on.

Outer Join
Useful to find rows that do not have a match in the other table

how = ‘outer’

Self Join
This merger is an inner join with a table on itself where a row in the table relates to another row in the same table

The how argument is an inner join, therefore no need to specify the argument inner as it is the default argument when calling the merge function

Merging on indexes
Works the same as merging on columns i.e. can inner, self, left or right join. Therefore, if you can merge on indexes there is no need to turn the indexes into columns, just merge on the index.

movies_genres = movies.merge(movies_to_genres, left_on = ‘id’, left_index = True, right_on = ‘movie_id’, right_index = True) - when merging on indexes, if you specify a left_on and right_on argument then you must also specify the left_index and right_index arguments in order to tell the merge function to use the separate indexes

Do sequels earn more?
-	Notice the second block of code is a self-join on an index, which we haven’t seen before. As such we only set the right_index = True and not the left_index
# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                            right_on='id', right_index=True,
                            suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff',ascending = False).head())

sequels_fin

             		title 		sequel     	budget    		revenue
id                                              
19995        		Avatar   	<NA>  		2.370e+08  		2.788e+09
862       		Toy Story    	863  		3.000e+07  		3.736e+08
863     			Toy Story 2  	10193  	9.000e+07 		4.974e+08
597         		Titanic   	<NA>  		2.000e+08  		1.845e+09
24428  		The Avengers   <NA>  	2.200e+08  		1.520e+09

If we are merging sequels_fin on itself, when setting left_on and right_on - if we look just at Toy Story:
-	Our left table would be the row highlighted above. We want to find a row (which is itself) that has an id of 863, which in our left table is the sequel column. As such we set our left_on = ‘sequel’ and search for a row where id = 863 - we therefore set right_on = ‘id’ i.e. our right side table


Filtering Joins

Semi-join
We want to output only the left table based on a characteristic that exists in both tables.
Using the .isin() method

Steps
1.	Merge the left and right table
2.	Search the left table for the results in the merged table using .isin() creating a Boolean Series
3.	Subset step 2 to output the actual results

Anti-join

indicator = True - adds a column called _merge which outputs both (exists in both tables) or left_only (exists only in the left table). We then filter the _merge column == ‘left_only’ as this excludes rows that exist in both tables i.e. anti-join


Summary of .merge() arguments
on = [‘country’, ‘date’]
how = ‘left’/’right’/’inner’/’outer’
indicator = True adds a column called _merge, useful for anti-joins
left_on = when left and right table are matched on data that have different column names
right_on = when left and right table are matched on data that have different column names
suffixes = (‘_ward’, ‘_lic’)

For indexes
left_index = specify this argument when left_on is used
right_index = specify this argument when right_on is used


Concatenate tables vertically (as opposed to horizontally)
Used to combine tables vertically

pd.concat([df1, df2])

pd.concat() method and set axis = 0 to concatenate vertically. The axis argument is set to 0 by default for the .concat() method and so we don’t need to explicitly write this.

Tables are combined in the order they are passed into the .concat() method.

Tables maintain their original index numbers once combined. If we want to reset the index numbers we pass the argument ignore_index = True into the method.

If we want to set keys for each table (basically a second index with names for each table in the combined table) then we pass the argument keys = [‘key1’, ‘key2’, ‘key3’] into the method. Be sure to set ignore_index = False.

The sort = True argument alphabetically sorts the column names

Vertically concatenate tables with different columns
Set the join = ‘inner’ argument to concatenate only columns that are common to all tables. By default the argument is set as join = ‘outer’ meaning all columns from all tables are included. When you specify the join = ‘inner’ argument the sort = True argument has no effect as the order of the columns will be the same as in the original tables.

Append method
.append() is a simplified .concat() method and supports both the ignore_index and sort arguments but does not support the keys or join arguments (join is always set to outer) 

df1.append(df2)

Verifying Integrity
Duplicated data can skew the data set e.g. impact the mean, alter the line plot etc.

When concatenating or merging tables there may be duplicate values which will create an unintentional one-to-many or many-to-many relationship

Merge
Provide one of the following arguments based on what you expect the output relationship to be:

validate = ‘one_to_one’ - no duplicate keys
validate = ‘one_to_many’ - if there is a duplicate key in the right table
validate = ‘many_to_one’ - if there is a duplicate key in the left table
validate = ‘many_to_many’ - if there is a duplicate key in one of the tables

Python will output/validate whether this is true or not

Concatenating
Pass in the argument verify_integrity = True. This checks for duplicate values in the index and NOT the columns. By default this is set to False i.e. it does not check for duplicate values.


Ordered merge
Useful when working with ordered or time-series data where order matters. The method orders data based on the on = argument. You can still use all the same arguments as .merge()

Use the pd.merge_ordered() method

Difference between .merge() and pd.merge_ordered():
-	df1.mege(df2) vs pd.merge_ordered(df1, df2)
-	Default for .merge() is how = ‘inner’ but for merge_ordered() it is how = ‘outer’

Forward fill
Fills in missing data in the table by filling missing values with the previous value by using the fill_method = ‘ffill’ argument

.corr() function in python calculates the correlation

Be careful with forward fill
“When you merge on date first, the table is sorted by date then country. When forward fill is applied, Sweden's population value in January is used to fill in the missing values for both Australia and Sweden for the remainder of the year. This is not what you want. The fill forward is using unintended data to fill in the missing values. However, when you merge on country first, the table is sorted by country then date, so the forward fill is applied appropriately in this situation.”


merge_asof()
Matches on the nearest key column rather than actual values.
Useful when matching data that does not exactly align (such as matching on timestamps).
N.B. the columns you want to merge “on” must be sorted.

pd.merge_asof(df1, df2, on = “date_time”, suffixes = (“visa”, “ibm”), direction = “forward”)

The default value for the direction argument is ‘backward’.
When the direction argument is set to forward the method selects the first row in the right table whose on key argument is greater than or equal to the left key column. 

Can also set direction = ‘nearest’ for the closest match below or above the on key argument.


.query() method
Alternative to subsetting but more intuitive.
Similar to the statement after the WHERE clause in SQL.
The method accepts an input string to determine what rows are selected

stocks.query(‘nike > 90 and disney < 140’) - use single quotes when using .query()
stocks.query(‘stock == “disney” or (stock == “nike” and close < 90’) - use double quotes when checking text

gdp_pivot.query(‘date >= “1991-01-01”’)


.melt() method
Useful when you have a very wide pivot table that is not easy to work with.
This method changes a pivot table from wide to long format:
-	Wide format is usually easier for humans to read;
-	But long format is more accessible for computers to work with

social_fin.melt(id_vars = [‘financial’, ‘company’], value_vars = [‘2019’,’2018’], var_name = [‘year’], value_name = ‘dollars’) - the id_vars argument specifies the columns we DO NOT want to change. The value_vars argument specifies columns to un-pivot, with any columns not specified being dropped from the dataset. The var_name argument changes the name of the column variable to year and the value_name argument changes the name of the column value to dollars















































Project: The Github History of the Scala Language

When a csv file is imported into python as a DataFrame any date time objects are read as string objects rather than date time objects. It is hard to perform operations on such string data. As such we use the following method to covert the data to a date time object:

.to_datetime() - converts string date time into python date time object

Example: pulls['date'] = pd.to_datetime(pulls['date'], utc = True)

Syntax:
pd.to_datetime(arg, errors=’raise’, dayfirst=False, yearfirst=False, utc=None, box=True, format=None, exact=True, unit=None, infer_datetime_format=False, origin=’unix’, cache=False)
 
Parameters:
arg: An integer, string, float, list or dict object to convert in to Date time object.
dayfirst: Boolean value, places day first if True.
yearfirst: Boolean value, places year first if True.
utc: Boolean value, Returns time in UTC if True.
format: String input to tell position of day, month and year.


Step 4

%matplotlib inline

# Create a column that will store the month
data['month'] = data['date'].dt.month - the dt.month attribute returns the month from the rows in the date column

# Create a column that will store the year
data['year'] = data['date'].dt.year - the dt.year attribute returns the year from the rows in the date column

# Group by the month and year and count the pull requests
counts = data.groupby(['year','month']).count()

# Plot the results
counts.plot(kind='bar', figsize = (12,4))


Step 5
# Required for matplotlib
%matplotlib inline

# Group by the submitter
by_user = data.groupby('user')['pid'].count() - option 1 using .count function

OR

by_user = data.groupby('user').agg({'pid':'count'}) - option 2 using .agg method

# Plot the histogram
by_user.plot(kind='bar', figsize = (12,4))


Step 6

# Identify the last 10 pull requests
last_10 = pulls.sort_values(by = 'date').tail(10) - .tail(10) extracts the last 10 rows from the DataFrame

# Identify the unique files

files = joined_pr.drop_duplicates(subset='file') - identifies unique rows by the ‘file’ column
OR
files = set(joined_pr['file']) - identifies unique rows by the ‘file’ column


Step 7

# Print the top 3 developers
author_counts.nlargest(3, 'file') - prints the 3 largest rows according to values in the “file” column


Step 9
%matplotlib inline

# The developers we are interested in
authors = ['xeno-by', 'soc']

# Get all the developers' pull requests
by_author = pulls[pulls['user'].isin(authors)]

# Count the number of pull requests submitted each year
counts = by_author.groupby([by_author['user'], by_author['date'].dt.year]).agg({'pid': 'count'}).reset_index()

# Convert the table to a wide format
counts_wide = counts.pivot_table(index='date', columns='user', values='pid', fill_value=0)

# Plot the results
counts_wide.plot(kind='bar')








EXPLORATORY DATA ANALYSIS WITH PYTHON AND BINANCE

Step 1

# INSTALL DEPENDENCIES
!pip install python-binance 
!pip install pandas # for financial analysis, working with data in tabular format
!pip install mplfinance 

# IMPORT DEPENDENCIES
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager 
import pandas as pd


Step 3
tickers = client.get_all_tickers() - grabs all the tickers


Step 4

depth = client.get_order_book(symbol = "BTCUSDT") - gets the order book (price & volume)
depth_df.columns = ['Price','Volume'] # setting the column names - .columns is used to set column names

depth_df.dtypes - returns the data types of each column in the DateFrame

Output:

Price     	object - this means that price is a string
Volume    	object
dtype: 		object


Step 5

historical = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2011") - gets historical data per day from 1 Jan 2011


Step 6

hist_df[numeric_columns] = hist_df[numeric_columns].apply(pd.to_numeric, axis=1) - .apply converts the columns listed in numeric_columns into numeric values and the argument axis = 1 performs the method on the actual columns


Step 7

import mplfinance as mpf

hist_df_view = hist_df.set_index('Close time').tail(100) # last 100 rows

mpf.plot(hist_df_view, type = 'candle', 
         style = 'charles', 
         volume = True,
         title = 'BTCUSD last 100 days',
         mav = (10,20,30))













































INTRODUCTION TO DATA VISUALIZATION WITH MATPLOTLIB


Subplots/Small multiples
.subplots() are part of the matplotlib library - multiple small plots that show similar data across different conditions e.g. precipitation data across different cities.
Small multiples are called subplots in matplotlib - used to overcome the issues of having to plot too much data.
Can be used to compare multiple plots side-by-side.
Useful when creating a figure with multiple axes.


Syntax
Import matplotlib.pyplot as plt - .pyplot is a sub module

Adding data to a figure is done by calling methods of the Axes object.
fig, ax = plt.subplots() -  when called without any inputs subplots creates two objects: 1. fig - figure, holds everything we see 2. ax - axes, holds the data


Plot method
Ax is the object and .plot is the method

ax.plot(seattle_weather[“MONTH”], seattle_weather[“MLY-TAVG-NORMAL”] - this is a plotting command, which is a method of the axis object. The first argument is the x coordinate and the second is the y coordinate


Arguments for ax.plot() function

marker = ‘o’ - adds a markers shaped like an ‘o’ for x,y coordinates on the graph
https://matplotlib.org/stable/api/markers_api.html - visit this link for all marker styles
linestyle = ‘--’ - changes the line style to ‘--’
https://matplotlib.org/2.0.1/api/lines_api.html - visit this link for more line styles
linestyle = ‘none’ - eliminates the line and only shows the markers
color = ‘r’ - changes the color of the markers and line to red


Set methods
Used to change certain properties of the object

ax.set_xlabel(“Time (months)”) - setting the name of the x label. Only capitalize the first word in an axis label, unless subsequent words are proper nouns
ax.set_ylabel(“Average temperature”) - adds y label
ax.set_title(“Weather in Seattle”) - adds a title


Subplots part 2

Adding data to a figure is done by calling methods of the Axes object.
fig, ax = plt.subplots(3,2) - creates an array of subplots with 3 rows and 2 columns i.e. 6 subplots
ax[0,0].plot = (seattle_weather[“MONTH”], seattle_weather[“MLY-TAVG-NORMAL”]) - sets the subplot at row 0, column 0.

REMEMBER - even though we created the subplot as an array (3,2) the top left plot is at coordinates [0,0], the top right plot is at [0,1], bottom right [2,1] etc.

fig, ax = plt.subplots(2,1, sharey = True) - sharey set to True means both subplots will have the same range of y-axis values

Exception: when the array is 1-dimensional i.e. fig, ax = plt.subplots(2,1) - 2 rows and 1 column - when setting the subplot at [0,0] we just use [0] and similarly when setting the second row we just use [1]


Plotting Time Series

Reading in a csv file with date data in string format:

climate_change = pd.read_csv(“climate_change.csv”, parse_dates = True, index_col = 0) 

By setting parse_dates = True Python sets all date data to DateTime Python objects. Setting index_col = 0 tells Python to treat the first column as the index.

If we call print(climate_change.index) Python prints a list of the index, which has been set to the date column in this case (as the first column consisted of dates).


Plotting Time Series with different variables

If we want to plot two sets of data with the same x-axis and but whose y-axes scales differ we use the following line of code in line 2:

Line 1: 	ax.plot(climate_change.index, climate_change[‘Co2’])  - 1st plot
Line 2:		ax2 = ax.twinx() - twin axes object
Line 3:		ax2.plot(climate_change.index, climate_change[‘relative_temp’]) - 2nd plot

If we want to change the color of the ticks and tick marks on the x or y axis we use the following method and pass the argument ‘y’ or ‘x’ depending on which ticks we want to change.
ax.tick_params(‘y’, colors = ‘blue’)


Function that plots time series data
Defining functions allows us to reuse the same code without having to repeat all of it.
The function calls the methods of the axes object

def plot_timeseries(ax, x, y, color, xlabel, ylabel):
	ax.plot(x, y, color = color)
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	ax.tick_params(‘y’, colors = color)

Using the function:
Line 1:		plot_timeseries(ax, climate_change.index, climate_change[‘co2’], ‘blue’,
‘Time’, ‘Co2 (ppm)’)
Line 2:		ax2 = ax.twinx()
Line 3:		plot_timeseries(ax2, climate_change.index, 
climate_change[‘relative_temp’], ‘red’,‘Time’, ‘Relative temperature’)


Annotating Time Series data

https://matplotlib.org/stable/tutorials/text/annotations.html  - visit this link for all matplotlib annotation documentation

ax.annotate(“>1 degree”, xy = (pd.TimeStamp(‘2015-10-06’), 1), xytext = (pd.TimeStamp(‘2008-10-06’), -0.2), arrowprops = {“arrowstyle”: “->”, “color”:”gray”})

“>1 degree”  - refers to the annotation text
 xy = (pd.TimeStamp(‘2015-10-06’) - is the coordinates the text refers to
xytext = (pd.TimeStamp(‘2008-10-06’), -0.2) - is the coordinates where the text is placed
arrowprops = {“arrowstyle”: “->”, “color”:”gray”}) - a dictionary of arrowstyle and arrow colo


Quantitative comparisons and statistical visualizations

Stacked bar charts
A stacked bar chart contains bars, where the height of each bar represents values. In addition, stacked on top of the first variable may be another variable. The additional height of this bar represents the value of this variable.

Line 1:	fig, ax = plt.subplots() - initializing the figure and axes objects
Line 2:	ax.bar(medals.index, medals[“Gold”], label = “Gold) - adds a bar graph and the label 
“Gold” which will be represented on the graph when the legend method is called later
Line 3:	ax.bar(medals.index, medals[“Silver”], bottom = medals[“Gold”], label = “Silver”)
Creates a stacked bar chart where gold medals are visually represented below the silver medals	
Line 4:	ax.bar(medals.index, medals[“Bronze”], bottom = medals[“Gold”] + 
medals[“Silver”],label = “Bronze”) 
Adds bronze medals and stacks gold and silver medals are visually below. The order here doesn’t matter as gold will be at the bottom given that it was defined first in the argument in Line 3
Line 5: ax.set_xticklabels(medals.index, rotation = 90) - sets labels for each tick on the x 
axis and rotates them by 90 degrees
Line 6:	ax.legend() - call the axes legend method which adds in a legend
Line 7: plt.show()


Histograms
Shows the number of observations (on the y-axis) within a particular ‘bin’ of values (on the x-axis)
Line 1:	ax.hist(mens_rowing[“Height”], label = “Rowing”, bins = 20, histtype = “step”)
By default the number of bins is 10. Can also pass a list to bins = [10,20,30,40,50] which would be the boundaries between individual bins. 
By default histtype = “bar”, however if multiple histograms are plotted they can obscure each other. Setting histtype = “step” only show the outlines of the bars
Line 2: ax.set_xlabel(“Height in cm”)
Line 3:	ax.set_ylabel(“# of observations”)
Line 4:	ax.legend()


Statistical plotting

ax.bar(“Rowing”, mens_rowing[“Height”].mean(), yerr = mens_rowing[“Height”].std())
Bar graph with the x tick mark “Rowing”. The yerr argument adds markers to the graph. In in this case it adds just one marker showing the standard deviation

ax.errorbar(seattle_weather[“MONTH”], seattle_weather[“AVG_TEMP”], yerr = seattle_weather[“STD_TEMP”])
The errorbar method, of the axes object, produces a line chart plotting month vs average temperature and places markers of standard deviation for each month (based on the STD_TEMP column)

Line 1:	ax.boxplot([mens_rowing[“Height”], mens_gymnastics[“Height”]])
Takes in a list into the boxplot methods and outputs two boxplots of height for rowing and gymnastics
Line 2:	ax.set_xticklables([“Rowing”, “Gymnastics”])
Notice the square brackets to specify the list of x-axis labels


Scatter plots
Useful for bi-variate comparison i.e. comparing two variables (such as the relationship between height and weight)

Line 1:	fig, ax = plt.subplots()
Line 2:	ax.scatter(climate_change[“co2”], climate_change[“relative_temp”], c = climate_change.index)
	Note that climate_change.index refers to the date column in this DataFrame. The 
argument c = is a color encoding argument that displays different colors for the range 
of variables passed to this argument.

Plot styles

Refer to the link below for different plot styles
https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html

plt.style.use(“ggplot”) - plot style from the ggplot library
plt.style.ust(“Solarize_Light2”) - cool style
plt.style.use(“default”) - reverts back to the original style

Seaborn is a library for statistical visualization that is based on Matplotlib.

Saving your plot to a file

fig.savefig(“gold_medals.png”) - this file format provides lossless compression of image (high quality and large file size). 

fig.savefig(“gold_medal.jpg”, quality = 50) - use .jpg for lossy compression if you want to use less space and lower quality. The argument quality takes in a number from 1 to 100 depending on the quality you desire. Avoid values>95 as the compression is no longer effective
 
fig.savefig(“gold_medal.svg”) - produces a vector graphics file which can be edited by advanced graphics software

fig.savefig(“gold_medals.png”,dpi = 300) - the dpi (dots-per-inch) argument refers to quality with which the image is rendered


fig.set_size_inches([5,3]) - 1st number sets width, 2nd number sets height. This determines the aspect ratio

If we then call the Unix function:
ls - this provides a lists of file in the present directory


Automating figures from data
One of the main strengths of Matplotlib is that it can be automated to adapt to the data that it receives as input. For example, if you receive data that has an unknown number of categories, you can still create a bar plot that has bars for each category.

sports = [“Rowing”, “Baseball”, “Tennis, “Soccer”]

fig, ax = plt.subplots()
for x in sports:
	sport_df = summer_2016_medals[summer_2016_medals[“Sport”] == x]
	# pulls all rows where the value in the “Sport” column is equal to x
	ax.bar(x, sport_df[“Height”].mean(), yerr = sport_df[“Height”].std()
ax.set_ylabel(“Height (cm)”)
ax.set_xticklabels(sport, rotation = 90)
plt.show()


Where to go next
Refer to the site below

https://matplotlib.org/2.0.2/gallery.html

3D images
https://matplotlib.org/2.0.2/mpl_toolkits/mplot3d/tutorial.html

Creating colorful images
https://matplotlib.org/2.0.2/users/image_tutorial.html

Animated visuals
https://matplotlib.org/stable/api/animation_api.html

(Pandas & Matplotlib) using Seaborn
https://seaborn.pydata.org/examples/index.html
https://seaborn.pydata.org/examples/index.html













































INTRODUCTION TO DATA VISUALIZATION WITH SEABORN

1. Introduction to Seaborn

Built on top of Matplotlib.
Handles lots of the complexity in the background.
Works well with Pandas data structures.

Steps in data analysis:
1.	Gather data
2.	Transform & clean
3.	Exploration
4.	Analyze and build models
5.	Communicate results

Seaborn is useful for steps 3 & 5 in the data analysis journey.

Syntax:

import seaborn as sns
import matplotlib.pyplot as plt

x = [180, 175, 178]
y = [74,80, 82]
sns.scatterplot(x = height, y = weight)
plt.show()

region = [South Africa, US, South Africa, Holland, Holland, South Africa]
sns.countplot(y = region) - displays the region on the y-axis, while the x-axis displays a bar graph of the count/number in each region. You can either set the y or x axis depending on how you want the bars displayed i.e. horizontally (set y) or vertically (set x)


Creating a plot from a DataFrame

sns.countplot(x = “how_masculine”, data =df) - we are plotting the column how_masculine from the DataFrame df. If you want the bars to be horizontal, instead of vertical, set y = “how_masculine”, instead of x


Adding a third variable with hue (subgroups)

sns.scatterplot(x = “total_bill”, y = “tips”, data = tips, hue = “smoker”) - the hue argument adds a third variable which adds color to the various x and y coordinates based on whether that person is a smoker or not. Seaborn also adds a legend to identify what each color means. 

Additional arguments
hue_order = [“Yes”, “No”] - assigns the order to the legend
palette = {“Yes”: “black”, “No”: “red”} - sets the colors for the hue

Matplotlib colors
“blue”/”b”
“green”/”g”
“red”/”r”
“cyan”/”c”
“magenta”/”m”
“yellow”/”y”
“black”/”k”
“white”/”w”


2. Visualising two quantitative variables

Relational plots/Subplots
Used to show the relationship between two quantitative variables i.e. scatter plots and line plots

relplot() - relational plot. Supports making subplots.

sns.relplot(x = “total_bill”, y = “tips”, data = tips, kind = ‘scatter’, col = ‘smoker’, row = ‘time’) - the argument kind can either be ‘scatter’ or ‘line’. Setting the col argument produces two separate plots: one for smokers and one for non-smokers. The row argument creates another two plots on the row below. The col argument arranges the plots side-by-side. The row argument arranges the plots vertically.


Additional arguments
col_wrap = 2 - sets the maximum number of columns for subplots equal to 2 i.e. 2 columns of plots
col_order = [ ] - pass a list of the order you want the plots to appear in


Customising scatter plots
These arguments can be used for either relplot() or scatterplot(), but relplot() offers more flexibility so it is better to use

size = “weights” - set the size of each point based on the weights column in the data set
hue = “weights” - changes the colour of each point based on the weights column
style = “smoker” - uses different point styles for each value of the variable i.e. yes and no are assigned different styles
alpha 0.4 - changes the transparency. 0 is completely transparent and 1 is fully transparent


Introduction to line plots

Set the argument kind = “line”.
If there are multiple observations per x-value then the line plot displays the mean of these values.
Seaborn automatically calculates a confidence region displayed by the shaded region around the line plot. This indicates the uncertainty with respect to the mean value. We are 95% confident that the mean falls within this region of the plot.

Setting the argument ci = “cd” shows the shaded region around the plot as the standard deviation rather than the confidence level. This shows us the distribution of observations.

Setting ci = None turns off the shaded area.

Customising line plots
markers = True - places markers on a line plot for each data point
dashes = False - turns off dashed lines in a line plot


3. Visualising a categorical and a quantitative variable

Categorical plots
Categorical plots include: count plots, bar plots, box plots and point plots

catplot() - similar functionality to relplot() but used to plot the distribution of a quantitative variable by category. Supports making subplots

Use col and row parameters to add subplots, in addition to hue


Count plots
Previously:	sns.countplot(x = “how_masculine”, data =masculinity_data)
Now:		sns.catplot(x = “how_masculine”, data =masculinity_data, kind = ‘count’)

Additional arguments
order = [ ] - pass a list into this parameter to set the order you want the categories to appear on the plot


Bar plots
Bar plots show the mean of a quantitative variable per category.
By default Seaborn shows the 95% confidence level for these means, which show us the level of uncertainty.

sns.catplot(x = ‘day’, y = ‘total_bill’, data = tips, kind = ‘bar’)

Additional arguments
ci = None - turns off the confidence intervals

Note
When the y-variable is True/False, bar plots will show the percentage of responses reporting True. This plot shows us that males report a much higher interest in math compared to females.


Box plots
Useful for comparing categorical data (such as days of the week) across quantitative variables (such as total tips)

sns.catplot(x = ‘day’, y = ‘total_bill’, data = tips, kind = ‘box’)

Additional arguments
sym = “ ” - passing an empty string into this parameter will omit the outliers in the box plot.
whis = 2.0 - by default the whiskers are set to 1.5 * IQR (interquartile range = Q3 - Q1).
whis = [5, 95] - alternatively this will specify the lower whisker be drawn at the 5th percentile and the upper whisker at the 95th percentile.
whis = [0, 100] - places the whiskers at the min and max values.


Point plots
Shows the mean of a quantitative variable for each category as a point.
The confidence interval for the mean is drawn as a vertical line (95% confidence interval).

sns.catplot(x = “age”, y = “masculinity_important”, data = masculinity_data, hue = “feel_masculine”, kind = “point”)

Additional arguments
join = False - removes the joining lines between mean values
capsize = 0.2 - changes the size of the caps at the end of each confidence interval line
ci = None - turns off the confidence interval off and just shows the mean value

Displaying the median instead of the mean
from numpy import median
sns.catplot(x = “smoker”, y = “total_bill”, data = tips, kind = “point”, estimator = median) - instead of plotting the mean, setting the estimator argument to median plots the median values


4. Customising Seaborn plots

Changing plot style and color

sns.set_style(“whitegrid”) - changes the background to show a whitegrid. You can also pass in “dark”, “white”, “darkgrid” and “ticks” (adds tick marks to x and y axis)

sns.set_palette(“RdBu”) - this a scale of colours. 
Can also pass in:
Diverging palettes: “PRGn”, “RdBu_r”, “PRGn_r”; or
Sequential palettes: “Greys”, “Blues”, “PuRd”, “GnBu”, “Purples”

custom_palette = [“red”, “green”, “orange”]
sns.set_palette[custom_palette] - set your own custom palette


Changing the scale

sns.set_context() - changes the size of the scale. Pass in the arguments: “paper” (smallest - use in a paper session), “notebook” (use in an iPython Notebook), “talk” (use in a talk/presentation) or “poster” (largest - use in a poster session)


Adding titles and labels
Must first determine whether the plot is a FacetGrid and AxesSubplot.
relplot() and catplot() are FacetGrids (can create subplots) while scatterplot(), countplot(), boxplot() etc. are AxesSubplots (only creates a single plot)

Do this by setting:

g = sns.scatterplot(x = ‘height’, y = ‘weight’, data = df)
type(g) - determine the type of the plot. If it is a FacetGrid then use the code below.

For a FacetGrid type object:
g.fig.suptitle(“New Title”, y = 1.05) - the y parameter sets the height of the label. The default height is 1.

For an AxesSubplot type object:
g.fig.suptitle(“New Title”, y = 1.05) - setting the main title
g.set_title(“This is {col_name}”) - this will set each subplot title based on the name in the column

Axis labels (for both FacetGrid and AxesSubplot objects):
g.set(xlabel = “New x label”, ylabel = “New y label”)

To rotate labels (for both FacetGrid and AxesSubplot objects):
plt.xticks(rotation = 90)





























PYTHON DATA SCIENCE TOOLBOX (PART 1)

1. Writing your own functions

Strings in Python
Unlike with numeric types such as ints and floats, the + operator concatenates strings together, while the * concatenates multiple copies of a string together.

Docstrings
-	Describe what the function does
-	Placed immediately after the function header
-	“““Placed between triple quotation marks”””


Function header

Define the function
def shout(word):
	shout_loud = word + “!!!”
	print(shout_loud)

Call the function
shout(“congratulations”)
	
Note that shout(word), the part of the header that specifies the function name and parameter(s), is known as the signature of the function.

Function body
Function bodies need to be indented by a consistent number of spaces and the choice of 4 is common.

Return vs Print
The return keyword lets you return values from functions. Returning values is generally more desirable than printing them out because a print() call assigned to a variable has type NoneType.


Multiple parameters and return values

Tuples: immutable (cannot modify values once constructed), defined using ( ) brackets

def raise_both(value1, value2):
   """Raise value1 to the power of value2 and vice versa."""
					
   new_value1 = value1 ** value2
   new_value2 = value2 ** value1
		
   new_tuple = (new_value1, new_value2) - stores the result as a tuple
   return new_tuple

Note that the return statement return x, y has the same result as return (x, y): the former actually packs x and y into a tuple under the hood!


2. Default arguments, variable-length arguments and scope

Scope and user-defined functions
Global scope: defined in the main body of a script
Local scope: defined inside a function
Built-in scope: pre-defined built-in functions

Global keyword
Defining a variable as global within the function means any call to that variable (like print(x)) in the main body of code, takes the variable value from within the function. This would not otherwise be the case if the global keyword was not used as this variable is defined locally.

Built-in functions
To access a list of the built-in functions

import builtins - the name builtins is not itself builtin therefore we must import it
dir(builtins) - prints a list of the builtin function

Nested functions
Useful when we want to use a process a number of times to improve efficiency

def outer(...):
	x = …

	def inner(...): 

#nested/inner function
	
y = x ** 2
	return …

Python first searches the local scope inner to find x, and if it doesn’t find it, it searches the scope of the function outer. The function outer is known as an enclosing function as it encloses the function inner. If Python can’t find x in the scope of the enclosing function it searches the global scope and then the built-in scope

Name references will search at 4 scope levels, in this order (LEGB):
1.	Local scope
2.	Enclosing functions
3.	Global
4.	Built-in

N.B. assigning names will only create or change local names, unless these changes are preceded by the statement global or nonlocal. The keyword nonlocal is used in the inner function to create and change names in the enclosing scope (outer function).

Nonlocal is similar in meaning to global. But it takes effect primarily in nested methods. It means "not a global or local variable." So it changes the identifier to refer to an enclosing method's variable.

Nested functions 1

# Define three_shouts
def three_shouts(word1, word2, word3):
   """Returns a tuple of strings
   concatenated with '!!!'."""

   # Define inner
   def inner(word):
       """Returns a string concatenated with '!!!'."""
       return word + '!!!'

   # Return a tuple of strings
   return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))


Closure
In data science closure refers to when the nested or inner function remembers the state of its enclosing scope when called. Thus, anything defined locally in the enclosing/outer scope is available to the inner function even when the outer function has finished execution.


Default arguments

In order to create a default argument, when defining the argument in the function header use the equals sign:

def power (num, pow = 1):
	new_value = num ** pow
	return new_value

Calls to the power function
1.	power(9,2) - we have changed the default argument to equal 2
2.	power(9,1) - equivalent to power(9)
3.	power(9) - the default argument is set to 1 and so doesn’t need to be specified in the call


Flexible arguments
Useful when don’t know how many arguments there will be

def add_all(*args):
# turns all the arguments passed to it into a tuple

	sum_all = 0 
	
	for num in args:
		sum_all += args

	return sum_all


Call the function with any number of arguments
add_all (4,6,8,3,5)
	
26


Keyword argument
Argument preceded by identifiers.
Turns the identifier keyword pairs into a dictionary within the function body


Calling the .items() method when iterating over a dictionary:

def print_all(**kwargs):
# print out key-value pairs in **kwargs

for key, value in kwargs.items():
		print(key + “--” + str(value))
		# prints all the key-value pairs stored in the dictionary kwargs

print_all(name=”Karl”, age=26, sex=”male’)

Note: the names *args and **kwargs are not important - it is the asterisk/star preceded by the name that matters.


Bringing it all together Part 1
Initializing a dictionary.
“Developing a function that counts how many tweets are in certain languages. The output of your function was a dictionary that had the language as the keys and the counts of tweets in that language as the value.”

tweets_df = pd.read_csv(“tweets.csv”)

# Define count_entries()
def count_entries(df, col_name='lang'):
   """Return a dictionary with counts of
   occurrences as value for each key."""

   # Initialize an empty dictionary: cols_count
   cols_count = {}

   # Extract column from DataFrame: col
   col = df[col_name]
  
   # Iterate over the column in DataFrame
   for entry in col:

       # If entry is in cols_count, add 1
       if entry in cols_count.keys():
           cols_count[entry] += 1

       # Else add the entry to cols_count, set the value to 1
       else:
           cols_count[entry] = 1

   # Return the cols_count dictionary
   return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df)

# Call count_entries(): result2
result2 = count_entries(tweets_df,'source')

# Print result1 and result2
print(result1)
print(result2)


Bringing it all together Part 2
Using *args and iterating over column name args.
Notice the difference in the line item for extracting a column from the DataFrame to the code above.
tweets_df = pd.read_csv(“tweets.csv”)

# Define count_entries()
def count_entries(df, *args):
   """Return a dictionary with counts of
   occurrences as value for each key."""
  
   #Initialize an empty dictionary: cols_count
   cols_count = {}
  
   # Iterate over column names in args
   for col_name in args:
  
       # Extract column from DataFrame: col
       col = df[col_name]
  
       # Iterate over the column in DataFrame
       for entry in col:
  
           # If entry is in cols_count, add 1
           if entry in cols_count.keys():
               cols_count[entry] += 1
  
           # Else add the entry to cols_count, set the value to 1
           else:
               cols_count[entry] = 1

   # Return the cols_count dictionary
   return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang','source')

# Print result1 and result2
print(result1)
print(result2)



3. Lambda functions and error handling

Lambda functions
Useful for writing simple functions quickly.

raise_to_power = lambda x: y = x**y

raise_to_power(2,4)

We specify the names of the arguments.
After the colon we specify what we want the function to do.


Anonymous functions (using lambda)
The functionality is not stored in the environment, unlike a function with def.
Passes the function over all elements of a sequence i.e. on a unitary basis.
Lambda functions include: map(), filter() and reduce()


Map

nums = [2,4,6,8]

square_all = map(lambda num: num **2, nums)

print(list(square_all)) - must pass to list function first as this is a map object


Filter
Used to filter out elements from a list that don’t satisfy a specified criteria.


Create, from an input list of strings, a new list that contains only strings that have more than 6 characters:

fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

result = filter(lambda member: len(member) > 6 , fellowship)

print(list(result))


Reduce
The reduce() function is useful for performing some computation on a list and, unlike map() and filter(), returns a single value as a result. To use reduce(), you must import it from the functools module.

from functools import reduce

stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

result = reduce(lambda item1, item2: item1 + item2, stark)

print(result)


Error handling
Exceptions - errors caught during execution.
Use the try-except clause. Runs the code following try, but if it can’t then it runs the code following except.


Example

def sqrt(x):
	“““Returns the square root of a number”””
if x < 0:
raise ValueError(‘x must be non-negative’)	
try:
		return x ** 0.5
	except TypeError:
		print(‘x must be an integer or a float’)


Bringing it all together example

def count_entries(df, col_name='lang'):
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

PYTHON DATA SCIENCE TOOLBOX (PART 2)

1. Using iterators in PythonLand

Iterables
-	Lists, strings, range objects, dictionaries and file connections are all iterables. There are many others.
-	It is an object that has an associated iter method. Once applied to an iterable, an iterator is created.
-	So an iterable is an object that can return an iterator once the iter() method is applied to it.
-	An iterator keeps state and produces the next value when you call next() on it.
-	Under the hood a for loop performs the above functionality i.e. you can either use a for loop or the above functionality utilizing the next() method.
-	You use the iter() function to get an iterator object, and the next() function to retrieve the values one by one from the iterator object.

Iterator
-	An object that has an associated next() method that produces the consecutive values

Next() method

Example 1
word = ‘da’		iterable
it = iter(word)		iterator
next(it)		retrieving values from the iterator object

‘d’

next(it)

‘a’

Example 2
Recall that range() doesn't actually create the list; instead, it creates a range object with an iterator that produces the values until it reaches the limit.

for i in range(4):
	print(i)

The above is equivalent to:

small_value = iter(range(4))
print(next(small_value)
print(next(small_value)
print(next(small_value)

Iterating all at once
Using the * character to iterate over a sequence all at once.

Example (using the splat * operator)
# prints everything

word = ‘da’
it = iter(word)
print(*it)

d a

Iterating over dictionaries
Using the items() method

for key, value in dict_name.items():
	print(key, value)

Iterating over file connections

file  = open(‘file.txt’)
it = iter(file)
print(next(it))

This is the first line

print(next(it))

This is the second line


Enumerate
A function that takes any iterable as a function (such as a list) and returns an enumerate object.
The enumerate object is also an iterable.
Enumerate() returns an enumerate object that produces a sequence of tuples, and each of the tuples is an index-value pair.

Enumerate and unpack

for index, value in enumerate(avengers):
	print(index, value)

Output
0 hawkeye
1 iron man
2 thor

for index, value in enumerate(avengers, start = 10): #starts at index 10
	print(index, value)


Zip()
A zip() object is an iterator of tuples.

Example
# creating a list of tuples
avengers = [‘thor’, ‘iron man’]
names = [‘batman’, ‘spider man’]

z = zip(avengers, names)
z_list = list(z)
print(z_list)

Output
[(‘thor’,’batman’), (‘iron man’,’spider man’)]


Alternative 1
for a, b in zip(avengers, names):
	print(a, b)

Output
thor batman
iron man spider man


Alternative 2 (using the splat * operator)
avengers = [‘thor’, ‘iron man’]
names = [‘batman’, ‘spider man’]
z = zip(avengers, names)
print(*z)  # print the tuples by unpacking with *

Output
(‘thor’,’batman’) (‘iron man’,’spider man’)

Unzip the above
z = zip(avengers, names) # recreate a zip object
result 1, result 2 = zip(*z) # unzip by unpacking with *
print(result1)
print(result2)

Output
(‘thor’, ‘iron man’)
(‘batman’, ‘spider man’)


Using iterators to load large files in chunks
Sometimes, the data we have to process reaches a size that is too much for a computer's memory to handle. A solution to this is to process an entire data source chunk by chunk, instead of a single go all at once.

import pandas as pd
result = [ ]
for chunk in pd.read_csv(‘data.csv’, chunksize = 1000):
# the object created by read_csv is an iterable i.e. it can be iterated over
# each chunk will be a DataFrame
	result.append(sum(chunk[‘x’]))
	# compute the sum of the column of interest and append it to the list
# we are breaking up the ‘x’ column into 1000 chunks and calculating the sum of each chunk
total = sum(result)
# gives the total sum 

Alternatively
total = 0
for chunk in pd.read_csv(‘data.csv’, chunksize = 1000):
	total += sum(chunk[‘x’])
print(total)


2. List comprehensions and generators
List comprehensions condense for loops for building lists into a single line of code.
List comprehensions can be written over any iterable.
The tradeoff is that you sacrifice some readability with list comprehensions.
You cannot loop or build list comprehensions over integers

Components:
-	Iterable
-	Iterator variable (analogous to the loop variable)
-	Output expression

[[output expression] for iterator variable in iterable]

Example 1

nums = [12, 8, 21]

For loop
new_nums = [ ]
for num in nums:
	new_nums.append(num + 1)
print(new_nums)

VS

List comprehension
new_nums = [num + 1 for num in nums]
print(new_nums)


Example 2
A list comprehension that produces a list of the square of the numbers in the range 0 to 9

square_nums = [i ** 2 for i in range(0,10)]
print(square_nums)

Nested list comprehensions

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]
# [col for col in range(0,5)] is the output we want and for each output (or ‘row’ as the iterator variable is called) we are going to loop through this 4 times


# Print the matrix
# This part of the code places each list on a separate line
for row in matrix:
    print(row)

Output
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]


Conditionals in comprehensions

[ output expression for iterator variable in iterable if predicate expression ]

Example (conditional statement in the predicate expression)
[num ** 2 for num in range(0,10) if num % 2 == 0 else 0]

Output
[0, 0, 4, 0, 16, 0, 36, 0, 64, 0]

Alternatively (conditional statement in the output expression)
[num ** 2 if num % 2 == 0 else 0 for num in range(9)]


Dictionary comprehensions
Use curly brackets instead of square brackets

{num: -num for num in range(4)}

Output
{0:0, 1:-1, 2:-2, 3:-3, 4:-4}


Generator expressions
Similar to a list comprehension but it does not store the list in memory, it returns a generator object.
Helps with preserving computing power.
Functions like .items(),and range(), for example, are generator expressions. When you use these functions, Python creates generators for you behind the scenes.
It is an object we can iterate over.
Use ( ) instead of [ ]

Example 1
(num for num in range(3))

Example 2
result = (num for num in range(3)
# pass the generator object to the function list
print(list(result))

Output
[0, 1, 2, 3]

Example 3
result = (num for num in range(3)
print(next(result)

Output
0

print(next(result)

Output
1

Example 4
results = (num for num in range(3))

for num in result():
	print(num)

Output
0
1
2
3


Generator functions
When called they produce generator objects.
Defined like a regular function with def.
However, instead of using return to return values, we use the yield keyword.

Example
def num_sequence(n):
	i = 0
	while i < n:
		yield i
		i += 1

Call the function
result = num_sequence(3)
for item in result:
	print(item)

Output
0
1
2


3. Bringing it all together

Processing data in chunks
To begin, you need to open a connection to this file using what is known as a context manager. For example, the command with open('datacamp.csv') as datacamp binds the csv file 'datacamp.csv' as datacamp in the context manager. Here, the with statement is the context manager, and its purpose is to ensure that resources are efficiently allocated when opening a connection to a file.

Using a generator to load data
Generators allow users to lazily evaluate data. This concept of lazy evaluation is useful when you have to deal with very large datasets because it lets you generate values in an efficient manner by yielding only chunks of data at a time instead of the whole thing at once.

.readline() - reads a line from a file

Writing an iterator to load data in chunks
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    
    # Iterate over each DataFrame chunk
    for x in urb_pop_reader:
        df_pop_ceb = x[x['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
       df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

INTERMEDIATE DATA VISUALIZATION WITH SEABORN

1. Seaborn introduction
Seaborn leverages Matplotlib and integrates with Pandas.
Built on Matplotlib and works best with Pandas’ DataFrames.
Has embedded functionality that makes visualizations look better.
Seaborn generally does more statistical analysis on data and can provide more sophisticated insight into the data.


Using the distribution plot

Matplotlib histogram
df[‘alcohol’].plot.hist()
plt.show()
plt.clf() - clears the plot

Seaborn version of a histogram
Gaussian Kernel Density Estimate (KDE) function
The KDE helps to smooth the distribution and is a useful way to look at the data.
sns.distplot(df[‘alcohol’])
plt.show()

Additional arguments (creates standard histogram without Seaborn extras)
sns.distplot(df[‘alcohol’], kde = False, bins = 10)
plt.show()

Additional arguments
kde = False - disables the KDE output and turns the KDE function into a standard histogram
hist = False - shows the outline of the histogram bars as a line, but omits the bars
rug = True - draws a rugplot on the x-axis (small vertical lines to show each observation in the distribution)
kde_kws = {‘shade’: True} - shades the plot by passing in the kde keywords dictionary


Regression plots
The previous analysis we have done is called univariate analysis as we only look at one variable.
Regression analysis is bivariate as we look for relationships between two variables

sns.regplot(x = ‘alcohol’, y = ‘pH’, data = df)
-	Must explicitly define x and y variables and source of the data. The x and y variables refer to the columns in the DataFrame - we don’t subset the DataFrame as we explicitly define the source of the data as one of the arguments.

regplot() vs lmplot()
Both produce similar results but the lmplot() is much more powerful

Additional arguments lmplot()
hue = ‘type’ - overlays two plots of different colors distinguished by type
col = ‘type’ - creates two separate plots (stacked horizontally) distinguished by type
row = ‘type’ - creates two separate plots (stacked vertically) distinguished by type

Note
Faceting: plotting multiple graphs while changing a single variable. Use the col or row argument to do this.



2. Customizing Seaborn plots

Setting styles
sns.set() - default Seaborn style applied to a chart
sns.set_style() - pass in either of the arguments ‘white’, dark’, ‘whitegrid’, ‘darkgrid’, ‘ticks’
sns.despine(left = True) - removes the y axis spine to make chart look cleaner


Colors
We are able to apply Matplotlib color codes

sns.set(color_codes = True)
# Matplotlib color codes can now be applied
sns.distplot(df[‘Tuition’], color = ‘g’)

sns.set_palette() - set the color palette. Can pass either of the arguments ‘deep’, ‘muted’, ‘pastel’, ‘bright’, ‘dark’, ‘colorblind’


Example to loop through multiple chart colors
for p in [‘deep’, ‘pastel’]:
	sns.set_palette(p)
	sns.distplot(df[‘fmr_3’])
	plt.show()


Palettes
Three types of palettes: sequential (continuous order), diverging (high vs low) and circular (no particular order to data)

sns.set_palette(“RdBu”) - this a scale of colours. 


Viewing palettes
Use sns.palplot() to view the palette when calling sns.color_palette

sns.palplot(sns.color_palette(“Blues”, 6) - contains 6 colors from the “Blues” palette 
plt.show() - shows the palettes


Customising with Matplotlib
Most of the time, you can use the Seaborn API to modify your visualizations but sometimes it is helpful to use matplotlib's functions to customize your plots. 
Available through Matplotlib’s axes objects.
Once you have an axes object, you can perform a lot of customization of your plot.


Example
fig, ax = plt.subplots()
sns.distplot(df[‘Tuition’], ax = ax)
ax.set(xlabel = “Tuition 2013”, ylabel = “Distribution”, xlim = (0, 50000), title = “Tuition and fees”)
# xlim sets a limit range between $0 - $50,000


Example
fig, (ax0, ax1) = plt.subplots(nrows = 1, ncols = 2, sharey = True, figsize = (7,4))
# sharey means the subplots will have the same range of y axis values
sns.distplot(df[‘Tuition’], ax = ax0)
# 1st plot
sns.distplot(df[‘Fees’], ax = ax1)
# 2nd plot
ax0.set(xlabel = “Tuition 2013”, ylabel = “Distribution”)
# sets the labels for ax0 
ax1.axvline(x = 20000, label = ‘My budget’, linestyle = ‘--’)
# draws a vertical line at x = 20000 on the ax1 plot
# could also set x = df[‘Fees’].mean() to show the mean
ax1.legend()
# turns on the legend for the axvline for the ax1 plot



3. Additional plot types

Categorical plot types
sns.stripplot(data = df, y = ‘drg definition’, x = ‘average cover charge’, jitter = True)
# plots each observation
sns.swarmplot(data = df, y = ‘drg definition’, x = ‘average cover charge’) 
# swarmplot does not scale well to large data sets
# plots each observation
sns.boxplot(data = df, y = ‘drg definition’, x = ‘average cover charge’)
sns.violinplot(data = df, y = ‘drg definition’, x = ‘average cover charge’)
# combination of the boxplot and KDE function
sns.lvplot(data = df, y = ‘drg definition’, x = ‘average cover charge’)
# the Letter Value plot is a hybrid between box and violin plot

Statistical summaries of categorical data
sns.barplot(data = df, y = ‘drg definition’, x = ‘average cover charge’, hue = ‘region’)
# shows the confidence interval
sns.pointplot(data = df, y = ‘drg definition’, x = ‘average cover charge’, hue = ‘region’)
# shows the confidence interval
sns.countplot(data = df, y = ‘drg definition’, hue = ‘region’)
# shows the number of instances of each variable
# N.B. only specify either the x or y variable as the other variable becomes the count of that variable

Example
sns.violinplot(data=df, x='Award_Amount', y='Model Selected', palette='husl')
# sets the palette color
# other colors include ‘Paired’


Regression plots
sns.regplot(data = df, x = ‘temp’, y = ‘total_rentals’, marker = ‘+’)
# plots a linear regression model 
sns.residplot(data = df, x = ‘temp’, y = ‘total_rentals’)
# plots the residuals of a linear regression model
sns.regplot(data = df, x = ‘temp’, y = ‘total_rentals’, order = 2)
# Seabron attempts to fit a polynomial function to the data
sns.regplot(data = df, x = ‘month’, y = ‘total_rentals’, x_jitter = .1)
# regression plot of a categorical variable showing the distribution by month
sns.regplot(data = df, x = ‘month’, y = ‘total_rentals’, x_estimator = np.mean)
sns.regplot(data = df, x = ‘temp’, y = ‘total_rentals’, x_bins = 4, color = ‘g’)
# divides the temperatures into 4 bins and sets color to green

Additional arguments
fit_reg = False - disables the regression line


Matrix plots
heatmap() - requires data to be in a grid format
crosstab() - pandas function used to manipulate data into a grid format

Example 1
new_heatmap = pd.crosstab(df[‘month’], df[‘weekday’], values = df[‘total_rentals’], aggfunc = ‘mean’)
sns.heatmap(new_heatmap)

Additional arguments
annot = True - turns on annotations in the individual cells
fmt =’d’ - format argument ensures results are displayed as integars
cmap = ‘YlGnBu’ - changes color combination (yellow, green, blue)
cbar = False - the color bar is not displayed
linewidths = 0.5 - creates small spacing between each cell so that they are easier to view
center = new_heatmap.loc(9,6) - centers the heatmap colors on a specific set of coordinates

Example 2
sns.heatmap(new_heatmap.corr()) - plots the heatmap based on correlations between the columns specified in the crosstab function





4. Creating plots on data aware grids

FacetGrid()
Seaborn's FacetGrid is the foundation for building data-aware grids. A data-aware grid allows you to create a series of small plots that can be useful for understanding complex data relationships.
Analyzing data with many variables - compare multiple plots using the same scales and axes.

Two step process:
1.	Create a FacetGrid object with columns (col), rows (row) or hue (hue); and
2.	Mapping individual plots to the grid

Example
g = sns.FacetGrid(data = df, col = ‘HIGHDEG’)
g.map(sns.boxplot, ‘Tuition’)


factorplot()
Shortcut by combining faceting and mapping into one function

Example
sns.factorplot(x = ‘Tuition’, data =df, col = ‘HIGHDEG, kind = ‘box’)


lmplot()
The lmplot is used to plot scatter plots with regression lines on FacetGrid objects. The API is similar to factorplot with the difference that the default behavior of lmplot is to plot regression lines.

Example
sns.lmplot(data=df, x='UG', y='PCTPELL', col="Degree_Type", col_order = [‘Graduate’, ‘Bachelors’])
plt.show()


PairGrid()
You don’t define x and y as you want to examine all pairwise relationships between the data specified. Used to understand the best set of features to explain a relationship between variables.

Example 1
g = sns.PairGrid(data = df, vars = [‘Fair_mkt_rent’, ‘Median_Income’]
# we don’t define x and y variables as Seaborn will vary the x and y variables for each of the plots
g.map(plt.scatter)

Example 2
g = sns.PairGrid(data = df, vars = [‘Fair_mkt_rent’, ‘Median_Income’])
# we don’t define x and y variables as Seaborn will vary the x and y variables for each of the plots
g.map_diag(plt.hist)
# refers to the main diagonal from top left to bottom right
g.map_offdiag(plt.scatter)
# defines the diagonal plots as either a histogram or scatter plot


pairplot()
Works similar to FactorPlot

Example 1
g = sns.pairplot(data = df, vars = [‘Fair_mkt_rent’, ‘Median_Income’], kind = ‘reg’, diag_kind = ‘hist’)

Example 2
g = sns.pairplot(data = df.query(‘Bedrms < 3’), vars = [‘Fair_mkt_rent’, ‘Median_Income’, ‘Utility’], hue = ‘Bedrms’, palette = ‘husl’, plot_kws = {‘alpha’: 0.5})
# plots a third variable (there are now 9 plots)

Additional arguments
diag_kws = {‘alpha’: 0.5} - changes the transparency of the other diagonal plots


JointGrid
Seaborn's JointGrid combines univariate plots such as histograms, rug plots and kde plots with bivariate plots such as scatter and regression plots
Similar to the other grid plots.

Example 1
g = sns.JointGrid(data = df, x = ‘Tuition’, y = ‘ADM_RATE_ALL’)
# must define the x and y variables
g.map(sns.regplot, sns.distplot)
# the main plot is a regression plot and the two side plots (marginal plots) are distribution plots

Example 2
g = sns.JointGrid(data = df, x = ‘Tuition’, y = ‘ADM_RATE_ALL’)
g.plot_joint(sns.kdeplot)
# this is the center plot
g.plot_marginals(sns.kdeplot, shade = True)
# this is the plot on the margins
g.annotate(stas.pearsonr)
# annotates the plot with the Pearson correlation value


jointplot
Easier to use but has fewer customizations than the JointGrid

Example 1
sns.jointplot(data = df, x = ‘Tuition’, y = ‘ADM_RATE_ALL’, kind = ‘hex’)
# hex plot has been used

Additional arguments
xlim = (0, 25000) - sets the limits for the x-axis
Example 2
The jointplot is a convenience wrapper around many of the JointGrid functions. However, it is possible to overlay some of the JointGrid plots on top of the standard jointplot.

g = (sns.jointplot(x="temp",
             y="registered",
             kind='scatter',
             data=df,
             marginal_kws=dict(bins=10, rug=True))
    .plot_joint(sns.kdeplot))

plt.show()


When to use each Seaborn plots
distplot() is the best place to start to see the relationship between variables
rugplot() and kdeplot() can be useful alternatives

lmplot() is a regression plot that supports facetting. Combines features of the scatterplot, regplot and residplot. Best function for determining linear relationships between data

factorplot() - use this if you need to facet the data

pairplot() & jointplot() - useful after you have done preliminary analysis using lmplot(). Then apply the distplot function to pairplot() or jointplot()


























PROJECT: A VISUAL HISTORY OF NOBEL PRIZE WINNERS


Part 2
# Display the number of prizes won by male and female recipients.
#display(nobel['sex'].value_counts)
display(nobel['sex'].value_counts())
# the display() formal looks much better than print()


Part 3
# Calculating the proportion of USA born winners per decade
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)


Part 4
# setting the size of all plots.
plt.rcParams['figure.figsize'] = [11, 7]


Part 5
# Adding %-formatting to the y-axis
from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter(1.0))


Part 6
# Picking out the first woman to win a Nobel Prize
(nobel[nobel['sex'] == 'Female']).nsmallest(1,'year')


Part 7
# Selecting the laureates that have received 2 or more prizes.
# ... YOUR CODE FOR TASK 5 ...
nobel.groupby('full_name').filter(lambda x: len(x) >= 2)


Part 8
# Converting birth_date from String to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])

# Calculating the age of Nobel Prize winners
nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year








INTRODUCTION TO IMPORTING DATA

1. Introduction and Flat Files

Reading a text file
Such as the text from a book

file_name = ‘huck_finn.txt’
# read in the file
# you don’t have to specify mode =, you can just write ‘r’
file = open(file_name, mode = ‘r’)
text = file.read()
file.close() # good practice to close the file immediately
print(text)

OR, using a Context Manager:

with open (‘huck_finn.txt’, ‘r’) as file:
	print(file.read())
# no need to close this file as the context manager closes it automatically

Note: print(file.closed) # checks whether the file is closed by returning a Boolean

Additional commands
print(file.readline()) - reads the first line, if called again it reads the second line and so on


Flat files
Text files containing records
Such as csv files. Can also be a .txt file with records
Each row is a a separate record and each column is an attribute of that record

If we want to store the text file as an array, use Numpy.
If we want to store the text file as a DataFrame, use Pandas.


Importing flatfiles using Numpy
●	Good to use if all data is numerical
●	loadtext() vs genfromtext()

import numpy as np
np.loadtext(‘mnist.txt’, delimiter = ‘,’)

Additional arguments
delimiter = ‘\t’ - tab delimited
skiprows = 1 - skips the first row i.e. if there is text in it
usecols = [0,2]) - selects only the 1st and 3rd columns
dtype = str - imports all the data as strings

Note: if there are multiple data types in a column i.e. floats and strings, then loadtext() struggles

data = np.genfromtext('titanic.csv', delimiter = ',', names = True, dtype = None)
# dtype = None means the function will figure out what data type each column should be
# names = True tells us that there is a header

Because the data are of different types, data is an object called a structured array. Because numpy arrays have to contain elements that are all the same type, the structured array solves this by being a 1D array, where each element of the array is a row of the flat file imported.

data = np.recfromcsv(‘file.txt’, delimiter=',')
# Only need to pass the file name to it because it has the defaults delimiter=',' and names=True in addition to dtype=None


Importing flat files using Pandas
Slice, reshape, groupby, sort, join, merge.
Perform statistics.
Work with time series data.
Great for data analysis, wrangling, pre-processing, modeling and visualising

import pandas as pd
df = pd.read_csv(‘file.csv’)

Additional arguments
nrows = 5 - imports the first 5 rows into the DataFrame
header = None - tells Python that there are no column headers for the imported data
sep = ‘\t’ - the Pandas version of delimiter 
comment = ‘#’ - takes away comments that occur after the # sign
na_values='Nothing' - takes a list of strings to recognize as NA/NaN, in this case the string 'Nothing'

data_array = df.values - will convert the DataFrame to a Numpy array



2. Importing Data from Other File Types

Pickled files
There are a number of datatypes that cannot be saved easily to flat files, such as lists and dictionaries. If you want to be able to import them into Python, you can serialize them. All this means is converting the object into a sequence of bytes, or a bytestream.
●	Native to Python
●	Used to store data structures such as dictionaries

import pickle
with open(‘pickled_fruit.pkl’, ‘rb’) as file:
# rb means read-only and binary
	data = pickle.load(file)
print(data)


Excel files

import pandas as pd
file = ‘urban_pop.xlsx’
data = pd.ExcelFile(file)
print(data.sheet_names)
# this will print the sheet names

Output
[‘1960-1966’, ‘1967-1970’]

data.parse(‘1960-1966’)
# selects the first sheet using the sheet name

OR

data.parse(0)
# selects the first sheet using the sheet index

Additional arguments
data.parse(‘1960-1966’, usecols=[0], skiprows=[0], names=['Country'])
# usecols[0] includes only the first column, skiprows[0] skips the first row, and names renames the column. All arguments passed need to be of type list.


Importing SAS/Stata files using Pandas

SAS files
Business analytics

import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT(‘urbanpop.sas7bdat’) as file:
	df_sas = file.to_data_frame()

Stata files
Academic social sciences research

import pandas as pd
data = pd.read_stata(‘urbanpop.dta’)

HDF5 files
Hierarchical Data Format version 5.
Storing large quantities of numerical data.

import h5py
file_name = ‘hlc.hdf5’
data = h5py.File(file_name, ‘r’)


MATLAB files
Matrix Laboratory. Numerical computing environment.

scipy.io.savemat() - write .mat files

import scipy.io
filename = ‘workspace.mat’
scipy.io.loadmat(filename)
# read the file

keys = MATLAB variable names
values = objects assigned to variables



3. Working with Relational Databases in Python

Intro to relational databases
PostgreSQL
MySQL
SQLite

Creating a database engine in Python
We will use the SQLite database.
We then use SQLAlchemy to access the SQLite database

from sqlalchemy import create_engine
engine = create_engine(‘sqlite:///Northwind.sqlite’)
# sqlite:///Northwind.sqlite' is called the connection string to the SQLite database Northwind.sqlite
# creates an engine for the SQLite database Northwind.sqlite

table_names = engine.table_names()
print(table_names)
# print the table names in the Northwind database


Querying relational databases in Python
SELECT * FROM table_name
# returns all columns of all rows from the table_name table

Workflow:
1.	Import packages and functions
2.	Create the database engine
3.	Connect the engine
4.	Query the database
5.	Save query results to a DataFrame
6.	Close the connection

1. 	import sqlalchemy from create_engine
	import pandas as pd
2.	engine = create_engine(‘sqlite:///Northwind.sqlite’)
3.	con = engine.connect()
4.	rs = con.execute(“SELECT * FROM Orders”)
	# pass in the relevant SQL query
	# this creates a SQLAlchemy results object which we assign to the variable rs
5.	df = pd.DataFrame(rs.fetchall())
	# converts the results object into a DataFrame
	# fetchall fetches all rows
	df.columns = rs.keys()
	# sets the column names in the DataFrame equal to the keys from the database
6.	con.close()


Using a context manager
Means you don’t have to close the connection as it closes automatically
Step 3 above becomes:

with engine.connect() as con:
	rs = con.execute(“SELECT * FROM Orders”)
	df = pd.DataFrame(rs.fetchmany(size = 5))
	# imports 5 rows
	df.columns = rs.keys()


Querying relational databases directly with Pandas

Using Pandas, we can distill the above code (from Step 3 onwards) into a single line:

engine = create_engine('sqlite:///Chinook.sqlite')
df = pd.read_sql_query(“SELECT * FROM Orders”, engine)























INTERMEDIATE IMPORTING DATA IN PYTHON

1. Importing data from the Internet
URL = Universal Resource Locator

Importing flat files from the Internet

Example 1

from urllib.request import urlretrieve
import pandas as pd

# Assign url of file: url
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame
df = pd.read_csv('winequality-red.csv', sep=';')


Example 2
If you just wanted to load a file from the web into a DataFrame without first saving it locally, you can do that easily using pandas

import pandas as pd

url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
df = pd.read_csv(url, sep = ';')


Example 3
Importing excel files from the web

import pandas as pd

url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file
# The output is a dictionary with sheet names as keys and corresponding DataFrames as values
xls = pd.read_excel(url, sheet_name = None)

# Print the sheet names to the shell
print(xls.keys())


HTTP requests to import files from the Web
●	We will focus on web addresses.
●	Two elements that uniquely specify web addresses:
1.	Protocol identifier: http
2.	Resource name: datacamp.com

●	http = hypertext transfer protocol
●	Https is a more secure form of http.
●	Every time you go to a website you send an http GET request to the site
●	urlretrieve() performs a GET request and saves the data locally
●	HTML = hypertext markup language is the standard language for the web

Example 1
from urllib.request import urlopen, Request

url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request
request = Request(url)

# Sends the request and catches the response
response = urlopen(request)

# Extracts the HTML
html = response.read()

# Prints the HTML
print(html)

# Close the response
response.close()

Example 2
●	Using the requests library
●	Quicker alternative to example 1
●	No need to close the connection (unlike urllib)

import requests

url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response
r = requests.get(url)

# Extract the response
text = r.text

# Print the html
print(text)




Scraping the web with Python
●	HTML is a mix of structured and unstructured data
●	BeautifulSoup: parse and extract structured data from HTML

Example 
import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response
r = requests.get(url)

# Extracts the response as html
html_doc = r.text

# Create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html_doc)

# Print the title of the webpage
print(soup.title)

# Print the text
print(soup.get_text())

# Prettify the BeautifulSoup object
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)

# extract the URLs of the hyperlinks from the webpage
# Find all 'a' tags (which define hyperlinks)
# Print the URLs to the shell
for link in soup.find_all('a'):
    print(link.get('href'))



2. Interacting with APIs to import data from the Web

Intro to APIs and JSON
●	APIs are protocols for building and interacting with software applications
●	JSON: JavaScript Object Notation
○	File format for real time server to browser communication

Example

import json
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k, v in json_data.items():
    print(k + ': ', v)

APIs
●	Much of the data you get from APIs is packaged as JSONs
●	APIs allow software programs to communicate with each other

URLs
●	http - making an http request
●	www.omdbapi.com - makes a query to the API
●	?t=hackers - query string, which in this case is querying the data for the movie with the title (t) Hackers

Example
import requests

url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

# Package the request, send the request and catch the response
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])



3. Diving deep into the twitter API

Example 1

import tweepy

# Store credentials in relevant variables
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"

# Create your Stream object with credentials
stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)

# Filter your Stream variable
stream.filter(["clinton", "trump", "sanders", "cruz"])


Example 2
import json

tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, mode = "r")

# Read in tweets and store in list
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())




























CLEANING DATA IN PYTHON

1. Common data problems

Data type constraints

sales[‘revenue’] = sales[‘revenue’].str.strip(‘$’) - takes out the dollar sign from all revenue figures in the revenue column.
sales[‘revenue’] = sales[‘revenue’].astype(‘int’) - converts all data in the revenue column into integers.
assert sales[‘revenue’].dtype == ‘int’ - the assert statement returns nothing if the condition is true i.e. the revenue column contains only integers. Returns an error if it is not met.

Converting to a categorical data type
df[‘marriage status’] = df[‘marriage status’].astype(‘category’) - converts all data to type category. This is useful when we use numbers to describe married vs not married vs divorced, but we don’t want these numbers to behave as integers, but rather as categorical data types. 


Data range constraints (dealing with out of range data)
●	Dropping data
●	Setting custom minimums and maximums to your columns
●	Treat as missing and impute
●	Setting custom value depending on the business scenario

Example 1
movies.drop(movies[movies['avg_rating'] > 5].index, inplace = True) - drops all rows in the avg_rating column with a rating exceeding 5. inplace means all values are dropped in their place and no new column is created.

Example 2
movies.loc[movies['avg_rating'] > 5, 'avg_rating'] = 5 - the first argument of .loc method finds all rows in the avg_rating column which exceed 5 and the second argument specifies that it is the avg_rating column we are working in. It then sets all rows in this column that exceed 5, to 5.

Example 3
import datetime as dt
user_signups[‘date'] = pd.to_datetime(user_signups[‘date']).dt.date - converting the date column into a Pandas datetime object. dt.date converts the DateTime object into a date i.e. it is now an object (otherwise known as a string).

Example 4
today_date = dt.date.today() - sets today's date to the variable today_date
user_signups.loc[user_signups[‘date'] > today_date, 'date'] = today_date - for all rows in the ‘date’ column that are greater than today’s date, set them to today’s date
assert user_signups[date].max().date() <= today_date - confirms that the maximum date is less than or equal to today’s date. Make sure to chain this with the .date() method to return a date instead of a time stamp.


Note
Data type ‘object’ represents strings in Pandas.


Uniqueness constraints (duplicate values)
●	Use the .duplicated() method to find duplicates in a dataset
○	Returns booleans showing True for duplicate values
■	Note: the entire row of data has to be duplicated for it to return True. This is why the subset argument is useful, as it filters the search.
○	Arguments:
■	subset - list of column names to check for duplication
●	If you don’t use subset then only complete duplicates are dropped
■	keep - whether to keep (‘first’), (‘last’) or all (False) duplicate values
●	I.e. (‘first’) means the first instance of the duplicated data is kept
●	Use .drop_duplicates() to drop the duplicate values
○	Argument:
■	subset - list of column names to check for duplication
■	Keep - whether to keep (‘first’) or (‘last’) duplicate values
■	inplace = True
●	Complete duplicates means the entire row is duplicated. Incomplete means only some information is duplicated

Example 1
# Find duplicates
duplicates = ride_sharing.duplicated(subset = 'ride_id', keep = False)

# Sort your duplicated rides
# subset the ride_sharing DataFrame by the duplicates variable created above
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])

Output
 

Example 2
# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Drops incomplete duplicates by grouping by ride_id and computing the aggregation above
# e.g. looking at the output above for ride_id 33 - both rows will be grouped together using the minimum of birth_year (1979 vs 1979) in the combined entry and the average duration ((10+2)/2)
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()



2. Text and categorical data problems

Predefined finite set of categories
●	In machine learning we often will represent categories with numbers as shown in the examples below:
 

●	However, there may be inconsistencies in categorical data due to:
○	Data entry issues: such as free text vs drop downs
○	Parsing errors
○	Other errors
●	Solutions to treating these problems:
○	Dropping data
○	Remapping categories
○	Inferring categories


Membership constraints

Example
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary
# The difference method finds all differences between the column ‘blood_type’ in the ‘study_data’ table and the column ‘blood_type’ in the ‘categories’ table
inconsistent_categories = set(study_data['blood_type']).difference(categories['blood_type'])

# Use the isin method to find all all the inconsistent data in the first table ‘study_data’
# This returns a boolean (True for inconsistent rows and False for consistent rows)
inconsistent_rows = study_data['blood_type'].isin(inconsistent_categories)

# Subset the DataFrame for the inconsistent rows
inconsistent_data = study_data[inconsistent_rows]
# To drop inconsistent categories and get consistent data only
# Use the tilde symbol (~) while subsetting to get the opposite of inconsistent rows i.e. consistent rows
consistent_data = study_data[~inconsistent_rows]


Categorical variables
●	Inconsistent capitalization: e.g. “Married” vs “married”
○	Use .str.upper() or .str.lower() functions to make columns consistent
●	Leading or trailing spaces: e.g. “Married” vs “ Married”
○	Use .str.strip() method - when given no input it removes all leading and trailing white spaces
●	Note: to count different data use the following methods
○	Use the .value_counts() method on a series
○	Use the .count() method on a DataFrame

Series example
marriage_status = demographics['marriage_status']
marriage_status.value_counts()
 

DataFrame example
marriage_status.groupby('marriage_status').count()
 


Collapsing data into categories
●	Use pd.cut() to group data into categories

Remapping categories
●	Use .replace()

Example (inconsistent capitalization and remapping)
# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower() 

# Pass a dictionary to the replace method ({item to be replaced:replacement item})
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

Example (remapping categories)
# Create ranges for categories
# np.inf is a Numpy function specifying infinity
# This means 0 - 60 = short, 60 - 180 = medium and 180 - infinity = long
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
# pd.cut disaggregates the data based on the bins that we define in the argument. We thus define the bins by the numeric range provided in label_ranges above and assign each portion of the range to the label_names defined. This new data is placed into a new column called wait_type
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, 
                               labels = label_names)

# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}

# Create a new column, day_week, which replaces the old mappings (Monday, Tuesday etc.) with the new mapping (weekday, weekend)
airlines['day_week'] = airlines['day'].replace(mappings)


Text data problems
●	Data inconsistency: e.g. “+9671” vs “09671”
●	Fixed length problems: e.g. phone numbers/passwords need to be a certain length
●	Typos:

Example
# Use .str.replace() to replace unwanted characters with empty strings
phones["number"] = phones["number"].str.replace("+", "")

# Use an assert statement to check that the length of the minimum phone numbers is equal to or exceeds 10 digits
assert phones["number"].str.len().min() >= 10 
# Replaces all phone numbers with less than 10 digits with Numpy’s NaN object
phones.loc[phones['number'].str.len() < 10, ‘number’] = np.nan

# Use an assert statement with the .contains method, where the bar pipe ‘|’ means ‘or’ and the .any() method searches for any of those arguments (and will return a True Boolean if our output contains either + or -) As we have omitted these the output should return False.
assert phone['number'].str.contains("+|-").any() == False


Regular expressions
Regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be used without invoking their special meaning
●	phones['number'] = phones[‘number'].str.replace(r'\D+', '')



3. Advanced data problems

Uniformity
●	E.g. showing temperature as celsius vs fahrenheit or showing weight as kg vs pounds
●	Verifying unit uniformity is imperative
●	Date time inconsistencies such as 01/03/2021 vs 1 March 2021:
○	Use pd.to_datetime() as for most cases can pick up formats automatically and convert to a standard format
○	Datetime formats (refer to dt.strftime below)
■	%d-%m-%Y
■	%m-%d-%Y
■	%c (e.g. December 25 2019)
○	Sometimes fails with unrecognizable formats

Example 1
# Attempt to infer format of each date
# ‘coerce’ returns NA for rows where conversion failed
birthdays['Birthday'] = pd.to_datetime(birthdays['Birthday'], infer_datetime_format = True, errors = 'coerce')

Example 2
# dt.strftime accepts a DateTime format of your choice
# This method converts all dates to the format specified
birthdays['Birthday'] = birthdays['Birthday'].dt.strftime("%d-%m-%Y")


Cross field validation
●	The use of multiple fields in a dataset to sanity check data integrity
●	E.g. where you have a total column for each row - summing the individual columns to make sure they do in fact equal to the value in the total column

Example
# axis = 1 indicates that we are summing by row
sum_classes = flights[['economy_class', 'business_class', 'first_class']].sum(axis = 1)

# Find rows in the total_passengers column that equal to the sum_classes variable defined above and set this equal to passenger_equ 
passenger_equ = sum_classes == flights['total_passengers']

# Use the tilde symbol to find inconsistent passenger totals
inconsistent_pass = flights[~passenger_equ]

# Find consistent passenger totals
consistent_pass = flights[passenger_equ]

Example 2
# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where age column == ages_manual
age_equ = banking['age'] == ages_manual

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]


Completeness
●	I.e. missing data - no variable is stored for a variable in an observation
●	Takes on forms such as NA, NaN, 0, . etc.
●	Use the .isna() method to find rows with missing values - returns True for missing values
●	Chain .isna().sum() to obtain a breakdown of missing values by column


Example
# A useful package for visualising missing data
import missingno as msno

# Use the msno.matrix() function 
banking_sorted = banking.sort_values('age')
msno.matrix(banking_sorted)
plt.show()

 
Missing data types
●	Missing completely at random: no relationship between missing data and other values (i.e. due to human error)
●	Missing at random: relationship between missing data and other observed data (i.e. missing ozone data for high temperatures)
○	I.e. values missing due to another variable
●	Missing not an random: relationship between missingness and its values (missing or non-missing). (i.e. missing temperatures for high temperatures - where a thermometer stops working when it gets very hot)
○	I.e. values missing due to the missingness of the same variable
○	There is a relationship/correlation between the missing variable and another missing variable

Dealing with missing data
●	Dropping data
●	Imputing with statistical measures (mean, median, mode)
●	Using machine learning

Example 1 (dropping rows containing ‘na’ values)
# Use the subset argument to specify which columns to drop missing values
airquality_dropped = airquality.dropna(subset = ['CO2'])

Example 2 (filling missing rows using imputed values - instead of dropping them)
# Calculate the mean values for each row in the CO2 column
co2_mean = airquality['CO2'].mean()

# Assign the mean values to the CO2 column using the fillna method
# fillna takes in a dictionary with columns as keys and imputed values as values
airquality_imputed = airquality.fillna({'CO2': co2_mean})



4. Record linkage

Minimum edit distance
●	Least possible amount of steps needed to get from one string to another
●	Can be done by:
○	Inserting new characters
○	Deleting characters
○	Substituting characters
○	Transposing characters

Example 1
# The fuzzywuzzy package allows us to compare single strings
from fuzzywuzzy import fuzz

# Use WRatio function to compare two strings
fuzz.WRatio(“Reeding”, “Reading)

Output
# Returns a string between 0 - 100 with 100 being an exact match
86



Comparison with arrays
●	Using process.extract
●	The output is a list of tuples where each is formatted like: (closest match, similarity score, index of match)

Example 2
# Import the process module from fuzzywuzzy
from fuzzywuzzy import process

# Define string and array of possible matches
string = "Houston Rockets vs Los Angeles Lakers"
choices = pd.Series(['Rockets vs Lakers', 'Lakers vs Rockets',
                     'Houson vs Los Angeles', 'Heat vs Bulls'])

# Extract is used to compare a string with an area of strings
# Takes in a string, an area of strings, and a number of possible matches to return ranked from highest to lowest
process.extract(string, choices, limit = 2)

Example 3 (collapsing categories with string matching)

 

# For each correct category
for state in categories['state']:

# Find potential matches in states with typos
# Set the limit argument to the length of the survey DataFrame i.e. shape[0] will output just the number of rows
matches = process.extract(state, survey['state'], limit = survey.shape[0])

# For each potential match
for potential_match in matches:

# If high similarity score
# Remember: potential_match[1] is the similarity score for that match
if potential_match[1] >= 80:

# Replace typo with correct category
# Remember: potential_match[0] is the actual match
survey.loc[survey['state'] == potential_match[0], 'state'] = state


Generating pairs (using record linkage)
●	Linking data from different sources regarding the same entity
●	Generate different pairs of potentially matching rows by searching for exact matches or similar strings
○	This can be useful in removing duplicated data between two DataFrames and then merging the unique data in each DataFrame
●	Similar to joins:
○	But unlike joins, record linkage does not require exact matches between different pairs of data, and instead can find close matches using string similarity
○	Effective when there are no common unique keys between the data sources

Example
import recordLinkage

# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('cuisine_type')

# Generate pairs between the two DataFrames
pairs = indexer.index(restaurants, restaurants_new)

# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')

# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold = 0.8) 

# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

Output
●	Values being 1 for a match, and 0 for not a match for each pair of rows in your DataFrames
●	To find potential matches, you need to find rows with more than matching value in a column. You can find them with
○	potential_matches[potential_matches.sum(axis = 1) >= n]
 

# Find matches in all three columns
matches = potential_matches[potential_matches.sum(axis = 1) >= 3]


Linking DataFrames
●	We now have row indices between restaurants and new_restaurants that are most likely duplicates
●	We now need to remove duplicate values and append the restaurants DataFrame to the restaurants_new DataFrame 

Example (continued)

# Get values of second column index of matches
# Using index of 1 searches in the restaurants_new data, which is the 2nd column (index of 0 would be the restaurants data)
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values using the tilde symbol
# All of the values in the 2nd column are data from restaurants_new that has matching data in the restaurants DataFrame - as such we want to remove this duplicated data from restaurants_new as shown below
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)
WORKING WITH DATES AND TIMES IN PYTHON

1. Dates and calendars


Example 1
# Import date from datetime
from datetime import date

# Create a date object
# Pass in the date (year, month, day) to the date object
hurricane_andrew = date(1992, 8, 24)

# Which day of the week is the date?
# Use the weekday method
print(hurricane_andrew.weekday())


Methods & attributes
●	weekday() method - returns 0 for Monday, 1 for Tuesday etc.
●	.year attribute
●	.month
●	.day


Example 2
# Counter for how many before June 1
# Initialise an empty counter
early_hurricanes = 0

# We loop over the dates
# florida_hurrican_dates contains a list of dates from 1950 - 2017
for hurricane in florida_hurricane_dates:
  # Check if the month is before June (month number 6)
  if hurricane.month < 6:
    early_hurricanes = early_hurricanes + 1
    

Math with dates
●	When subtracting dates you get an object ‘time delta’
○	Access the .days attribute of this object to get the number of days
●	When adding days to dates refer to the example below

Example 1 (subtracting)
from datetime import date

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

# Subtract the two dates and print the number of days
print((end - start).days)

Example 2 (adding)
from datetime import timedelta

# Create a 29 day timedelta
d1 = date(2017, 11, 5)
td = timedelta(days=29)
print(d1 + td)

Output
2017-12-04

Example 3
# Put the dates in order
# You can use sorted() on several data types in Python, including sorting lists of numbers, lists of strings, or even lists of lists
dates_ordered = sorted(dates_scrambled)

# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])


Turning dates into strings
●	Convert from datetime object into a string using isoformat() and strftime()
●	ISO 8601 format is YYYY-MM-DD
○	This format can be sorted using the sorted() method

Every other format
●	Use d.strftime())
○	d.strftime(‘%Y’) lets you pass a format string which Python uses to format the date
○	d.strftime(‘%Y/%m/%d’’)
○	%B will print out the name of the month written out in full
○	%j will print out the day in the year (out of 365 days)

Example
# Assign the earliest date to first_date
first_date = min(florida_hurricane_dates)

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

print("ISO: " + iso)
print("US: " + us)


2. Combining dates and times

Dates and times

Example 1
Write the date and time October 1, 2017 3:23:25 PM
# Import datetime
from datetime import datetime
dt = datetime(2017, 10, 1, 15, 23, 25, 500000)

Example 2 (alternative using explicit assignment)
# Import datetime
from datetime import datetime
dt = datetime(year=2017, month=10, day=1, hour=15, minute=23, second=25, microsecond=500000)

Example 3
# Use the .replace method to alter the date and time
new_dt = dt.replace(minute=0, second=0, microsecond=0)

Example 4
# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}
  
# Loop over all trips
for trip in onebike_datetimes:
  # Check to see if the trip starts before noon using the .hour attribute
  if trip['start'].hour < 12:
    # Increment the counter for before noon
    trip_counts['AM'] += 1
  else:
    # Increment the counter for after noon
    trip_counts['PM'] += 1
  
print(trip_counts)


Printing and parsing datetimes

Example
# Create datetime
dt = datetime(2017, 12, 30, 15, 19, 13)
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
print(dt.isoformat())

Parsing datetimes with strptime
●	strftime() and strptime() are the opposite of one another
○	strftime() create strings from date objects
○	strptime() create date objects from strings
Example 1
# Import datetime
from datetime import datetime

# Pass in the string we want to parse as well as the format string
# dt will be a string representation of the datetime when printed
dt = datetime.strptime("12/30/2017 15:19:13", "%m/%d/%Y %H:%M:%S")


Example 2
Some computers store time as the number of seconds since 1 Jan 1970 (Unix timestamp)

# A timestamp of the number of seconds
ts = 1514665153.0
# Convert to datetime and print
print(datetime.fromtimestamp(ts))

Example 3

Input
 

# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = [ ]

# Loop over all trips
for (start, end) in onebike_datetime_strings:
  trip = {'start': datetime.strptime(start, fmt),
          'end': datetime.strptime(end, fmt)}
  
  # Append the trip
  onebike_datetimes.append(trip)

Output
 


Working with durations


Example 1
# Create example datetimes
start = datetime(2017, 10, 8, 23, 46, 47)
end = datetime(2017, 10, 9, 0, 10, 57)

# Subtract datetimes to create a timedelta
duration = end - start

# Subtract datetimes to create a timedelta
print(duration.total_seconds())

N.B.
# Calling the .seconds attribute will print the number of seconds and omit the number of days
# Whereas total_seconds() prints the number of seconds and days of elapsed time
print(duration.seconds)


Example 2 (creating timedeltas)
# Import timedelta
from datetime import timedelta

# Create a one day and one second timedelta
delta2 = timedelta(days=1, seconds=1)
 
# One day and one second later
print(start + delta2)



3. Time zones and daylight savings

UTC offsets
●	All clocks are set relative to UTC (also called GMT)
●	UTC is the the UK
●	Moving east is +UTC and moving west is -UTC
●	Setting a timezone tells datetime how to align itself to UTC

Example 1
# Import relevant classes
from datetime import datetime, timedelta, timezone

# US Eastern Standard time zone
ET = timezone(timedelta(hours=-5))

# Timezone-aware datetime
# If tzinfo is not set, then datetime is timezone naive
dt = datetime(2017, 12, 30, 15, 9, 3, tzinfo = ET)

print(dt)

Output
Shows the UTC offset i.e. shows UTC and the time delta
I.e. clocks in the US Eastern time would be showing 10:09:03
 

Example 2 (adjusting timezones)
●	When you need to move a datetime from one timezone to another

# India Standard time zone
IST = timezone(timedelta(hours=5, minutes=30))

# Convert to IST
print(dt.astimezone(IST))

Output
1:39:03 is the time in India which is 5hr30min past UTC
 

Distinguishing between adjusting timezones and changing tzinfo
●	print(dt.replace(tzinfo=timezone.utc))
○	Changes the tzinfo argument to equal UTC meaning there is 0 offset
○	The clock stays the same, but the UTC offset changes

 

●	print(dt.astimezone(timezone.utc))
○	Changes both the clock itself and the UTC offset
○	In this instance this is the actual UTC time

 


Timezone database
●	There is a database of the timezones called tz
●	Format ‘Continent/City’
●	Used as an alternative to specifying the UTC offset yourself

Example 1
# Imports
from datetime import datetime
from dateutil import tz

# Eastern time
et = tz.gettz('America/New_York')

# Last ride
# Instead of specifying the UTC offset yourself you pass in the timezone you got from et
last = datetime(2017, 12, 30, 15, 9, 3, tzinfo=et)
print(last)

Output
 

Example 2
# Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(uk)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

Output
●	The first shows the original time relative UTC
●	The second shows the time relative to London (UTC +1) i.e. shows the UK timezone
 


Daylight saving time (daylight shifting time)
●	Clocks move forward in spring
●	Clocks move back in autumn
●	When we compare times in local time zones, everything gets converted into clock time. Remember if you want to get absolute time differences, always move to UTC!
○	Use df.astimezone(timezone.utc) to convert to UTC time

Ending daylight saving time
●	Clock gets pushed back
●	Map everything back to UTC
●	Use tz.enfold to fold over the duplicate times, when the clock gets pushed back
○	tz.enfold takes the new enfolded time i.e. the time that was pushed back

Example 1
from dateutil import tz

# Loop over trips
for trip in onebike_datetimes:

  # Rides with ambiguous start
  # Ambiguous times are when there are two overlapping times due to daylight saving ending
  if tz.datetime_ambiguous(trip['start']):
    print("Ambiguous start at " + str(trip['start']))

  # Rides with ambiguous end
  if tz.datetime_ambiguous(trip['end']):
    print("Ambiguous end at " + str(trip['end']))


Example 2
from datetime import timezone
from dateutil import tz

trip_durations = []

for trip in onebike_datetimes:
  # When the start is later than the end, set the fold to be 1
  if trip['start'] > trip['end']:
    trip['end'] = tz.enfold(trip['end'])

  # Convert to UTC
  start = trip['start'].astimezone(timezone.utc)
  end = trip['end'].astimezone(timezone.utc)

  # Subtract the difference
  trip_length_seconds = (end-start).total_seconds()
  trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))

Note
Since Python does not handle tz.enfold() when doing arithmetic, we must put our datetime objects into UTC, where ambiguities have been resolved (using timezone.utc)



4. Easy and powerful: dates and times in Pandas

Loading a .csv file in Pandas

Example 1
# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', 
                    parse_dates = ['Start date','End date'])

Example 2
# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds and create a new columnf
rides['Duration'] = ride_durations.dt.total_seconds()


Summarizing datetime data in Pandas
●	.resample() is the same as groupby but allows you to groupby time i.e. ‘M’ is month, ‘D’ is days etc.
●	Whereas .resample() groups rows by some time or date information, .groupby() groups rows based on the values in one or more columns.
●	.resample() can be called after .groupby(). For example, how long was the median ride by month, and by Membership type?

Example 1
# Import matplotlib
import matplotlib.pyplot as plt

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 150])

# Show the results
plt.show()

Example 2
# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M', on = 'Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
# .value_counts() counts the number of member and casual rides
# .size() counts the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())

Example 3
# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type').resample('M', on = 'Start date')

# Print the median duration for each group
print(grouped['Duration'].median())


Additional datetime methods in Pandas


Example 1
# Localize the Start date column to America/New_York
# dt.tz_localize sets a new timezone, but keeps date and time the same
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', ambiguous='NaT')

# Print first value
print(rides['Start date'].iloc[0])

# Convert the Start date column to Europe/London
# dt.tz_convert changes the date and time to match a new timezone
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')

# Print the new value
print(rides['Start date'].iloc[0])


Example 2
# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.day_name()

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())

Output
 
DEALING WITH MISSING DATA IN PYTHON


1. The problem with missing data
●	Workflow for dealing with missing data:
1.	Convert all missing data to null values
2.	Analyze the type and amount of missing data
3.	Delete or impute missing values
4.	Evaluate the performance of the deleted/imputed dataset

Null value operations
●	None vs np.nan
●	None is of type NoneType while np.nan is of float. This allows np.nan to have both arithmetic and logical operations.

Example (Handling missing values)
# When importing a file - specify the argument na_values equal to the value you want to replace with NaN
import pandas as pd
college = pd.read_csv('college.csv', na_values = '.')


Example (Replace missing values with NaN)
# Set rows in the BMI column of the diabetes DataFrame that are equal to 0 to NaN
import numpy as np
diabetes[diabetes[‘BMI’] == 0] = np.nan

Example (unique values & sorting data)
# Store unique values of 'csat' column to 'csat_unique'
csat_unique = college.csat.unique()

# Print the sorted values of csat_unique
print(np.sort(csat_unique))

Example
# Set the 0 values of column 'BMI' to np.nan
diabetes.BMI[diabetes.BMI == 0] = np.nan

# Print the 'NaN' values in the column BMI
print(diabetes.BMI[np.isnan(diabetes.BMI)])

Analyze missingness
●	Use isnull() or isna() as both are the same
○	Returns a boolean

Example
# A useful package for visualising missing data
import missingno as msno

# Use the msno.bar() and msno.matrix() functions
# Set the frequency to month for msno.matrix()
# Call both these functions on the original DataFrame and not once isna() or isnull() is called
msno.bar(air_quality)
msno.matrix(air_quality, freq = ‘M’)
plt.show()



2. Does missingness have a pattern
●	Heatmap
○	Lighter colors signify greater correlation between variables
●	Dendrogram
○	Tree diagram of missingness
○	Describes correlation of variables by grouping them


Example
import missingno as msno
diabetes = pd.read_csv('pima-indians-diabetes data.csv')
msno.heatmap(diabetes)
msno.dendrogram(diabetes)
plt.show()

Output (for dendrogram)
 


How to delete missing data
●	Keep, impute or delete


Pairwise & Listwise deletion
●	Used when values are missing completely at random (i.e. the number of missing values should be small)
●	Listwise deletion drops the whole row whereas pairwise deletion drops individual entries

Example
# Visualize the missingness in the data
msno.matrix(diabetes)

# Visualize the correlation of missingness between variables
msno.heatmap(diabetes)

# Show heatmap
plt.show()

# Drop rows where 'BMI' has a missing value
diabetes.dropna(subset=['BMI'], how='all', inplace=True)



3. Imputation techniques

The .fillna() method
●	The method attribute can be set equal to:
○	‘ffill’ or ‘pad’: this is the forward fill and fills missing values based on the last observed value
○	‘bfill’ or ‘backwardfill’: fills missing values based on the next observed value
○	E.g. airquality.fillna(method='ffill', inplace=True)

The .interpolate() method
●	This method extends the sequence of values to the missing values
●	The method in .interpolate() can be set to:
○	‘linear’: fills in values by extrapolating a straight line between the last observed value and the next observed value after the NaNs
○	‘quadratic’: parabolic trajectory in the negative direction and gives back a positive value
○	‘nearest’: uses a combination of ‘ffill’ and ‘bfill’ to fill in the missing values
○	E.g. airquality.interpolate(method='linear', inplace=True)



4. Advanced imputation techniques

Imputing using fancyimpute (machine learning models)
●	KNN (K-nearest neighbor): selects similar data points using all the non-missing features. Takes the average of selected data points to fill in the missing feature.
●	MICE (Multiple imputation by chained equations)
○	Performs multiple regression over a random sample of data and the takes the average to impute the missing data

Example 1
from fancyimpute import KNN

# Initialize KNN
knn_imputer = KNN()

# Create a copy of the DateFrame so that we can compare to the original DataFrame later
diabetes_knn = diabetes.copy(deep=True)
diabetes_knn.iloc[:, :] = knn_imputer.fit_transform(diabetes_knn)


Example 2
from fancyimpute import IterativeImputer
MICE_imputer = IterativeImputer()
diabetes_MICE = diabetes.copy(deep=True)
diabetes_MICE.iloc[:, :] = MICE_imputer.fit_transform(diabetes_MICE)


Imputing categorical data
●	Categories usually consist of strings 
●	These need to be converted to numeric values by encoding them
●	Three steps:
1.	Convert non-missing categorical columns to ordinal values
2.	Impute the missing values in the original DataFrame
3.	Convert back from ordinal values to categorical values
●	Categorical features can be encoded using two techniques namely, one-hot encoding and ordinal encoding. In one-hot encoding, each category becomes a column and the respective category column for each row is 1 and the others 0. In ordinal encoding, the categories are mapped to integer values starting from 0 to number of categories.

Example 1
from sklearn.preprocessing import OrdinalEncoder

# Create Ordinal encoder
ambience_ord_enc = OrdinalEncoder()

# Select non-null values of ambience column in users
# OrdinalEncoder() cannot handle NaN value - therefore we must remove them
ambience = users['ambience']
ambience_not_null = ambience[ambience.notnull()]

# Reshape ambience_not_null to shape (-1, 1)
reshaped_vals = ambience_not_null.values.reshape(-1,1)

# Ordinally encode reshaped_vals
encoded_vals = ambience_ord_enc.fit_transform(reshaped_vals)

# Assign back encoded values to non-null values of ambience in users
users.loc[ambience.notnull(), 'ambience'] = np.squeeze(encoded_vals)

Example 2 (automate the encoding using a loop)
# Create an empty dictionary ordinal_enc_dict
ordinal_enc_dict = {}

for col_name in users:
    # Create Ordinal encoder for col
    ordinal_enc_dict[col_name] = OrdinalEncoder()
    col = users[col_name]
    
    # Select non-null values of col
    col_not_null = col[col.notnull()]
    reshaped_vals = col_not_null.values.reshape(-1, 1)
    encoded_vals = ordinal_enc_dict[col_name].fit_transform(reshaped_vals)
    
    # Store the values to non-null values of the column in users
    users.loc[col.notnull(), col_name] = np.squeeze(encoded_vals)

Example 3 (imputing the data)
# Create KNN imputer
KNN_imputer = KNN()

# Impute and round the users DataFrame
users.iloc[:, :] = np.round(KNN_imputer.fit_transform(users))

# Loop over the column names in users
for col_name in users:
    
    # Reshape the data
    reshaped = users[col_name].values.reshape(-1, 1)
    
    # Perform inverse transform of the ordinally encoded columns
    users[col_name] = ordinal_enc_dict[col_name].inverse_transform(reshaped)




























WRITING FUNCTIONS IN PYTHON


1. Best practices
●	Popular docstring formats:
○	Google style
○	Numpydoc

Google style
 


Numpy Doc





















Retrieving docstrings
●	We don’t want to call the function. Instead treat the function like an object:
○	The call would be: the_answer.__doc__ and NOT the_answer().__doc__

 

Immutable vs Mutable data types





















Note
When you need to set a mutable variable as a default argument, always use None and then set the value in the body of the function. This prevents unexpected behavior like adding multiple columns if you call the function more than once.
 
Example
# Use an immutable variable for the default argument
def better_add_column(values, df=None):

# Update the function to create a default DataFrame
    if df is None:
    df = pandas.DataFrame()
  df['col_{}'.format(len(df.columns))] = values
  return df



2. Context managers

2.1 Using context managers
●	Sets up a context, runs code and then removes the context

Syntax
with <context manager>(<args>) as <variable name>:
	# This code runs inside the context
# This code runs after the context is removed

Example
# ‘open’ sets up a context by opening a file, lets you run any code on that file and then removes the context by closing the file
with open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

# fstring literal
print(f “Lewis Carroll uses the word "cat" {n} times”)


2.2 Writing context managers (using decorators)
●	Two ways to define a context manager:
○	Class based
○	Function based: a context manager function is technically a generator that yields a single value

Function based
# Decorate the function with the contextmanager decorator from the contextlib module
@contextlib.contextmanager
# Define a function
def my_context():
	# add set-up code
	# use the yield keyword
	yield
	# add any tear-down code


	




















Example
Create a read-only version of the open() context manager. This function is an example of a context manager that does return a value, so we write yield read_only_file instead of just yield. Then the read_only_file object gets assigned to my_file in the with statement so that whoever is using your context can call its .read() method in the context block.

@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())



2.3 Advanced topics

Nested contexts

Example
def copy(src, dst):
  # Open both files
  # Open the file to read from
  with open(src) as f_src:
    # Open the file to write to
    with open(dst, 'w') as f_dst:
      # Read and write each line, one at a time
      for line in f_src:
        f_dst.write(line)


When to use a context manager
●	When you need to open/close file paths etc.
 

3. Decorators

3.1 Functions as objects
●	Decorators modify the behavior of functions
●	Functions are just another type of object

Example
def create_math_function(func_name):
  if func_name == 'add':
    # Define the add() function
    def add(a, b):
      return a + b
    # Return the add function back to the main function create_math_function
    return add
  elif func_name == 'subtract':
    # Define the subtract() function
    def subtract(a,b):
      return a - b
    return subtract
  else:
    print("I don't know that one")
    
# Calling the functions
add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))


3.2 Scope
●	In the case of nested functions, Python checks the scope of the parent function before checking the global function i.e. the local scope is the nested function and the nonlocal scope is the parent function
○	Nonlocal means it is not the local scope of the child function and not the global scope
































●	The global variable is used when you are inside a function (in the local scope) and want to update the variable in the global scope
●	However, try to avoid using the global variable as it makes testing and debugging tricky



















●	Use the nonlocal variable when you are inside a nested function and want to update the variable inside the parent function


3.3 Closures

Nonlocal variables
●	Variables defined in the parent function that are used by the child function
Closure
●	Nonlocal variables that are attached to a returned function


Example 1

def parent(arg_1, arg_2):
  value = 22
  my_dict = {'chocolate': 'yummy'}

# Python’s way of attaching nonlocal variables to a returned function so that a function can operate even when called outside of the parent’s scope i.e. value and my_dict variables
  def child():
    print(2 * value)
    print(my_dict['chocolate'])
    print(arg_1 + arg_2)

  return child

new_function = parent(3, 4)
print([cell.cell_contents for cell in new_function.__closure__])

Example 2
Values passed to return_a_func() are still accessible to the new function returned, even after the program left the scope of return_a_func().

Values get added to a function's closure in the order they are defined in the enclosing function (in this case, arg1 and then arg2), but only if they are used in the nested function. That is, if return_a_func() took a third argument (e.g., arg3) that wasn't used by new_func(), then it would not be captured in new_func()'s closure.

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure
closure_values = [my_func.__closure__[i].cell_contents for i in range(2)]
print(closure_values == [2, 17])

Output
 



3.4 Decorators
●	Functions that take another function as an argument and return a modified version of that function

Example
Version 1 (using decorator syntax)
# assuming we have written the double_args decorator elsewhere, which doubles the arguments passed to the function
# we are decorating the multiply function
@double_args
def multiply(a, b):
  return a * b
multiply(1, 5)

Output
20

Version 2 (redefining the multiply function)
def multiply(a, b):
  return a * b
def double_args(func):
  def wrapper(a, b):
    return func(a * 2, b * 2)
  return wrapper
multiply = double_args(multiply)
multiply(1, 5)

Output
20

Note
The @double_args before the definition of my_function is exactly equivalent to multiply = double_args(multiply). Remember, even though decorators are functions themselves, when you use decorator syntax with the @ symbol you do not include the parentheses after the decorator name.



4. More on decorators
●	Use a decorator when you want to add some common code to multiple functions

4.1 Real-world examples

Example
The timer functions is useful for finding the slow parts of your code

import time

 def timer(func):

  """A decorator that prints how long a function took to run."""
  # Define the wrapper function to return.
  # wrapper takes any number of positional and key-word arguments so that it can be used to decorate any function
# this is the function that the decorator will return
  def wrapper(*args, **kwargs):

    # When wrapper() is called, get the current time.
    t_start = time.time()

    # Call the decorated function and store the result.
    result = func(*args, **kwargs)

    # Get the total time it took to run, and print it.
    t_total = time.time() - t_start
    print(f”{func.__name__} took {t_total}s”)

    return result
  return wrapper

Using timer()
@timer
def sleep_n_seconds(n):
  time.sleep(n)


4.2 Decorators and metadata
●	When trying to access the metadata (such as docstrings, name or arguments) of the decorated function you will run into problems as you will be referencing the metadata of the nested function (i.e. the wrapper() function) that was returned by the decorator.
●	To solve this do the following:

Example
from functools import wraps

def timer(func):

	# use @wraps to decorate the wrapper function
	# this modifies the metadata of wrapper to look like the function you are decorating
	@wraps(func)
	def wrapper(*args, **kwargs)
	“	“
	return wrapper

Result
@timer
def sleep_n_seconds(n=10):
  """Pause processing for n seconds.
  Args:
    n (int): The number of seconds to pause for.
"""
  time.sleep(n)
print(sleep_n_seconds.__doc__)

Output
# the docstring of the decorated function is now appropriately displayed
Pause processing for n seconds.
 Args:
   n (int): The number of seconds to pause for.


4.3 Decorators that take arguments
●	Have to first turn the decorator into a function that returns a decorator (rather than a function that is a decorator)
○	This is because the original decorator function can only take another function as its argument

Example
def run_n_times(n):
  """Define and return a decorator"""
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

# when we call @run_n_times notice that we use curly brackets
# we call the decorator by adding parentheses
# we are calling the function run_ n_times and decorating print_sum with the result of that function call
@run_n_times(3)
def print_sum(a, b):
print(a + b)

Result
8
8
8






























PYTHON PROGRAMMING

Question 4
Complete the code to return the output

Expected Output
g(2,3)

g = lambda x, y: x + y


Question 6
Add 'Gloomhaven' to the boardgames list in the first position

boardgames = [
  'Pandemic Legacy: Season 1', 
  'Terraforming Mars', 
  'Brass: Birmingham'
]

boardgames.insert(0, 'Gloomhaven')


Question 13
Complete the code to return the output

Expected Output
245

class Building:
    def __init__(self, number):
        self.number = number
b = Building(245)
b.number


Question 15
Complete the code to return the output

Expected Output
p
r
o
g
r

for i in "programming":
  if i == "a":
    break
  print(i)

EXPLORATORY DATA ANALYSIS IN PYTHON
Exploratory data analysis is a process for exploring datasets, answering questions, and visualizing results. Clean and validate data, to visualize distributions and relationships between variables, and use regression models to predict and explain. You'll use Pandas, NumPy, SciPy, StatsModels for regression, and Matplotlib for visualization.

1. Read, Clean & Validate

1.1 DataFrames & Series
Pandas attributes to remember:
●	.shape - returns number of rows & columns
●	.columns - returns column names as an index (which is a data structure similar to a list)

1.2 Clean & Validate
●	.value_counts().sort_index() - compare results to original dataset to validate data
●	.describe()
●	.replace([list of values to replace], np.nan) - takes a list of values we want to replace and the value we want to replace them with (in this case NaN)
●	.replace([list of values to replace], np.nan, inplace = True) - modifies the Pandas Series in place i.e. without making a copy, instead of making a new series

1.3 Filter & Visualize
●	When you compare a series to a value, the result is a boolean series
○	E.g. pre_term = nsfg[‘preg_length’] < 37
○	Boolean series treats True as 1 and False as 0
○	E.g. pre_term.sum() - sums the True values
●	Filter for weight of pre-term babies using the boolean series:
○	pre_term_weight = nsfg[‘birth_weight’][pre_term]
●	Logical operators:
○	birth_weight[A&B] - A and B
○	birth_weight[A|B] - A or B
●	plt.hist(nsfg[‘agecon’], bins=20, histtype='step') - creates an unfilled histogram

Example
# Filter full-term babies
full_term = nsfg['prglngth'] >= 37

# Filter single births
single = nsfg['nbrnaliv'] == 1

# Compute birth weight for single full-term babies
single_full_term_weight = birth_weight[full_term & single]
print('Single full-term mean:', single_full_term_weight.mean())

# Compute birth weight for multiple full-term babies
mult_full_term_weight = birth_weight[~single & full_term]
print('Multiple full-term mean:', mult_full_term_weight.mean())


2. Distributions

2.1 Probability Mass Functions (PMF)
●	Link to library
○	https://pypi.org/project/empiricaldist/

Example
# Make a PMF of age
# Pmf comes from a class created in the library above
pmf_age = Pmf(gss['age'])

# Plot the PMF
pmf_age.plot()

plt.show()


2.2 Cumulative Distribution Functions (CDF)
●	Link to library
○	https://pypi.org/project/empiricaldist/
●	Good way to visualize and compare distribution
●	PMF vs CDF
○	CDF(3) is 4/5 because 4 out of 5 values are less than or equal to 3














Example (evaluating the inverse CDF)
p = 0.25
q = cdf.inverse(p)
print(q)

Output
30 (25% of respondents are 30 years old or younger)









2.3 Comparing Distributions
●	CDFs omit most of the noise present in PMFs
●	Good for exploratory data analysis

Example
# Bachelor's degree
bach = (gss['educ'] >= 16)

# Associate degree
assc = (gss['educ'] >= 14) & (gss['educ'] < 16)

# Create a variable to extract income
income = gss['realinc']

# Plot the CDFs
# Extract incomes for associates and incomes for bachelors and then plot these
Cdf(income[assc]).plot(label='Associate')
Cdf(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()


2.4 Modeling Distributions
●	Probability density function (PDF)
●	Normal/Gaussian distribution (bell curve)
○	KDE (Kernel Density Estimate)
■	Use points in the sample to estimate the PDF they came from
■	Used to move from a PMF to a PDF
■	Uses Seaborn library
●	Use CDFs for exploration
●	Use PMFs if there are a small number of unique values
●	Use KDE if there a lot of values
●	If data is said to be ‘lognormal’ then it fits a normal distribution

Example (using CDF)
Assessing whether income data is lognormal by comparing Cdf of the logarithm of the data to a normal distribution with the same mean and standard deviation.

# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(income)

# Create and plot the Cdf of log_income
Cdf(log_income).plot()
plt.show()

# Compute mean and standard deviation
mean = log_income.mean()
std = log_income.std()

# Make a norm object
from scipy.stats import norm
dist = norm(mean,std)

# Evaluate the model CDF
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs)

# Plot the model CDF
plt.clf()
plt.plot(xs, ys, color='gray')


Example (using PDF)
# Evaluate the normal PDF
xs = np.linspace(2, 5.5)
ys = dist.pdf(xs)

# Plot the model PDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Plot the data KDE
sns.kdeplot(log_income)
plt.show()




3. Relationships (between variables)

3.1 Exploring Relationships
●	When a dataset has been smoothed i.e. data has been rounded, we can use a process called jittering to add randomness into the dataset and make it more realistic
○	Say the variable height in the DataFrame df has been smoothed, we can jitter it by:
■	height_jitter = df[‘height’] + np.random.normal(0, 1, size = len(df))

3.2 Visualizing Relationships (refer to Seaborn course) 
●	Violin plot: estimating the KDE function for each column of data and plotting it
●	Box plot
●	plt.yscale(‘log’) - changes the y-scale to the logarithmic scale


3.3 Correlation
●	Does not work well for non-linear relationships - will underestimate the correlation
●	In general you can conclude:
○	Correlation close to 1 means there is a linear relationship
○	Correlation close to 0 does not mean there is no relationship - but the relationship is likely non-linear

3.4 Simple/Linear Regression

Example
from scipy.stats import linregress

# Extract the variables
# Must drop NaN values as linear regression can’t handle them
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']

# Compute the linear regression
res = linregress(xs,ys)
print(res)

Output
LinregressResult(slope=0.06988048092105019, intercept=1.5287786243363106, rvalue=0.11967005884864099, pvalue=1.378503916248713e-238, stderr=0.002110976356332333, intercept_stderr=0.013196467544093607)

Example (continued)
# Plot the line of best fit
fx = np.array([xs.min(),xs.max()])
fy = res.intercept + res.slope*fx
plt.plot(fx, fy, '-', alpha=0.7)
plt.show()


4. Multivariate relationships

4.1 Limits of Simple Regression
●	Only measures the strength of a linear relationship

4.2 Multiple Regression
●	Useful when we want to add control (constant) variables and describe non-linear relationships

Example 1

import statsmodels.formula.api as smf

# realinc is what we are trying to predict (y) and educ is the variable we are using to inform the prediction (x variable)
# Regress realinc as a function of educ
# OLS stands for ordinary least squares (another name for regression)
# the result from ols represents the model
# run .fit() to get the results
gss = pd.read_hdf('gss.hdf5', 'gss')
results = smf.ols('realinc ~ educ', data=gss).fit()
results.params

Output (shows intercept and slope)
Intercept   -11539.147837
educ          3586.523659
dtype: float64

This means each additional year of education is associated with a $3586 increase in income 


Example 2
Incorporating age

# on the right side of the formula you can add as many variables as you like
# adding age means we expect educ & age to contribute to realinc
results = smf.ols('realinc ~ educ + age', data=gss).fit()
results.params

Output (shows intercept and slope)
Intercept   -16117.275684
educ          3655.166921
age	      83.731804


Non-linear relationships
●	One option is to add a new variable that is a non-linear combination of other variables
●	E.g. adding a quadratic term

Example
import statsmodels.formula.api as smf

# Add a new column with educ squared
gss['educ2'] = gss['educ']**2

# Run a regression model with educ, educ2 and age
results = smf.ols('realinc ~ educ+educ2+age', data = gss).fit()

# Print the estimated parameters
print(results.params)


4.3 Visualizing Regression Results

Generating predictions
●	Uses the model to generate predictions
●	Easier to evaluate a model looking at its predictions rather than its parameters

Example
Using .predict(), which takes a DataFrame as a parameter and returns a series with a prediction for each row in the DataFrame

# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Make the DataFrame
df = pd.DataFrame()
df['educ'] = np.linspace(0,20)
df['age'] = 30
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2

# Plot mean income in each age group
grouped = gss.groupby('educ')
mean_income_by_educ = grouped['realinc'].mean()
plt.plot(mean_income_by_educ,'o', alpha = 0.5)

# Generate and plot the predictions
pred = results.predict(df)
plt.plot(df['educ'], pred, label='Age 30')

# Label axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.legend()
plt.show()









4.4 Logistic Regression
●	Useful for exploring relationships between quantitative and categorical variables (must be binary)
●	Explaining and predicting binary variables i.e. those that can be assigned a 1 and 0 (i.e. to represent yes and no, agree and disagree etc.

Example
# Recode grass
# Only binary variables can be used (0 & 1), whereas currently the variables are (1&2)
# Replace 2 with 0
gss['grass'].replace(2, 0, inplace=True)

# Run logistic regression
# We are going to predict whether individuals are in favor of cannabis legalization based on certain factors
# Use C() to identify categorical variables
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params

# Make a DataFrame with a range of ages
# We will feed this DataFrame into the regression model above
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2

# Set the education level to 12
# We hold this constant i.e. individuals in our sample data set have 12 years of education
df['educ'] = 12
df['educ2'] = df['educ']**2

# Generate predictions for men and women
df['sex'] = 1
pred1 = results.predict(df)

df['sex'] = 2
pred2 = results.predict(df)

# Plot mean of those in favor of legalization in each age group
grouped = gss.groupby('age')
favor_by_age = grouped['grass'].mean()
plt.plot(favor_by_age, 'o', alpha=0.5)

# Plot the predictions
plt.plot(df['age'], pred1, label='Male')
plt.plot(df['age'], pred2, label = 'Female')

plt.xlabel('Age')
plt.ylabel('Probability of favoring legalization')
plt.legend()
plt.show()















INTRODUCTION TO NUMPY

1. Understanding Numpy Arrays

1.1 Introducing Arrays
●	Pandas, SciPy, Matplotlib, TensorFlow and Scikit Learn are built on top of Numpy
●	The array is the main object - grid like structure that holds data
●	Create 1D array (pass in a list): np.array([1,2,3,4])
●	Create 2D array (pass in a list of lists: np.array([[1,2,3,4], [5,6,7,8]])
●	Numpy arrays must be of the same data type - makes the operation more efficient i.e. less memory space
●	np.zeros((5,3)) - takes in a tuple and creates an empty array of zeros with 5 rows and 3 columns 
○	Similar to creating an empty list [ ] which can be used as a placeholder to fill in later on
●	np.random.random((5,3)) - takes in a tuple and assigns random floats between 0 and 1 over 5 rows and 3 columns
○	np.random is the Numpy module
○	The second random in np.random.random() is the function name
●	np.arange(-3,4) - creates evenly spaced array of numbers based on a start and stop value (stop value is exclusive)
○	Passing a third argument is interpreted as the step value

Example
from matplotlib import pyplot as plt
plt.scatter(np.arange(0,7), np.arange(-3,4))
plt.show()







1.2 Array Dimensionality
●	Single number (like 3) is known as a scalar
●	1D arrays are known as vectors (neither explicitly horizontal or vertical)
○	Shape (5,) or shape (,5) would be the same
●	2D array is called as matrix
○	To create an array that is explicitly horizontal or vertical it must be a 2D array
○	Shape(5,1) or shape (1,5)
●	3D arrays + is called a tensor
●	.shape attribute for number of rows and columns
●	.flatten() takes all elements of an array and puts them in 1D (preserves the order)
●	.reshape() allows you to redefine the shape of the array
○	The new shape must contain the same number of elements as the original
○	E.g. (2,3) can be reshaped to (3,2) but not (3,3) 


1.3 Numpy Data Types
●	8 bits = 1 byte
●	int32 can store 2**32 = 4.2bn possible combinations of integers
○	This is between -2.1bn to 2.1bn
●	.dtype attribute for the data type
●	.astype() is used for type conversion
●	Type coercion - when you try to create an array with multiple data types Numpy will convert the array to one date type

Example
boolean_array = np.array([[True, False], [False, False]], dtype=np.bool_)
boolean_array.astype(np.int32)

Output
array([[1,0],
	[0,1]])


2. Selecting and Updating Data

2.1 Indexing & Slicing Arrays
●	Slicing and indexing 1D arrays is the same as with lists
●	Indexing 2D arrays: provide both row and column location to return a single element
○	E.g. array[2,4] - returns element in row 2 and column 4
○	E.g. array[0] - returns all the elements in row 1
○	E.g. array[:,2] - returns all elements in column 3
●	Slicing 1D:
○	E.g. array[2:4] - select elements between position 3 and 4
●	 Slicing 2D:
○	E.g. array[3:6, 3:6] - slices rows and then columns
●	Slicing 2D with steps:
○	E.g. array[3:6:2, 3:6:2] - step size of 2, searches for every other value
●	np.sort() - sorts the columns in a given row in the array in ascending order
○	In 2D array the direction along rows is axis 0, and along columns axis 1
○	Passing the argument axis = 0 will sort the rows in a given column in ascending order
○	Default of np.sort() is axis = 1 i.e. sort by columns















2.2 Filtering Arrays
●	Masks & fancy indexing
○	Useful when we are only interested in elements that meet a certain condition
○	Fancy indexing returns an array of the elements

Example
# create an array of numbers from 1 to 5 (stop value is exclusive)
one_to_five = np.arange(1, 6)

# the mask is an array of booleans with the same shape as the array
mask = one_to_five % 2 == 0

# index the array using the mask (fancy indexing) i.e. identify numbers in the array that are divisible by 2 (True)
one_to_five[mask]

Output
array([2, 4])


●	np.where()
○	Returns an array of the indices of elements that meet a certain condition
●	np.where(condition, how to change element if condition met, how to change element if condition not met)
○	Can also be used to replace elements with other elements

Example (fancy indexing vs np.where)
# Create the block_313879 array containing trees on block 313879 using fancy indexing
block_313879 = tree_census[tree_census[:,1] == 313879]
print(block_313879)

VS

# Create an array of row_indices for trees on block 313879 using np.where()
row_indices = np.where(tree_census[:,1] == 313879)

# Create an array which only contains data for trees on block 313879
block_313879 = tree_census[row_indices]
print(block_313879)


Example
# Create and print a 1D array, which replaces a tree's trunk diameter with its stump diameter if the trunk diameter is zero.
# Note: tree_census columns in order refer to a tree's ID, its block ID, its trunk diameter, and its stump diameter.
trunk_stump_diameters = np.where(tree_census[:, 2] == 0, tree_census[:, 3], tree_census[:, 2])
print(trunk_stump_diameters)


2.3 Adding & Removing Data
●	np.concatenate((array1, array2)) - pass a tuple of the array you wish to concatenate
○	Concatenates alongs the 1st axis (rows/axis=0) by default i.e. we add new rows/stack arrays on top of each other

●	np.concatenate((array1, array2), axis = 1) - pass axis = 1 to concatenate by column
●	The arrays you want to concatenate must have the same shape across all axis, except the one being concatenated along
○	E.g. for 2D arrays: concatenating by column, you can join a (3,3) array to a (3,1) array but not a (1,3) array i.e. both arrays must have 3 rows as we are concatenating by columns.
○	Otherwise you will get a ValueError
●	 The arrays must also have the same number of dimensions
●	np.delete() - takes 3 arguments
○	E.g. np.delete(array, 1, axis = 0) - deletes the second (1) row (axis = 0) from the array
○	If you want to delete a column, set axis = 1



3. Array Mathematics

3.1 Summarizing Data
●	.sum() - sums the entire array
○	Setting the argument axis = 0 will sum the rows in each column, creating column totals
○	Conversely, setting axis =1 creates row totals
○	When specifying the argument keepdims = True the dimensions that are collapsed when aggregating are left in the shape of the output array
■	Useful if we want to achieve dimension compatibility i.e. to concatenate
●	.min() - takes in the same arguments as .sum()
●	.max()  takes in the same arguments as .sum()
●	.mean() - takes in the same arguments as .sum()
●	.cumsum() - takes in the axis argument

Example
# Create a 2D array of total monthly sales across industries i.e. create row totals
monthly_industry_sales = monthly_sales.sum(axis=1, keepdims=True)
print(monthly_industry_sales)

# Add this column as the last column in monthly_sales
monthly_sales_with_total = np.concatenate((monthly_sales,monthly_industry_sales), axis = 1)
print(monthly_sales_with_total)


3.2 Vectorized Operations
●	Using the C programming language under the hood to perform computations efficiently
●	Multiply an array by a scalar (such as 0.05) will multiply each element in the array
●	If adding two arrays together, each array must be of the same shape. Elements from the first array are added to their corresponding element in the second array
●	Vectorizing python functions using np.vectorize()

Example
# using python functions like len does not treat each element in an array separately
# len will calculate the number of elements in the array and not the length of each element in the array
# usually we would have to write a for loop to solve this, or we can use np.vectorize()
array = np.array(["NumPy", "is", "awesome"])
len(array) > 2

Output
True

# vectorize the python len function
vectorized_len = np.vectorize(len)
vectorized_len(array) > 2
array([ True, False,  True])


3.3 Broadcasting
●	Performing mathematical operations across arrays of different shapes i.e. stretching the smaller array across the larger one
●	Adding a scalar to an array uses broadcasting
●	In order to broadcast arrays must be compatible
○	Two arrays are compatible when both of these conditions are met:
■	One set of dimensions is 1 
■	The other set of dimensions is equal 
■	E.g. shape(10,5) is compatible with shape(10,1) but not with (10,2)
●	Two arrays don’t have to have the same number of dimensions to be broadcastable
○	E.g. shape(10,5) is compatible with shape(5, ) - the second array is a 1D array which is essentially 5 ‘columns’ of data
●	The same logic applied to multiplying and subtracting

Example
Recall that when broadcasting across columns, NumPy requires you to be explicit that it should broadcast a vertical array, and horizontal and vertical 1D arrays do not exist in NumPy. Instead, you must first create a 2D array to declare that you have vertical data. Then, NumPy creates a copy of this 2D vertical array for each column and applies the desired operation.

# Convert monthly_growth_rate (currently a list) into a NumPy array and reshape it
# we reshape the 1D array into a 2D array
monthly_growth_D = np.array(monthly_growth_rate).reshape(12,1)

# Multiply each column in monthly_sales - which has shape(12,3) - by monthly_growth_2D - which has shape(12,1)
# broadcast across columns
print(monthly_sales*monthly_growth_D)


4. Array Transformations

4.1 Saving & Loading Arrays

Example
# rb is read binary
with open("logo.npy", "rb") as f:
logo_rgb_array = np.load(f)

Example
# Load the mystery_image.npy file 
# save the contents as rgb_array
# wb is ‘write binary’
# if no file is yet created for mystery_image.npy, a new file will be created, however if a file is already created it will be overwritten
with open("mystery_image.npy", mode = 'wb') as f:
    np.save(f,rgb_array)

plt.imshow(rgb_array)
plt.show()

 

4.2 Array Acrobatics
●	Data augmentation is useful in machine learning (ML) when training a model
○	Perform small manipulations on data that is already available
○	I.e. you want to train the model to recognise a bottle - you can rotate the bottle many different ways to train the model that it is still the same bottle
●	np.flip() - flips the array along every axis
○	Takes an axis keyword argument if you wish to specify the axis to manipulate
○	Setting axis = 1 flips the image along the 2nd/y-axis/column axis i.e. produces the mirror image
●	np.transpose() - changes axis order, but keeps element order within each axis the same
○	I.e. elements on row 1 now move to column 1, but maintain their order
○	Takes an axes keyword argument if you wish to specify the axis to manipulate
○	Pass the axes order you want the final array to appear in i.e. axes = (1,0,2) - columns and rows have switched

Example
# Transpose the 3-D rgb_array so that the image appears rotated 90 degrees left and as a mirror image of itself.
transposed_rgb = np.transpose(rgb_array, axes = (1,0,2))
plt.imshow(transposed_rgb)
plt.show()

 



4.3 Stacking & Splitting
●	np.split() - allows us to split arrays along its axes
●	np.stack() - allows us to concatenate data in a new dimension

Example
# Split monthly_sales into quarterly data
# rows contain months and columns contain sales data for each month
q1_sales, q2_sales, q3_sales, q4_sales = np.split(monthly_sales, 4, axis =0)

print(q1_sales)

 

# Stack the four quarterly sales arrays to create a 3 D array made up of 4 quarterly 2D arrays
quarterly_sales = np.stack([q1_sales, q2_sales, q3_sales, q4_sales], axis= 0)
print(quarterly_sales)













ANALYZING POLICE ACTIVITY WITH PANDAS


1. Preparing the data for analysis

1.1 Stanford open policing project dataset
●	.dtypes - attribute for checking data types
●	Dropping columns:
○	.drop(columns = ‘column name’, inplace = True)
●	Dropping rows:
○	.dropna(subset = [‘column/s to subset’], inplace = True)
●	Analyze the sum of missing values in each column:
○	df.isnull().sum()


1.2 Using proper data types
●	DataType impacts what operations you can perform
●	Avoid storing data as strings where possible
●	.astype() - pass the new data type you want as an argument

Note: Dot vs bracket notation - both mean the same thing
●	Dot notation: df.column
○	However, you must use bracket notation on the left side of an assignment statement i.e. to create a new series or overwrite an existing series
●	Bracket notation: df[‘column’] 


1.3 Creating a DateTimeIndex
●	df[‘column’].str.replace(‘string to replace’, ‘replacement string’)
●	pd.to_datetime(‘column’) - converts column to a DateTime object
●	df.set_index(‘column’, inplace = True’) - sets column as the index
○	N.B. - the index is not considered to be one of the DataFrame columns
○	df.index - attribute to examine the data in the index
○	df.columns - attribute to examine the data in the columns
●	df[‘column1’].str.cat(df[‘column2’], sep = ‘ ’) - concatenates column1 and column2, separating the data with a space/empty string



2. Exploring the relationship between gender and policing
●	df[‘column’].value_counts() - counts unique values in a series
○	Best suited for categorical data
●	df[‘column’].value_counts().sum() - known as ‘method chaining’
○	This should always be equal to the number of rows in the DataFrame - provided there is no missing values
●	df[‘column’].value_counts(normalize = True) - calculates the percentage/proportions of the total for each variable


2.1 Do genders commit different violations
●	df[(df[‘column1’] == ‘condition1’) & (df[‘column2’] == ‘condition2’)]
○	Ampersand (&) represents the logical ‘and’ operator
○	Pipe (|) represents the logical ‘or’ operator


2.2 Does gender affect who gets a speeding ticket

Example (filter the DataFrame first and then subset the filtered DateFrame)
# Create a DataFrame of female drivers stopped for speeding
female_and_speeding = ri[(ri[‘driver_gender’] == 'F') & (ri['violation'] == 'Speeding')]

# Compute the stop outcomes for female drivers (as proportions)
print(female_and_speeding['stop_outcome'].value_counts(normalize = True))


2.3 Does gender affect whose vehicle is searched

Example
# Calculate the search rate for each combination of gender and violation
print(ri.groupby(['driver_gender','violation'])['search_conducted'].mean())


2.4 Does gender affect who is frisked during a search
●	df[‘column’].value_counts(dropna=False)
○	.value_counts() excludes missing values by default
○	Specify the argument dropna = False to include the count of missing values
●	df[‘column’].str.contains(‘string to look for’, na = False) - this string method checks whether a defined string is present in each row of a given column
○	Setting na = False means it returns False if not found and True if found 



3. Visual exploratory data analysis

3.1 Does time of day affect arrest rate?

Example
# Calculate the hourly arrest rate, save as hourly_arrest_rate
# remember that the index contains the date and time, so we can call the .hour attribute of index
hourly_arrest_rate = ri.groupby(ri.index.hour).is_arrested.mean()


3.2 Are drug-related stops on the rise?
●	df[‘column’].resample(‘M’) - is the same as groupby month but allows you to groupby time i.e. ‘M’ is month, ‘D’ is days etc.
○	Can be called after .groupby()

Example (calculate mean price by month)
apple.groupby(apple.index.month).price.mean()
VS
apple[‘price’].resample('M').mean()

Example
# Concatenate 'annual_drug_rate' and 'annual_search_rate'
# axis can also be set to 1 to signify columns
# creates a new DateFrame with index date and two columns
annual = pd.concat([annual_drug_rate, annual_search_rate], axis='columns')

# Create subplots from 'annual'
# plots date vs drug rate and date vs search rate
# Setting subplots = True means both plots will share the x-axis but have separate y-axes
annual.plot(subplots=True)
plt.show()
















3.3 What violations are caught in each district?
●	pd.crosstab(df[‘column1’], df[‘column2’])
○	Pass two Pandas series, that represent categories, to the crosstab function
○	Outputs a frequency table for how many times each combination of categories appears in the dataset
















Example
# Create a stacked bar plot of 'k_zones'
k_zones.plot(kind='bar', stacked =True)
plt.show()



3.4 How long might you be stopped for a violation?

Example
# Create a dictionary that maps strings to integers
mapping = {'0-15 Min':8, '16-30 Min':23, '30+ Min':45}

# Convert the 'stop_duration' strings to integers using the 'mapping'
# mapping the dictionary above to the DataFrame
ri['stop_minutes'] = ri.stop_duration.map(mapping)

Example
# Save the resulting Series as 'stop_length'
stop_length = ri.groupby('violation_raw').stop_minutes.mean()

# Sort 'stop_length' by its values and create a horizontal bar plot
stop_length.sort_values().plot(kind='barh')
plt.show()























4. Analyzing the effect of weather on policing

4.1 Exploring the weather data set

Example
# Create a histogram with 20 bins to visualize 'TDIFF'
weather.TDIFF.plot(kind='hist',bins=20)
plt.show()



4.2 Categorizing the weather

Example
# Changing data type from object(string) to category
cats = ['short', 'medium', 'long']
ri['stop_length'] = ri.stop_length.astype('category', ordered=True, categories=cats)

# Show the memory usage
# memory usage is less for categories than objects
ri.stop_length.memory_usage(deep=True)
3400602

Note how categories are now ordered in the bottom line of code

















4.3 Merging the datasets

Example
# Merge 'ri' and 'weather_rating' using a left join
ri_weather = ri.merge(weather_rating, left_on='stop_date', right_on='DATE', how='left')

# Set 'stop_datetime' as the index of 'ri_weather'
ri_weather.set_index('stop_datetime', inplace=True)


4.4 Does weather affect the arrest rate
●	The output of a single .groupby() operation on multiple columns is a Series with a MultiIndex i.e. multi indexed series (as shown in the screenshot)
●	The outer index ‘Violation’ is like the DataFrame rows and the inner index ‘driver_gender’ like the columns
●	You can call search_rate.loc[‘Equipment’,’M’] to select the row and column















●	To convert the multi indexed series into a DataFrame use .unstack()
●	If you want to avoid having to use .groupby() and then an .unstack() to create this DataFrame you can use .pivot_table()
○	Remember that mean is the default aggregation function of a pivot table

































INTRODUCTION TO STATISTICS IN PYTHON

1. Summary Statistics

1.1 What is statistics?
●	Descriptive (current state) vs inferential stats
●	Numeric (quantitative) data:
○	Continuous (measured e.g. time, speed)
○	Discrete data (counted e.g. number of pets)
●	Categorical (qualitative) data
○	Nominal (unordered) e.g. married vs unmarried
○	Ordinal (ordered) e.g. survey question indicating degree to which you agree


1.2 Measures of center
●	np.mean()
●	np.median()
●	statistics.mode() - import statistics first
●	Skewed data: the mean is pulled in the direction of the skew
○	Left skewed data (long left tail)
○	This can impact the reliability of the mean

Example
# Subset for Belgium and USA only in the food_consumption DataFrame
be_and_usa = food_consumption[(food_consumption['country'] == "Belgium") | (food_consumption['country'] == 'USA')]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg([np.mean, np.median]))



1.3 Measures of spread
●	A quartile is one type of quantile

Example
# Calculate the quartiles of co2_emission
# np.linspace shows the 5 quantiles that splits the data up into 4 parts
print(np.quantile(food_consumption['co2_emission'], np.linspace(0,1,5))


2. Random numbers and probability

2.1 What are the chances?


2.2 Discrete distributions


2.3 Continuous distributions


2.4 The binomial distribution


3. More distributions and the central limit theorem

3.1 The normal distribution


3.2 The central limit theorem


3.3 The poisson distribution


3.4 More probability distributions


4. Correlation and experimental design

4.1 Correlation


4.2 Correlation caveats


4.3 Design of experiments
