---
title: Faster filter drivers
description: Faster filter drivers
ms.assetid: df708a7d-70e9-4a29-bbd2-4e2b84ed493d
keywords:
- filter drivers WDK networking , NDIS
- NDIS filter drivers WDK
- intermediate drivers WDK networking , vs filter drivers
- NDIS intermediate drivers WDK , vs filter drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Faster filter drivers





The NDIS 6.x filter driver model supersedes the NDIS 5.x filter intermediate driver model. The new filter driver model enhances system performance in several ways:

-   Unlike an NDIS filter intermediate driver, an NDIS 6.0 or later filter driver is not implemented as a combination miniport driver and protocol driver. It has a unique interface that is similar to miniport and protocol drivers but is optimized for filtering information that is passed on a driver stack.

-   NDIS 6.0 and later filter drivers support bypass capabilities so that the driver does not process data when such processing is not required.

-   NDIS 6.0 and later filter drivers can be dynamically inserted into or removed from a driver stack during run time without tearing down bindings. Before such a dynamic operation occurs, NDIS 6.0 pauses all the NDIS drivers in the stack. NDIS restarts the stack when the reconfiguration is complete.

For more information about NDIS 6.0 filter drivers, see [NDIS 6.0 Filter Drivers](ndis-filter-drivers.md).

 

 





