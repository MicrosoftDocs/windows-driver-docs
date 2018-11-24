---
title: Update product data
description: This method, in the Microsoft Hardware API, updates details of a product.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 04/05/2018
ms.localizationpriority: medium
---

# Update product data  
Use this method in the Microsoft Hardware API to update details of a product. Prior to using this method ensure you have created a product. For details, see [create a new product](create-a-new-product.md). 

## Prerequisites 
If you have not done so already, complete all the prerequisites for the Microsoft Hardware APIs before trying to use any of these methods. 
 
## Request 
This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body. 


| Method | Request URI |
|:--|:--|
| PATCH | `https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}` |

### Request header

| Header | Type | Description |
|:--|:--|:--|
| Authorization | String	| Required. The Azure AD access token in the form **Bearer** \<token\>. |
| accept |	String | Optional. Specifies the type of content. Allowed value is “application/json” |

### Request parameters

Do not provide request parameters for this method.

### Request body

The following example demonstrates the JSON request body for updating a product. Only 3 types of changes can be made to a product -  announcementDate, marketingNames and productName.

```json 
{
  "announcementDate": "2018-04-05T08:59:03.414Z",
  "marketingNames": ["name1"],
  "productName": "updatedProductName"
}
```

For details about the fields in the request, refer to [product resource](get-product-data.md#product-resource).

### Request examples
The following example demonstrates how to update a product.

```json 
PATCH https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14631253285588838 HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The response will be empty with a HTTP status of 204.

After this step, use the method [get product details](get-a-product.md) to get the updated details of the product.

## Error codes
Refer to [Error codes](get-product-data.md#error-codes) for details.

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
