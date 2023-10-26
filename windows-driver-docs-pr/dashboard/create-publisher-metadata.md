---
title: Create Publisher Driver Metadata
description: Describes the API call to create publisher driver package metadata for Partner Center submissions.
ms.topic: article
ms.date: 11/06/2019
---

# Create Publisher Driver Metadata

Use this method in the Microsoft Hardware API to create the Publisher Driver Metadata for a submission that was shared with you. Publisher driver metadata cannot be created for inbox or system submissions. To learn more about the driver metadata package please see the [Driver package metadata](driver-package-metadata.md) page.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

| Method | Request URI                                                                                                    |
|:-------|:---------------------------------------------------------------------------------------------------------------|
| POST   | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionID}/createpublishermetadata`|

### Request header

| Header | Type | Description |
|:--|:--|:--|
| Authorization | String | Required. The Microsoft Entra Identity access token in the form **Bearer** \<token\>. |
| accept | String | Optional. Specifies the type of content. Allowed value is “application/json” |

### Request parameters

Do not provide request parameters for this method.

### Request body

Do not provide request body for this method.

### Request examples

The following example demonstrates how to create publisher driver metadata for a submission.

```cpp
POST https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/14631253285588838/submissions/1152921504621465124/createpublishermetadata HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

### Response body

The response will be empty with a HTTP status of 202.

After this step, please allow for several hours to complete creation of publisher driver metadata. Then use the method [get submission details](get-a-submission.md) to get the link for the publisher driver metadata file.

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes).

## See also

[hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
