---
title: Accessing an Operation Region
description: Accessing an Operation Region
ms.assetid: 9a1aa29e-679c-4f7f-a16c-3e1c94be66a7
keywords:
- ACPI devices WDK , operation regions
- operation regions WDK ACPI
- function drivers WDK ACPI , operation regions
- WDM function drivers WDK ACPI , operation regions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing an Operation Region





When a function driver registers an operation region handler, the driver must specify the access type ACPI\_OPREGION\_ACCESS\_AS\_COOKED. Cooked access supports transfer of information from an ACPI device to the device's function driver, but not from the function driver to the device.

Only the system-supplied ACPI driver modifies the data in an operation region. The function driver can read the data in an operation region. However, it must not modify the data. When called, an operation region handler transfers bytes in the operation region to and from the ACPI driver's data buffer. The ACPI driver manages accessing the correct bytes to read and write a data field in an operation region.

 

 




