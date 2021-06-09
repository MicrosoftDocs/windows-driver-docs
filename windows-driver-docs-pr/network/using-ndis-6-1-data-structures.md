---
title: Using NDIS 6.1 Data Structures
description: Using NDIS 6.1 Data Structures
keywords:
- data structures WDK networking
- NDIS WDK , structures
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using NDIS 6.1 Data Structures





NDIS can support multiple versions of the same data structure. NDIS 6.1 drivers that use updated structures in Windows Server 2008, Windows Vista with Service Pack 1 (SP1), or both operating systems must report the correct **Revision** member and **Size** member value in the [**NDIS\_OBJECT\_HEADER**](/windows-hardware/drivers/ddi/objectheader/ns-objectheader-ndis_object_header) structure that is in the **Header** member of a structure, if any, when the drivers initialize NDIS 6.1 data structures.

**Note**  To determine the correct version and size information, see the reference pages for each structure that includes a **Header** member. The reference pages for structures that contain a **Header** member and that have been updated for NDIS 6.1 include new information for NDIS 6.1 drivers. If there is no update to the structure for NDIS 6.1, the information that is provided for NDIS 6.0 drivers also applies to NDIS 6.1 drivers.

 

 

