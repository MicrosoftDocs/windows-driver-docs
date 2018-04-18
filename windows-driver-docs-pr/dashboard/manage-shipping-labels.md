---
title: Manage Shipping Labels
description: This document gives information about how to create or update shipping labels
author: balapv
ms.author: balapv
ms.date: 04/12/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---
# Manage Shipping Labels

Use the following methods in *Microsoft Hardware APIs* to manage shipping lables for your submissions. For an introduction to Microsoft Hardware APIs, including prerequisites for using the API, see [Manage hardware submissions using APIs](dashboard-api.md).

```
https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productid}/submissions/{submissionid}/shippingLabels
```

Methods for managing shipping labels

| Method | URI | Description |
|:--|:--|:--|
|POST|`https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productid}/submissions/{submissionid}/shippingLabels`|[Create a new shipping label](create-a-new-shipping-label.md)|
|PATCH|`https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productid}/submissions/{submissionid}/shippingLabels/{shippingLabelId}`|Update a shipping label - **<font color="red">link TBD</font>**|

##Create a new shipping label

1.	If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs.

2.	[Obtain an Azure AD access token](dashboard-api.md#obtain-an-azure-ad-access-token). You must pass this access token to the methods in the Microsoft Store submission API. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can obtain a new one.

3.	You should have created a product and submission in order to create a shipping label. Refer [manage product submissions](manage-product-submissions.md) for details on how to create a product and submission.

4.  [Create a new shipping label](create-a-new-shipping-label.md) for this submission by executing the following method in the Microsoft Hardware API.  Use the ProductID and SubmissionID created in the step above.
    
    ```
    https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productid}/submissions/{submissionid}/shippingLabels
    ```
    
    The response body contains a [shipping label resource](get-shipping-labels.md#shippinglabel-resource) which includes the ID for the newly created shipping label and other details.

## Code examples

The following code examples demonstrates how to use the Microsoft Hardware API:

* [C# sample](http://download.microsoft.com/download/C/F/4/CF404E53-87A0-4204-BA13-A64B09A237C1/HardwareApiCSharpSample.zip) **<font color="red">TBD</font>** - add sample for shipping labels

##Data resources

The Microsoft Hardware APIs to create and update shipping labels use the following JSON data resources:

*   [Shipping Label Resource](get-shipping-labels.md#shippinglabel-resource)

## Error codes

See [Error codes](get-product-data.md#error-codes)