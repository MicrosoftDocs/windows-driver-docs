---
title: Get shipping label data
description: These methods from the Microsoft Hardware APIs get data for shipping labels of hardware products registered to your Dev Center Account.
author: balapv
ms.author: balapv
ms.date: 04/12/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---
# Get shipping label data

Use the following methods in *Microsoft Hardware APIs* to get data for shipping labels of hardware products registered to your Dev Center Account. For an introduction to Microsoft Hardware APIs, including prerequisites for using the API, see [Manage hardware submissions using APIs](dashboard-api.md).

```
https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productId}/submissions/{submissionId}/shippingLabels/
```

Before you can use these methods, the product and submission must already exist in your Dev Center account. To create or manage submissions for products, see the methods in [Manage product submissions](manage-product-submissions.md).

| Method | URI | Description |
|-|-|-|
|GET |	`https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productId}/submissions/{submissionId}/shippingLabels/`	|[Get data for all shipping labels of a submission](get-all-shipping-labels.md)|
|GET |	`https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productId}/submissions/{submissionId}/shippingLabels/{shippingLabelId}`	|[Get data for a specific shipping label of a submission](get-a-shipping-label.md)|

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

## Data resources

The Microsoft Hardware APIs methods for getting shipping label  data use the following JSON data resources

### ShippingLabel resource

This resource represents a shipping label created for a submission of your product that is registered to your account.

```json
{
  "id": 1152921504606978422,
  "productId": 14461751976964157,
  "submissionId": 1152921504621467613,
  "publishingSpecifications": {
    "goLiveDate": "2018-04-12T05:28:32.721Z",
    "visibleToAccounts": [
      27691110, 27691111
    ],
    "isAutoInstallDuringOSUpgrade": true,
    "isAutoInstallOnApplicableSystems": true,
    "isDisclosureRestricted": false,
    "publishToWindows10s": false,
    "additionalInfoForMsApproval": {
      "microsoftContact": "abc@mcirosoft.com",
      "validationsPerformed": "Validation 1",
      "affectedOems": [
        "OEM1", "OEM2"
      ],
      "isRebootRequired": false,
      "isCoEngineered": true,
      "isForUnreleasedHardware": true,
      "hasUiSoftware": false,
      "businessJustification": "This is a business justification"
    }
  },
  "recipientSpecifications": {
    "receiverPublisherId": "27691110",
    "enforceChidTargeting": true
  },
  "targeting": {
    "hardwareIds": [
      {
        "bundleId": "amd64",
        "infId": "foo.inf",
        "operatingSystemCode": "WINDOWS_v100_SERVER_X64_RS4_FULL",
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
    "restrictedToAudience": "00000000-0000-0000-0000-000000000000"
  },
  "workflowStatus": {
    "currentStep": "finalizePublishing",
    "state": "completed",
    "messages": [],
    "errorReport": ""
  },
  "links": [
    {
      "href": "https://manage.devcenter.microsoft.com/api/v1/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606978422",
      "rel": "self",
      "method": "GET"
    }
  ],
  "name": "Shipping Label Name",
  "destination": "windowsUpdate"
}
```
This resource has the following values

