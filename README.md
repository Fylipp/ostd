# ostd

Simple [OpenSubtitles.org](https://www.opensubtitles.org) download CLI-tool and API. You will have to acquire a user-agent [as described here](http://trac.opensubtitles.org/projects/opensubtitles/wiki/DevReadFirst). The user-agent for test purposes is: `TemporaryUserAgent` (the API docs state this may change without notice, so keep that in mind).

## Installation

```sh
pip install ostd
```



## CLI

```sh
py -m ostd <USER-AGENT> <SUBTITLE-ID>
```

## API

```python
from ostd import Downloader

ids = (1234, 5678, 9012)

with Downloader('Your User-Agent') as downloader:
  for result in downloader.download(ids):
    print(result.content)  # Watch out for file and console encoding mismatches!
```

## License

MIT.

