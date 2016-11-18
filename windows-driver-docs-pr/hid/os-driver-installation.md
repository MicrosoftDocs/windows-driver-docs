---
title: OS Driver installation
author: windows-driver-content
description: This section documents the following class-specific INF file entries that a vendor can use to control how the Microsoft-supplied keyboard and mouse class installers install devices under Microsoft Windows 2000 and later.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: A934B1F3-01FA-4B70-92B8-9CB3EB096C89
---

# OS Driver installation


This section documents the following class-specific INF file entries that a vendor can use to control how the Microsoft-supplied keyboard and mouse class installers install devices under Microsoft Windows 2000 and later

:

[INF DDInstall.MigrateToDevNode Section](inf-ddinstall-migratetodevnode-section.md)

[INF SharedDriver Entry](inf-shareddriver-entry.md)

[INF PS2\_Inst.NoInterruptInit.Bioses Section](inf-ps2-inst-nointerruptinit-bioses-section.md)

[INF PS2\_Inst.NoInterruptInit Section](inf-ps2-inst-nointerruptinit-section.md)

For specific examples, see the usage of these INF file entries in keyboard.inf and msmouse.inf -- the Microsoft-supplied INF files for the keyboard and mouse device setup classes.

## General rules for PS/2 keyboards and mice


For every internal / integrated device connected via a PS/2-compatible controller, the Microsoft Windows operating system uses ACPI to construct a list of device identification strings for the device. The Plug and Play Manager uses these device identification strings to match a device to an INF file. Plug and Play device strings are divided into the following types:

-   A single unique Device ID (often just the first ID in the list of Hardware IDs)
-   An ordered list of Hardware IDs
-   An ordered list of Compatible IDs

The Plug and Play Manager always uses all the identifiers in the list when it tries to match a device to an INF file, but it tries to use the most specific identifier first. This allows the setup software to give preference to drivers in the order of their suitability, with those drivers supplied by the vendor being at the top of the priority list.

To locate a driver match, Setup compares the device's Hardware IDs and Compatible IDs (as reported by the device's parent bus driver) to the Hardware IDs and Compatible IDs listed in the INF files on the machine. If Setup finds more than one match, it assigns a "rank" to each possible driver match. The lower the rank number, the better match the driver is for the device.

To achieve the scenario described above, ACPI should report the following:

One or more Hardware IDs to identify the firmware and/or hardware model. Format of the HWID (as defined in ACPI specification V5.0) is as follows:

-   ACPI\\VEN\_vvvv&DEV\_dddd&SUBSYS\_ssssssss&REV\_rrrr
-   ACPI\\VEN\_vvvv&DEV\_dddd&SUBSYS\_ssssssss
-   ACPI\\VEN\_vvvv&DEV\_dddd&REV\_rrrr
-   ACPI\\VEN\_vvvv&DEV\_dddd&CLS\_cccc&SUBCLS\_nnnn&PI\_pp
-   ACPI\\VEN\_vvvv&DEV\_dddd
-   ACPI\\vvvdddd
-   ACPI\\vvvvdddd

One Compatible ID to allow the operating system to load a generic class driver. These Generic IDs are already listed in the keyboard and mouse INFs.

An example of a system with a correctly formatted PS/2 keyboard hardware ID is as follows:

-   Hardware ID: ACPI\\MSF0001;
-   Compatible ID: \*PNP0303

Notes:

-   Windows allows legacy (e.g. ACPI 4.0) style ACPI hardware IDs but prefers that they always identify a unique keyboard or mouse device.
-   The Windows Hardware Certification Kit includes the following requirement (System.Fundamentals.Input.PS2UniqueHWID). System manufacturers embedding keyboards and mice over PS/2 on mobile computing elements must ensure a unique hardware ID. The unique Hardware ID must be in a format that allows Windows Update (WU) to identify the device and load the correct drivers for it. This Windows 8 logo requirement applies to x86/64 mobile systems (no support for PS/2 on ARM systems)

For additional details, please refer to the MSDN whitepaper titled “Hardware IDs for PS/2 Input Devices on Laptops ”.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20OS%20Driver%20installation%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


