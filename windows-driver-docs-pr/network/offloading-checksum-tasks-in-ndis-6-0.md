---
title: Offloading Checksum Tasks in NDIS 6.0
description: Offloading Checksum Tasks in NDIS 6.0
ms.assetid: 00a73fbd-6e5a-483e-b638-982f0bf07f35
keywords:
- checksum tasks WDK networking
- task offload porting WDK networking , checksum tasks
- TCP/IP offload service porting WDK networking , checksum tasks
- offload service porting WDK networking , checksum tasks
- porting task offload services WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Offloading Checksum Tasks in NDIS 6.0





Offloading TCP/IP checksum tasks at run time in NDIS 6.0 is similar to NDIS 5.*x*. The primary differences are:

-   Send and receive operations in NDIS 6.0 use [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures instead of [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures.

-   Out-of-band (OOB) data in NDIS 6.0 is stored in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) information array. For more information about OOB data, see [Accessing TCP/IP Offload NET\_BUFFER\_LIST Information](accessing-tcp-ip-offload-net-buffer-list-information.md).

For more information about offloading TCP/IP checksum tasks, see [Offloading Checksum Tasks](offloading-checksum-tasks.md).

 

 





