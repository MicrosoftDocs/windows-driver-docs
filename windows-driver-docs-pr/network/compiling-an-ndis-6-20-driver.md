---
title: Compiling an NDIS 6.20 driver
description: This section explains how to compile an NDIS 6.20 driver
ms.assetid: 07940d98-63fb-4629-943c-f56ebdfcdd76
keywords:
- NDIS 6.20 WDK , compiling a driver
- compiling an NDIS 6.20 driver WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Compiling an NDIS 6.20 Driver





The Build utility for Windows 7 and later supports header versioning. Header versioning makes sure that NDIS 6.20 drivers use the appropriate NDIS 6.20 data structures at compile time. You must update the SOURCES file to indicate NDIS 6.20.

For each type of driver, add information to the SOURCES file as follows:

-   For a miniport driver, add NDIS620\_MINIPORT=1.

-   For a protocol driver, add NDIS620=1.

-   For a filter driver, add NDIS620=1.

 

 





