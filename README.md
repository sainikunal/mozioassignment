### Project setup in local
Clone the repo

Install requirements

`pip3 install -r requirements.txt`

Now Run django development server

## Project is already deployed on AWS EC2

**Access it on [52.91.223.173:8002](http://52.91.223.173:8002/area)**
## Documentation
There are two models named as `Provider` and `ServiceArea`

We will expose API endpoints for these models

To create new Provider ([/provider](http://52.91.223.173:8002/provider))
![alt text](https://github.com/sainikunal/mozioassignment/blob/master/images/ProviderCreate.png)

To Edit newly created Provider ([/provider/1](http://52.91.223.173:8002/provider/1))
![alt text](https://github.com/sainikunal/mozioassignment/blob/master/images/ProviderEdit.png)

To Create new ServiceArea ([/area](http://52.91.223.173:8002/area/))
![alt text](https://github.com/sainikunal/mozioassignment/blob/master/images/ServiceAreaCreate.png)

To Edit Existing ServiceArea ([/area/1](http://52.91.223.173:8002/area/1/))
![alt text](https://github.com/sainikunal/mozioassignment/blob/master/images/ServiceAreaEdit.png)

To Filter all ServiceAreas using given latitude and longitude ([/filter/?latitude=2&longitude=2](http://52.91.223.173:8002/filter/?latitude=2&longitude=2))
![alt text](https://github.com/sainikunal/mozioassignment/blob/master/images/FilterServiceArea.png)
