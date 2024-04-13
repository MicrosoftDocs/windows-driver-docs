---
title: Best Practices for Handling Account Arrival and Removal Events
description: Best practices for handling account arrival and removal events
ms.date: 04/20/2017
---

# Best practices for handling account arrival and removal events


Mobile broadband accounts can be added or removed during the lifetime of the mobile broadband app. This can be caused by the addition or removal of hardware, PIN unlocking, or SIM swapping. The arrival or removal of an account is transient in many cases. Proper handling of these events has significant implications on the usability of the application. The following best practices apply to handling account arrival and removal events:

-   Do not immediately raise an error dialog when the active account that is being used is removed.

-   Do not assume that the user has removed the hardware. Hardware might be temporarily unavailable during sleep/resume of the machine, depending on the behavior of the driver or the bus.

-   Do not release any started account watcher objects without calling their [**Stop**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_Stop) method first. Account watchers, like all Windows Runtime (WinRT) objects, are reference counted. Calling [**Start**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_Start) increments their reference count (**Stop** decrements it). If you release a started account watcher, it will keep triggering events but you cannot call **Stop** on the handle that you’ve just released.

-   Remember that account watcher objects automatically stop when the app gets suspended by Windows, and restart when the app resumes. This is the same result as if your app had called [**Stop**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_Stop) and [**Start**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher#Windows_Networking_NetworkOperators_MobileBroadbandAccountWatcher_Start), and results in the same events. Use these events to bring the app up-to-date with anything significant that occurred during the time that it was suspended.

## <span id="related_topics"></span>Related topics


[Best practices for using Mobile Broadband Windows Runtime API](best-practices-for-handling-account-arrival-and-removal-events.md)

 

