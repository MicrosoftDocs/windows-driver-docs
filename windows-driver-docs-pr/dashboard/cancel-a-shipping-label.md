---
title: Cancel a shipping label
description: Use this method in the Microsoft Hardware API to request cancellation of a shipping label in Microsoft Approval or Gradual Rollout.
ms.topic: article
ms.date: 11/13/2019
---

# Cancel a shipping label

Use this method in the *Microsoft Hardware API* to request cancellation of a shipping label in Microsoft Approval or Gradual Rollout. Before using this method, make sure your shipping label is in Microsoft Approval or Gradual Rollout. For more info about getting a shipping label, see [Get a new shipping label](get-a-shipping-label.md).

> [!NOTE]
> You cannot cancel a shared shipping label. However, you can revoke sharing after the workflow has completed.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before using this method.

## Request

This method has the following syntax. The other sections in this topic provide usage examples and descriptions of the header and request body.

| Method | Request URI |
|:--|:--|
| PUT | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionId}/shippingLabels/{shippingLabelId}/cancel` |

The *productID*, *submissionID* and *shippingLabelId* in the method represent the product, submission and shipping label for cancellation.

### Request header

| Header | Type | Description |
|:--|:--|:--|
| Authorization | String | Required. The Azure Entra Identity access token in the form **Bearer** \<token\>. |
| Accept | String | Optional. Specifies the type of content. Allowed value is “application/json” |

### Request parameters

Do not provide request parameters for this method.

### Request body

Do not provide request body for this method.

### Request examples

The following example demonstrates how to request cancellation of a shipping label.

```json
PUT https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/14461751976964156/submissions/1152921504621467600/shippingLabels/1152921504606980300/cancel HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The response will be empty with a HTTP status of 204.

After this step, use the method in [Get a shipping label](get-a-shipping-label.md) to get the updated details of the shipping label. Please note that actual cancellation of the driver in the driver flighting systems may take over a day to complete.

## Error codes

For more info about error codes, see [Error codes](get-product-data.md#error-codes).

## See also

- [hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
