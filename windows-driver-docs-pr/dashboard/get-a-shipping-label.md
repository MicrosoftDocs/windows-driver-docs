---
title: Get a specific shipping labels for a submission
description: These methods from the Microsoft Hardware APIs get data for shipping labels of hardware products registered to your Dev Center Account.
author: balapv
ms.author: balapv
ms.date: 04/13/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Get a shipping label

Use this method in the *Microsoft Hardware API* to retrieve data for a specific shipping label of a specific submission of a product.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods. Before you can use these methods, the product and submission must already exist in your Dev Center account. To create or manage submissions for products, see the methods in [Manage product submissions](manage-product-submissions.md).

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

|Method|Request URI|
|--|--|
|GET|`https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productId}/submissions/{submissionId}/shippingLabels/{shippingLabelId}`|

### Request header

| Header | Type | Description |
|:--|:--|:--|
| authorization | string | Required. The Azure AD access token in the form **Bearer** \<token\>. |
| accept | string | Optional. Specifies the type of content. Allowed value is “application/json” |


### Request parameters

Request parameters are optional for this method.

|Name|Type|Description|
|:--|:--|:--|
| includeTargetingInfo | boolean | Optional. If this parameter is set to true, the shipping label returns the targeting details of the shipping label like hardware IDs and CHIDs. Refer [targeting object](get-shipping-lables.md#targeting-object) for more deatils |

### Request body

Do not provide a request body for this method.