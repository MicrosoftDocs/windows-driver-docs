---
title: Using ACPI for Device Container Grouping
description: Using ACPI for Device Container Grouping
ms.assetid: c49949cd-59e0-4ad2-a067-bc4e048f26c5
---

# Using ACPI for Device Container Grouping


Using ACPI settings to specify device container groupings is intended for use by computer original equipment manufacturers (OEMs). By configuring ACPI objects in the computer BIOS, it is possible to indicate the precise configuration of the computer. This capability is in addition to other device container grouping mechanisms that are described in this paper.

The use of ACPI to indicate the computer configuration has several advantages:

-   The settings persist in the computer BIOS and are preserved across operating system upgrades.

-   Windows evaluates ACPI settings after it evaluates bus driver-supplied Removable capabilities. Therefore, a manufacturer can use the ACPI settings to fix devices that are incorrectly reported as Removable and Windows can group the functionality into the computer's device container.

-   Using ACPI settings is especially useful for computer OEMs to indicate which USB ports are internal to the computer and which USB ports the user is capable of attaching external devices. For more information, see [Using ACPI to Configure USB Ports on a Computer](using-acpi-to-configure-usb-ports-on-a-computer.md).

    The computer OEM is strongly encouraged to configure the ACPI BIOS settings to accurately reflect the USB port topology of the computer. This ensures that USB devices physically integrated with the computer (for example, an internal Bluetooth radio or an integrated webcam) are grouped into the computer's device container. It also allows the operating system to better determine the boundary between the computer and externally attached devices, because devices attached to connectable/user-visible ports are assumed to be external devices.

For more information about how to use ACPI object settings for device container grouping, see the [Container Groupings in Windows 7](http://go.microsoft.com/fwlink/p/?linkid=158386) white paper on the Microsoft Windows Hardware Developer Central (WHDC) website.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20ACPI%20for%20Device%20Container%20Grouping%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




