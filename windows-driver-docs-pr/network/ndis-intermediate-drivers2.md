---
title: NDIS Intermediate Drivers
description: NDIS Intermediate Drivers
ms.assetid: 773d9711-fdea-4541-bb0d-6b07b50892fc
keywords:
- intermediate drivers WDK networking
- network drivers WDK , intermediate drivers
- NDIS WDK , intermediate drivers
- NDIS intermediate drivers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Intermediate Drivers





NDIS intermediate drivers interface between upper-level protocol drivers and miniport drivers. Some applications that might require an intermediate driver include:

-   Media translation between an old transport driver and a miniport driver that manages a media type unknown to the transport driver.

-   Data filtering for security or other purposes.

-   Load Balancing Failover (LBFO) solutions.

-   Monitoring and collecting of network data statistics.

Before attempting to write an intermediate driver, you should read about NDIS miniport and protocol drivers. For more information about NDIS miniport drivers, see [NDIS Miniport Drivers](ndis-miniport-drivers.md). For more information about NDIS protocol drivers, see [NDIS Protocol Drivers](ndis-protocol-drivers.md).

The following sections introduce intermediate drivers and describe how to create and install such drivers:

[Roadmap for Developing NDIS Intermediate Drivers](roadmap-for-developing-ndis-intermediate-drivers.md)

[Introduction to NDIS Intermediate Drivers](introduction-to-ndis-intermediate-drivers.md)

[Writing NDIS Intermediate Drivers](writing-ndis-intermediate-drivers.md)

[Intermediate Driver Design Concepts](intermediate-driver-design-concepts.md)

[Installing Intermediate Drivers](installing-an-intermediate-driver.md)

 

 





