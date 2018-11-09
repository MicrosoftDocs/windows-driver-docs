---
title: Get shipping label data
description: These methods from the Microsoft Hardware APIs get data for shipping labels of hardware products registered to your Dev Center Account.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 08/21/2018
---
# Get shipping label data

For an introduction to Microsoft Hardware APIs, including prerequisites for using the API, see [Manage hardware submissions using APIs](dashboard-api.md).

Use the following methods in *Microsoft Hardware APIs* to get data for shipping labels of hardware products registered to your Hardware Dev Center Account.

```html
https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productId}/submissions/{submissionId}/shippingLabels/
```

Before you can use these methods, the product and submission must already exist in your Dev Center account. To create or manage submissions for products, see the methods in [Manage product submissions](manage-product-submissions.md).

|Description|Method|URI|
|-|-|-|
|[Get data for all shipping labels of a submission](get-all-shipping-labels.md)|GET|`https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productId}/submissions/{submissionId}/shippingLabels/`|
|[Get data for a specific shipping label of a submission](get-a-shipping-label.md)|GET|`https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productId}/submissions/{submissionId}/shippingLabels/{shippingLabelId}`|

## Prerequisites

If you have not done so already, complete all the [Prerequisites](https://docs.microsoft.com/windows-hardware/drivers/dashboard/dashboard-api#complete-prerequisites-for-using-the-microsoft-hardware-api) for the Microsoft Hardware APIs before trying to use any of these methods.

## Data resources

The Microsoft hardware dashboard API methods for getting shipping label  data use the following JSON data resources.

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
      "microsoftContact": "abc@microsoft.com",
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
    "currentStep": "finalizePublishing",
    "state": "completed",
    "messages": [],
    "errorReport": ""
  },
  "links": [
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14461751976964157/submissions/1152921504621467613/shippingLabels/1152921504606978422",
      "rel": "self",
      "method": "GET"
    }
  ],
  "name": "Shipping Label Name",
  "destination": "windowsUpdate"
}
```

This resource has the following values:

| Value | Type | Description |
|:--|:--|:--|
|id|long|The ID of the shipping label|
|productId|long|The private product ID to which this shipping label is associated|
|submissionId|long|The submission ID to which this shipping label is associated|
|publishingSpecifications|object|Refer [publishing specifications object](#publishing-specifications-object) for more details|
|recipientSpecifications|array of objects|Refer [recipient specifications object](#recipient-specifications-object) for more details|
|targeting|object|Refer [targeting object](#targeting-object) for more details|
|workflowStatus|object|This object depicts the status of the workflow for this shipping label. Refer [shipping label workflow status object](#shipping-label-workflow-status-object)  for more details|
|links|array of objects|For more info, see [link object](get-product-data.md#link-object).|
|name|string|The name of the shipping label|
|destination|string|Indicates the destination of the shipping label. Possible values are (description in parenthesis): <ul><li>anotherPartner (*this shipping label is for sharing the submission with another partner*)</li><li>windowsUpdate (*this shipping label is for publishing to Windows Update*)</li><li>notSet</li></ul>|

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
    "microsoftContact": "abc@microsoft.com",
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
|goLiveDate|datetime|Date for the driver to be available for download on Windows Update. If no date is provided, the driver is published immediately after certification.|
|visibleToAccounts|array of long|List of SellerIDs who will have read-only permissions to the driver and shipping label. This information is useful when you want a partner to be aware of a shipping label request, such as when you publish a driver on their behalf.|
|isAutoInstallDuringOSUpgrade|boolean|Whether the driver will be delivered to applicable machines during an operating system upgrade.|
|isAutoInstallOnApplicableSystems|boolean|Whether the driver will be automatically delivered to applicable machines.|
|isDisclosureRestricted|boolean|Whether the driver will/should be prevented from appearing in WSUS and the Windows Update Catalog.|
|publishToWindows10s|boolean|Whether the driver will be published to Windows 10 S|
|additionalInfoForMsApproval|object|For info, see [Additional information for the Microsoft object](#additional-information-for-the-microsoft-object).|

### Additional information for the Microsoft object

This object represents some additional information which is required by Microsoft to review the Shipping label. This object will be available/needed only when the *destination* of the shipping label is *windowsUpdate* and the shipping label is marked as *isAutoInstallDuringOSUpgrade* or *isAutoInstallOnApplicableSystems*.

```json
{
    "microsoftContact": "abc@microsoft.com",
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
|validationsPerformed|string|Description of how driver was validated. Microsoft uses this information during the review.|
|affectedOems|string|List of names of OEMs affected by this publication. This information will be used by Microsoft during the review.|
|isRebootRequired|boolean|Whether a reboot is required after installing the driver. Microsoft uses this information during the review.|
|isCoEngineered|boolean|Whether the driver is a co-engineered driver working on active (unreleased) builds of Windows. Microsoft uses this information during the review.|
|isForUnreleasedHardware|boolean|Whether the driver supports a new or unreleased device. Microsoft uses this information during the review.|
|hasUiSoftware|boolean|Whether the driver will deploy a UI and/or software? Microsoft uses this information during the review.|
|businessJustification|string|Business justification for promoting this publication request. Microsoft uses this information during the review.|

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
|enforceChidTargeting|boolean|Indicates whether a partner is required to apply CHIDs to any shipping labels they create for this driver submission. This allows you to protect your users when a Hardware ID may be shared among many partner companies.|

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
}
```
This object has the following values

| Value | Type | Description |
|:--|:--|:--|
|hardwareIds|array of objects|For more info, see [Hardware ID object](#hardware-id-object)|
|chids|array of objects|For more info, see [CHIDs object](#chids-object).|
|restrictedToAudiences|array of Strings|An array of strings which represents Audiences. Audiences allow you to restrict this publication to machines with a particular configuration. For example, a test audience will only be delivered to clients with a particular registry key installed. For info about identifying and managing the audiences applicable to your organization, see [Get audience data](get-audience-data.md).|
|inServicePublishInfo|object|Refer [in service publish information object](#in-service-publish-information-object) for more details. The targeting object can contain either inServicePublishInfo *or* coEngDriverPublishInfo, not both.|
|coEngDriverPublishInfo|object|Refer [co-engineering driver publish information object](#co-engineering-driver-publish-information-object) for more details. The targeting object can contain either inServicePublishInfo *or* coEngDriverPublishInfo, not both.|

### Hardware ID object

This object represents the details of the hardware ID which needs to be targeted by the shipping label. Refer [hardware IDs](https://docs.microsoft.com/windows-hardware/drivers/install/hardware-ids) for more details.

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
|bundleId|string|ID which represents the bundle in which the hardware ID is present.|
|infId|string|The name of the inf file which contains this hardware ID|
|operatingSystemCode|string|The operating system code applicable for this specific hardware ID - architecture combination. Refer [list of OS codes](get-product-data.md#list-of-operating-system-codes) for possible values.|
|pnpString|string|The PNP ID or hardware ID which is to be targeted.|
|distributionState|string|Represents the current targeting status of this hardware ID. Possible values are (description in paranthesis):<ul><li>pendingAdd (*Add has been requested for this hardware ID and is in progress*)</li><li>pendingRemove (*A remove (expire) has been requested for this hardware ID and is in progress*)</li><li>added (*This hardware ID has been succesfully added as target in this shipping label*)</li><li>notSet (*No action has been taken or status has not been set on this hardware ID*)</li></ul>|
|action|string|This is applicable only while Update/patch of a shipping label. The possible values are: <ul><li>add</li><li>remove</li></ul> |

The hardware ID object should contain a valid combination of bundle ID, PNP ID, OS Code and INF name while creating a new shipping label. To get the allowed/valid combinations of these attributes for your submission (package), you can download the driver metadata file which is provided as a link when you get details of a submission. For more information refer to [driver package metadata](driver-package-metadata.md).


### CHIDs object

This object represents the CHID (computer hardware ID) which needs to be targeted by the shipping label. Refer [using CHIDs](https://docs.microsoft.com/windows-hardware/drivers/dashboard/using-chids) for more details.
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
|action|string|This is applicable only while Update/patch of a shipping label. The possible values are: <ul><li>add</li><li>remove</li></ul> |

### In Service Publish Information object

This object represents distribution ranges which are defined by a floor and ceiling. A floor describes the earliest Windows version the driver will be distributed to, and a ceiling marks the latest. By adding a floor and ceiling, you can restrict your driver’s distribution.
```json
{
  "flooring": "RS1",
  "ceiling": "RS3",

}
```
This object has the following values

| Value | Type | Description |
|:--|:--|:--|
|flooring|string|Use this option when you want a driver to be offered only at and above the listed Windows 10 operating system. For example, selecting an RS4 flooring would mean only systems running Windows 10 1803 (RS4) and later will be offered this driver. Possible values are: <ul><li>TH</li><li>RS1</li><li>RS2</li><li>RS3</li><li>RS4</li><li>RS5</li></ul> Note that the possible values will expand to include the current version of the OS (which is RS5 at the time of this document)|
|ceiling|string|*Access to this feature is limited*. Use this option when you want a driver to be offered only for the listed operating system and earlier systems. For example, selecting an RS3 ceiling on a Windows 10 1607 RS1 certified driver would mean your driver would never be offered to systems running Windows 10 1803 (RS4) or above.Possible values are: <ul><li>TH</li><li>RS1</li><li>RS2</li><li>RS3</li><li>RS4</li><li>RS5</li></ul> Note that the possible values will expand to include the current version of the OS (which is RS5 at the time of this document)|

For more info about these values, see [Limiting driver distribution by Windows versions](https://docs.microsoft.com/windows-hardware/drivers/dashboard/limit-driver-distribution).

### Co-Engineering Driver Publish Information object

This object represents distribution ranges which are defined by a floor and ceiling when developing drivers for newer and unreleased versions of Windows. *This object is to available for Microsoft co-engineering partners only*. A floor describes the earliest Windows version the driver will be distributed to, and a ceiling marks the latest. By adding a floor and ceiling, you can restrict your driver’s distribution. 
```json
{
  "flooringBuildNumber": 17135,
  "ceilingBuildNumber": 17139
}
```
This object has the following values

| Value | Type | Description |
|:--|:--|:--|
|flooringBuildNumber|number|The build number of the release when you want a driver to only be offered at and above this build number. For example, if the floor needs to be 10.1.17135, the input needs to be 17135. The major version (10.1) always defaults to the appropriate version automatically.|
|ceiling|number|The build number of the release when you want a driver to only be offered at or below this build number. For example, if the ceiling needs to be 10.1.17139, the input needs to be 17139. The major version (10.1) always defaults to the appropriate version automatically.|

For more info, see [Limiting driver distribution by Windows versions](https://docs.microsoft.com/windows-hardware/drivers/dashboard/limit-driver-distribution).

### Shipping Label Workflow Status object

This object represents the status of workflow for a given entity.

```json
{
      "currentStep": "Created",
      "state": "completed",
      "messages": []
    }
