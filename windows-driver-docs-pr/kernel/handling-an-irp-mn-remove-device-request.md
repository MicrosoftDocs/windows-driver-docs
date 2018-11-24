---
title: Handling an IRP_MN_REMOVE_DEVICE Request
description: Handling an IRP_MN_REMOVE_DEVICE Request
ms.assetid: 1e0c8b41-5375-41dd-80eb-e48c0f513e01
keywords: ["IRP_MN_REMOVE_DEVICE"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling an IRP\_MN\_REMOVE\_DEVICE Request





The PnP manager uses this IRP to direct drivers to remove a device's software representation (device objects, and so forth). The PnP manager sends this IRP when a device has been removed in an orderly fashion (for example, initiated by a user in the Unplug or Eject Hardware program), by surprise (a user pulls the device from its slot without prior warning), or when the user requests to update drivers.

On Windows 2000 and later systems, the PnP manager sends this IRP when Device Manager disables the device. On Windows 98/Me, the PnP manager sends stop IRPs instead. See [Stopping a Device](stopping-a-device.md) for details.

The PnP manager does the following before sending this IRP to the drivers for a device:

-   Sends **IRP\_MN\_REMOVE\_DEVICE** requests to the device's children, if any.

-   Notifies any user-mode components and kernel-mode drivers that registered for notification that the device is being removed. The PnP manager calls any user-mode components that registered for target device notification on a handle to the device and calls any kernel-mode drivers that registered for **EventCategoryTargetDeviceChange**.

-   (On Windows 2000 and later systems) If a file system is mounted on the device, the PnP manager sends a remove request to the file system and any file system filters. In response, a file system typically dismounts the volume.

The top driver in a device stack handles a remove IRP and passes it to the next lower driver. The parent bus driver for a device is the last driver to perform its remove-device operations. A driver handles remove IRPs in its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine.

Before a driver returns success for an **IRP\_MN\_REMOVE\_DEVICE** request, it must ensure that all resources for the device have been released. This IRP could be the last call before the driver is unloaded.

Removing one device can create the need to remove a series of other devices. The PnP manager coordinates the removal of the additional device objects from the top level down to the root-device level.

This section describes:

[Removing a Device in a Function Driver](removing-a-device-in-a-function-driver.md)

[Removing a Device in a Filter Driver](removing-a-device-in-a-filter-driver.md)

[Removing a Device in a Bus Driver](removing-a-device-in-a-bus-driver.md)

 

 




