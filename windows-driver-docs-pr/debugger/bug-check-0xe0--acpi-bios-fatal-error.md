---
title: Bug Check 0xE0 ACPI_BIOS_FATAL_ERROR
description: The ACPI_BIOS_FATAL_ERROR bug check has a value of 0x000000E0. This indicates that one of your computer components is faulty.
ms.assetid: 4cc4c96e-6e0e-4bf1-8e72-4e6f39848914
keywords: ["Bug Check 0xE0 ACPI_BIOS_FATAL_ERROR", "ACPI_BIOS_FATAL_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ACPI_BIOS_FATAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xE0: ACPI\_BIOS\_FATAL\_ERROR


The ACPI\_BIOS\_FATAL\_ERROR bug check has a value of 0x000000E0. This indicates that one of your computer components is faulty.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ACPI\_BIOS\_FATAL\_ERROR Parameters


The parameters for this bug check are issued by the BIOS, not by Windows. They can only be interpreted by the hardware vendor.

Cause
-----

Your computer's BIOS has reported that a component in the system is so faulty that there is no way for Windows to operate. The BIOS is indicating that there is no alternative but to issue a bug check.

Resolution
----------

You can determine which component is faulty by running the diagnostic disk or tool that was included with your computer.

If you do not have this tool, you must contact the system vendor and report this error message to them. They will be able to help you correct this hardware problem. This enables Windows to operate.

Microsoft cannot address this error. Only the hardware vendor is qualified to analyze it.

 

 




