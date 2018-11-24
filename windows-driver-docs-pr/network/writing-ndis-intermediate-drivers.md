---
title: Writing NDIS Intermediate Drivers
description: Writing NDIS Intermediate Drivers
ms.assetid: c37224b2-8d96-44c2-8b56-884089b9cfcd
keywords:
- intermediate drivers WDK networking
- network drivers WDK , intermediate drivers
- NDIS WDK , intermediate drivers
- NDIS intermediate drivers WDK
- NDIS intermediate drivers WDK , NDIS 6.0
- intermediate drivers WDK networking , NDIS 6.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing NDIS Intermediate Drivers





Unless noted otherwise, NDIS intermediate drivers provide the same services as miniport drivers and protocol drivers. The intermediate driver's miniport edge provides miniport driver services and the protocol edge provides protocol driver services. (For more information, see [Writing NDIS Miniport Drivers](writing-ndis-miniport-drivers.md) and [Writing NDIS Protocol Drivers](writing-ndis-protocol-drivers.md).)The initialization for NDIS 6.0 and later intermediate drivers is different from the initialization for legacy intermediate drivers. Also, NDIS 6.0 and later drivers can register as a combined miniport-intermediate driver.

The following topics provide more information about intermediate driver initialization:

-   [Initializing an Intermediate Driver](initializing-an-intermediate-driver.md)
-   [Initializing a Miniport-Intermediate Driver](initializing-a-miniport-intermediate-driver.md)
-   [Unloading an Intermediate Driver](unloading-an-intermediate-driver.md)
-   [Initializing a Virtual Miniport](initializing-a-virtual-miniport.md)
-   [Halting a Virtual Miniport](halting-a-virtual-miniport.md)

 

 





