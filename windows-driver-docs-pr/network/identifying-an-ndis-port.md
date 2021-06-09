---
title: Identifying an NDIS Port
description: Identifying an NDIS Port
keywords:
- ports WDK NDIS , identifyng
- NDIS ports WDK , identifyng
- identifyng NDIS ports
- port numbers WDK NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Identifying an NDIS Port





An NDIS port is identified by its port number. When a miniport driver calls the [**NdisMAllocatePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismallocateport) function to allocate a port, NDIS allocates and assigns the lowest available port number to the port. When a miniport driver calls the [**NdisMFreePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreeport) function to free a port, NDIS also frees the port number that is assigned to the freed port so that NDIS can reuse the port number.

If a driver maintains separate context areas for each port, the driver must provide an efficient algorithm for translating the port number to the corresponding context area.

 

