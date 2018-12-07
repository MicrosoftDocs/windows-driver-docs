---
title: Delayed Acknowledgement Timer
description: Delayed Acknowledgement Timer
ms.assetid: f3004af1-b807-4bff-a388-32396202a8f6
keywords:
- timers WDK TCP chimney offload , delayed acknowledgement timers
- TCP timers WDK TCP chimney offload , delayed acknowledgement timers
- delayed acknowledgement timers WDK TCP chimney offload
- acknowledgement timers WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Delayed Acknowledgement Timer


\[The TCP chimney offload feature is deprecated and should not be used.\]

The count of the delayed acknowledgement (ACK) timer is not preserved across initiate offload and terminate offload operations.

Before offloading a TCP connection, the host stack stops its delayed ACK timer and sends any acknowledgements that need to be sent.

Before terminating the offload of a TCP connection, an offload target stops its delayed ACK timer and sends any acknowledgements that need to be sent.

 

 





