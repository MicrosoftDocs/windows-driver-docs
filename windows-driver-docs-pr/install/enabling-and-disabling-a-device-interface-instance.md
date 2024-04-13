---
title: Enabling and Disabling a Device Interface Instance
description: Enabling and Disabling a Device Interface Instance
keywords:
- interface classes WDK device installations
- disabling device interface instances
- IoSetDeviceInterfaceState
- device interface classes WDK device installations
ms.date: 04/20/2017
---

# Enabling and Disabling a Device Interface Instance





After successfully starting the device, the driver that registered the interface calls [**IoSetDeviceInterfaceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacestate) to enable an interface instance. The driver passes the symbolic link name returned by [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) together with the Boolean value **TRUE** to enable the interface instance.

If the driver can successfully start its device, it should call this routine while handling the Plug and Play (PnP) manager's [**IRP_MN_START_DEVICE**](../kernel/irp-mn-start-device.md) request.

After the IRP_MN_START_DEVICE request completes, the PnP manager issues device interface arrival notifications to any kernel-mode or user-mode components that requested them. For more information, see [Registering for Device Interface Change Notification](../kernel/registering-for-device-interface-change-notification.md).

To disable a device interface instance, a driver calls [**IoSetDeviceInterfaceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacestate), passing the *SymbolicLinkName* returned by [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) and **FALSE** as the value of *Enable*.

A driver should disable a device's interfaces when it handles an [**IRP_MN_SURPRISE_REMOVAL**](../kernel/irp-mn-surprise-removal.md) or [**IRP_MN_REMOVE_DEVICE**](../kernel/irp-mn-remove-device.md) request for the device. If a driver does not disable a device's interfaces when it handles these removal IRPs, it must not subsequently attempt to do this because the PnP manager will disable the interfaces when it removes the device.

A driver should not disable the interfaces when the device is stopped ([**IRP_MN_STOP_DEVICE**](../kernel/irp-mn-stop-device.md)); instead, it should leave any device interfaces enabled and queue I/O requests until it receives another [**IRP_MN_START_DEVICE**](../kernel/irp-mn-start-device.md) request. Similarly, a driver should not disable its interfaces when the device is put in a sleep state. It should queue I/O requests until the device wakes up. For more information, see [Supporting Devices that Have Wake-Up Capabilities](../kernel/supporting-devices-that-have-wake-up-capabilities.md).

 

