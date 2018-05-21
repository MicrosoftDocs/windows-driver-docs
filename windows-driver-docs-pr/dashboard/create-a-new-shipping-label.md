---
title: Create a new shipping label
description: Use this method in the Microsoft Hardware API to create a new shipping label.
author: balapv
ms.author: balapv
ms.date: 04/12/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
    "restrictedToAudience": "00000000-0000-0000-0000-000000000000"
  },
  "name": "Shipping Label Name",
  "destination": "windowsUpdate"
}
```
For details about the fields in the request, refer to [shipping label resource](get-shipping-labels.md#shippinglabel-resource). 

#### Few points to remember when creating shipping labels:

*   When publishing to Windows Update (*destination* is **windowsUpdate**)

    -  The [publishingSpecifications](get-shipping-labels.md#publishing-specifications-object) is required

    -  For automatic installs (*isAutoInstallDuringOSUpgrade* or *isAutoInstallOnApplicableSystems* is true), the *additionalInfoForMsApproval* is required

*   When sharing with other partners  (*destination* is **anotherPartner**)

    -  The [recipientSpecifications](get-shipping-labels.md#recipient-specifications-object) is required

#### Populating targeting information

The targeting object contains data which instructs Windows Update how the driver should be targeted in terms of hardware IDs and whether CHID or restrictions should be applied. The hardware ID object should contain a valid combination of bundle ID, PNP ID, OS Code and INF name while creating a new shipping label. To get the allowed/valid combinations of these attributes for your submission (package), you can download the driver metadata file which is provided as a link when you get details of a submission. For more information refer to [driver package metadata](driver-package-metadata.md).

### Request examples

The following example demonstrates how to create a new product.

```
POST https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}/submissions/{submissionId}/shippingLabels HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for creating a shipping label. For more details about the values in the response body, see the following section.

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

Refer to [shipping label resource](get-shipping-labels.md#shippinglabel-resource) for more details

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes).