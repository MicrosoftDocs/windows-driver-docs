---
title: Offloading the Segmentation of Large TCP Packets in NDIS 6.0
description: Offloading the Segmentation of Large TCP Packets in NDIS 6.0
ms.assetid: b602bb85-b597-4541-b536-732e5086e1ac
keywords:
- LSOV1 WDK networking
- large send offload WDK networking
- LSOV2 WDK networking
- task offload porting WDK networking , segmentation of large TCP packets
- TCP/IP offload service porting WDK networking , segmentation of large TCP packets
- offload servi
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Offloading the Segmentation of Large TCP Packets in NDIS 6.0





Offloading the segmentation of large TCP packets at run time in NDIS 6.0 is similar to NDIS 5.*x*. The primary differences are:

-   Send and receive operations in NDIS 6.0 use [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures instead of [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures.

-   Out-of-band (OOB) data in NDIS 6.0 is stored in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) information array. For more information about OOB data, see [Accessing TCP/IP Offload NET\_BUFFER\_LIST Information](accessing-tcp-ip-offload-net-buffer-list-information.md).

-   NDIS 6.0 supports an updated version of the NDIS 5.*x* large send offload (LSO) service, which is called large send offload version 1 (LSO1).

-   NDIS 6.0 supports large send offload version 2 (LSOV2), which provides enhanced large packet segmentation services, including support for IPv6.

For more information about the segmentation of large TCP packets for large send offload (LSO), see [Offloading the Segmentation of Large TCP Packets](offloading-the-segmentation-of-large-tcp-packets.md).

 

 





