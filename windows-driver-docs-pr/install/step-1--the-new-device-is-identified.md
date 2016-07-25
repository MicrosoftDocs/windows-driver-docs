---
title: Step 1 The New Device is Identified
description: Step 1 The New Device is Identified
ms.assetid: e0df70ca-cea3-44a1-b5ff-407f72a216f9
---

# Step 1: The New Device is Identified


Before a driver is installed for a new device, the bus or hub driver to which the device is connected assigns a [hardware identifier (ID)](hardware-ids.md) to the device. Windows uses hardware IDs to find the closest match between a device and a [driver package](driver-packages.md) that contains the driver for the device. For more information about hardware IDs, see [Device Identification Strings](device-identification-strings.md).

The format of the hardware ID typically consists of the following:

-   A bus-specific prefix, such as PCI\\ or USB\\.
-   Vendor-specific identifiers for the device, such as a vendor, model, and revision identifier. The format of these identifiers within the hardware ID is also specific to the bus driver.

An independent hardware vendor (IHV) can also define one or more [compatible IDs](compatible-ids.md) for the device. Compatible IDs have the same format as hardware IDs; however, they are typically more generic than hardware IDs and do not require specific manufacturer or model information. Windows uses these identifiers to select a [driver package](driver-packages.md) for a device if the operating system cannot find a matching driver package for the device's hardware ID. IHVs specify one or more compatible IDs for the device within the driver package's [INF file](inf-files.md).

Windows uses hardware IDs and compatible IDs to search for a [driver package](driver-packages.md) for the device. It finds a matching driver package for the device by comparing the device's hardware IDs and compatible IDs against those IDs that are specified within the package's [INF file](inf-files.md).

For example, when a user plugs a wireless local area network (WLAN) adapter into the port of a USB hub that is attached to the computer, the following steps occur:

1.  The device is detected by the USB hub driver. Based on information that it queries from the adapter, the hub driver creates a hardware ID for the device.

    For example, the USB hub driver could create a hardware ID of USB\\VID\_1234&PID\_5678&REV\_0001 for the WLAN adapter, where:

    -   VID\_1234 is the identifier of the vendor.
    -   PID\_5678 is the product, or model, identifier of the device.
    -   REV\_0001 is the revision identifier of the device.

    For more information about the format of USB hardware IDs, see [Identifiers for USB Devices](identifiers-for-usb-devices.md).

2.  The USB hub driver notifies the [Plug and Play (PnP) manager](pnp-manager.md) that a new device was detected. The PnP manager queries the hub driver for all of the device's hardware IDs. The hub driver can create multiple hardware IDs for the same device.

3.  The [PnP manager](pnp-manager.md) notifies Windows that a new device needs to be installed. As part of this notification, Windows is provided with the list of hardware IDs.

4.  Windows starts a search for a [driver package](driver-packages.md) that matches one of the device's hardware IDs. If Windows cannot find a matching hardware ID, it searches for a driver package that has a matching compatible ID for the device.

    For more information about this process, see [Step 2: A Driver for the Device is Selected](step-2--a-driver-for-the-device-is-selected.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Step%201:%20The%20New%20Device%20is%20Identified%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




