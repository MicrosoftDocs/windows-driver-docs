---
title: PnP Notification Overview
description: PnP Notification Overview
ms.assetid: 134a1ea1-78c2-4bab-b5e9-ae21901772ea
keywords: ["PnP WDK kernel , notifications", "Plug and Play WDK kernel , notifications", "notifications WDK PnP , about notifications", "event notifications WDK PnP", "EventCategoryDeviceInterfaceChange notification", "EventCategoryTargetDeviceChange notification", "EventCategoryHardwareProfileChange notification"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# PnP Notification Overview





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

 

 




