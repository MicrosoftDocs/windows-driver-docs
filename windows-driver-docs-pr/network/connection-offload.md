---
title: Connection Offload
description: Connection Offload
ms.assetid: 4c1b1a98-6ad3-4817-9e3d-d6112c887352
keywords:
- connection offload WDK TCP/IP transport
- TCP/IP offload WDK networking , connection offload
- offload WDK TCP/IP transport , connection offload
- connection offload WDK TCP/IP transport , about connection offload
- capabilities WDK TCP/IP offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connection Offload





To increase its performance, the Microsoft TCP/IP transport can offload connections to a NIC that has the appropriate TCP/IP-connection offload capabilities.

The NDIS connection offload interface provides hooks to enable configuration of connection offload services such as TCP chimney offload. For more information about connection offload services in NDIS, see [Offloading TCP/IP Connections](offloading-tcp-ip-connections.md).

TCP chimney offload services are supported in NDIS 6.0 and later.

This section includes:

-   [Determining Connection Offload Capabilities](determining-connection-offload-capabilities.md)
-   [Reporting a NIC's Connection Offload Capabilities](reporting-a-nic-s-connection-offload-capabilities.md)
-   [Enabling and Disabling Connection Offload Services](enabling-and-disabling-connection-offload-services.md)
-   [Determining the Current Connection Offload Settings](determining-the-current-connection-offload-settings.md)
-   [Using Registry Values to Enable and Disable Connection Offloading](using-registry-values-to-enable-and-disable-connection-offloading.md)
-   [Offloading TCP/IP Connections](offloading-tcp-ip-connections.md)

 

 





