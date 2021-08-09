---
title: Removing IEEE 1394 Virtual Devices
description: Removing IEEE 1394 Virtual Devices
keywords:
- emulation drivers WDK IEEE 1394 bus
- hardware emulation drivers WDK IEEE 1394 bus
- virtual devices WDK IEEE 1394 bus
- removing virtual devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Removing IEEE 1394 Virtual Devices





There are two methods of removing the physical device object (PDO) of a virtual device:

1.  **The standard Plug and Play (PnP) method of removing a device**. To use this method, have your driver send an [**IRP_MN_REMOVE_DEVICE**](../kernel/irp-mn-remove-device.md) request to the virtual device.

    The I/O stack should contain the following values:

    -   **MajorFunction** = IRP_MJ_PNP
    -   **MinorFunction** = IRP_MN_REMOVE_DEVICE

2.  **An I/O request packet (IRP) of type** IOCTL_IEEE1394_API_REQUEST: To use this method, have your driver send an [**IRP_MJ_DEVICE_CONTROL**](../kernel/irp-mj-device-control.md) request to the virtual device.

    The I/O stack should contain the following values:

    -   **MajorFunction** = IRP_MJ_DEVICE_CONTROL
    -   **Parameters.DeviceIoControl.IoControlCode** = [**IOCTL_IEEE1394_API_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537241)

    The IRP should contain the following values:

    -   **AssocicatedIrp.SystemBuffer-&gt;SystemBuffer** points to an [**IEEE1394_API_REQUEST**](/previous-versions/ff537204(v=vs.85)) structure
    -   **RequestNumber** member of IEEE1394_API_REQUEST = [**IEEE1394_API_REMOVE_VIRTUAL_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff537201)

The first method (IRP_MN_REMOVE_DEVICE) will remove the device, but if the device is persistent it will be restored the next time the computer initiates. The second method (IEEE1394_API_REMOVE_VIRTUAL_DEVICE) completely removes the device, so that it will no longer persist across reboots. The next time the computer starts up the device will not be restored.

Note that an upper-level driver or user-mode service can determine, through the usual PnP mechanism, which virtual devices are present. This mechanism uses the class GUID that is provided in the virtual driver's INF file.

 

