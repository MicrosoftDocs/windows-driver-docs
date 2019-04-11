---
title: Mobile Plans callback notifications
description: This topic describes the Callback notifications support by Mobile Plans app
ms.assetid: A3CE0B7D-80C5-4A98-8615-250A3C760B85
keywords:
- Windows Mobile Plans Callback notifications, Mobile Plans implementation mobile operators
ms.date: 03/25/2019
ms.localizationpriority: medium
---

# Mobile Plans callback notifications

## Overview

After the user completes the MO portal flow, the MO portal must return control to the Mobile Plans app. This is done by issuing a notification to the app with the result of the user interaction with the MO portal.

Transactions that the MO portal supports include, but are not limited to, the following:

- Selling a new eSIM profile (issuing an activation code).
- Activating a subscription.
- Purchasing a new data plan (either postpaid or prepaid).
- Canceling a subscription.

> [!NOTE]
> This callback should be returned from the host defined in [Service configuration](mobile-plans-service-configuration.md).

## Inline profile delivery

The following diagram shows the high level flow for how the Mobile Plans program supports downloading a profile without control leaving the MODirect portal.

![Mobile Plans inline profile download sequence diagram](images/dynamo_inline_profile_flow.png)

When the MO Direct portal is ready for a profile download, install, and activation to occur, the portal should call `MobilePlansInlineProfile.notifyInlineProfileDownload`.
### MobilePlansInlineProfile.notifyInlineProfileDownload

| Parameter name | Type | Description |
| --- | --- | -- |
| purchaseMetadata | Object | This object contains metadata about the user's purchase. This includes details about the user account, the purchase method or instrument, details if the user is adding a new line, and the name of the plan that the user purchased. All these are used for reporting. |
| activationCode | String | The activation code for downloading the eSIM profile. The ICCID for the profile is inferred from the profile metadata. |

The following Javascript function shows an example of the API to inform the application that an inline profile download should start.

```Javascript
function NotifyMobilePlans() { 
    var purchaseMetaData = MobilePlans.createPurchaseMetaData(); 
    purchaseMetaData.userAccount = MobilePlansUserAccount.new; 
    purchaseMetaData.purchaseInstrument = MobilePlansPurchaseInstrument.new; 
    purchaseMetaData.lineType = MobilePlansLineType.new; 
    purchaseMetaData.modirectStatus = MobilePlansMoDirectStatus.complete; 
    purchaseMetaData.planName = "My Plan"; 
    MobilePlansInlineProfileDownload.registrationChangedScript = "onRegistrationChanged";
    MobilePlansInlineProfileDownload.profileActivationCompleteScript = "onActivationComplete";
    MobilePlansInlineProfileDownload.notifyInlineProfileDownload(purchaseMetaData , "1$smdp.address$matchingID"); 
}
```

