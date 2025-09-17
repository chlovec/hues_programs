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