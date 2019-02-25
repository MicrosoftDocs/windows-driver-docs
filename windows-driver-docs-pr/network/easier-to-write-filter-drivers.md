---
title: Easier-to-Write Filter Drivers
description: Easier-to-Write Filter Drivers
ms.assetid: 77cb7a9a-f823-4dfa-a0fc-11c174f34250
keywords:
- filter drivers WDK networking , writing filter drivers
- NDIS filter drivers WDK , writing filter drivers
- writing filter drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Easier-to-Write Filter Drivers





NDIS 6.0 filter drivers are easier to write than the previous NDIS filter intermediate drivers.

When compared to filter intermediate drivers, filter drivers provide the following implementation advantages:

-   Filter drivers do not include a complete miniport driver interface and a complete protocol driver interfaces.

-   Filter drivers do not create and manage a virtual device. There is no virtual miniport in a filter driver.

-   If a filter driver filters specific services, the driver can bypass other services. The driver does not require code for services that are bypassed. For example, if a filter driver filters OID requests but does not filter send and receive operations, the filter driver does not require send and receive entry points.

For more information about NDIS 6.0 filter drivers, see [NDIS 6.0 Filter Drivers](ndis-filter-drivers.md).

 

 





