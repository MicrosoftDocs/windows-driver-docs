---
title: Using a Device Interface
description: Using a Device Interface
keywords:
- interface classes WDK device installations
- device interface classes WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using a Device Interface





Device interfaces are available to both kernel-mode components and user-mode applications. User-mode code can use **SetupDi***Xxx* functions to find out about registered, enabled device interfaces. See [SetupDi Device Interface Functions](using-device-installation-functions.md#ddk-setupdi-device-interface-functions-dg) for more information.

Before a kernel-mode component can use a specific device or file object, it must do the following:

1.  Determine whether the required device interface class is registered and enabled.

    A driver can register with the PnP manager to be notified when an instance of a device interface is enabled or disabled. To register, the component calls [**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification). This routine stores the address of a driver-supplied callback, which is called whenever an instance of a device interface instance is enabled or disabled, for a specified device class. The callback routines receive the [**DEVICE_INTERFACE_CHANGE_NOTIFICATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_interface_change_notification) structure, which contains a Unicode string representing the interface instance's symbolic link. See [Using PnP Device Interface Change Notification](../kernel/using-pnp-device-interface-change-notification.md) for more information.

    A driver or other kernel-mode component can also call [**IoGetDeviceInterfaces**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces) to get a list of all registered, enabled device interface instances for a specific device interface class. The returned list contains pointers to the Unicode symbolic link strings that identify the device interface instances.

2.  Get a pointer to a device or file object that corresponds to an instance of the interface.

    To access a specific device object, the driver must call [**IoGetDeviceObjectPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer), passing the Unicode string for the required interface in the *ObjectName* parameter. To access a file object, the driver must call [**InitializeObjectAttributes**](/windows-hardware/drivers/ddi/wudfwdm/nf-wudfwdm-initializeobjectattributes), passing the Unicode string in the *ObjectName* parameter, and then pass the successfully initialized attribute structure in a call to [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile).

