# Python client to the Apiaxle REST api

About
==========

- Uses pycurl
- As of today, only allows key and api creation and linking

Examples
========
### Import Apiaxle

        >>> from apiaxle import Apiaxle
        >>> aa = Apiaxle("localhost","3000")

### Add new api

        >>> aa.new_api('<new_api_name>',endPoint='<new_api_endpoint>:<port>')

* Apiaxle.new_api() will accept any input specified in the apiaxle api for provisioning an new api as a keywork argument

### Add new key
        
        >>> aa.new_key('<key_text>') 

* Apiaxle.new_key() will accept any input specified in the apiaxle api for provisioning an new key as a keyword_argument

### Link key to api
    
        >>> aa.link_key('<api_name>','<key_text>')
        
### Update existing api
        >>> demo_api = aa.api('<api_name>')
        >>> demo_api.update(keyWord='value',keyWord2='value2')

### Update existing key
        >>> demo_key = aa.key('<key_name>')
        >>> demo_key.update(keyWord='value',keyWord2='value2')

Tests
========
Tests are run with nose:
       >>> nosetests


Contributing
============

Any contribution is highly encouraged and desired. :)

* Fork on Github.
* Make the changes. Bonus points if changes include documentation and tests.
* Send a pull request.


License
=======

[MIT](https://github.com/vadio/python-apiaxle/blob/master/LICENSE.txt)
