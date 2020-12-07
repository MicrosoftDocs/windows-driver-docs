---
title: Know when network connectivity changes
description: Know when network connectivity changes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Know when network connectivity changes


To know when network connectivity changes, use the [**AccountUpdated**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event of [**MobileBroadbandAccountWatcher**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher):

1.  Instantiate a [**MobileBroadbandAccountWatcher**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher) object.

2.  Add an [**AccountUpdated**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event handler.

3.  Invoke [**Start**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_Start) on the watcher.

4.  Query the [**HasNetworkChanged**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs#Windows_Networking_NetworkOperators_MobileBroadbandAccountUpdatedEventArgs_HasNetworkChanged) property of the [**MobileBroadbandAccountUpdatedEventArgs**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs) object in the [**AccountUpdated**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountUpdated) event handler.

5.  If the network has changed, query the [**CurrentNetwork**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount#Windows_Networking_NetworkOperators_MobileBroadbandAccount_CurrentNetwork) property for the current network object.

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

