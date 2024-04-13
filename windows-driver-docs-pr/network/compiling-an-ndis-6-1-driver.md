---
title: Compiling an NDIS 6.1 driver
description: This section explains how to compile an NDIS 6.1 driver
keywords:
- NDIS WDK , compile flags
- compile flags WDK networking
ms.date: 03/02/2023
---

# Compiling an NDIS 6.1 Driver





The Build utility for Windows Server 2008 supports header versioning. Header versioning makes sure that NDIS 6.1 drivers use the appropriate NDIS 6.1 data structures at compile time. You must update the SOURCES file to indicate NDIS 6.1.

For each type of driver, add information to the SOURCES file as follows:

-   For a miniport driver, add NDIS61\_MINIPORT=1.

-   For a protocol driver, add NDIS61=1.

-   For a filter driver, add NDIS61=1.

 

 





