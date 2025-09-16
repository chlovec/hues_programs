pip install ipykernel

python -m ipykernel install --user --name=myvenv --display-name "Python (myvenv)"

1. One thread to process 1 Month
2. Send request for the first day of the month
3. Send requests for missing dates in the month
4. What happens if an error occurs? Network error? retry else stop
5. Check robot.text file for this api / the rate limiter
http://web.archive.org/wayback/available?url=screenboston.com&timestamp=20240101

http://archive.org/wayback/available?url=screenboston.com&timestamp=20240101

fetched_data = {
    'url': 'screenboston.com',
    'archived_snapshots': {
        'closest': {
            'status': '200',
            'available': True,
            'url': 'http://web.archive.org/web/20240904042102/https://screenboston.com/',
            'timestamp': '20240904042102'
        }
    },
    'timestamp': '20240901'
}

When retrieving JSON content with <code>requests</code>, us the `json()` method rather than the `text` attribute to extract the content from the returned request object into a nested dictionary rather than a string.

Problem 3, hint 1 is ambiguous
It suggests that we need to read the movies data as json from the Wayback api. However, while the availability check api returns json data, the actual api for fetching the movies content returns a html file which needs to be parsed again to extract the movies.
Am I calling the wrong api?