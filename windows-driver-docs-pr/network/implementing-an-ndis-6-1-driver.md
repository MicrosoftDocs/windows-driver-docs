---
title: Implementing an NDIS 6.1 Driver
description: Implementing an NDIS 6.1 Driver
keywords:
- NDIS WDK , versions in network drivers
ms.date: 03/02/2023
---

# Implementing an NDIS 6.1 Driver





An NDIS 6.1 driver must report the correct NDIS version when it registers with NDIS:

* You must update the major and minor NDIS version number in the NDIS\_*Xxx*\_DRIVER\_CHARACTERISTICS structure to support NDIS 6.1. The **MajorNdisVersion** member must contain 0x06 and the **MinorNdisVersion** member must contain 0x01. This requirement applies to miniport, protocol, and filter drivers.

* Miniport drivers must set the **Header** member of [**NDIS_MINIPORT_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics): Set **Revision** to NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2. 

* Filter drivers must set the **Header** member of [**NDIS_FILTER_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics): Set **Revision** to NDIS_FILTER_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_2. 

* Protocol drivers must set the **Header** member of [**NDIS_PROTOCOL_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_driver_characteristics): Set **Revision** to NDIS_PROTOCOL_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_PROTOCOL _DRIVER_CHARACTERISTICS_REVISION_2.

 

 





