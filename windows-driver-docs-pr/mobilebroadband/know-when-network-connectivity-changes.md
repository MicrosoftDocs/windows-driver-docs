---
title: Know when network connectivity changes
description: Know when network connectivity changes
ms.assetid: 2937ba62-16ad-4a81-92e8-62a8bb40d608
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Know when network connectivity changes


To know when network connectivity changes, use the [**AccountUpdated**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event of [**MobileBroadbandAccountWatcher**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher):

1.  Instantiate a [**MobileBroadbandAccountWatcher**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher) object.

2.  Add an [**AccountUpdated**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event handler.

3.  Invoke [**Start**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_Start) on the watcher.

4.  Query the [**HasNetworkChanged**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs#Windows_Networking_NetworkOperators_MobileBroadbandAccountUpdatedEventArgs_HasNetworkChanged) property of the [**MobileBroadbandAccountUpdatedEventArgs**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs) object in the [**AccountUpdated**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event handler.

5.  If the network has changed, query the [**CurrentNetwork**](https://docs.microsoft.com/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount#Windows_Networking_NetworkOperators_MobileBroadbandAccount_CurrentNetwork) property for the current network object.

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






