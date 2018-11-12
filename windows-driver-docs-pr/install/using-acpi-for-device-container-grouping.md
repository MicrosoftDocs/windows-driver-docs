---
title: Using ACPI for Device Container Grouping
description: Using ACPI for Device Container Grouping
ms.assetid: c49949cd-59e0-4ad2-a067-bc4e048f26c5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using ACPI for Device Container Grouping


Using ACPI settings to specify device container groupings is intended for use by computer original equipment manufacturers (OEMs). By configuring ACPI objects in the computer BIOS, it is possible to indicate the precise configuration of the computer. This capability is in addition to other device container grouping mechanisms that are described in this paper.

The use of ACPI to indicate the computer configuration has several advantages:

-   The settings persist in the computer BIOS and are preserved across operating system upgrades.

-   Windows evaluates ACPI settings after it evaluates bus driver-supplied Removable capabilities. Therefore, a manufacturer can use the ACPI settings to fix devices that are incorrectly reported as Removable and Windows can group the functionality into the computer's device container.

-   Using ACPI settings is especially useful for computer OEMs to indicate which USB ports are internal to the computer and which USB ports the user is capable of attaching external devices. For more information, see [Using ACPI to Configure USB Ports on a Computer](using-acpi-to-configure-usb-ports-on-a-computer.md).

    The computer OEM is strongly encouraged to configure the ACPI BIOS settings to accurately reflect the USB port topology of the computer. This ensures that USB devices physically integrated with the computer (for example, an internal Bluetooth radio or an integrated webcam) are grouped into the computer's device container. It also allows the operating system to better determine the boundary between the computer and externally attached devices, because devices attached to connectable/user-visible ports are assumed to be external devices.

For more information about how to use ACPI object settings for device container grouping, see the [Container Groupings in Windows 7](http://go.microsoft.com/fwlink/p/?linkid=158386) white paper

 

 





