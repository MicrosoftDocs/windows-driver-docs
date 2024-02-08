---
title: Enumerate Available Mobile Broadband Accounts
description: Enumerate available mobile broadband accounts
ms.date: 04/20/2017
---

# Enumerate available mobile broadband accounts


There are two methods that you can use to enumerate network accounts: polling or event-based.

-   **Polling** The mobile broadband app can poll for available network accounts by using the static [**MobileBroadbandAccount.AvailableNetworkAccountIds**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount#Windows_Networking_NetworkOperators_MobileBroadbandAccount_AvailableNetworkAccountIds) method. This is ideal if the application simply needs a snapshot of the accounts and does not need to respond at run time to accounts that are being added or removed.

-   **Event-based** You can use the [**MobileBroadbandAccountWatcher**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher) class to enumerate and then monitor for changes to mobile broadband accounts. The event-based method is ideal when the application must respond to changes (that is, return to the account selection page when the currently selected account is removed). The procedure to use this class is as follows:

    1.  Instantiate a [**MobileBroadbandAccountWatcher**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher) object.

    2.  Add event handlers to the [**AccountAdded**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountAdded), [**AccountRemoved**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountRemoved), and [**EnumerationCompleted**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_EnumerationCompleted) events.

    3.  Invoke Start() on the watcher.

    The [**AccountAdded**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountAdded) event handlers are invoked for each existing network account. When all of the existing network accounts are enumerated, the [**EnumerationCompleted**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_EnumerationCompleted) event is raised.

    Additional [**AccountAdded**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountAdded) and [**AccountRemoved**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountRemoved) events are raised as account availability changes (that is, when mobile broadband hardware or the SIM is removed).

**Important**  
Account watcher objects automatically stop when the app is suspended by Windows, and restart when the app is resumed. This is done to preserve battery life because resuming a suspended app to process an event and then putting it back in the suspended state can result in significant disk activity. The Stopped event occurs when the watcher stops (this happens either right before or right after the app gets its Suspending event). When the app resumes, all watchers that were running before the app was suspended automatically restart, thereby triggering a series of [**AccountAdded**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_AccountAdded) events that are followed by an [**EnumerationCompleted**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_EnumerationCompleted) event (the same way as if the [**Start**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_Start) method had been called). This enables the app to get up-to-date with anything significant that occurred during the time that it was suspended.

[**MobileBroadbandAccountWatcher**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher) objects are independent of each other. This means that you cannot depend on all watchers reporting the same set of events – as a group, they will report all events. However, any given watcher might not report any given event, because that event has been consumed by another watcher. Unless you have good reason, you should use only one account watcher object per app.

 

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

