---
title: Implementing an NDIS 6.30 Driver
description: Implementing an NDIS 6.30 Driver
ms.date: 03/02/2023
---

# Implementing an NDIS 6.30 Driver


An NDIS 6.30 driver must follow the requirements that are defined in [Implementing an NDIS 6.20 Driver](implementing-an-ndis-6-20-driver.md).

In addition, an NDIS 6.30 driver must be compliant with the following requirements:

-   An NDIS 6.30 driver must report the correct NDIS version when it registers with NDIS.

    * You must update the major and minor NDIS version number in the NDIS\_*Xxx*\_DRIVER\_CHARACTERISTICS structure to support NDIS 6.30. The **MajorNdisVersion** member must contain **6** and the **MinorNdisVersion** member must contain **30**. This requirement applies to miniport, protocol, and filter drivers. You must also update the version information for the compiler, see [Compiling an NDIS 6.30 Driver](compiling-an-ndis-6-30-driver.md).

    * Miniport drivers must set the **Header** member of [**NDIS_MINIPORT_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics): Set **Revision** to NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2. 

    * Filter drivers must set the **Header** member of [**NDIS_FILTER_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics): Set **Revision** to NDIS_FILTER_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_2. 

    * Protocol drivers must set the **Header** member of [**NDIS_PROTOCOL_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_driver_characteristics): Set **Revision** to NDIS_PROTOCOL_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_PROTOCOL _DRIVER_CHARACTERISTICS_REVISION_2.

-   To inform NDIS and overlying drivers about device and driver capabilities, NDIS 6.30 drivers must implement the NDIS 6.30 device capability interfaces for the following features:

    -   [Virtualized Networking](virtualized-networking-enhancements-in-ndis-6-30.md)

    -   [Power Management](power-management-enhancements-in-ndis-6-30.md)

    -   [NDIS Quality of Service (QoS)](quality-of-service--qos--support-in-ndis-6-30.md)

-   NDIS 6.30 miniport drivers for the Windows 8 and Windows Server 2012 operating systems must use the NDIS 6.30 versions of data structures. For more information, see [Using NDIS 6.30 Data Structures](using-ndis-6-30-data-structures.md).

 

 





