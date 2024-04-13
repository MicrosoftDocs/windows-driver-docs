---
title: Using a Device Interface
description: Learn more about how to use a device interface
keywords:
- interface classes WDK device installations
- device interface classes WDK device installations
ms.date: 04/11/2022
---

# Using a device interface

Device interfaces are available to both kernel-mode components and user-mode applications. User-mode code can use [**CfgMgr32** functions](/windows/win32/api/cfgmgr32/) (for example, [CM_Get_Device_Interface_List](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_listw)) or **SetupDi***Xxx* functions (see [SetupDi device interface functions](using-device-installation-functions.md#ddk-setupdi-device-interface-functions-dg)) to find out about registered, enabled device interfaces. The user-mode application can then use I/O APIs such as [CreateFile](/windows/win32/api/fileapi/nf-fileapi-createfilew) to obtain a handle to the device in order to send I/O to it.  To get notified about the enablement and disablement of device interfaces and how to react to those actions, see [Registering for notification of device interface arrival and device removal](registering-for-notification-of-device-interface-arrival-and-device-removal.md).

Before a kernel-mode component can use a specific device or file object, it must do the following:

1. Determine whether the required device interface class is registered and enabled.

    A driver can register with the PnP manager to be notified when an instance of a device interface is enabled or disabled. To register, the component calls [**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification). This routine stores the address of a driver-supplied callback, which is called whenever an instance of a device interface instance is enabled or disabled, for a specified device class. The callback routines receive the [**DEVICE_INTERFACE_CHANGE_NOTIFICATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_interface_change_notification) structure, which contains a Unicode string representing the interface instance's symbolic link. See [Using PnP device interface change notification](../kernel/using-pnp-device-interface-change-notification.md) for more information.

    A driver or other kernel-mode component can also call [**IoGetDeviceInterfaces**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces) to get a list of all registered, enabled device interface instances for a specific device interface class. The returned list contains pointers to the Unicode symbolic link strings that identify the device interface instances.

2. Get a pointer to a device or file object that corresponds to an instance of the interface.

    To access a specific device object, the driver must call [**IoGetDeviceObjectPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer), passing the Unicode string for the required interface in the *ObjectName* parameter. To access a file object, the driver must call [**InitializeObjectAttributes**](/windows-hardware/drivers/ddi/wudfwdm/nf-wudfwdm-initializeobjectattributes), passing the Unicode string in the *ObjectName* parameter, and then pass the successfully initialized attribute structure in a call to [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile).
