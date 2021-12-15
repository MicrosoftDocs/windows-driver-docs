---
title: Creating NDIS Interfaces for NDIS Ports
description: Creating NDIS Interfaces for NDIS Ports
keywords:
- ports WDK NDIS , creating NDIS interfaces
- NDIS ports WDK , creating NDIS interfaces
- registering NDIS interface providers
ms.date: 04/20/2017
---

# Creating NDIS Interfaces for NDIS Ports





By default, NDIS does not create an NDIS network interface for an NDIS port. If necessary, NDIS drivers can call the [**NdisIfRegisterProvider**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifregisterprovider) function to register as an NDIS interface provider and call the [**NdisIfRegisterInterface**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifregisterinterface) function to register an interface for a port.

For more information about NDIS network interfaces, see [NDIS 6.0 Network Interfaces](/windows-hardware/drivers/ddi/_netvista/).

 

