---
title: Receive notification for device information account changes
description: Receive notification for device information account changes
ms.assetid: 67d96f61-57dc-4e4b-a6c1-5c3da28e8aaf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receive notification for device information account changes


To receive a notification for device information account changes, use the [**AccountUpdated**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event of [**MobileBroadbandAccountWatcher**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher) as described here:

1.  Instantiate a [**MobileBroadbandAccountWatcher**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher) object.

2.  Add an [**AccountUpdated**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event handler.

3.  Invoke [**Start**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_Start) on the watcher.

4.  Query the [**HasDeviceInformationChanged**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs#Windows_Networking_NetworkOperators_MobileBroadbandAccountUpdatedEventArgs_HasDeviceInformationChanged) property of the [**MobileBroadbandAccountUpdatedEventArgs**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs) object in the [**AccountUpdated**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event handler.

5.  If the device information has changed, query the account [**CurrentDeviceInformation.TelephoneNumbers**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation#Windows_Networking_NetworkOperators_MobileBroadbandDeviceInformation_TelephoneNumbers) property for the telephone number.

    For example:

    ``` syntax
    if (account.currentDeviceInformation.TelephoneNumbers.length > 0)
    {
      // there is now at least one telephone number
    }
    ```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






