---
title: Commit a product submission
description: Use this method in the Microsoft Hardware API to commit a new submission to the Partner Center.
ms.date: 04/05/2018
ms.topic: article
---

# Commit a product submission

Use this method in the Microsoft Hardware API to commit a new submission to the Partner Center. This will alert Partner Center that you are done with your product submission and validation will be started for the submission.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

Another prerequisite to commit a submission is to complete the upload of the driver package to the SAS URI provided while [creating a new submission](create-a-new-submission-for-a-product.md) . For more information about how the commit operation fits into the process of submitting a product app by using the Microsoft Hardware API, see [manage product submissions](manage-product-submissions.md) .

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

| Method | Request URI                                                                                                    |
|:-------|:---------------------------------------------------------------------------------------------------------------|
| POST   | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionID}/commit`|

The productId in the method is the product for which the submission is intended. The submssionID in the method is the submission which is being committed.

### Request header

| Header | Type | Description |
|:--|:--|:--|
| Authorization | String | Required. The Microsoft Entra ID access token in the form **Bearer** \<token\>. |
| accept | String | Optional. Specifies the type of content. Allowed value is “application/json” |

In the headers, set `Content-Length: 0` and `Content-type: application/json`.

### Request parameters

Do not provide request parameters for this method.

### Request body

Do not provide request body for this method.

### Request examples

The following example demonstrates how to commit a submission.

```cpp
POST https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/14631253285588838/submissions/1152921504621465124/commit HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

A successful request for creating a new submission for a product returns an empty 202 response.

### Response body

| Value | Type | Description |
|:--|:--|:--|
| commitStatus | string | The status of the submission. The value returned would be CommitPending |

After this step, use the method [get submission details](get-a-submission.md)  to get the status of the submission.

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes).

## See also

[hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
