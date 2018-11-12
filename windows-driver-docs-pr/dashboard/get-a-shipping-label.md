---
title: Get a shipping label
description: These methods from the Microsoft Hardware APIs get data for shipping labels of hardware products registered to your Hardware dev center Account.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 08/21/2018
---

# Get a shipping label

Use this method to retrieve data for a specific shipping label of a specific submission of a product.

## Prerequisites

If you have not done so already, complete all the [Prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods. Before you can use these methods, the product and submission must already exist in your Dev Center account. To create or manage submissions for products, see the methods in [Manage product submissions](manage-product-submissions.md).

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

|Method|Request URI|
|--|--|
|GET|`https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productId}/submissions/{submissionId}/shippingLabels/{shippingLabelId}`|

### Request header

| Header | Type | Description |
|:--|:--|:--|
| authorization | string | Required. The Azure AD access token in the form **Bearer** \*<token\>*. |
| accept | string | Optional. Specifies the type of content. Allowed value is “application/json” |

### Request parameters

Request parameters are optional for this method.

|Name|Type|Description|
|:--|:--|:--|
| includeTargetingInfo | boolean | Optional. If this parameter is set to true, the shipping label returns the targeting details of the shipping label, like hardware IDs and CHIDs. For more info, see [Targeting object](get-shipping-labels.md#targeting-object).|

### Request body

Do not provide a request body for this method.

### Request examples

The following example demonstrates how to retrieve information about a specific product registered to your account.

```cpp
GET https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964156/submissions/1152921504621467600/shippingLabels/1152921504606980300 HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for a specific shipping label. Details about the values in the response body appear in the table following the example.

```json
{
  "id": 1152921504606978300,
  "productId": 14461751976964156,
  "submissionId": 1152921504621467600,
  "publishingSpecifications": {
    "goLiveDate": "2018-04-12T05:28:32.721Z",
    "visibleToAccounts": [
      27691110,
      27691111
    ],
    "isAutoInstallDuringOSUpgrade": true,
    "isAutoInstallOnApplicableSystems": true,
    "isDisclosureRestricted": false,
    "publishToWindows10s": false,
    "additionalInfoForMsApproval": {
      "microsoftContact": "abc@mcirosoft.com",
      "validationsPerformed": "Validation 1",
      "affectedOems": [
        "OEM1",
        "OEM2"
      ],
      "isRebootRequired": false,
      "isCoEngineered": true,
      "isForUnreleasedHardware": true,
      "hasUiSoftware": false,
      "businessJustification": "This is a business justification"
    }
  },
  "targeting": {
    "hardwareIds": [
      {
        "bundleId": "amd64",
        "infId": "foo.inf",
        "operatingSystemCode": "WINDOWS_v100_SERVER_X64_RS4_FULL",
        "pnpString": "hid\\vid_dummy256f&pid_dummyc62f",
        "distributionState": "pendingAdd"
      },
      {
        "bundleId": "amd64",
        "infId": "foo.inf",
        "operatingSystemCode": "WINDOWS_v100_RS2_FULL",
        "pnpString": "hid\\vid_dummy256f&pid_dummyc62f",
        "distributionState": "pendingAdd"
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
    },
    "coEngDriverPublishInfo": {
      "flooringBuildNumber": 17135,
      "ceilingBuildNumber": 17139
    }
  },
  "workflowStatus": {
    "currentStep": "microsoftApproval",
    "state": "started",
    "messages": []
  },
  "links": [
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606978459",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606978459",
      "rel": "update_shippinglabel",
      "method": "PATCH"
    }
  ],
  "name": "VR_RS4Build_DualPublishCheck",
  "destination": "windowsUpdate"
}
```
### Response body

For details about the response body, see [ShippingLabel resource](get-shipping-labels.md#shippinglabel-resource).

## Error codes

For info about error codes, see [Error codes](get-product-data.md#error-codes).

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
