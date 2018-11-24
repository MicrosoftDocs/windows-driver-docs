---
title: Offloading Internet Protocol Security Tasks in NDIS 6.0
description: Offloading Internet Protocol Security Tasks in NDIS 6.0
ms.assetid: 3c8461a5-63fe-429a-b133-3d3dd144f9e3
keywords:
- IPsec WDK networking
- task offload porting WDK networking , IPsec
- TCP/IP offload service porting WDK networking , IPsec
- offload service porting WDK networking , IPsec
- porting task offload services WDK networking , IPsec
- Internet protocol security
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Offloading Internet Protocol Security Tasks in NDIS 6.0





Offloading Internet protocol security (IPsec) tasks at run time in NDIS 6.0 is similar to NDIS 5.*x*. The primary differences are:

-   Send and receive operations in NDIS 6.0 use [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures instead of [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures.

-   Out-of-band (OOB) data in NDIS 6.0 is stored in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) information array. For more information about OOB data, see [Accessing TCP/IP Offload NET\_BUFFER\_LIST Information](accessing-tcp-ip-offload-net-buffer-list-information.md).

For more information about offloading IPsec tasks, see [Offloading IPsec Tasks](offloading-ipsec-tasks.md).

 

 





