# CSE 8A Winter 2026 PA8

**Due Date: Sunday, March 15, 2026, 11:59 PST**

## Provided Files
Code files:
- `csv_processing.py` (Starter code file)
- `CSE8ACSV.py` (Do not modify this file)

CSV files:
- `fortune500.csv` (CSV file containing the Fortune 500 company data)
- `spotify.csv` (CSV file containing the Spotify song data)

## File(s) to Submit
`csv_processing.py` (Your implementation of the required functions)
---

## Part 0. Setup and Background

Before start coding, make sure you have downloaded `CSE8ACSV.py` and both of the provided CSV files (`fortune500.csv` and `spotify.csv`) into the same directory as your `csv_processing.py` file. In this programming assignment, you will be working with CSV files and practicing processing CSV data using Python. For basic knowledge of CSV files and how to use the `CSE8ACSV` provided functions, refer to the [lab instructions](https://github.com/CaoAssignments/cse8a-wi26-pa8/blob/main/PA8%20Lab.md#part-2-working-with-csv-files)). The starter code has been provided in `csv_processing.py` including function signatures and necessary data loading.

## Part 1. Implementation (100 points)

In this programming assignment, you will implement a total of four functions that process the provided CSV files.

### Part 1.1: Process Fortune 500 Data

The first part of the PA processes the `fortune500.csv` contains data about the top 500 companies in the world by revenue. Each row corresponds to a company and each column corresponds to a specific attribute of the company. Below is a description of each field in the CSV file:

| Field Name | Field Type | Description |
| :--- | :--- | :--- |
| Rank | int | Company's numerical rank based on revenue. |
| Name | String | Name of the company. |
| Industry | String | Specific industry the company operates in. |
| Sector | String | Broader economic sector of the company. |
| Headquarters | String | City and state of the company's headquarters. |
| Revenue | float | Total revenue in billions of USD. |
| Change | float | Percentage change in revenue from the previous year. |
| Profit | float | Net profit in billions of USD. |
| Asset | float | Total financial assets in billions of USD. |
| Market Value | float | Total market capitalization in billions of USD. |
| Employees | int | Total number of employees. |


For this CSV file, you will implement two functions:

#### `def get_total_revenue_in_sectors(fortune_data, sector_list)`

This function takes in a dataset of companies and a list of sectors, and returns the total combined revenue of all companies that belong to any of the specified sectors. Your function should return a single floating-point number.

- You can assume fortune_data is a list of dictionaries representing the Fortune 500 data, where each dictionary corresponds to a row. (You should use the `load_csv` function from `CSE8ACSV` library to read the CSV file into this format.)
- You can assume sector names shown in `sector_list` always exist in the dataset. `sector_list` can also contain zero sector names, in which case the function should return 0.0.
- Examples:
```python
get_total_revenue_in_sectors(fortune_data, ["Energy"]) # should return 2496.33, the total revenue of all companies in the Energy sector
get_total_revenue_in_sectors(fortune_data, ["Energy", "Retailing"]) # should return 4940.04, the total revenue of all companies in the Energy and Retailing sectors
get_total_revenue_in_sectors(fortune_data, []) # should return 0.0
```
- Don't worry about the formatting and rounding of the returned output. Autograder will check for the correctness of the returned value within a reasonable tolerance.

#### `def find_profitable_companies_above_threshold(fortune_data, profit_threshold)`

This function takes in a dataset of companies and a profit threshold, and returns a list of tuples containing the names and profits of all companies with profits above the threshold.

- You can assume fortune_data is a list of dictionaries representing the Fortune 500 data, where each dictionary corresponds to a row. (You should use the `load_csv` function from `CSE8ACSV` library to read the CSV file into this format.)
- You should check if `profit_threshold` is a valid number (not negative). If it is invalid, return an empty list.
- The returned list should contain tuples of the form `(company_name, profit)`, where `company_name` is a string and `profit` is a float. The order of the tuples in the returned list does not matter.

- Examples:
```python
find_profitable_companies_above_threshold(fortune_data, 50.0) # should return [('Exxon Mobil', 55.74), ('Apple', 99.8), ('Alphabet', 59.97), ('Microsoft', 72.74)] (order does not matter)
find_profitable_companies_above_threshold(fortune_data, -10.0) # should return [] (invalid threshold)
```

### Part 1.2: Process Spotify Data
The second part of the PA processes the `spotify.csv` file which contains data about various tracks on Spotify. We will be using a truncated version of the original dataset for this PA which has 1000 rows and 18 columns. For the original full dataset, see [link](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset). Each row corresponds to a track and each column corresponds to a specific attribute of the track. Below is a description of each field in the CSV file:


| Field Name | Field Type | Description |
| :--- | :--- | :--- |
| track_id | String | The unique Spotify ID for the track. |
| artists | String | Artist names (separated by `;` if multiple). |
| album_name | String | Name of the album containing the track. |
| track_name | String | Name of the track. |
| popularity | int | Popularity score from 0 to 100 based on recent plays. |
| duration_ms | int | Track length in milliseconds. |
| explicit | boolean | Indicates if the track has explicit lyrics (true/false). |
| danceability | float | Suitability for dancing, from 0.0 (least) to 1.0 (most). |
| energy | float | Intensity and activity measure, from 0.0 to 1.0. |
| key | int | Musical key using standard Pitch Class notation (-1 if undetected). |
| loudness | float | Overall loudness of the track in decibels (dB). |
| mode | int | Modality of the track (1 = major, 0 = minor). |
| speechiness | float | Presence of spoken words, from 0.0 (music) to 1.0 (speech-only). |
| acousticness | float | Confidence measure of acoustic nature, from 0.0 to 1.0. |
| instrumentalness | float | Likelihood the track contains no vocals, from 0.0 to 1.0. |
| liveness | float | Probability the track was performed live, from 0.0 to 1.0. |
| valence | float | Musical positiveness/mood, from 0.0 (negative) to 1.0 (positive). |
| tempo | float | Estimated tempo in beats per minute (BPM). |
| time_signature | int | Estimated time signature (beats per bar, ranging from 3 to 7). |
| track_genre | String | The genre to which the track belongs. |

For this CSV file, you will implement two functions:

#### `def get_average_duration_by_artist(spotify_data, artist_list)`

This function takes in a dataset of Spotify tracks and a list of artist names, and returns the average duration (in milliseconds) of all tracks by those artists.

- You can assume `spotify_data` is a list of dictionaries representing the Spotify track data, where each dictionary corresponds to a row. (You should use the `load_csv` function from `CSE8ACSV` library to read the CSV file into this format.)
- You can assume `artist_list` is a list of strings representing the names of the artists you want to search for. For artist name that does not exist in the dataset, please ignore them and do not include them in the average duration calculation. If none of the artists in `artist_list` exist in the dataset, return 0.0.

- Examples:
```python
get_average_duration_by_artist(spotify_data, ['Jason Mraz']) # should return 224410.66 (average duration of all tracks by Jason Mraz in the dataset)
get_average_duration_by_artist(spotify_data, ['Nonexistent Artist']) # should return 0.0 (no tracks by this artist in the dataset)
```
- Don't worry about the formatting and rounding of the returned output. Autograder will check for the correctness of the returned value within a reasonable tolerance.

#### `def find_most_popular_by_artist(spotify_data, artist_list)`

This function takes in a dataset of Spotify tracks and a list of artist names, and returns a **dictionary** of the most popular track for each artist in the list. The keys of the dictionary should be the artist names, and the values should be tuples containing the track name and its popularity score.

- You can assume `spotify_data` is a list of dictionaries representing the Spotify track data, where each dictionary corresponds to a row. (You should use the `load_csv` function from `CSE8ACSV` library to read the CSV file into this format.)
- You can assume `artist_list` is a list of strings representing the names of the artists you want to search for. For artist name that does not exist in the dataset, please ignore them and do not include them in the returned dictionary. If none of the artists in `artist_list` exist in the dataset, return an empty dictionary.
- The returned dictionary should contain the artist names as keys and tuples of the form `(track_name, popularity)` as values, where `track_name` is a string and `popularity` is an integer. The order of the tuples in the returned list does not matter.

- Examples:
```python
find_most_popular_by_artist(spotify_data, ['Jason Mraz']) # should return {'Jason Mraz': ("I'm Yours", 80)} (the most popular track by Jason Mraz in the dataset is "I'm Yours" with a popularity score of 80.0)
find_most_popular_by_artist(spotify_data, ['Jason Mraz', 'Andrew Foy']) # should return {'Jason Mraz': ("I'm Yours", 80.0), 'Andrew Foy': ('Love Nwantiti', 30.0)}
find_most_popular_by_artist(spotify_data, ['Nonexistent Artist']) # should return {} (no tracks by this artist in the dataset)
```

## Part 2: Submission

When you are ready, submit your code to Gradescope.

**You must submit this file:**
- `csv_processing.py`

The file name must match exactly to pass the autograder.

### How to Submit to Gradescope

1. Go to Gradescope and find the PA8 assignment
2. Upload `csv_processing.py`
3. Click "Submit"
4. Wait for the autograder to run

### Understanding Your Results

This PA uses **20 test cases total**:
- 5 tests for `get_total_revenue_in_sectors`
- 5 tests for `get_top_n_companies_by_profit`
- 5 tests for `find_most_popular_by_artist`
- 5 tests for `get_average_duration_by_artist`

There are total of 3 hidden test cases that are only visible after the grades are published. The hidden test cases include:
- 1 hidden test case for `get_total_revenue_in_sectors`: Test when all sectors shown in the dataset are included in `sector_list`.
- 1 hidden test case for `find_most_popular_by_artist`: Test when all artists shown in the dataset are included in `artist_list`.
- 1 hidden test case for `get_average_duration_by_artist`: Test when all artists shown in the dataset are included in `artist_list`.

If you fail a test case, Gradescope feedback may show:
- The test name (which tells you what it's testing)
- The input parameters
- The expected output
- Your actual output

You can submit multiple times. Use the feedback to debug and improve your code.

When you pass all public test cases, you should receive most of the points. Hidden tests help us check additional edge cases and discourage hard-coding.


### Getting Help
- **Office hours**: Attend tutor or TA office hours
- **Piazza**: Post questions on Piazza (don't share your code publicly!)
- **Start Early**: Give yourself plenty of time to work on the assignment and debug any issues that arise.
