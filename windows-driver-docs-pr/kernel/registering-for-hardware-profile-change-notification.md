---
title: Registering for Hardware Profile Change Notification
author: windows-driver-content
description: Registering for Hardware Profile Change Notification
MS-HAID:
- 'PlugPlay\_7bd29beb-cf16-4e99-90e8-a69d9e9a95cb.xml'
- 'kernel.registering\_for\_hardware\_profile\_change\_notification'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3aaa09f7-ac63-4b56-917a-74cf344f6dd3
keywords: ["notifications WDK PnP , hardware profile changes", "hardware profile change notifications WDK PnP", "EventCategoryHardwareProfileChange notification", "profile change notifications WDK PnP", "registering hardware profile change notifications", "machine hardware profile change notifications WDK PnP", "IoRegisterPlugPlayNotification"]
---

# Registering for Hardware Profile Change Notification


## <a href="" id="ddk-registering-for-hardware-profile-change-notification-kg"></a>


A driver registers for notification of hardware profile changes by calling [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526).

The following information applies to calling this routine for hardware profile change notification:

-   Specify an *EventCategory* of **EventCategoryHardwareProfileChange**.

-   *EventCategoryData* must be **NULL**.

-   Specify a driver-defined *Context*, if appropriate, that the PnP manager will pass to the callback routine.

A driver removes notification registration by calling [**IoUnregisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550398) with the *NotificationEntry* returned by **IoRegisterPlugPlayNotification**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20for%20Hardware%20Profile%20Change%20Notification%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


