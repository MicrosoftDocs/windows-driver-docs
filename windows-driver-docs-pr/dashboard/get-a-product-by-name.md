---
title: Get a product by name
description: This method in the Microsoft Hardware API retrieves data for a specific product name.
ms.topic: article
ms.date: 11/18/2020
ms.localizationpriority: medium
---

# Get a product

Use this method in the Microsoft Hardware API to retrieve data for a specific product name.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md)  for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

|Method|Request URI|
|:--|:--|
|GET|TBD|

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
GET TBD
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for a specific product name. For more details about the values in the response body, see the following section.

```json
{
TBD
}
```

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes).

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
