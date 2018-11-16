---
title: Creating IEEE 1394 Virtual Devices
description: Creating IEEE 1394 Virtual Devices
ms.assetid: 5b6a4d7a-e116-4a68-a1f8-fd561fbc0495
keywords:
- emulation drivers WDK IEEE 1394 bus
- hardware emulation drivers WDK IEEE 1394 bus
- virtual devices WDK IEEE 1394 bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating IEEE 1394 Virtual Devices





Upper-level drivers and user-mode services can add or remove virtual 1394 devices by means of a device control request with an [**IOCTL\_IEEE1394\_API\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537241) control code. The request contains an [**IEEE1394\_API\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537204) structure whose **RequestNumber** member indicates the action to be taken (addition or removal) by the bus driver. Since a virtual device has no device ID or instance ID, the driver or the user program that requests that a virtual device be created, must supply the device ID and instance ID in an [**IEEE1394\_VDEV\_PNP\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537206) structure.

When the IEEE1394\_REQUEST\_FLAG\_PERSISTENT is specified using IOCTL\_IEEE1394\_API\_REQUEST, the 1394 bus driver stores nonvolatile context information about the virtual device in the registry. This allows the bus driver to automatically recreate the virtual PDO on the next boot without intervention from an upper-level driver.

The bus driver uses this registry entry to "enumerate" a virtual device for each 1394 device stack in the system. After creating a virtual PDO for the virtual device, the 1394 bus driver calls [**IoInvalidateDeviceRelations**](https://msdn.microsoft.com/library/windows/hardware/ff549353), just as it would after creating a PDO for a real device. This call informs the Plug and Play (PnP) manager that a new device has arrived, and the PnP manager loads the driver for the virtual device.

If more than one 1394 host controller is present on the system, a virtual device that is defined in the registry is enumerated more than once. To ensure that each virtual device has a unique instance ID, the upper-level driver or user service that creates the virtual device should not specify a specific "hard-coded" instance ID for virtual devices on systems that have more than one 1394 host controller. Instead, the upper-level software should set the IEEE1394\_REQUEST\_FLAG\_USE\_LOCAL\_HOST\_EUI flag in the IEEE1394\_API\_REQUEST. If this flag is set, the next time the bus driver enumerates the device, it uses the instance ID of the host controller as the instance ID of the virtual device. Because each 1394 device stack will have a host controller with a unique instance ID, a virtual device, whose instance ID is the same as the instance ID of its host controller, will also have a unique instance ID.

In order to expose a virtual device on the 1394 bus, an emulation driver must add a unit directory for the virtual device using the following steps:

1.  Send a [**REQUEST\_SET\_LOCAL\_HOST\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/ff537663) request to the bus driver with **u.SetLocalHostProperties.nLevel** member of the IRB set to SET\_LOCAL\_HOST\_PROPERTIES\_MODIFY\_CROM in order to add a unit directory to the system's IEEE 1394 configuration ROM. This request also adds any other necessary configuration data to the configuration ROM in order to expose the emulated device functionality. The request must be sent using the virtual PDO that the emulation driver is associated with.

2.  Issue a bus reset to inform the 1394 nodes present on the bus that the system configuration ROM has changed.

 

 




