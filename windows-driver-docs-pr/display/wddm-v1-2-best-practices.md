---
title: WDDM 1.2 best practices
description: To deliver the best experience in Windows 8 and later, Windows takes advantage of the graphics hardware paired with a Windows Display Driver Model (WDDM) 1.2 or later driver. This section summarizes the best practices.
ms.assetid: 130C66F0-1ACE-4C6E-AE16-AEFCD4847312
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDDM 1.2 best practices


To deliver the best experience in Windows 8 and later, Windows takes advantage of the graphics hardware paired with a Windows Display Driver Model (WDDM) 1.2 or later driver. This section summarizes the best practices.

**System manufacturers:**

-   Ensure the following cases are fully tested and work well with your system configurations:
    -   Compatible with Microsoft Basic Display Driver
    -   Updates on servers that don't need a reboot
-   Design new servers with WDDM hardware and adopt the relevant WDDM driver type that best suits your customer's needs.
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

 

 





