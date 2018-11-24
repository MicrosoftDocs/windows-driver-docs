---
title: Identifying an NDIS Port
description: Identifying an NDIS Port
ms.assetid: 40917e62-5424-4c46-9b5b-a1a15812ef59
keywords:
- ports WDK NDIS , identifyng
- NDIS ports WDK , identifyng
- identifyng NDIS ports
- port numbers WDK NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Identifying an NDIS Port





An NDIS port is identified by its port number. When a miniport driver calls the [**NdisMAllocatePort**](https://msdn.microsoft.com/library/windows/hardware/ff562779) function to allocate a port, NDIS allocates and assigns the lowest available port number to the port. When a miniport driver calls the [**NdisMFreePort**](https://msdn.microsoft.com/library/windows/hardware/ff563588) function to free a port, NDIS also frees the port number that is assigned to the freed port so that NDIS can reuse the port number.

If a driver maintains separate context areas for each port, the driver must provide an efficient algorithm for translating the port number to the corresponding context area.

 

 





