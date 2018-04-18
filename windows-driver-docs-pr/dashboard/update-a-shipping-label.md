---
title: Update a shipping label
description: Use this method in the Microsoft Hardware API to update shipping label.
author: balapv
ms.author: balapv
ms.date: 04/12/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Update a shipping label

Use this method in the *Microsoft Hardware API* to create a new shipping label. Prior to using this ensure you have created a shipping label. For details, refer [create a new shipping label](create-a-new-shipping-label.md).

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md)  for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

| Method | Request URI |
|:--|:--|
| PATCH | `https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/{productID}/submissions/{submissionId}/shippingLabels/{shippingLabelId}` | 

The productID, submissionID and shippingLabelId in the method represent the product, submission and shipping label which needs to be updated.

### Request header

| Header | Type | Description |
|:--|:--|:--|
| Authorization | String | Required. The Azure AD access token in the form **Bearer** \<token\>. |
| Accept | String | Optional. Specifies the type of content. Allowed value is “application/json” |


### Request parameters

Do not provide request parameters for this method. 

### Request body

The following example demonstrates the JSON request body a shipping label. Only the following types of changes can be made to a shipping label
*   Add hardware IDs
*   Remove/expire hardware IDs
*   Add CHIDs
*   Remove CHIDs
*   Add audience
*   Update/remove audience

```json 
{
  "targetingInfo": {
    "chids": [
      {
        "chid": "812fac65-9c26-473c-b3a9-1eb3803ac22c",
        "action": "add"
      },
      {
        "chid": "aed6336d-0958-444c-89b6-bf471191d6f0",
        "action": "remove"
      }
    ],
    "hardwareIds": [
      {
        "action": "remove",
        "bundleId": "a2dfbcd8-1d4a-4885-90a3-2ac8360542da",
        "infId": "iigd_extension.inf",
        "operatingSystemCode": "WINDOWS_v100_X64_RS3_FULL",
        "pnpString": "pci\\ven_8086&dev_5a85"
      },
      {
        "action": "add",
        "bundleId": "48140805-45a3-4a76-8818-e75c117adba9",
        "infId": "iigd_extension.inf",
        "operatingSystemCode": "WINDOWS_v100_X64_RS3_FULL",
        "pnpString": "pci\\ven_8086&dev_5a85"
      }
    ],
    "audience": "812fac65-9c26-473c-b3a9-1eb3803ac22c"
  }
}
```