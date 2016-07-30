---
title: Removing IEEE 1394 Virtual Devices
author: windows-driver-content
description: Removing IEEE 1394 Virtual Devices
MS-HAID:
- '1394-configrom\_ed5ffff1-cea2-43e1-8ec8-3b5f76aeca96.xml'
- 'IEEE.removing\_ieee\_1394\_virtual\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ea2d4b9e-7774-42dc-98dd-d95298012d72
keywords: ["emulation drivers WDK IEEE 1394 bus", "hardware emulation drivers WDK IEEE 1394 bus", "virtual devices WDK IEEE 1394 bus", "removing virtual devices"]
---

# Removing IEEE 1394 Virtual Devices


## <a href="" id="ddk-removing-ieee-1394-virtual-devices-kg"></a>


There are two methods of removing the physical device object (PDO) of a virtual device:

1.  **The standard Plug and Play (PnP) method of removing a device**. To use this method, have your driver send an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request to the virtual device.

    The I/O stack should contain the following values:

    -   **MajorFunction** = IRP\_MJ\_PNP
    -   **MinorFunction** = IRP\_MN\_REMOVE\_DEVICE

2.  **An I/O request packet (IRP) of type** IOCTL\_IEEE1394\_API\_REQUEST: To use this method, have your driver send an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request to the virtual device.

    The I/O stack should contain the following values:

    -   **MajorFunction** = IRP\_MJ\_DEVICE\_CONTROL
    -   **Parameters.DeviceIoControl.IoControlCode** = [**IOCTL\_IEEE1394\_API\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537241)

    The IRP should contain the following values:

    -   **AssocicatedIrp.SystemBuffer-&gt;SystemBuffer** points to an [**IEEE1394\_API\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537204) structure
    -   **RequestNumber** member of IEEE1394\_API\_REQUEST = [**IEEE1394\_API\_REMOVE\_VIRTUAL\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff537201)

The first method (IRP\_MN\_REMOVE\_DEVICE) will remove the device, but if the device is persistent it will be restored the next time the computer initiates. The second method (IEEE1394\_API\_REMOVE\_VIRTUAL\_DEVICE) completely removes the device, so that it will no longer persist across reboots. The next time the computer starts up the device will not be restored.

Note that an upper-level driver or user-mode service can determine, through the usual PnP mechanism, which virtual devices are present. This mechanism uses the class GUID that is provided in the virtual driver's INF file.

 

 


--------------------


