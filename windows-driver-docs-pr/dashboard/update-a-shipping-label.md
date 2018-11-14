---
title: Update a shipping label
description: This method updates a shipping label in the Hardware dashboard API.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 08/21/2018
---

# Update a shipping label

Use this method in the *Microsoft Hardware API* to update a shipping label. Before using this method, make sure you have already created a shipping label. For more info about creating a shipping label, see [Create a new shipping label](create-a-new-shipping-label.md).

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before using any of these methods.

## Request

This method has the following syntax. The other sections in this topic provide usage examples and descriptions of the header and request body.

| Method | Request URI |
|:--|:--|
| PATCH | `https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}/submissions/{submissionId}/shippingLabels/{shippingLabelId}` |

The *productID*, *submissionID* and *shippingLabelId* in the method represent the product, submission and shipping label to be updated.

### Request header

| Header | Type | Description |
|:--|:--|:--|
| Authorization | String | Required. The Azure AD access token in the form **Bearer** \<token\>. |
| Accept | String | Optional. Specifies the type of content. Allowed value is “application/json” |

### Request parameters

Do not provide request parameters for this method. 

### Request body

The following example demonstrates the JSON request body a shipping label. Only the following types of changes can be made to a shipping label:

* Add hardware IDs
* Remove/expire hardware IDs
* Add CHIDs
* Remove CHIDs
* Add audience
* Update/remove audience
* Provide Business Justification for the changes

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
        "infId": "foo.inf",
        "operatingSystemCode": "WINDOWS_v100_X64_RS3_FULL",
        "pnpString": "pci\\ven_8086&dev_5a85"
      },
      {
        "action": "add",
        "bundleId": "48140805-45a3-4a76-8818-e75c117adba9",
        "infId": "foo.inf",
        "operatingSystemCode": "WINDOWS_v100_X64_RS3_FULL",
        "pnpString": "pci\\ven_8086&dev_5a85"
      }
    ],
    "restrictedToAudiences": [
      "00000000-0000-0000-0000-000000000000",
      "00000000-0000-0000-0000-000000000001"
      ],
    "inServicePublishInfo": {
      "flooring": "RS1",
      "ceiling": "RS3"
    },
    "businessJustification": "Business justification for updating shipping label"
  }
}
```

For details about the fields in the request, see [ShippingLabel resource](get-shipping-labels.md#shippinglabel-resource).

Points to note:

* You must provide a value for *action* when updating CHIDs or HardwareIDs.

* *Audience* is an update-only field. Providing a value in this field overwrites any previous value. Leaving the value blank removes the previous value.

* To learn how to get a list of audiences for your organization, see [get audience](get-audience-data.md).

* The hardware ID object should contain a valid combination of bundle ID, PNP ID, OS Code, and INF name when creating a new shipping label. To get the valid, allowed combinations of these attributes for your submission (package), download the driver metadata file (provided as a link) when you get the details of a submission. For details, see [Driver package metadata](driver-package-metadata.md).

### Request examples

The following example demonstrates how to update a product.

```json
PATCH https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964156/submissions/1152921504621467600/shippingLabels/1152921504606980300 HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The response will be empty with a HTTP status of 204.

After this step, use the method in [Get a shipping label](get-a-shipping-label.md) to get the updated details of the shipping label.

## Error codes

For more info about error codes, see [Error codes](get-product-data.md#error-codes).

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
