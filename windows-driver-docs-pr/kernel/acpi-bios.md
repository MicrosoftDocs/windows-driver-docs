---
title: ACPI BIOS
description: ACPI BIOS
ms.assetid: 787e82ed-e58c-461f-abb6-71ed6cba411c
keywords: ["ACPI BIOS WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# ACPI BIOS





The integrated power management features supported by Microsoft Windows operating systems are available only on computers that have an Advanced Configuration and Power Interface (ACPI) BIOS.

Windows Server 2003, Windows XP, and Windows 2000 require that an ACPI BIOS be dated January 1, 1999 or later. However, if one of these Windows versions determines that such a BIOS is known to exhibit ACPI problems, the loader disables ACPI and instead uses Advanced Power Management (APM). Beginning with Windows Vista, the operating system supports only a computer with an ACPI-compliant BIOS that is dated January 1, 1999 or later.

Device Manager shows whether an individual computer supports ACPI. Check the driver information for the **Computer** device category.

For more information about ACPI, see the [ACPI 5.0 specification](https://www.uefi.org/specifications).

