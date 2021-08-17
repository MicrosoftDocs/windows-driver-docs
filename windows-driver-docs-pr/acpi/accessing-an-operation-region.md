---
title: Accessing an Operation Region
description: Provides information about accessing an operation region
keywords:
- ACPI devices WDK , operation regions
- operation regions WDK ACPI
- function drivers WDK ACPI , operation regions
- WDM function drivers WDK ACPI , operation regions
ms.date: 04/14/2021
ms.localizationpriority: medium
---

# Accessing an Operation Region

When a function driver registers an operation region handler, the driver must specify the access type ACPI_OPREGION_ACCESS_AS_COOKED. Cooked access supports transfer of information from an ACPI device to the device's function driver, but not from the function driver to the device.

Only the system-supplied ACPI driver modifies the data in an operation region. The function driver can read the data in an operation region. However, it must not modify the data. When called, an operation region handler transfers bytes in the operation region to and from the ACPI driver's data buffer. The ACPI driver manages accessing the correct bytes to read and write a data field in an operation region.

## See also

[RegisterOpRegionHandler](/windows-hardware/drivers/ddi/oprghdlr/nf-oprghdlr-registeropregionhandler)
