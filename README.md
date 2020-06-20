# py-md5-attack

# Usage
```shell
python2 <known message> <md5 digest> <string to append> [length of secret]
```

# Example
> Original Message: "hello"   
> Secret: "welcome"   
> Length of Secret: 7   
> MD5 (secret + Original Message): "3752460bd048f6527619c4f6067d3afd"   
> Appened Message: "good"
```sh
python2 main.py "hello" "3752460bd048f6527619c4f6067d3afd" "good" 7
```

# Requirement
To conduct a hash extension attack on MD5, the fllowing information are needed
1. Digest of `secret + Original Message`
2. Length of `secret + Original Message`
3. Content of `Original Message`

# Acknowledgement
Thanks [@d0nutptr](https://gist.github.com/d0nutptr/e4e6a9384a0fffdb3c708319f8e95b2f) for the python implementation of MD5.
