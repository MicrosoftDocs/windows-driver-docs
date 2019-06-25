---
title: Creating NDIS Interfaces for NDIS Ports
description: Creating NDIS Interfaces for NDIS Ports
ms.assetid: 3a856e4d-e32a-4c8a-8fa0-9976966bdf87
keywords:
- ports WDK NDIS , creating NDIS interfaces
- NDIS ports WDK , creating NDIS interfaces
- registering NDIS interface providers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating NDIS Interfaces for NDIS Ports





By default, NDIS does not create an NDIS network interface for an NDIS port. If necessary, NDIS drivers can call the [**NdisIfRegisterProvider**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisifregisterprovider) function to register as an NDIS interface provider and call the [**NdisIfRegisterInterface**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisifregisterinterface) function to register an interface for a port.

For more information about NDIS network interfaces, see [NDIS 6.0 Network Interfaces](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_netvista/).

 

 