See [purchase metadata properties](#Purchase-Metadata-Properties-details) for details about the puchaseMetadata object.

## Inline profile operations
When the MO Direct portal wants to do operations without returning control to the Mobile Plans app, inline operations should be used.

### MobilePlansInlineOperations.notifyBalanceAddition(purchaseMetaData)
| Parameter name | Type | Description |
| --- | --- | -- |
| purchaseMetadata | Object | This object contains metadata about the user's purchase. This includes details about the user account, the purchase method or instrument, details if the user is adding a new line, and the name of the plan that the user purchased. All these are used for reporting. |

When the MO would like to add balance to a given account, the MO should call the `MobilePlansInlineOperations.notifyBalanceAddition` API.

The following Javascript function shows an example of the API to inform the application that a balance addition has been made.

```Javascript
function NotifyMobilePlans() { 
    var purchaseMetaData = MobilePlans.createPurchaseMetaData(); 
    purchaseMetaData.userAccount = MobilePlansUserAccount.new; 
    purchaseMetaData.purchaseInstrument = MobilePlansPurchaseInstrument.new; 
    purchaseMetaData.lineType = MobilePlansLineType.new; 
    purchaseMetaData.modirectStatus = MobilePlansMoDirectStatus.complete; 
    purchaseMetaData.planName = "My Plan"; 
    MobilePlansInlineOperations.notifyBalanceAddition(purchaseMetaData); 
}
```

### MobilePlansInlineOperations.notifyBalanceAddition(purchaseMetaData, iccid)
| Parameter name | Type | Description |
| --- | --- | -- |
| purchaseMetadata | Object | This object contains metadata about the user's purchase. This includes details about the user account, the purchase method or instrument, details if the user is adding a new line, and the name of the plan that the user purchased. All these are used for reporting. |
| iccid | String | The ICCID which should be made active after the balance addition

Balance addition can also be made to a non active profile if the ICCID of the profile is known. Using the `MobilePlansInlineOperations.notifyBalanceAddition` with an ICCID will inform Mobile Plans of the balance addition as well as make Mobile Plans switch the active profile to the profile corresponding to the provided ICCID.

The following Javascript function shows an example of the API to inform the application that a balance addition has been made.

```Javascript
function NotifyMobilePlans() { 
    var purchaseMetaData = MobilePlans.createPurchaseMetaData(); 
    purchaseMetaData.userAccount = MobilePlansUserAccount.new; 
    purchaseMetaData.purchaseInstrument = MobilePlansPurchaseInstrument.new; 
    purchaseMetaData.lineType = MobilePlansLineType.new; 
    purchaseMetaData.modirectStatus = MobilePlansMoDirectStatus.complete; 
    purchaseMetaData.planName = "My Plan"; 
    MobilePlansInlineOperations.notifyBalanceAddition(purchaseMetaData, "8900000000000000001"); 
}
```

### Listening for network registration changes

To listen for network registration changes, the `MobilePlansInlineProfileDownload.registrationChangedScript` must be set to a string that is the name of a Javascript function that takes a string for the `registrationArgs`.

The registration args are a string that represents a JSON object.

#### ProfileRegistrationCompleteArgs

| Property name | Type | Description |
| --- | --- | -- |
| networkRegistrationState | String | A string representing the current network registration state. The values of this property can be seen in `MobilePlansNetworkRegistrationState`. |
| iccid | String | The ICCID for which the network registration state has changed. |

#### MobilePlansNetworkRegistrationState

| Property name | Type | Description |
| --- | --- | -- |
| none | String | No connectivity. |
| deregistered | String | The device is not registered and is not searching for a network provider. |
| searching | String | The device is not registered and is searching for a network provider. |
| home | String | The device is on a home network provider. |
| roaming | String | The device is on a roaming network provider. |
| partner | String | The device is on a roaming partner network provider. |
| denied | String | The device was denied registration. |

The following Javascript example shows how to implement a listener for network registration changed events.

```Javascript
function onRegistrationChanged(registrationArgs) {
    var registrationObj = JSON.parse(registrationArgs);
    if(registrationObj.networkRegistrationState == MobilePlansNetworkRegistrationState.home ||
       registrationObj.networkRegistrationState == MobilePlansNetworkRegistrationState.roaming ||
       registrationObj.networkRegistrationState == MobilePlansNetworkRegistrationState.partner)
    {
        Log('Registration Successful!');
    }
}
```

### Listening for profile activation

To listen for profile activation events, the `MobilePlansInlineProfileDownload.profileActivationCompleteScript` must be set to a string that is the name of a Javascript function that takes a string for the `activationArgs`.

The `activationArgs` is a string that represents a JSON object.

#### ProfileActivationCompleteArgs

| Property name | Type | Description |
| --- | --- | -- |
| activationResult | String | The result of the activation. The values of this property can be seen in `MobilePlansActivationError`. |
| iccid | String | The ICCID of the profile that was activated. |

#### MobilePlansActivationError

| Property name | Type | Description |
| --- | --- | -- |
| success | String | Indicates that an operation was successful. |
| notAuthorized | String | Indicates that the operation was not authorized. |
| notFound | String | Indicates that the specified eSIM profile was not found. |
| policyViolation | String | Indicates that the operation violates policy. |
| insufficientSpaceOnCard | String | Indicates that there is not enough storage space on the card to complete the operation. |
| serverFailure | String | Indicates that a server failure occurred during the operation. |
| serverNotReachable | String | Indicates that the server could not be reached during the operation. |
| timeoutWaitingForUserConsent | String | Indicates that user consent was not granted within the timeout period of the operation. |
| incorrectConfirmationCode | String | Indicates that the wrong confirmation code was supplied during the operation. |
| confirmationCodeMaxRetriesExceeded | String | Indicates that the wrong confirmation code was supplied during the operation, and that no more retries are permitted. |
| cardRemoved | String | Indicates that the SIM card has been removed. |
| cardBusy | String | Indicates that the SIM card is busy. |
| other | String | Indicates a status that is not accounted for by a more specific status. |
| cardGeneralFailure | String | Indicates that a card error occurred that prevented the download, install, or other operation from completing successfully. |
| confirmationCodeMissing | String | Indicates that a confirmation code is needed to download the eSIM profile. |
| invalidMatchingId | String | Indicates that the matching ID from the activation code or discovered event was refused. |
| noEligibleProfileForThisDevice | String | Indicates that an eSIM profile compatible with this device could not be found. For example, a profile was found that requires LTE support, but the device only supports 3G. |
| operationAborted | String | Indicates that the operation aborted. |
| eidMismatch | String | Indicates that an eSIM profile on the mobile operator server is already allocated for a different eSIM EID than the one the device has. |
| profileNotAvailableForNewBinding | String | Indicates that the user is trying to download an eSIM profile that has already been claimed or downloaded. |
| profileNotReleasedByOperator | String | Indicates that the eSIM profile is available, but it is not yet marked as released for download by the mobile operator. Only released profiles can be downloaded, so the MO needs to mark the profile as released. |
| operationProhibitedByProfileClass | String | Indicates that the operation is not allowed for the eSIM profile class. |
| profileNotPresent | String | Indicates that an eSIM profile could not be found. |
| noCorrespondingRequest | String | Indicates that no corresponding request could be found. |
| unknownError | String | Indicates that LPA returned an error that is unknown. |
| lpaInitializationError | String | Indicates that an error occurred when trying to initialize LPA. |
| modemNotFound | String | Indicates that no cellular modem was found on the device. |
| localSettingsAccessFailed | String | Indicates that accessing app local settings failed. |
| invalidJson | String | Indicates that the MO portal has provided invalid JSON when calling the Mobile Plans app. |
| invalidActivationCode | String | Indicates that the MO portal has given invalid activation code. |
| invalidIccid | String | Indicates that the MO portal has given an invalid ICCID. |

The following Javascript example shows how to implement a listener for the profile activation event.

```Javascript
function onActivationComplete(activationArgs) {
    var activationObj = JSON.parse(activationArgs);
    if(activationObj.activationResult == MobilePlansActivationError.success)
        Log('Activation Success');
}
```

## Asynchronous connectivity

The following diagram shows the high level flow for how the Mobile Plans program supports delayed connectivity.

![Mobile Plans delayed connectivity sequence diagram](images/dynamo_async_connectivity_flow.png)

After the user successfully completes a purchase that requires a profile download from the mobile operator's MO Direct portal, the portal informs the Mobile Plans application that it should trigger the delayed connectivity flow using the `MobilePlans.notifyPurchaseWithProfileDownload` API. 

### MobilePlans.notifyPurchaseWithProfileDownload

| Parameter name | Type | Description |
| --- | --- | -- |
| purchaseMetadata | Object | This object contains metadata about the user's purchase. This includes details about the user account, the purchase method or instrument, details if the user is adding a new line, and the name of the plan that the user purchased. All these are used for reporting. |
| activationCode | String | The activation code for downloading the eSIM profile. The ICCID for the profile is inferred from the profile metadata. |
| networkRegistrationInterval | Unsigned integer | The time needed for the mobile operator to provision connectivity to the user. The Mobile Plans app attempts to register to the network within the specified time interval, in minutes. **Note** This time is rounded to the nearest 15 minute interval. For example, if this is set as 5 minutes, the application tries to re-register to the network after approximately 15 minutes (but it might take longer). if set to "0" the device will attempt to register immediately. |

The following Javascript function shows an example of the API to inform the application that the user purchase requires a delayed provisioning of connectivity.

 ```Javascript
function finishPurchaseWithDownload() {
        var metadata = MobilePlans.createPurchaseMetaData();
        metadata.userAccount = MobilePlansUserAccount.new;
        metadata.purchaseInstrument = MobilePlansPurchaseInstrument.new;
        metadata.moDirectStatus = MobilePlansMoDirectStatus.complete;
        metadata.line = MobilePlansLineType.new;
        metadata.planName = "2GB Monthly";
        MobilePlans.notifyPurchaseWithProfileDownload(metadata, "1$smdp.address$matchingID", 15);
}
```

See [purchase metadata properties](#Purchase-Metadata-Properties-details) for details about the puchaseMetadata object.

## Adding balance

When a user completes a purchase in the MO Direct portal by adding more data to their account (no profile download needed because the user used the current profile on the eSIM), the MO portal should invoke the `MobilePlans.notifyBalanceAddition` API return control back to the Mobile Plans app.

### MobilePlans.notifyBalanceAddition

| Parameter name | Type | Description |
| --- | --- | -- |
| purchaseMetadata | Object | This object contains metadata about the user's purchase. This includes details about the user account, the purchase method or instrument, details if the user is adding a new line, and the name of the plan that the user purchased. All these are used for reporting. |
| iccid | String | The ICCID to which data is assigned. If this ICCID is not active, the Mobile Plans app activates the corresponding profile.|

The following Javascript function shows an example of the API to inform the application that the user has completed a purchase using a profile already available, but not necessarily active, on the eSIM.

 ```Javascript
function finishPurchaseWithBalanceAddition() {
        var metadata = MobilePlans.createPurchaseMetaData();
        metadata.userAccount = MobilePlansUserAccount.new;
        metadata.purchaseInstrument = MobilePlansPurchaseInstrument.none;
        metadata.moDirectStatus = MobilePlansMoDirectStatus.complete;
        metadata.line = MobilePlansLineType.new;
        metadata.planName = "2GB Monthly";
        MobilePlans.notifyBalanceAddition(metadata, "89000000000000000000");
    }
```

See [purchase metadata properties](#Purchase-Metadata-Properties-details) for details about the `puchaseMetadata` object.

## Canceling purchase flow

If a user cancels the purchase flow at the MO portal, then the portal must invoke the `MobilePlans.notifyCancelledPurchase` API to return control back to the Mobile Plans app.

### MobilePlans.notifyCancelledPurchase

| Parameter name | Type | Description |
| --- | --- | -- |
| purchaseMetadata | Object | This object contains metadata about the user's purchase. This includes details about the user account, the purchase method or instrument, details if the user is adding a new line, and the name of the plan that the user purchased. All these are used for reporting. |

The following Javascript function shows an example of the API to inform the application that the user has canceled a purchase.

 ```Javascript
function finishPurchaseWithCancellation() {
        var metadata = MobilePlans.createPurchaseMetaData();
        metadata.userAccount = MobilePlansUserAccount.new;
        metadata.purchaseInstrument = MobilePlansPurchaseInstrument.new;
        metadata.moDirectStatus = MobilePlansMoDirectStatus.cancelled;
        metadata.line = MobilePlansLineType.bailed;
        metadata.planName = "";
        MobilePlans.notifyCancelledPurchase(metadata);
    }
```

See [purchase metadata properties](#Purchase-Metadata-Properties-details) for details about the `puchaseMetadata` object.

## Purchase Metadata Properties details

The following table describes the details used in the purchase metadata.

| Property name | Type | Description | Example |
| --- | --- | --- | --- |
| userAccount | String | Possible values: <ul><li>New: Indicates that a new user account was created by the user.</li><li>Existing: Indicates that the user logged on with an existing user account.</li><li>Bailed: Indicates that the user ended the purchase flow at this step.</li><li>None: Indicates that the user didn’t reach this step.</li></ul> | "userAccount":"New" |
| purchaseInstrument | String | Possible values: <ul><li>New: Indicates that a new user account was created by the user.</li><li>Existing: Indicates that the user logged on with an existing user account.</li><li>Bailed: Indicates that the user ended the purchase flow at this step.</li><li>None: Indicates that the user didn’t reach this step.</li></ul> | "purchaseInstrument":"New" |
| line | String | Possible values: <ul><li>New: Indicates that a SIM card was added by the user account.</li><li>Existing: Indicates that the user transferred an existing line to the device.</li><li>Bailed: Indicates that the user ended the purchase flow at this step.</li><li>None: Indicates that the user didn’t reach this step.</li></ul> | "line":New" |
| moDirectStatus | String | Possible values: <ul><li>Complete: Indicates that the user completed the purchase successfully.</li><li>ServiceError: Indicates that the user was unable to complete the purchase due to an MO service error.</li><li>InvalidSIM: Indicates that the ICCID passed to the portal was incorrect.</li><li>LogOnFailed: indicates that the user failed to log in to the MO portal.</li><li>PurchaseFailed: Indicates that the purchase failed due to a billing error.</li><li>ClientError: Indicates that invalid arguments were passed to the portal.</li>BillingError: Indicates that there was an error with the user billing.</li></ul> | "moDirectStatus":"Complete" |
| planName | String | For a successful transaction, this field must not be empty and must provide a descriptive plan name. For an unsuccessful transaction, this field must be an empty string. | "planName":"2GB Monthly"|

## Legacy callback notifications

> [!NOTE]
> This section serves as reference only. While this notification is supported in Mobile Plans app, the recommendation is not to implement it in new Mobile Plans implementations.

The notification to the Mobile Plans app should be sent using JavaScript with the following syntax:

```javascript
DataMart.notifyPurchaseResult(notificationPayload);
```

An example of the notification payload for an eSIM is as follows:

```javascript
let notificationPayload = new Object();
notificationPayload.ver = '1';
notificationPayload.purchaseResult = "{\"userAccount\":\"New\",\"purchaseInstrument\":\"New\",\"line\":\"New\",\"moDirectStatus\":\"Complete\",\"planName\":\"MyPlan\"}";
notificationPayload.success = true;
notificationPayload.transactionId = 'MSFT_ecf5a4d6-024c-46c3-8fcd-2c1f0deed572';
notificationPayload.activationCode = '1$trl.prod.ondemandconnectivity.com$JO46UQDI07IKQDGG';
notificationPayload.iccid = '8988247000101997790';

DataMart.notifyPurchaseResult(JSON.stringify(notificationPayload));
```

An example of the notification payload for a physical SIM is as follows:

```javascript
let notificationPayload = new Object();
notificationPayload.ver = '1';
notificationPayload.purchaseResult = "{\"userAccount\":\"New\",\"purchaseInstrument\":\"New\",\"line\":\"New\",\"moDirectStatus\":\"Complete\",\"planName\":\"MyPlan\"}";
notificationPayload.success = true;
notificationPayload.transactionId = 'MSFT_ecf5a4d6-024c-46c3-8fcd-2c1f0deed572';
notificationPayload.iccid = '8988247000101997790';

DataMart.notifyPurchaseResult(JSON.stringify(notificationPayload));
```

An example of the notification payload for an eSIM where the user abandoned the MO portal without a successful transaction is as follows. To implement all cases that apply to your specific implementation, see the table that follows the example.

```javascript
let notificationPayload = new Object();
notificationPayload.ver = '1';
notificationPayload.purchaseResult = "{\"userAccount\":\"Bailed\",\"purchaseInstrument\":\"None\",\"line\":\"None\",\"moDirectStatus\":\"None\",\"planName\":\"\"}";
notificationPayload.success = false;
notificationPayload.transactionId = 'MSFT_ecf5a4d6-024c-46c3-8fcd-2c1f0deed572';
notificationPayload.activationCode = '';
notificationPayload.iccid = '';

DataMart.notifyPurchaseResult(JSON.stringify(notificationPayload));
```

The MO Portal URI from which the notification is sent must be in the secure *https* protocol. You can specify the host but not necessarily the full path, which leaves some flexibility for the future. 

The following table describes each field in the JSON payload of the notification:

| JSON field         | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Example                                |
| ------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| success            | Boolean | **True** if the user purchased an MO Direct plan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `“success”:true`                     |
| iccid              | String  | For an eSIM, this indicates the ICCID that the client must use for consuming the MO Direct plan purchased.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `iccid:”8988247000100297655”`        |
| activationCode     | String  | The activation code to retrieve the eSIM profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `“ActivationCode”`                   |
| transactionId      | String  | The Transaction ID that the MO portal received as a query parameter when the portal was launched.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `transctionId= rRi8OzhI3EiR02nm.2.0.1` |
| purchaseResult     | String  | Contains the details of the user interaction with the MO portal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                        |
| userAccount        | Enum    | This field is required. <p>Possible values:</p><ul><li>New: Indicates that a new user account was created by the user.</li><li>Existing: Indicates that the user logged on with an existing user account.</li><li>Bailed: Indicates that the user ended the purchase flow at this step.</li><li>None: Indicates that the user didn’t reach this step.</li></ul>                                                                                                                                                                                                                                                                                                                 | `“userAccount”:”New”`              |
| purchaseInstrument | Enum    | This field is required. <p>Possible values:</p><ul><li>New: Indicates that the user used a new method of payment.</li><li>Existing: Indicates that the user used an existing payment method that was on file.</li><li>Bailed: Indicates that the user ended the purchase flow at this step.</li><li>None: Indicates that the user didn’t reach this step.</li></ul>                                                                                                                                                                                                                                                                                                             | `“purchaseInstrument”:”New”`       |
| line               | Enum    | This field is required. <p>Possible values:</p><ul><li>New: Indicates that a SIM card was added by the user account.</li><li>Existing: Indicates that the transferred an existing line to the device.</li><li>Bailed: Indicates that the user ended the purchase flow at this step.</li><li>None: Indicates that the user didn’t reach this step.</li></ul>                                                                                                                                                                                                                                                                                                                     | `“line”:”New”`                     |
| moDirectStatus     | Enum    | This field is required. <p>Possible values:</p><ul><li>Complete: Indicates that the user completed the purchase successfully.</li><li>ServiceError: Indicates that the user was unable to complete the purchase due to an MO service error.</li><li>InvalidSIM: Indicates that the ICCID passed to the portal was incorrect.</li><li>LogOnFailed: Indicates that the user failed to log in to the MO portal.</li><li>PurchaseFailed: Indicates that the purchase failed due to a billing error.</li><li>ClientError: Indicates that invalid arguments were passed to the portal.</li><li>None: Indicates that the user ended the transaction without a specific error.</li></ul> | `“moDirectStatus”:”Complete”`      |
| planName           | String  | For a successful transaction, this field must not be empty and must provide a descriptive plan name. For an unsuccessful transaction, this field must be an empty string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `“planName”:”prepaid_3GperMonth”`  |
