---
title: Create a new submission for a product
description: Use this method in the Microsoft Hardware API to create a new submission for a product.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 04/05/2018
ms.localizationpriority: medium
---

# Create a new submission for a product

Use this method in the Microsoft Hardware API to create a new submission for a product. Prior to using this method ensure you have created a new product. For details, see [create a new product](create-a-new-product.md).

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

| Method | Request URI |
|:--|:--|
| POST | `https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}/submissions` |


The productId in the method is the product for which the submission is intended.

### Request header

| Header | Type | Description |
|:--|:--|:--|
| Authorization | String | Required. The Azure AD access token in the form **Bearer** \<token\>. |
| Accept | String | Optional. Specifies the type of content. Allowed value is “application/json” |


### Request parameters

Do not provide request parameters for this method.

### Request body

The following example demonstrates the JSON request body for creating a new submission.

```json
{
  "name": "VST_apdevtest1_init",
  "type": "initial"
}
```

For details about the fields in the request, refer to [Submission resource](get-product-data.md#submission-resource).

### Request examples

The following example demonstrates how to create a new submission.

```cpp
POST https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14631253285588838/submissions HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for creating a new submission for a product. For more details about the values in the response body, see the following section.

```json
{
  "id": 1152921504621465124,
  "productId": 14631253285588838,
  "downloads": {
    "items": [
      {
        "type": "initialPackage",
        "url": "https://ingestionpackagesint1.blob.core.windows.net/ingestion/38c19eaf-7377-4834-893c-28d5791f7896?sv=2017-04-17&sr=b&sig=SlD5j5e067oA4Y3hdk1sPW3UycTSUVlIp80WbWvj4A8%3D&se=2018-03-20T05:00:14Z&sp=rwl"
      }
    ],
    "messages": []
  },
  "links": [
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14631253285588838/submissions/1152921504621465124",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14631253285588838/submissions/1152921504621465124",
      "rel": "update_submission",
      "method": "PATCH"
    }
  ],
  "commitStatus": "commitPending",
  "isExtensionInf": true,
  "isUniversal": true,
  "isDeclarativeInf": true,
  "name": "VST_apdevtest1_init",
  "type": "initial"
}
```

### Response body

Refer to [Submission resource](get-product-data.md#submission-resource) for more details.

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes).

## See also

[Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
