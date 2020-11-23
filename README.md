# Mock permissions

This is a toy service which mocks an OPA permissions engine

Not impmented - service authentication 

This service exposes a single endpoint, `/v1/data/permissions`, which takes in
the body three fields:

* `method`: the method called to the beacon
* `path`: the path of the call - this can be used as a general rest label
* `user_tokens`: tokens associated with the user

It returns a json object, `datasets`, which is an array of strings indicating
the allowed datasets for this request.  The default is an empty array; you
can specifify a dataset name to return by running with e.g. `--response dataset1`

Build and run this server with:

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt

./main.py --response dataset1
```

and then in another terminal

```
./lookup_permissions.sh
```
