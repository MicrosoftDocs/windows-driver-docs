---
title: Using NDIS 6.20 Data Structures
description: Using NDIS 6.20 Data Structures
ms.assetid: 19810a7c-91c1-4014-a364-2819d743627d
keywords:
- NDIS 6.20 WDK , data structures
- data structures WDK NDIS 6.20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using NDIS 6.20 Data Structures





NDIS can support multiple versions of the same data structure. NDIS 6.20 and later drivers that use updated structures must report the correct **Revision** member and **Size** member value in the [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure that is in the **Header** member of a structure, if any, when the drivers initialize NDIS 6.20 data structures.

**Note**  To determine the correct version and size information see the reference pages for each structure that includes a **Header** member. The reference pages for structures that contain a **Header** member and that have been updated for NDIS 6.20 include new information for NDIS 6.20 and later drivers. If there is no update to the structure for NDIS 6.20, the information that is provided for NDIS 6.0 or NDIS 6.1 drivers also applies to NDIS 6.20 and later drivers.

 

 

 





