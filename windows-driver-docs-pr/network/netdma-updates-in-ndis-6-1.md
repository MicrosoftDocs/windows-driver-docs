---
title: NetDMA Updates in NDIS 6.1
description: NetDMA Updates in NDIS 6.1
keywords:
- NetDMA WDK networking , about NetDMA interface
ms.date: 03/02/2023
---

# NetDMA Updates in NDIS 6.1

>[!IMPORTANT]
> The NetDMA interface is not supported in Windows 8 and later.

The NetDMA interface provides offloading of direct memory access (DMA) to network interface cards (NICs) that support a NetDMA DMA engine. The Windows Server 2008 and Windows Vista with Service Pack 1 (SP1) operating systems add NetDMA versions 1.1 and 2.0. NDIS 6.1 and later drivers can use NetDMA version 1.0, 1.1, and 2.0 interfaces. These interfaces manage interactions with the DMA engine and manage DMA transfers at run-time.

The NetDMA interface is an optional service that is provided for NICs and other drivers.

For more information about NetDMA, see [NetDMA Drivers](/previous-versions/windows/hardware/network/netdma-drivers).
