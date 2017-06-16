---
title: PnP Notification Overview
author: windows-driver-content
description: PnP Notification Overview
ms.assetid: 134a1ea1-78c2-4bab-b5e9-ae21901772ea
keywords: ["PnP WDK kernel , notifications", "Plug and Play WDK kernel , notifications", "notifications WDK PnP , about notifications", "event notifications WDK PnP", "EventCategoryDeviceInterfaceChange notification", "EventCategoryTargetDeviceChange notification", "EventCategoryHardwareProfileChange notification"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PnP Notification Overview


## <a href="" id="ddk-pnp-notification-overview-kg"></a>


The PnP manager provides a mechanism for drivers and applications to be notified when certain events occur on a specific device or on the system in general. A driver can register for notification of the following categories of events:

-   **EventCategoryDeviceInterfaceChange**

    When a driver registers for this category of events on a device interface, the PnP manager notifies the driver of the following events:

    <a href="" id="guid-device-interface-arrival"></a>GUID\_DEVICE\_INTERFACE\_ARRIVAL  
    Indicates that a device interface of the specified class has been enabled. For example, a user added a new disk to the machine and the volume manager enabled a new volume (a device interface of the class "volume").

    <a href="" id="guid-device-interface-removal"></a>GUID\_DEVICE\_INTERFACE\_REMOVAL  
    Indicates that a device interface of the specified class has been disabled.

    See [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) and related routines for more information about device interfaces.

-   **EventCategoryTargetDeviceChange**

    When a driver registers for this category of events on a device, the PnP manager notifies the driver when the following events occur on the device:

    <a href="" id="guid-target-device-query-remove"></a>GUID\_TARGET\_DEVICE\_QUERY\_REMOVE  
    Indicates that the PnP manager is about to remove the drivers for the device. Several actions can cause this event, including: a user has requested to remove the specified device from the machine or a user has issued an update-driver request for the device. This notification requests the drivers for the device to either approve or veto the impending remove operation.

    <a href="" id="guid-target-device-remove-complete"></a>GUID\_TARGET\_DEVICE\_REMOVE\_COMPLETE  
    Indicates that the specified device has been removed from the machine or that a user is changing the driver(s) for the device.

    <a href="" id="guid-target-device-remove-cancelled"></a>GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED  
    Indicates that an impending remove operation on the specified device has been canceled.

    <a href="" id="guid-xxx---custom-events-"></a>GUID\_*XXX* (custom events)  
    Indicates that a custom event has occurred on the specified device.

    A driver writer can define a custom event for a device. When the driver (or another related component) notifies the PnP manager that the custom event has occurred, the PnP manager notifies any components that registered for target device change notifications on the device.

    Unlike registering for device interface changes, which can be considered a "passive" interest in the interface, registering for target device changes indicates an "active" interest in a device.

-   **EventCategoryHardwareProfileChange**

    This category includes the following events:

    <a href="" id="guid-hwprofile-query-change"></a>GUID\_HWPROFILE\_QUERY\_CHANGE  
    Indicates that a user has requested to change the hardware profile of the machine. The PnP manager uses this notification to ask registered components whether it can change the hardware profile without disrupting system operation. Registered components typically succeed these query requests.

    <a href="" id="guid-hwprofile-change-complete"></a>GUID\_HWPROFILE\_CHANGE\_COMPLETE  
    Indicates that the hardware profile of the machine has changed. If a driver maintains profile-specific settings, such a driver should refresh those settings after a hardware profile change.

    <a href="" id="guid-hwprofile-change-cancelled"></a>GUID\_HWPROFILE\_CHANGE\_CANCELLED  
    Indicates that an impending hardware profile change has been canceled.

PnP notification works as follows for kernel-mode components:

1.  A driver registers for notification on a category of events by calling [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526).

    A PnP notification callback routine remains registered until the driver explicitly removes the registration.

2.  The PnP manager calls the driver's callback routine when an event in the registered category occurs.

3.  The driver removes the callback registration by calling [**IoUnregisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550398).

Drivers must not generate a synchronous event or wait for an asynchronous event to occur during the processing of a close.

For further information about PnP notification, see the following sections:

[Guidelines for Writing PnP Notification Callback Routines](guidelines-for-writing-pnp-notification-callback-routines.md)

[Using PnP Device Interface Change Notification](using-pnp-device-interface-change-notification.md)

[Using PnP Target Device Change Notification](using-pnp-target-device-change-notification.md)

[Using PnP Hardware Profile Change Notification](using-pnp-hardware-profile-change-notification.md)

[Using PnP Custom Notification](using-pnp-custom-notification.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20PnP%20Notification%20Overview%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


