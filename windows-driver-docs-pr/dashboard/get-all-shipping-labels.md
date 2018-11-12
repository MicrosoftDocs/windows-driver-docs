---
title: Get all shipping labels for a submission
description: These methods from the Microsoft Hardware APIs get data for shipping labels of hardware products registered to your Hardware dashboard Account.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 08/21/2018
---

# Get all shipping labels

Use this method in the *Microsoft Hardware API* to retrieve data for all the shipping labels of a specific submission of a product.

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods. Before you can use these methods, the product and submission must already exist in your Dev Center account. To create or manage submissions for products, see the methods in [Manage product submissions](manage-product-submissions.md).

## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

|Method|Request URI|
|--|--|
|GET|`https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productId}/submissions/{submissionId}/shippingLabels/`|

### Request header

|Header|Type|Description|
|--|--|--|
|Authorization|string|Required. The Azure AD access token in the form **Bearer** \*<token\>*.|
|accept|string|Optional. Specifies the type of content. Allowed value is “application/json”|

### Request parameters

Do not provide request parameters for this method.

### Request body

Do not provide a request body for this method.

### Request examples

The following example demonstrates how to retrieve information about all products that are registered to your account.

```cpp
GET https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/ HTTP/1.1
Authorization: Bearer <your access token>
```
## Response

The following example demonstrates the JSON response body returned by a successful request for all the shipping labels of a specific submission of a product that is registered to your developer account. For brevity, this example only shows the data for the first three shipping labels returned by the request. Details about the values in the response body appear in the table following the example.

```json
{
  "value": [
    {
      "id": 1152921504606980300,
      "productId": 14461751976964156,
      "submissionId": 1152921504621467600,
      "publishingSpecifications": {
        "goLiveDate": "2018-04-04T16:11:27.2965057+00:00",
        "visibleToAccounts": [],
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
      "workflowStatus": {
        "currentStep": "microsoftApproval",
        "state": "started",
        "messages": []
      },
      "links": [
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606980231",
          "rel": "self",
          "method": "GET"
        },
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606980231",
          "rel": "update_shippinglabel",
          "method": "PATCH"
        }
      ],
      "name": "Publish to Windows Update with promotions",
      "destination": "windowsUpdate"
    },
    {
      "id": 1152921504606978500,
      "productId": 14461751976964156,
      "submissionId": 1152921504621467600,
      "recipientSpecifications": {
        "receiverPublisherId": "27691110",
        "enforceChidTargeting": false
      },
      "workflowStatus": {
        "currentStep": "finalizeSharing",
        "state": "completed",
        "messages": []
      },
      "links": [
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606978460",
          "rel": "self",
          "method": "GET"
        },
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606978460",
          "rel": "update_shippinglabel",
          "method": "PATCH"
        }
      ],
      "name": "Share submission with another Partner",
      "destination": "anotherPartner"
    },
    {
      "id": 1152921504606978500,
      "productId": 14461751976964156,
      "submissionId": 1152921504621467600,
      "publishingSpecifications": {
        "goLiveDate": "2018-04-03T04:50:52.2293001+00:00",
        "visibleToAccounts": [],
        "isAutoInstallDuringOSUpgrade": false,
        "isAutoInstallOnApplicableSystems": false,
        "isDisclosureRestricted": false,
        "publishToWindows10s": false
      },
      "workflowStatus": {
        "currentStep": "finalizePublishing",
        "state": "completed",
        "messages": []
      },
      "links": [
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606978538",
          "rel": "self",
          "method": "GET"
        },
        {
          "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606978538",
          "rel": "update_shippinglabel",
          "method": "PATCH"
        }
      ],
      "name": "Publish to Windows Update without promotions",
      "destination": "windowsUpdate"
    }
  ],
  "links": [
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products?pageSize=50",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```
This resource has the following values

| Value | Type | Description |
|:--|:--|:--|
| value | array | An array of objects that contain information about each shipping label. For more information about the data in each object, see [Shipping label resource](get-shipping-labels.md#shippinglabel-resource). |
| links | array | An array of objects with helpful links about the containing entity. See [Link object](get-product-data.md#link-object)  for more details.|

## Error codes

For info, about error codes, see [Error codes](get-product-data.md#error-codes).

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
