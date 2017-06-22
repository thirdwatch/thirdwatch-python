# coding: utf-8

"""
    Thirdwatch API

    The first version of the Thirdwatch API is an exciting step forward towards making it easier for developers to pass data to Thirdwatch.   # Introduction Once you've [registered your website/app](https://thirdwatch.ai) it's easy to start sending data to Thirdwatch.  All endpoints are only accessible via https and are located at `api.thirdwatch.ai`. For instance: you can send event at the moment by ```HTTP POST``` Request to the following URL with your API key in ```Header``` and ```JSON``` data in request body. ```   https://api.thirdwatch.ai/event/v1 ``` Every API request must contain ```API Key``` in header value ```X-THIRDWATCH-API-KEY```  Every event must contain your ```_userId``` (if this is not available, you can alternatively provide a ```_sessionId``` value also in ```_userId```).  # Score API The Score API is use to get an up to date cutomer trust score after you have sent transaction event and order successful. This API will provide the riskiness score of the order with reasons. Some examples of when you may want to check the score are before:    - Before Shippement of a package   - Finalizing a money transfer   - Giving access to a prearranged vacation rental   - Sending voucher on mail    ```   https://api.thirdwatch.ai/neo/v1/score?api_key=<your api key>&order_id=<Order id> ```  According to Score you can decide to take action Approve or Reject. Orders with score more than 70 will consider as Riskey orders. We'll provide some reasons also in rules section.  ## Response score API  ``` {   \"order_id\": \"OCT45671\",   \"user_id\": \"ajay_245\",   \"order_timestamp\": \"2017-05-09T09:40:45.717Z\",   \"score\": 82,   \"flag\": \"red\",     -\"reasons\": [     {         \"name\": \"_numOfFailedTransactions\",         \"display_name\": \"Number of failed transactions\",         \"flag\": \"green\",         \"value\": \"0\",         \"is_display\": true       },       {         \"name\": \"_accountAge\",         \"display_name\": \"Account age\",         \"flag\": \"red\",         \"value\": \"0\",         \"is_display\": true       },        {         \"name\": \"_numOfOrderSameIp\",         \"display_name\": \"Number of orders from same IP\",         \"flag\": \"red\",         \"value\": \"11\",         \"is_display\": true       }     ] } ``` 

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AddToCart(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, user_id=None, session_id=None, device_ip=None, origin_timestamp=None, item=None, custom_info=None):
        """
        AddToCart - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_id': 'str',
            'session_id': 'str',
            'device_ip': 'str',
            'origin_timestamp': 'str',
            'item': 'Item',
            'custom_info': 'CustomInfo'
        }

        self.attribute_map = {
            'user_id': '_userId',
            'session_id': '_sessionId',
            'device_ip': '_deviceIp',
            'origin_timestamp': '_originTimestamp',
            'item': '_item',
            'custom_info': '_customInfo'
        }

        self._user_id = user_id
        self._session_id = session_id
        self._device_ip = device_ip
        self._origin_timestamp = origin_timestamp
        self._item = item
        self._custom_info = custom_info

    @property
    def user_id(self):
        """
        Gets the user_id of this AddToCart.
        The user's account ID according to your systems. Note that user IDs are case sensitive.

        :return: The user_id of this AddToCart.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AddToCart.
        The user's account ID according to your systems. Note that user IDs are case sensitive.

        :param user_id: The user_id of this AddToCart.
        :type: str
        """

        self._user_id = user_id

    @property
    def session_id(self):
        """
        Gets the session_id of this AddToCart.
        The user's current session ID, used to tie a user's action before and after login or account creation. Required if no user_id values is provided.

        :return: The session_id of this AddToCart.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this AddToCart.
        The user's current session ID, used to tie a user's action before and after login or account creation. Required if no user_id values is provided.

        :param session_id: The session_id of this AddToCart.
        :type: str
        """

        self._session_id = session_id

    @property
    def device_ip(self):
        """
        Gets the device_ip of this AddToCart.
        IP address of the request made by the user. Recommended for historical backfills and customers with mobile apps.

        :return: The device_ip of this AddToCart.
        :rtype: str
        """
        return self._device_ip

    @device_ip.setter
    def device_ip(self, device_ip):
        """
        Sets the device_ip of this AddToCart.
        IP address of the request made by the user. Recommended for historical backfills and customers with mobile apps.

        :param device_ip: The device_ip of this AddToCart.
        :type: str
        """

        self._device_ip = device_ip

    @property
    def origin_timestamp(self):
        """
        Gets the origin_timestamp of this AddToCart.
        Represents the time the event occured in your system. Send as a UNIX timestamp in milliseconds in string.

        :return: The origin_timestamp of this AddToCart.
        :rtype: str
        """
        return self._origin_timestamp

    @origin_timestamp.setter
    def origin_timestamp(self, origin_timestamp):
        """
        Sets the origin_timestamp of this AddToCart.
        Represents the time the event occured in your system. Send as a UNIX timestamp in milliseconds in string.

        :param origin_timestamp: The origin_timestamp of this AddToCart.
        :type: str
        """

        self._origin_timestamp = origin_timestamp

    @property
    def item(self):
        """
        Gets the item of this AddToCart.

        :return: The item of this AddToCart.
        :rtype: Item
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this AddToCart.

        :param item: The item of this AddToCart.
        :type: Item
        """

        self._item = item

    @property
    def custom_info(self):
        """
        Gets the custom_info of this AddToCart.

        :return: The custom_info of this AddToCart.
        :rtype: CustomInfo
        """
        return self._custom_info

    @custom_info.setter
    def custom_info(self, custom_info):
        """
        Sets the custom_info of this AddToCart.

        :param custom_info: The custom_info of this AddToCart.
        :type: CustomInfo
        """

        self._custom_info = custom_info

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AddToCart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
