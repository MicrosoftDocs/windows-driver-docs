---
title: Enumerate available mobile broadband accounts
description: Enumerate available mobile broadband accounts
ms.assetid: 6dcf4789-09e8-43d2-9617-a026cbe0dfbb
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enumerate available mobile broadband accounts


There are two methods that you can use to enumerate network accounts: polling or event-based.

-   **Polling** The mobile broadband app can poll for available network accounts by using the static [**MobileBroadbandAccount.AvailableNetworkAccountIds**](https://msdn.microsoft.com/library/windows/apps/hh770608) method. This is ideal if the application simply needs a snapshot of the accounts and does not need to respond at run time to accounts that are being added or removed.

-   **Event-based** You can use the [**MobileBroadbandAccountWatcher**](https://msdn.microsoft.com/library/windows/apps/hh770597) class to enumerate and then monitor for changes to mobile broadband accounts. The event-based method is ideal when the application must respond to changes (that is, return to the account selection page when the currently selected account is removed). The procedure to use this class is as follows:

    1.  Instantiate a [**MobileBroadbandAccountWatcher**](https://msdn.microsoft.com/library/windows/apps/hh770597) object.

    2.  Add event handlers to the [**AccountAdded**](https://msdn.microsoft.com/library/windows/apps/hh770599), [**AccountRemoved**](https://msdn.microsoft.com/library/windows/apps/hh770600), and [**EnumerationCompleted**](https://msdn.microsoft.com/library/windows/apps/hh770602) events.

    3.  Invoke Start() on the watcher.

    The [**AccountAdded**](https://msdn.microsoft.com/library/windows/apps/hh770599) event handlers are invoked for each existing network account. When all of the existing network accounts are enumerated, the [**EnumerationCompleted**](https://msdn.microsoft.com/library/windows/apps/hh770602) event is raised.

    Additional [**AccountAdded**](https://msdn.microsoft.com/library/windows/apps/hh770599) and [**AccountRemoved**](https://msdn.microsoft.com/library/windows/apps/hh770600) events are raised as account availability changes (that is, when mobile broadband hardware or the SIM is removed).

**Important**  
Account watcher objects automatically stop when the app is suspended by Windows, and restart when the app is resumed. This is done to preserve battery life because resuming a suspended app to process an event and then putting it back in the suspended state can result in significant disk activity. The Stopped event occurs when the watcher stops (this happens either right before or right after the app gets its Suspending event). When the app resumes, all watchers that were running before the app was suspended automatically restart, thereby triggering a series of [**AccountAdded**](https://msdn.microsoft.com/library/windows/apps/hh770599) events that are followed by an [**EnumerationCompleted**](https://msdn.microsoft.com/library/windows/apps/hh770602) event (the same way as if the [**Start**](https://msdn.microsoft.com/library/windows/apps/hh770604) method had been called). This enables the app to get up-to-date with anything significant that occurred during the time that it was suspended.

[**MobileBroadbandAccountWatcher**](https://msdn.microsoft.com/library/windows/apps/hh770597) objects are independent of each other. This means that you cannot depend on all watchers reporting the same set of events – as a group, they will report all events. However, any given watcher might not report any given event, because that event has been consumed by another watcher. Unless you have good reason, you should use only one account watcher object per app.

 

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Enumerate%20available%20mobile%20broadband%20accounts%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





