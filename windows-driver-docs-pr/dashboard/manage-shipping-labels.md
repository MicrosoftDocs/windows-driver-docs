---
title: Manage Shipping Labels
description: This document contains information about how to create or update shipping labels for driver submission in the hardware dashboard
ms.topic: article
ms.date: 08/23/2018
---
# Manage Shipping Labels

Use the following methods to manage shipping labels for your Windows hardware dashboard submissions. For an introduction to the Microsoft hardware dashboard APIs, including the prerequisites for using the API, see [hardware dashboard API](dashboard-api.md).

```cpp
https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productid}/submissions/{submissionid}/shippingLabels
```

Methods for managing shipping labels

|Description|Method |URI|
|:--|:--|:--|
|[Create a new shipping label](create-a-new-shipping-label.md)|POST|`https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productid}/submissions/{submissionid}/shippingLabels`|
|[Update a shipping label](update-a-shipping-label.md)|PATCH|`https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productid}/submissions/{submissionid}/shippingLabels/{shippingLabelId}`|
|[Cancel a shipping label](cancel-a-shipping-label.md)|PUT|`https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productid}/submissions/{submissionid}/shippingLabels/{shippingLabelId/cancel}`|

## Create a new shipping label

1. If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs.

2. [Obtain an Microsoft Entra Identity access token](dashboard-api.md#obtain-an-microsoft-entra-identity-access-token). You must pass this access token to the methods in the Microsoft Store submission API. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can obtain a new one.

3. You should have created a product and submission in order to create a shipping label. See [Manage product submissions](manage-product-submissions.md) for details about creating a product and submission.

4. [Create a new shipping label](create-a-new-shipping-label.md) for this submission by executing the following method.  Use the ProductID and SubmissionID created in [Manage product submissions](manage-product-submissions.md) during the previous step.

    ```cpp
    https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productid}/submissions/{submissionid}/shippingLabels
    ```
    The response body contains a [shipping label resource](get-shipping-labels.md#shippinglabel-resource) which includes the ID for the newly created shipping label and other details.

## Code examples

The following code example demonstrates how to use the Microsoft Hardware API:

* [C# sample](https://download.microsoft.com/download/C/F/4/CF404E53-87A0-4204-BA13-A64B09A237C1/HardwareApiCSharpSample.zip)

## Data resources

The Microsoft Hardware APIs methods for creating and managing product data use the following JSON data resource:

* [Shipping Label Resource](get-shipping-labels.md#shippinglabel-resource)

## Error codes

For info about error codes, see [Error codes](get-product-data.md#error-codes).

## See also

- [hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
