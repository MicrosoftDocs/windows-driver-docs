---
title: 
description: 
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 04/05/2018
ms.localizationpriority: medium
---

# Get a submission

Use this method in the Microsoft Hardware API to retrieve data for a specific submission of a product.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

|Method|Request URI|
|:--|:--|
|GET|`https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}/submissions/{submissionID}` |

### Request header

|Header|Type|Description|
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
GET https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/13635057453741329/submissions/1152921504621441930 HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for a specific submission of a product. For more details about the values in the response body, see the following section.

```json
{
  "id": 1152921504621442000,
  "productId": 13635057453741328,
  "workflowStatus": {
    "currentStep": "finalizeIngestion",
    "state": "completed",
    "messages": []
  },
  "downloads": {
    "items": [
      {
        "type": "initialPackage",
        "url": "https://ingestionpackagesint1.blob.core.windows.net/ingestion/dc55b8c6-a01c-40b6-b815-cac8bc08812a?sv=2016-05-31&sr=b&sig=ipjW3RsVC75lZrcEZRh9JmTX89L4gTIKkxwqv9F8Axs%3D&se=2018-03-12T15:32:10Z&sp=rl"
      },
      {
        "type": "derivedPackage",
        "url": "https://ingestionpackagesint1.blob.core.windows.net/ingestion/6bd77dbf-a851-46d2-b703-29ea4efae006?sv=2016-05-31&sr=b&sig=O5XQf%2FzMbI2FFt5WwSUJWL1JbWY4JXXPRkCKAnX7IRs%3D&se=2018-03-12T15:32:10Z&sp=rl&rscd=attachment%3B filename%3DShell_1152921504621441930.hlkx"
      },
      {
        "type": "signedPackage",
        "url": "https://ingestionpackagesint1.blob.core.windows.net/ingestion/0b83a294-c1d1-4136-82a1-dd52f51841e3?sv=2016-05-31&sr=b&sig=zTfxKJmaTwpbFol%2FpAKG0QuXJTTxm5aZ0F2wQQI8whc%3D&se=2018-03-12T15:32:10Z&sp=rl"
      },
      {
        "type": "certificationReport",
        "url": "https:// manage.devcenter.microsoft.com/dashboard/hardware/Driver/DownloadCertificationReport/29963920/13635057453741329/1152921504621441930"
      }
    ],
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
```

### Response body

Refer to [Submission resource](get-product-data.md#submission-resource)  for more details

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes).

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
