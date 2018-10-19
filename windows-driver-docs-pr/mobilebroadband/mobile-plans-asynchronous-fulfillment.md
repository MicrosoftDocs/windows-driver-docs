---
title: Mobile Plans asynchronous fulfillment
description: Mobile Plans asynchronous fulfillment
ms.assetid: 56AB67D6-59A9-4483-B455-2FCC309C8903
keywords:
- Windows Mobile Plans asynchronous fulfillment mobile operators
ms.author: windowsdriverdev
ms.date: 09/28/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mobile Plans asynchronous fulfillment

[!include[Mobile Plans Beta Prerelease](../mobile-plans-beta-prerelease.md)]

## Overview

This topic provides the API details for mobile operators who can't either grant connectivity to the user at the time when the profile is profile is downloaded after purchase (Asynchronous connectivity) or when the profile is not available for download at purchase time (Asynchronous profile delivery).

## Asynchronous connectivity

The diagram below shows the high level flow supported by Mobile Plans to support delayed connectivity.

![Mobile Plans delayed connectivity sequence diagram](images/dynamo_async_connectivity_flow.png)

After the user successfully completes a purchase that requires a profile download from the mobile operator's MO Direct portal, the portal informs the Mobile Plans application to trigger the delayed connectivity flow using the DataMart.notifyPurchaseWithProfileDownload API. 

### DataMart.notifyPurchaseWithProfileDownload

| parameter name | type | description |
| --- | --- | -- |
| purchaseMetadata | object | This object contains the metadata about the puerchase made by the user. This includes details about the user account, the type of purchase intrumentation used to make the purchase, details if the user is adding a new line, the name of the plan purchased by user. All these are used for reporting. |
| activationCode | String | Activation code to be used to download the eSIM profile. ICCID for the profile is inferred from the profile metadata. |
| networkRegistrationInterval | unsigned integer | Time needed for the mobile operator to provision connectivity to the user. The Mobile Plans app will attempt to register to the network the specified time interval in minutes. NOTE: This will be rounded to the nearest 15 minute interval. For example, if this is set as 5 minutes, the application will try to reregister to the network after approximately 15 minutes (may take longer) |

The javascript function below shows an example usage of the API to inform the application that the user purchase requires a delayed provisioning of connectivity.

 ```javascript
function finishPurchaseWithDownload() {
        var metadata = DataMart.createPurchaseMetaData();
        metadata.userAccount = "New";
        metadata.purchaseInstrument = "New";
        metadata.moDirectStatus = "Complete";
        metadata.line = "New";
        metadata.planName = "2GB Monthly";
        DataMart.notifyPurchaseWithProfileDownload(metadata, "1$smdp.address$", 15);
    }
```

| Property Name | Type | Description | Example |
| --- | --- | --- | --- |
| userAccount | String | Possible values: New: Indicates that a new user account was created by the user Existing: Indicates that the user logged on with an existing user account Bailed: Indicates that the user ended the purchase flow at this step None: Indicates that the user didn’t reach this step | "userAccount":"New" |
| purchaseInstrument | String | Possible values: New: Indicates that a new user account was created by the user Existing: Indicates that the user logged on with an existing user account Bailed: Indicates that the user ended the purchase flow at this step None: Indicates that the user didn’t reach this step. | "purchaseInstrument":"New" |
| line | String | Possible values: New: Indicates that a SIM card was added by the user account Existing: Indicates that the transferred an existing line to the device Bailed: Indicates that the user ended the purchase flow at this step None: Indicates that the user didn’t reach this step. | "line":New" |
| moDirectStatus | String | Possible values: Complete: Indicates that the user completed the purchase successfully. ServiceError: Indicates that the user was unable to complete the purchase due to an MO service error. InvalidSIM: Indicates that the ICCID passed to the portal was incorrect. LogOnFailed indicates that the user failed to log in to the MO portal. PurchaseFailed: Indicates that the purchase failed due to a billing error. ClientError: Indicates that invalid arguments were passed to the portal. BillingError: Indicates that there was an error in with the user billing. | "moDirectStatus":"Complete" |
| planName | String | For a successful transaction, this field must not be empty and provide a descriptive plan name. For an unsuccessful transaction, this field must be an empty string. | "planName":"2GB Monthly"|