| Value | Type | Description |
|:--|:--|:--|
|id|long|The ID of the shipping label|
|productId|long|The private product ID to which this shipping label is associated|
|submissionId|long|The submission ID to which this shipping label is associated|
|publishingSpecifications|object|Refer [publishing specifications object](#publishing-specifications-object) for more details|
|recipientSpecifications|array of objects|Refer [recipient specifications object](#recipient-specifications-object) for more details|
|targeting|object|Refer [targeting object](#targeting-object) for more details|
|workflowStatus|object|This object depicts the status of the workflow for this submission. Refer [workflow status object](get-product-data.md#workflow-status-object)  for more details - TBD need to add morew status to Workflow object|
|links|array of objects|Refer [link object](get-product-data.md#link-object)  for more details - TBD need to add more links for SL|
|name|string|The name of the shipping label|
|destination|string|Indicates the destination of the shipping label. Possible values are(description in parenthesis): <ul><li>anotherPartner (*this shipping label is for sharing the submission with another partner*)</li><li>windowsUpdate (*this shipping label is for publishing to Windows Update*)</li><li>notSet</li></ul>|

### Publishing Specifications object

This object represents the specifications of how an object will be published to Windows Update. This object will be available/needed only when the *destination* of the shipping label is *windowsUpdate*

```json
{
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
}
```

This object has the following values

| Value | Type | Description |
|:--|:--|:--|
|goLiveDate|datetime|Date when you want your driver to be available for download on Windows Update. If no date is provided, it will be published immediately after certification|
|visibleToAccounts|array of long|List of SellerIDs who will have read-only permissions to the driver and shipping label. This information will be useful when you want a partner to be aware of this shipping label request, such as when you publish a driver on their behalf|
|isAutoInstallDuringOSUpgrade|boolean|Indicates whether driver will be delivered to applicable machines during an operating system upgrade|
|isAutoInstallOnApplicableSystems|boolean|Indicates whether driver will be automatically delivered to applicable machines|
|isDisclosureRestricted|boolean|Indicates whether the driver will/should be prevented from appearing in WSUS and the Windows Update Catalog.|
|publishToWindows10s|boolean|Inidcates whether this driver needs to be published to Windows 10 S|
|additionalInfoForMsApproval|object|Refer [additonal information object](#additional-information-for-microsoft-object) for details|

### Additional Information for Microsoft object

This object represents some additional information which is required by Microsoft to review the Shipping label. This object will be available/needed only when the *destination* of the shipping label is *windowsUpdate* and the shipping label is marked as *isAutoInstallDuringOSUpgrade* or *isAutoInstallOnApplicableSystems*.

```json
{
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
```
This object has the following values

| Value | Type | Description |
|:--|:--|:--|
|microsoftContact|string|Email address of the Microsoft sponsor working with you on this request|
|validationsPerformed|string|Description of how driver was validated. This information will be used by Microsoft during the review.|
|affectedOems|string|List of names of OEMs affected by this publication. This information will be used by Microsoft during the review.|
|isRebootRequired|boolean|Indicates whether is reboot required after installing this driver. This information will be used by Microsoft during the review.|
|isCoEngineered|boolean|Indicates whether the driver is a co-engineered driver working on active (unreleased) builds of Windows. This information will be used by Microsoft during the review.|
|isForUnreleasedHardware|boolean|Indicates whether the driver supports a new or unreleased device. This information will be used by Microsoft during the review.|
|hasUiSoftware|boolean|Indictaes whether the driver will deploy a UI and/or software? This information will be used by Microsoft during the review.|
|businessJustification|string|Business justification for promoting this publication request. This information will be used by Microsoft during the review.|

### Recipient specifications object

This object represents the details and conditions under which the submission is shared with another partner. This object will be available/needed only when the *destination* of the shipping label is *anotherPartner*.

```json
{
	"receiverPublisherId": "27691110",
	"enforceChidTargeting": false
}
```
This object has the following values

| Value | Type | Description |
|:--|:--|:--|
|receiverPublisherId|string|Seller ID with whom the driver is being shared. The recipients can download driver, publish to Windows Update, create DUA packages. Recipients cannot further share with other Partners.|
|enforceChidTargeting|boolean|Indicates whether partner is required to apply CHIDs to any shipping labels they create for this driver submission. This allows you to protect your users when a Hardware ID may be shared among many partner companies.|

### Targeting object

This object represents the targeting details of the shipping label which is required when published to Windows Update.

```json
{
  "hardwareIds": [
    {
      "bundleId": "amd64",
      "infId": "foo.inf",
      "operatingSystemCode": "WINDOWS_v100_SERVER_X64_RS4_FULL",
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
  "restrictedToAudience": "00000000-0000-0000-0000-000000000000"
}
```
This object has the following values

| Value | Type | Description |
|:--|:--|:--|
|hardwareIds|array of objects|Refer [hardware ID object](#hardware-id-object) for more details|
|chids|array of objects|Refer [CHID object](#chids-object) for more details|
|restrictedToAudience|GUID|GUID which represents an audience. Audiences allow you to restrict this publication to machines with a particular configuration. As an example, the test audience will only be delivered to clients with a particular registry key installed. TBD - how will users know list of available SSRKs?|

### Hardware ID object

This object represents the details of the hardware ID which needs to be targeted by the shipping label. Refer [hardware IDs](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/hardware-ids) for more details.

```json
{
	"bundleId": "amd64",
	"infId": "foo.inf",
	"operatingSystemCode": "WINDOWS_v100_SERVER_X64_RS4_FULL",
	"pnpString": "hid\\vid_dummy256f&pid_dummyc62f",
	"distributionState": "pendingAdd"
}
```
This object has the following values

| Value | Type | Description |
|:--|:--|:--|
|bundleId|string|The architecture for which this hardware ID - operating system is applicable. Possible values are <ul><li>tbd</li><li>tbd</li><li>tbd</li></ul>|
|infId|string|The name of the inf file which contains this hardware ID|
|operatingSystemCode|string|The operating system applicable for this specific hardware ID - architecture combination. Refer [list of OS codes](get-product-data.md#list-of-operating-system-codes) for possible values.|
|pnpString|string|The hardware ID which is to be targeted.|
|distributionState|string|Represents the current targeting status of this hardware ID. Possible values are (description in paranthesis):<ul><li>pendingAdd (*Add has been requested for this hardware ID and is in progress*)</li><li>pendingRemove (*A remove (expire) has been requested for this hardware ID and is in progress*)</li><li>added (*This hardware ID has been succesfully added as target in this shipping label*)</li><li>notSet (*No action has been taken or status has not been set on this hardware ID*)</li></ul>|


### CHIDs object

This object represents the CHID (computer hardware ID) which needs to be targeted by the shipping label. Refer [using CHIDs](https://docs.microsoft.com/en-us/windows-hardware/drivers/dashboard/using-chids) for more details.
```json
{
	"chid": "346511cf-ccee-5c6d-8ee9-3c70fc7aae83",
	"distributionState": "pendingAdd"
}
```
This object has the following values

| Value | Type | Description |
|:--|:--|:--|
|chid|GUID|The CHID which needs to be targeted|
|distributionState|string|Represents the current targeting status of this CHID. Possible values are (description in paranthesis):<ul><li>pendingAdd (*Add has been requested for this hardware ID and is in progress*)</li><li>pendingRemove (*A remove (expire) has been requested for this hardware ID and is in progress*)</li><li>added (*This hardware ID has been succesfully added as target in this shipping label*)</li><li>notSet (*No action has been taken or status has not been set on this hardware ID*)</li></ul>|

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes). TBD - need to add SL error codes