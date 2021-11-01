---
title: Implementing an NDIS 6.20 Driver
description: Implementing an NDIS 6.20 Driver
keywords:
- NDIS 6.20 WDK , implementing a driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing an NDIS 6.20 Driver





An NDIS 6.20 driver must report the correct NDIS version when it registers with NDIS: 

* You must update the major and minor NDIS version number in the NDIS\_*Xxx*\_DRIVER\_CHARACTERISTICS structure to support NDIS 6.20. The **MajorNdisVersion** member must contain 6 and the **MinorNdisVersion** member must contain 20. This requirement applies to miniport, protocol, and filter drivers. You must also update the version information for the compiler, see [Compiling an NDIS 6.20 Driver](compiling-an-ndis-6-20-driver.md).

* Miniport drivers must set the **Header** member of [**NDIS_MINIPORT_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics): Set **Revision** to NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2. 

* Filter drivers must set the **Header** member of [**NDIS_FILTER_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics): Set **Revision** to NDIS_FILTER_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_2. 

* Protocol drivers must set the **Header** member of [**NDIS_PROTOCOL_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_driver_characteristics): Set **Revision** to NDIS_PROTOCOL_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_PROTOCOL _DRIVER_CHARACTERISTICS_REVISION_2.

The NDIS 6.20 power management services are mandatory for NDIS 6.20 and later miniport drivers. For more information about the NDIS 6.20 power management interface, see [Power Management Enhancements in NDIS 6.20](power-management-enhancements-in-ndis-6-20.md).

The NDIS direct OID request interface is mandatory for NDIS 6.20 and later miniport drivers. For more information about the direct OIDs interface, see [Direct OID Request Interface in NDIS 6.1](direct-oid-request-interface-in-ndis-6-1.md).

To inform NDIS and overlying drivers about device and driver capabilities, NDIS 6.20 and later drivers must implement the NDIS 6.20 device capability interfaces for the following features:

-   [Power Management](power-management-enhancements-in-ndis-6-20.md)

-   [Receive Side Scaling (RSS)](./receive-side-scaling-version-2-rssv2-.md)

-   [Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq--in-ndis-6-20.md)

NDIS 6.20 and later drivers must support receive side throttle (RST) in receive interrupts. For more information about RST, see [Receive Side Throttle in NDIS 6.20](receive-side-throttle-in-ndis-6-20.md).

Replace code that uses obsolete interfaces with the NDIS 6.20 equivalents. For more information about obsolete functions, see [Obsolete Interfaces in NDIS 6.20](obsolete-interfaces-in-ndis-6-20.md). For information about updating structures to support NDIS 6.20 versions, see [Using NDIS 6.20 Data Structures](using-ndis-6-20-data-structures.md).

Use NDIS interfaces that support more than 64 processors, for example, use the NDIS 6.20 read and write lock interface. For more information about support for more than 64 processors, see [Support for More than 64 Processors in NDIS 6.20](support-for-more-than-64-processors-in-ndis-6-20.md).

 