## Asynchronous profile delivery

The diagram below shows the high level flow supported by Mobile Plans to support delayed profile download.

![Mobile Plans delayed profile download sequence diagram](images/dynamo_async_profile_flow.png)


After the user successfully completes a purchase that requires a profile download from the mobile operator's MO Direct portal, the portal informs the Mobile Plans application to trigger the delayed profile download flow using the DataMart.notifyPurchaseDelayedProfile API. 

### DataMart.notifyPurchaseDelayedProfile

| parameter name | type | description |
| --- | --- | -- |
| purchaseMetadata | object | This object contains the metadata about the puerchase made by the user. This includes details about the user account, the type of purchase intrumentation used to make the purchase, details if the user is adding a new line, the name of the plan purchased by user. All these are used for reporting. |
| profileDownloadDelayInterval | unsigned integer | Time needed for the mobile operator to create the profile for the user profile and have it ready for download from SM-DS. The Mobile Plans app will download the profile from SM-DS after this interval in minutes. NOTE: This will be rounded to the nearest 15 minute interval. For example, if this is set as 5 minutes, the application will try to reregister to the network after approximately 15 minutes (may take longer)|

The javascript function below shows an example usage of the API to inform the application that the user purchase requires a delayed profile download using SM-DS.

 ```javascript
function finishPurchaseWithSMDS() {
        var metadata = DataMart.createPurchaseMetaData();
        metadata.userAccount = "New";
        metadata.purchaseInstrument = "New";
        metadata.moDirectStatus = "Complete";
        metadata.line = "New";
        metadata.planName = "2GB Monthly";
        DataMart.notifyPurchaseDelayedProfile(metadata, 15);
    }
```

## Adding balance

When a user completes a purchase at the MO Direct portal by adding more data to their account (no profile download needed as the user is using the current profile on the eSIM), the MO portal should invoke the DataMart.notifyBalanceAddition API return the control back to the Mobile Plans app.

### DataMart.notifyBalanceAddition

| parameter name | type | description |
| --- | --- | -- |
| purchaseMetadata | object | This object contains the metadata about the puerchase made by the user. This includes details about the user account, the type of purchase intrumentation used to make the purchase, details if the user is adding a new line, the name of the plan purchased by user. All these are used for reporting. |
| iccid | Strign | The iccid to which data is assigned. If this iccid is not active, Mobile Plans will activate the corresponding profile.|

The javascript function below shows an example usage of the API to inform the application that the user has completed a purchase using a profile already available (not neccessarily active) on the eSIM.

 ```javascript
function finishPurchaseWithBalanceAddition() {
        var metadata = DataMart.createPurchaseMetaData();
        metadata.userAccount = "New";
        metadata.purchaseInstrument = "New";
        metadata.moDirectStatus = "Complete";
        metadata.line = "New";
        metadata.planName = "2GB Monthly";
        DataMart.notifyBalanceAddition(metadata, "89000000000000000000");
    }
```

## Cancelling purchase flow

If a user cancels the purchase flow at the MO portal, then the portal must invoke the DataMart.notifyCancelledPurchase API to return the control back to the application.

### DataMart.notifyCancelledPurchase

| parameter name | type | description |
| --- | --- | -- |
| purchaseMetadata | object | This object contains the metadata about the puerchase made by the user. This includes details about the user account, the type of purchase intrumentation used to make the purchase, details if the user is adding a new line, the name of the plan purchased by user. All these are used for reporting. |

The javascript function below shows an example usage of the API to inform the application that the user has completed a purchase using a profile already available (not neccessarily active) on the eSIM.

 ```javascript
function finishPurchaseWithCancellation() {
        var metadata = DataMart.createPurchaseMetaData();
        metadata.userAccount = "New";
        metadata.purchaseInstrument = "New";
        metadata.moDirectStatus = "Cancelled";
        metadata.line = "Bailed";
        metadata.planName = "";
        DataMart.notifyCancelledPurchase(metadata);
    }
```


