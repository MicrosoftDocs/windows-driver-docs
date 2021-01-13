---
title: Receive notification for device information account changes
description: Receive notification for device information account changes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receive notification for device information account changes


To receive a notification for device information account changes, use the [**AccountUpdated**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event of [**MobileBroadbandAccountWatcher**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher) as described here:

1.  Instantiate a [**MobileBroadbandAccountWatcher**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher) object.

2.  Add an [**AccountUpdated**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event handler.

3.  Invoke [**Start**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_Start) on the watcher.

4.  Query the [**HasDeviceInformationChanged**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs#Windows_Networking_NetworkOperators_MobileBroadbandAccountUpdatedEventArgs_HasDeviceInformationChanged) property of the [**MobileBroadbandAccountUpdatedEventArgs**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs) object in the [**AccountUpdated**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event handler.

5.  If the device information has changed, query the account [**CurrentDeviceInformation.TelephoneNumbers**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation#Windows_Networking_NetworkOperators_MobileBroadbandDeviceInformation_TelephoneNumbers) property for the telephone number.

    For example:

    ``` syntax
    if (account.currentDeviceInformation.TelephoneNumbers.length > 0)
    {
      // there is now at least one telephone number
    }
    ```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

