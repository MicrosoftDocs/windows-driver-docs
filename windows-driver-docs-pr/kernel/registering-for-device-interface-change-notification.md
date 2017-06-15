---
title: Registering for Device Interface Change Notification
author: windows-driver-content
description: Registering for Device Interface Change Notification
MS-HAID:
- 'PlugPlay\_c34c39cd-8cdb-4e80-9c71-4da168de62fd.xml'
- 'kernel.registering\_for\_device\_interface\_change\_notification'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 680e4c5c-dac6-41b1-b754-aee782145ed0
keywords: ["notifications WDK PnP , device interface changes", "EventCategoryDeviceInterfaceChange notification", "device interface change notifications WDK PnP", "registering device interface change notifications", "IoRegisterPlugPlayNotification"]
---

# Registering for Device Interface Change Notification


## <a href="" id="ddk-registering-for-device-interface-change-notification-kg"></a>


A driver registers for notification of device interface arrival and removal events by calling [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526).

The following information applies to calling this routine for device interface change notification:

-   Specify an *EventCategory* of **EventCategoryDeviceInterfaceChange**.

-   *EventCategoryData* must point to the GUID for a device interface class.

    The GUID for a interface class is typically defined in a header file with the structures, constants, and so forth, for the interface.

-   Specify an *EventCategoryFlags* of PNPNOTIFY\_DEVICE\_INTERFACE\_INCLUDE\_EXISTING\_INTERFACES.

    This flag directs the PnP manager to register the *CallbackRoutine* for future device interface arrivals and departures of the specified class and to call the *CallbackRoutine* immediately for any relevant device interfaces that are already active.

    A driver can call [**IoGetDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff549186) to get a list of existing interfaces of a specific class and then register its callback routine without this flag, but using the flag is easier and avoids a potential timing issue.

-   Specify a driver-defined *Context*, if appropriate, that the PnP manager will pass to the callback routine.

A driver that opens a handle to a device in response to a device interface arrival notification should register for **EventCategoryTargetDeviceChange** events on the device. (See [Using PnP Target Device Change Notification](using-pnp-target-device-change-notification.md).)

A driver cancels notification registration by calling [**IoUnregisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550398) with the *NotificationEntry* returned by **IoRegisterPlugPlayNotification**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20for%20Device%20Interface%20Change%20Notification%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


