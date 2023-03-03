---
title: How drivers manage IEEE 1394 virtual devices
description: How drivers manage IEEE 1394 virtual devices
keywords:
- emulation drivers WDK IEEE 1394 bus
- hardware emulation drivers WDK IEEE 1394 bus
- virtual devices WDK IEEE 1394 bus
ms.date: 03/03/2023
ms.custom: contperf-fy22q3
---

# How drivers manage IEEE 1394 virtual devices

Upper-level drivers and user-mode services send [**IOCTL_IEEE1394_API_REQUEST**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) to manage virtual 1394 devices.

The driver supplies the device ID and instance ID in an [**IEEE1394_VDEV_PNP_REQUEST**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) structure.

To expose a virtual device on the 1394 bus, an emulation driver uses the following steps:

1. Send a [**REQUEST_SET_LOCAL_HOST_PROPERTIES**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) request to the bus driver with **u.SetLocalHostProperties.nLevel** member
    of the IRB set to SET_LOCAL_HOST_PROPERTIES_MODIFY_CROM in order to add a unit directory to the system's IEEE 1394 configuration ROM.
    This request also adds any other necessary configuration data to the configuration ROM in order to expose the emulated device functionality.
    The request must be sent using the virtual PDO that the emulation driver is associated with.

2. Issue a bus reset to inform the 1394 nodes present on the bus that the system configuration ROM has changed.

## Removing devices

There are two methods of removing the physical device object (PDO) of a virtual device:

1.  **The standard Plug and Play (PnP) method of removing a device**. The driver sends an [**IRP_MN_REMOVE_DEVICE**](../kernel/irp-mn-remove-device.md) request to the virtual device.

    The I/O stack should contain the following values:

    -   **MajorFunction** = IRP_MJ_PNP
    -   **MinorFunction** = IRP_MN_REMOVE_DEVICE

2.  **An I/O request packet (IRP) of type** IOCTL_IEEE1394_API_REQUEST: The driver sends an [**IRP_MJ_DEVICE_CONTROL**](../kernel/irp-mj-device-control.md) request to the virtual device.

    The I/O stack should contain the following values:

    -   **MajorFunction** = IRP_MJ_DEVICE_CONTROL
    -   **Parameters.DeviceIoControl.IoControlCode** = [**IOCTL_IEEE1394_API_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537241)

    The IRP should contain the following values:

    -   **AssocicatedIrp.SystemBuffer-&gt;SystemBuffer** points to an [**IEEE1394_API_REQUEST**](/previous-versions/ff537204(v=vs.85)) structure
    -   **RequestNumber** member of IEEE1394_API_REQUEST = [**IEEE1394_API_REMOVE_VIRTUAL_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff537201)

The first method (IRP_MN_REMOVE_DEVICE) removes the device, but if the device is persistent it will be restored the next time the computer initiates.
The second method (IEEE1394_API_REMOVE_VIRTUAL_DEVICE) completely removes the device, so that it will no longer persist across reboots.
The next time the computer starts up the device will not be restored.

Note that an upper-level driver or user-mode service can determine, through the usual PnP mechanism, which virtual devices are present.
This mechanism uses the class GUID that is provided in the virtual driver's INF file.

 