---
title: Create a new product
description: Use this method in the Microsoft Hardware API to create a new hardware product.
author: balapv
ms.author: balapv
ms.date: 04/05/2018
ms.topic: article
ms.localizationpriority: medium
---

# Create a new product

Use this method in the Microsoft Hardware API to create a new hardware product.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md)  for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

| Method | Request URI |
|:--|:--|
| POST | `https://manage.devcenter.microsoft.com/v1.0/my/hardware/products` |


### Request header

| Header | Type | Description |
|:--|:--|:--|
| Authorization | string | Required. The Azure AD access token in the form **Bearer** \<token\>. |
| accept | string | Optional. Specifies the type of content. Allowed value is “application/json” |


### Request parameters

Do not provide request parameters for this method.

### Request body

The following example demonstrates the JSON request body for creating a new product. For more details about the values in the request body, see the table below the json.

```json
{
  "ProductName": "Test_Network_Product2-R",
  "TestHarness": "Attestation",
  "announcementDate": "2018-01-01T00:00:00",
  "deviceMetadataIds": [],
  "firmwareVersion": "980",
  "deviceType": "external",
  "isTestSign": false,
  "isFlightSign": false,  
  "marketingNames": [],
  "productName": "VST_apdevtest1",
  "selectedProductTypes": {
    "windows_v100_RS3": "Unclassified"
  },
  "requestedSignatures": [
    "WINDOWS_v100_RS3_FULL",
    "WINDOWS_v100_X64_RS3_FULL",
    "WINDOWS_VISTA"
  ],
  "additionalAttributes": {},
  "packageType": "HLK"
}
```

For details about the fields in the request, refer to [Product resource](get-product-data.md#product-resource).

### Request examples

The following example demonstrates how to create a new product.

```cpp
POST https://manage.devcenter.microsoft.com/v1.0/my/hardware/products HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for creating a product. For more details about the values in the response body, see the following section.

```json
{
  "id": 14631253285588838,
  "sharedProductId": 1152921504607010608,
  "links": [
    {
      "href": "https:// manage.devcenter.microsoft.com/api/v1/hardware/products/14631253285588838",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https:// manage.devcenter.microsoft.com/api/v1/hardware/products/14631253285588838/submissions",
      "rel": "get_submissions",
      "method": "GET"
    }
  ],
  "isCommitted": false,
  "isExtensionInf": false,
  "announcementDate": "2018-01-01T00:00:00",
  "deviceMetadataIds": [],
  "firmwareVersion": "980",
  "deviceType": "external",
  "isTestSign": false,
  "isFlightSign": false,  
  "marketingNames": [],
  "productName": "VST_apdevtest1",
  "selectedProductTypes": {
    "windows_v100_RS3": "Unclassified"
  },
  "requestedSignatures": [
    "WINDOWS_v100_RS3_FULL",
    "WINDOWS_v100_X64_RS3_FULL",
    "WINDOWS_VISTA"
  ],
  "additionalAttributes": {},
  "testHarness": "attestation"
}
```

### Response body

Refer to [Product resource](get-product-data.md#product-resource)  for more details

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes).

## See also

[Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
