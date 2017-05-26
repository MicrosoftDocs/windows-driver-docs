---
title: WDDM 1.2 best practices
description: To deliver the best experience in Windows 8 and later, Windows takes advantage of the graphics hardware paired with a Windows Display Driver Model (WDDM) 1.2 or later driver. This section summarizes the best practices.
ms.assetid: 130C66F0-1ACE-4C6E-AE16-AEFCD4847312
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDDM 1.2 best practices


To deliver the best experience in Windows 8 and later, Windows takes advantage of the graphics hardware paired with a Windows Display Driver Model (WDDM) 1.2 or later driver. This section summarizes the best practices.

**System manufacturers:**

-   Ensure the following cases are fully tested and work well with your system configurations:
    -   Compatible with Microsoft Basic Display Driver
    -   Updates on servers that don't need a reboot
-   Design new servers with WDDM hardware and adopt the relevant WDDM driver type that best suits your customerâ€™s needs.
-   Work with graphics hardware vendors to get certified WDDM 1.2 drivers for validation.
-   For headless systems:
    -   System firmware should set the VGA Not Present flag in the IAPC\_BOOT\_ARCH field of the Fixed ACPI Description Table (FADT), and if there is any VBIOS, it should implement an empty mode list through the VESA BIOS Extensions (VBE).
    -   In the absence of VBE support, the headless system should not represent a working display through the Unified Extensible Firmware Interface (UEFI) Graphics Output Protocol (GOP).
-   See [Windows hardware certification](http://go.microsoft.com/fwlink/p/?linkid=325510) for validation and testing information.
-   Test a variety of hardware configurations on both desktops and mobile systems to ensure a solid end-user experience on Windows 8 and later.

**Graphics hardware vendors:**

-   Work with Microsoft to develop WDDM 1.2 drivers.
-   Test pre-release WDDM 1.2 drivers on Windows 8 and later.
-   Provide updated WDDM 1.x drivers to Microsoft for deployment through Windows Update.
-   In addition to the Windows certification test suite, validate graphics and gaming performance, application compatibility, and various self-host scenarios on each ASIC family.
-   Test WDDM 1.0 and 1.1 drivers on Windows 8 and later.
-   Make the full retail package for WDDM 1.2 drivers available as early as possible.

**Independent software vendors (ISVs):**

-   Test existing and upcoming Microsoft DirectX games with WDDM 1.2 drivers on Windows 8 and later.
-   Test individual applications on Windows 8 and later.
-   Take advantage of the Windows 8 DirectX feature improvements.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20WDDM%201.2%20best%20practices%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




