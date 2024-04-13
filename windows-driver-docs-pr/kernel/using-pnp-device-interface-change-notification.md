---
title: Using PnP Device Interface Change Notification
description: Using PnP Device Interface Change Notification
keywords: ["notifications WDK PnP , device interface changes", "EventCategoryDeviceInterfaceChange notification", "device interface change notifications WDK PnP"]
ms.date: 06/16/2017
---

# Using PnP Device Interface Change Notification





A driver registers for **EventCategoryDeviceInterfaceChange** notification so the driver can be notified when device interfaces of a particular class arrive (are enabled) or are removed (disabled) on the machine. For example, a composite battery driver might register for notification of device interfaces of class battery so it can provide information to the operating system about total available battery power.

The following subsections discuss how to register for device interface change notification and how to handle device interface change events in a PnP notification callback routine:

[Registering for Device Interface Change Notification](registering-for-device-interface-change-notification.md)

[Handling Device Interface Change Events](handling-device-interface-change-events.md)

See [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) and related routines For information about device interfaces.

 

