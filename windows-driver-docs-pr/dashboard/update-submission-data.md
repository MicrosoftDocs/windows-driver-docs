---
title: Update submission data
description: This method, in the Microsoft Hardware API, updates details of a submission.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 04/05/2018
ms.localizationpriority: medium
---

# Update submission data 

Use this method in the Microsoft Hardware API to update details of a submission. Prior to using this method ensure you have created a submission. For details, see [create a new submission](create-a-new-hardware-submission.md).


## Prerequisites
If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

## Request
This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

| Method | Request URI |
|:--|:--|
| PATCH | `https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}/submissions/{submissionId}`

### Request header

| Header | Type | Description |
|:--|:--|:--|
|Authorization | String | Required. The Azure AD access token in the form **Bearer** \<token\>. |
| accept | String |	Optional. Specifies the type of content. Allowed value is “application/json” |

### Request parameters

Do not provide request parameters for this method.

### Request body

The following example demonstrates the JSON request body for updating a product. Only name change can be made to a submission.

```json
{
  "name": "updatedSubmissionName"
}
```

For details on the fields in the request, refer to [Submission resource](get-product-data.md#submission-resource).

### Request examples
The following example demonstrates how to update a product.

```json 
PATCH https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14631253285588838/submissions/1152921504627422408 HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The response will be empty with a HTTP status of 204.

After this step, use the method [get submission details](get-a-submission.md) to get the updated details of the product.

## Error codes
Refer to [Error codes](get-product-data.md#error-codes) for details.

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
