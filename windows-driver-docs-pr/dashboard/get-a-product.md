---
title: Get a product
description: This method in the Microsoft Hardware API retrieves data for a specific product registered to your Windows Dev Center account.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 04/05/2018
ms.localizationpriority: medium
---

# Get a product

Use this method in the Microsoft Hardware API to retrieve data for a specific product registered to your Windows Dev Center account.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md)  for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

|Method|Request URI|
|:--|:--|
|GET|https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}|

### Request header

| Header | Type | Description |
|:--|:--|:--|
| authorization | string | Required. The Azure AD access token in the form **Bearer** \<token\>. |
| accept | string | Optional. Specifies the type of content. Allowed value is “application/json” |


### Request parameters

Do not provide request parameters for this method

### Request body

Do not provide a request body for this method.

### Request examples

The following example demonstrates how to retrieve information about a specific product registered to your account.

```cpp
GET https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14039471039847257 HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for a specific product registered to a developer account. For more details about the values in the response body, see the following section.

```json
{
  "id": 9007199267351834,
  "sharedProductId": 1152921504606971100,
  "links": [
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/9007199267351834",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/9007199267351834/submissions",
      "rel": "get_submissions",
      "method": "GET"
    }
  ],
  "isCommitted": true,
  "isExtensionInf": false, "_comment": "This field is deprecated and moved to submission resource",
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
}
```

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes).

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
