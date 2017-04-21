---
title: Best practices for handling account arrival and removal events
description: Best practices for handling account arrival and removal events
ms.assetid: e299a920-a27e-4832-b81d-1562f86f37e2
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Best practices for handling account arrival and removal events


Mobile broadband accounts can be added or removed during the lifetime of the mobile broadband app. This can be caused by the addition or removal of hardware, PIN unlocking, or SIM swapping. The arrival or removal of an account is transient in many cases. Proper handling of these events has significant implications on the usability of the application. The following best practices apply to handling account arrival and removal events:

-   Do not immediately raise an error dialog when the active account that is being used is removed.

-   Do not assume that the user has removed the hardware. Hardware might be temporarily unavailable during sleep/resume of the machine, depending on the behavior of the driver or the bus.

-   Do not release any started account watcher objects without calling their [**Stop**](https://msdn.microsoft.com/library/windows/apps/hh770606) method first. Account watchers, like all Windows Runtime (WinRT) objects, are reference counted. Calling [**Start**](https://msdn.microsoft.com/library/windows/apps/hh770604) increments their reference count (**Stop** decrements it). If you release a started account watcher, it will keep triggering events but you cannot call **Stop** on the handle that you’ve just released.

-   Remember that account watcher objects automatically stop when the app gets suspended by Windows, and restart when the app resumes. This is the same result as if your app had called [**Stop**](https://msdn.microsoft.com/library/windows/apps/hh770606) and [**Start**](https://msdn.microsoft.com/library/windows/apps/hh770604), and results in the same events. Use these events to bring the app up-to-date with anything significant that occurred during the time that it was suspended.

## <span id="related_topics"></span>Related topics


[Best practices for using Mobile Broadband Windows Runtime API](best-practices-for-using-mobile-broadband-windows-runtime-api.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Best%20practices%20for%20handling%20account%20arrival%20and%20removal%20events%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





