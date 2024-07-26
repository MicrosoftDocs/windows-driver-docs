---
title: Get a submission
description: Retrieves data for a specific submission of a product to the hardware dashboard in the Microsoft Partner Center.
ms.topic: article
ms.date: 04/05/2018
---

# Get a submission

Use this method in the Microsoft Hardware API to retrieve data for a specific submission of a product.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

|Method|Request URI|
|:--|:--|
|GET|`https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionID}` |

### Request header

|Header|Type|Description|
|:--|:--|:--|
|Authorization|string|Required. The Microsoft Entra ID access token in the form **Bearer** \<token\>.|
|accept|string|Optional. Specifies the type of content. Allowed value is “application/json”|

### Request parameters

Do not provide request parameters for this method.

### Request body

Do not provide a request body for this method.

### Request examples

The following example demonstrates how to retrieve information about all submissions of a product.


```cpp
GET https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/13635057453741329/submissions/1152921504621441930 HTTP/1.1
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
         "url": "<SAS URL from Hardware API>"
      },
      {
        "type": "derivedPackage",
         "url": "<SAS URL from Hardware API>"
      },
      {
        "type": "signedPackage",
         "url": "<SAS URL from Hardware API>"
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
      "href": "https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/13635057453741329/submissions/1152921504621441930",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/13635057453741329/submissions/1152921504621441930",
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

- [hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
