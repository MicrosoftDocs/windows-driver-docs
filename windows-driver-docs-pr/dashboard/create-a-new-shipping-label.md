---
title: Create a new shipping label
description: This method shows how to create a new shipping label in the Microsoft Hardware API.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 08/21/2018
---

# Create a new shipping label

Use this method in the *Microsoft Hardware API* to create a new shipping label. Prior to using this ensure you have created a product and created a submission for that product. For details, refer [create a product](create-a-new-product.md) and [create a submission](create-a-new-submission-for-a-product.md).

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md)  for the Microsoft Hardware APIs before trying to use any of these methods.

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

| Method | Request URI |
|:--|:--|
| POST | `https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}/submissions/{submissionId}/shippingLabels` | 

The productID and submissionID in the method represent the submission for which the shipping label is to be created.

### Request header

| Header | Type | Description |
|:--|:--|:--|
| Authorization | String | Required. The Azure AD access token in the form **Bearer** \<token\>. |
| Accept | String | Optional. Specifies the type of content. Allowed value is “application/json” |


### Request parameters

Do not provide request parameters for this method. 

### Request body

The following example demonstrates the JSON request body for creating a new shipping label.

```json
{
  "publishingSpecifications": {
    "goLiveDate": "2018-02-22T06:50:54.793Z",
    "visibleToAccounts": [
      27691110,
      27691111
    ],
    "isAutoInstallDuringOSUpgrade": true,
    "isAutoInstallOnApplicableSystems": false,
    "isDisclosureRestricted": false,
    "publishToWindows10s": true,
    "additionalInfoForMsApproval": {
      "microsoftContact": "abc@microsoft.com",
      "validationsPerformed": "Validation 1",
      "affectedOems": [
        "OEM1",
        "OEM2"
      ],
      "isRebootRequired": false,
      "isCoEngineered": false,
      "isForUnreleasedHardware": false,
      "hasUiSoftware": false,
      "businessJustification": "This is a business justification"
    }
  },
  "targeting": {
    "hardwareIds": [
      {
        "bundleId": "3aba7558-10ca-42db-b1d1-57af5718aea3",
        "infId": "foo.inf",
        "operatingSystemCode": "WINDOWS_v100_RS3_FULL",
        "pnpString": "hid\\vid_dummy256f&pid_dummyc62f"
      }
    ],
    "chids": [
      {
        "chid": "346511cf-ccee-5c6d-8ee9-3c70fc7aae83",
        "distributionState": "pendingAdd"
      }
    ],
    "restrictedToAudiences": [
      "00000000-0000-0000-0000-000000000000",
      "00000000-0000-0000-0000-000000000001"
      ],
    "inServicePublishInfo": {
      "flooring": "RS1",
      "ceiling": "RS3"
    }
  },
  "name": "Shipping Label Name",
  "destination": "windowsUpdate"
}
```

For details about the fields in the request, see [ShippingLabel resource](get-shipping-labels.md#shippinglabel-resource).

#### Points to remember when creating shipping labels

- When publishing to Windows Update (*destination* is **windowsUpdate**), you must include a [publishingSpecifications](get-shipping-labels.md#publishing-specifications-object) object. For automatic installs (*isAutoInstallDuringOSUpgrade* or *isAutoInstallOnApplicableSystems* is true), you must set  *additionalInfoForMsApproval*.

- When sharing with other partners  (*destination* is **anotherPartner**), you must include the [recipientSpecifications](get-shipping-labels.md#recipient-specifications-object) object.

#### Populating targeting information

The **targeting** object contains data that instructs Windows Update about:

- How the driver should be targeted in terms of hardware IDs.

- Whether CHID or restrictions should be applied.

The hardware ID object should contain a valid combination of bundle ID, PNP ID, OS Code, and INF name when creating a new shipping label. Download the driver metadata file (provided as a link when you get details of a submission) to get the allowed, valid combinations of these attributes for your submission. For more info, see [driver package metadata](driver-package-metadata.md).

### Request examples

The following example demonstrates how to create a new product.

```cpp
POST https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}/submissions/{submissionId}/shippingLabels HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for creating a shipping label. Details about the values in the response body appear in the table following the example.

```json
{
  "id": 1152921504606997500,
  "productId": 14461751976964156,
  "submissionId": 1152921504621467600,
  "publishingSpecifications": {
    "goLiveDate": "2018-02-22T06:50:54.793+00:00",
    "visibleToAccounts": [
      27691110,
      27691111
    ],
    "isAutoInstallDuringOSUpgrade": true,
    "isAutoInstallOnApplicableSystems": false,
    "isDisclosureRestricted": false,
    "publishToWindows10s": true,
    "additionalInfoForMsApproval": {
      "microsoftContact": "abc@microsoft.com",
      "validationsPerformed": "Validation 1",
      "affectedOems": [
        "OEM1",
        "OEM2"
      ],
      "isRebootRequired": false,
      "isCoEngineered": false,
      "isForUnreleasedHardware": false,
      "hasUiSoftware": false,
      "businessJustification": "This is a business justification"
    }
  },
  "workflowStatus": {
    "currentStep": "preProcessShippingLabel",
    "state": "notStarted",
    "messages": []
  },
  "links": [
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606997603",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606997603",
      "rel": "update_shippinglabel",
      "method": "PATCH"
    }
  ],
  "name": "Shipping Label Name",
  "destination": "windowsUpdate"
}
```

### Response body

For details about the response body, see [shipping label resource](get-shipping-labels.md#shippinglabel-resource).

## Error codes

For info about error codes, see [Error codes](get-product-data.md#error-codes).

## See also

[Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
