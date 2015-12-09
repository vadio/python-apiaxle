



# Python client to the Apiaxle REST api

About
==========

- Uses pycurl
- As of today, only allows key and api creation and linking

Examples
========
### Import Apiaxle Client

        >>> from apiaxle import client
        >>> api_client = client.Client("localhost","3000")

### Add new api

        >>> api_client.new_api('<new_api_name>',endPoint='<new_api_endpoint>:<port>')

* Client.new_api() will accept any input specified in the apiaxle api for provisioning an new api as a keywork argument

### Add new key
        
        >>> api_client.new_key('<key_text>') 

* Client.new_key() will accept any input specified in the apiaxle api for provisioning an new key as a keyword_argument

### Link key to api
    
        >>> api_client.link_key('<api_name>','<key_text>')


Contributing
============

Any contribution is highly encouraged and desired. :)

* Fork on Github.
* Make the changes. Bonus points if changes include documentation and tests.
* Send a pull request.


License
=======

[MIT](https://github.com/vadio/python-apiaxle/blob/master/LICENSE.txt)

