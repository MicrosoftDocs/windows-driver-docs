---
title: Compiling an NDIS 6.1 driver
description: This section explains how to compile an NDIS 6.1 driver
ms.assetid: 9606a91c-c1cb-4d93-b648-3829d1b51954
keywords:
- NDIS WDK , compile flags
- compile flags WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Compiling an NDIS 6.1 Driver





The Build utility for Windows Server 2008 supports header versioning. Header versioning makes sure that NDIS 6.1 drivers use the appropriate NDIS 6.1 data structures at compile time. You must update the SOURCES file to indicate NDIS 6.1.

For each type of driver, add information to the SOURCES file as follows:

-   For a miniport driver, add NDIS61\_MINIPORT=1.

-   For a protocol driver, add NDIS61=1.

-   For a filter driver, add NDIS61=1.

 

 





