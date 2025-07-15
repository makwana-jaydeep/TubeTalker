from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ['www.youtube.com', 'youtube.com']:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith('/embed/'):
            return query.path.split('/')[2]
        elif query.path.startswith('/v/'):
            return query.path.split('/')[2]
    raise ValueError("Invalid YouTube URL")


if __name__ == '__main__':

    print(extract_video_id('https://www.youtube.com/watch?v=9sEMdiP3DxQ'))
