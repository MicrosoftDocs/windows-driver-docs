---
title: Added Costs for Testing Vulnerable NDIS Drivers
description: Added Costs for Testing Vulnerable NDIS Drivers
ms.assetid: ee748650-92e6-4885-895e-c030cf33f315
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Added Costs for Testing Vulnerable NDIS Drivers





We recommend that you remove any code that parses the packet payload, particularly in handling offload verification, from your driver's packet handling dispatch routines. To have confidence in such code, you would have to extensively test the drivers to make sure that all potential error conditions are handled safely and correctly. This kind of testing means increased testing costs.

Miniport drivers should avoid parsing the packet data. They should not try to handle offload operations that the hardware cannot handle. In the receive side of the system, be very careful about how your driver inspects packet payload information. The send side of the driver could also be potentially affected with routed/bridged system configurations.

 

 





