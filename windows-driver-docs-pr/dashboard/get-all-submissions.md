---
title: Get all submissions
description: This method in the Microsoft Hardware API retrieves data for all submissions of a product.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 04/05/2018
ms.localizationpriority: medium
---

# Get all submissions

Use this method in the Microsoft Hardware API to retrieve data for all submissions of a product.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md)  for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

|Method|Request URI|
|:--|:--|
|GET| `https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}/submissions` |

### Request header

|Header|Type|Description
|:--|:--|:--|
|Authorization|string|Required. The Azure AD access token in the form **Bearer** \<token\>.|
|accept|string|Optional. Specifies the type of content. Allowed value is “application/json”|

### Request parameters

Do not provide request parameters for this method.

### Request body

Do not provide a request body for this method.

### Request examples

The following example demonstrates how to retrieve information about all submissions of a product.


```cpp
GET https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/13635057453741329/submissions HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for all the submissions of a product. For brevity, this example only shows the data for the first two submissions returned by the request. For more details about the values in the response body, see the following section.

```json
{
  "value": [
    {
      "id": 1152921504621442000,
      "productId": 13635057453741328,
      "links": [
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/13635057453741329/submissions/1152921504621441944",
          "rel": "self",
          "method": "GET"
        },
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/13635057453741329/submissions/1152921504621441944",
          "rel": "update_submission",
          "method": "PATCH"
        }
      ],
      "isExtensionInf": true,
      "isUniversal": true,
      "isDeclarativeInf": true,
      "name": "HARRY-Duatest2",
      "type": "derived"
    },
    {
      "id": 1152921504621442000,
      "productId": 13635057453741328,
      "workflowStatus": {
        "currentStep": "finalizeIngestion",
        "state": "completed",
        "messages": []
      },
      "links": [
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/13635057453741329/submissions/1152921504621441946",
          "rel": "self",
          "method": "GET"
        },
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/13635057453741329/submissions/1152921504621441946",
          "rel": "update_submission",
          "method": "PATCH"
        }
      ],
      "isExtensionInf": true,
      "isUniversal": true,
      "isDeclarativeInf": true,
      "name": "updated-1",
      "type": "derived"
    },
    {
      "id": 1152921504621442000,
      "productId": 13635057453741328,
      "workflowStatus": {
        "currentStep": "finalizeIngestion",
        "state": "completed",
        "messages": []
      },
      "links": [
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/13635057453741329/submissions/1152921504621441930",
          "rel": "self",
          "method": "GET"
        },
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/13635057453741329/submissions/1152921504621441930",
          "rel": "update_submission",
          "method": "PATCH"
        }
      ],
      "isExtensionInf": true,
      "isUniversal": true,
      "isDeclarativeInf": true,
      "name": "HARRY-Duatest2",
      "type": "initial"
    }
  ],
  "links": [
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/13635057453741329/submissions",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

### Response body

|Value|Type|Description|
|:--|:--|:--|
|value|array|An array of objects that contain information about each submission of a product. For more information about the data in each object, see [Submission resource](get-product-data.md#submission-resource).|
|links|array|An array of objects with helpful links about the containing entity. Refer [link object](get-product-data.md#link-object)  for more details|

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes).

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
