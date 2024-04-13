---
title: Get all products
description: This method in the Microsoft Hardware API retrieves data for all products registered to your Windows Dev Center account.
ms.topic: article
ms.date: 04/05/2018
---

# Get all products

Use this method in the Microsoft Hardware API to retrieve data for all the products registered to your Windows Dev Center account.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

|Method|Request URI|
|--|--|
|GET| `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/` |

### Request header

|Header|Type|Description|
|--|--|--|
|Authorization|string|Required. The Microsoft Entra ID access token in the form **Bearer** \<token\>.|
|accept|string|Optional. Specifies the type of content. Allowed value is “application/json”|

### Request parameters

Do not provide request parameters for this method.

### Request body

Do not provide a request body for this method.

### Request examples

The following example demonstrates how to retrieve information about all products that are registered to your account.

```cpp
GET https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/ HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for all the products that are registered to a developer account. For brevity, this example only shows the data for the first two products returned by the request. For more details about the values in the response body, see the following section.

```json
{
  "value": [
    {
            "id": 9007199267351834,
            "sharedProductId": 1152921504606971255,
            "links": [
                {
                    "href": "https://hardwareapi.microsoft.com/api/v1/hardware/products/9007199267351834",
                    "rel": "self",
                    "method": "GET"
                },
                {
                    "href": "https://hardwareapi.microsoft.com/api/v1/hardware/products/9007199267351834/submissions",
                    "rel": "get_submissions",
                    "method": "GET"
                }
            ],
            "isCommitted": true,
            "isExtensionInf": false,
            "originType": "author",
            "sourceProductId": 0,
            "sourcePublisherId": 0,
            "isRetpolineCompiled": false,
            "message": "",
            "deviceMetadataIds": [],
            "deviceType": "notSet",
            "isTestSign": false,
            "isFlightSign": false,
            "marketingNames": [],
            "productName": "NewDriverHacked",
            "selectedProductTypes": {},
            "requestedSignatures": [
                "WINDOWS_v100_X64_TH1_FULL",
                "WINDOWS_v63_X64"
            ],
            "additionalAttributes": {},
            "testHarness": "hlk"
        },
        {
            "id": 9007199267351835,
            "sharedProductId": 1152921504606971256,
            "links": [
                {
                    "href": "https://hardwareapi.microsoft.com/api/v1/hardware/products/9007199267351835",
                    "rel": "self",
                    "method": "GET"
                },
                {
                    "href": "https://hardwareapi.microsoft.com/api/v1/hardware/products/9007199267351835/submissions",
                    "rel": "get_submissions",
                    "method": "GET"
                }
            ],
            "isCommitted": true,
            "isExtensionInf": false,
            "originType": "author",
            "sourceProductId": 0,
            "sourcePublisherId": 0,
            "isRetpolineCompiled": false,
            "message": "",
            "announcementDate": "2016-10-22T00:00:00Z",
            "deviceMetadataCategory": "Input.Digitizer.Multitouch",
            "deviceMetadataIds": [],
            "deviceType": "internalExternal",
            "isTestSign": false,
            "isFlightSign": false,
            "marketingNames": [
                "MEU"
            ],
            "productName": "Mew2?",
            "selectedProductTypes": {
                "Windows_v100": "Touch",
                "Windows81": "Unclassified"
            },
            "requestedSignatures": [
                "WINDOWS_v100_X64_TH1_FULL",
                "WINDOWS_v63_X64"
            ],
            "additionalAttributes": {},
            "testHarness": "hlk"
        }
  ]
}
```

### Response body

| Value | Type | Description |
|:--|:--|:--|
| value | array | An array of objects that contain information about each product that is registered to your account. For more information about the data in each object, see [Product resource](get-product-data.md#product-resource). |
| links | array | An array of objects with helpful links about the containing entity. Refer to [link object](get-product-data.md#link-object)  for more details  |


## Error codes

For more info, see [Error codes](get-product-data.md#error-codes). 

## See also

- [hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
