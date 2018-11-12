---
title: Choosing a WAN Driver Model
description: Choosing a WAN Driver Model
ms.assetid: 63976cfa-6f7b-44d0-a4c5-de82254bedbd
keywords:
- WAN miniport drivers WDK networking , driver models
- WAN miniport drivers WDK networking , NDIS WAN vs CoNDIS WAN drivers
- driver models WDK WAN
- CoNDIS drivers WDK networking , WAN drivers
- CoNDIS WAN drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Choosing a WAN Driver Model





Microsoft Windows 2000 and later operating systems support two WAN driver models: NDIS WAN and CoNDIS WAN.

NDIS WAN miniport drivers are built on the NDIS model for connectionless miniport drivers. NDIS WAN miniport drivers are not supported for NDIS version 5.0 and later drivers. New drivers should be based on the CoNDIS WAN driver architecture.

CoNDIS WAN drivers are built on the connection-oriented NDIS (CoNDIS) driver model.

CoNDIS WAN miniport drivers and miniport call managers (MCMs) can:

-   Call the same NDIS functions that non-WAN connection-oriented miniport drivers call.

-   Export the same set of *MiniportXxx* functions that non-WAN connection-oriented miniport drivers export.

-   Provide additional WAN-specific capabilities.

For more information about CoNDIS drivers, see [Connection-Oriented NDIS](connection-oriented-ndis.md).

If you are writing a new WAN driver, we recommend that you use the CoNDIS WAN model.

Microsoft will continue to support existing NDIS WAN miniport drivers. You do not have to write CoNDIS drivers for old hardware.

The following topics describe the primary advantages of using the CoNDIS WAN model:

[CoNDIS WAN Is More Flexible](condis-wan-is-more-flexible.md)

[CoNDIS WAN Is Less Complex](condis-wan-is-less-complex.md)

[Other Benefits of CoNDIS WAN](other-benefits-of-condis-wan.md)

[Other NDIS Features Available to CoNDIS WAN Drivers](other-ndis-features-available-to-condis-wan-drivers.md)

 

 