```

This object has the following values

| Value | Type | Description |
|:--|:--|:--|
| currentStep | string | The name of the current step in the overall workflow for this entity. <br>For shipping labels that are published to windows update, the possible values are (description in parenthesis):<ul><li>Created (*Creating shipping label*)</li><li>PreProcessShippingLabel (*Validating targeting information*)</li><li>FinalizePreProcessing (*Invoking appropriate next step after pre-prpcess*)</li><li>PublishJobValidation (*Verifying if package ingestion/submission is complete*)</li><li>UpdateGeneration (*Generating publishing details for WU*)</li><li>MicrosoftApproval (*Promotion/flighting*)</li><li>Publishing (*Pushing publishing details to WU*)</li><li>FinalizePublishing (*Completing publishing process*)</li></ul> For shipping labels that are shared with other partners, the possible values are (description in parenthesis): <ul><li>Created (*Creating shipping label*)</li><li>PreProcessShippingLabel (*Validating targeting information*)</li><li>FinalizePreProcessing (*Invoking appropriate next step after pre-prpcess*)</li><li>PublishJobValidation (*Verifying if package ingestion/submission is complete*)</li><li>ProcessSharing (*Generating sharing details for receiver*)</li><li>FinalizeSharing (*Completing sharing process*)</li></ul>|
| State | string | The state of the current step. Possible values are:<ul><li>notStarted</li><li>started</li><li>failed</li><li>completed</li></ul> |
| Messages | array | An array of strings to provide messages about current step (especially in case of failure) |

## Error codes

For info about the errors codes, see [Error codes](get-product-data.md#error-codes).

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
