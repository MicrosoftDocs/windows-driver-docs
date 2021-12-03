---
title: Step 1 The New Device is Identified
description: Step 1 The New Device is Identified
ms.date: 11/18/2021
ms.localizationpriority: High
---

# Step 1: The New Device is Identified

When a [bus driver](../kernel/bus-drivers.md) reports a new device to the Windows operating system, Windows needs to query information about this device from the bus driver to identify the device. This information is needed for, among other reasons, to identify the [driver package(s)](driver-packages.md) that may apply to this device.

The primary information needed from the [bus driver](../kernel/bus-drivers.md) in order to choose a driver package to install on the device are the device's [hardware identifiers (IDs)](hardware-ids.md) and [compatible IDs](compatible-ids.md). Windows uses these IDs to find the closest match between a device and a [driver package](driver-packages.md) in order to choose a driver package to install on the device. For more information about hardware IDs and compatible IDs, see [Device Identification Strings](device-identification-strings.md).

The format of a hardware ID or compatible ID typically consists of the following:

-   A bus-specific prefix, such as PCI\\ or USB\\.
-   Vendor-specific identifiers for the device, such as a vendor, model, and revision identifier. The format of these identifiers within the ID is also specific to the bus driver.

Compatible IDs are typically more generic than hardware IDs and may not include specific manufacturer or model information and may just represent the kind of device this hardware is. 

Windows uses hardware IDs and compatible IDs to search for a [driver package](driver-packages.md) for the device. It finds a matching driver package for the device by comparing the device's hardware IDs and compatible IDs against those IDs that are specified within the package's [INF file](overview-of-inf-files.md).

For example, when a user plugs a wireless local area network (WLAN) adapter into the port of a USB hub that is attached to the computer, the following steps occur:

1.  The device is detected by the USB hub driver. Based on information that it queries from the adapter, the hub driver creates a hardware ID for the device. For example, the USB hub driver could create a hardware ID of `USB\VID_1234&PID_5678&REV_0001` for the WLAN adapter. For more information about the format of USB hardware IDs, see [Identifiers for USB Devices](identifiers-for-usb-devices.md).

2.  The USB hub driver notifies the [Plug and Play (PnP) manager](pnp-manager.md) that a new device was detected. The PnP manager queries the hub driver for all of the device's hardware IDs and compatible IDs. The hub driver can create multiple hardware IDs and compatible IDs for the same device.

3.  Windows starts a search for a [driver package](driver-packages.md) in the [Driver Store](driver-store.md) that matches one of the device's hardware IDs. If Windows cannot find a matching hardware ID, it searches for a driver package that has a matching compatible ID for the device.

    For more information about this process, see [Step 2: A Driver for the Device is Selected](step-2--a-driver-for-the-device-is-selected.md).

Each bus driver constructs hardware IDs and compatible IDs in its own, bus-specific manner. For examples of standardized identifiers for other buses, see:

*  [Identifiers for PCI Devices](identifiers-for-pci-devices.md)
*  [Identifiers for SCSI Devices](identifiers-for-scsi-devices.md)
*  [Identifiers for IDE Devices](identifiers-for-ide-devices.md)
*  [Identifiers for PCMCIA Devices](identifiers-for-pcmcia-devices.md)
*  [Identifiers for ISAPNP Devices](identifiers-for-isapnp-devices.md)
*  [Identifiers for 1394 Devices](identifiers-for-1394-devices.md)
*  [Identifiers for Secure Digital (SD) Devices](identifiers-for-secure-digital--sd--devices.md)
*  [Identifiers for USB Devices](identifiers-for-usb-devices.md)


 





