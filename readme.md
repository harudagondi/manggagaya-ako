# Manggagaya Ako

A twitter bot that mimics a group of people.

## Getting Started

### Prerequisites

*Manggagaya Ako* needs tweepy, markovify, and yaml

```
sudo pip install tweepy markovify pyyaml
```

Add a `config.yaml` file with the following:

```
CONSUMER_KEY: 'consumer_key'
CONSUMER_SECRET: 'consumer_secret'
ACCESS_TOKEN: 'access_token'
ACCESS_SECRET: 'access_secret'
COUNT: number of tweets to get (the lower the faster)
USERS:
  - user1
  - user2
  - user3
```

## Built With

* [PyYAML](http://pyyaml.org/wiki/PyYAML) - PyYAML is a YAML parser and emitter for Python.
* [Tweepy](http://www.tweepy.org/) - An easy-to-use Python library for accessing the Twitter API.
* [Markovify](https://github.com/jsvine/markovify) - Markovify is a simple, extensible Markov chain generator.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
