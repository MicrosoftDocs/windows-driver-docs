---
title: Compile Flags for WDM Lower Edge
description: Compile Flags for WDM Lower Edge
keywords:
- NDIS-WDM miniport drivers WDK networking , compile flags
- NDIS-WDM miniport drivers WDK networking , building
- lower edge of NDIS miniport drivers WDK networking , compile flags
- WDM lower edge WDK networking , compile flags
- compile flags WDK NDIS-WDM
ms.date: 04/20/2017
---

# Compile Flags for WDM Lower Edge





You must include the following compile flags in the Sources file for an NDIS-WDM miniport driver to build the NDIS-WDM miniport driver:

-   -DNDIS\_WDM=1

    Directs NDIS to include the appropriate WDM header file.

Alternatively, you can embed compile flags at the start of the miniport driver's source code before the Ndis.h header file is included.

 

 





