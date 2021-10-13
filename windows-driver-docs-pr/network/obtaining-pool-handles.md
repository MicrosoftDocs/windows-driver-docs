---
title: Obtaining Pool Handles
description: Obtaining Pool Handles
keywords:
- pool handles WDK networking
- protocol drivers WDK networking , pool handles
- NDIS protocol drivers WDK , pool handles
- miniport drivers WDK networking , pool handles
- NDIS miniport drivers WDK , pool handles
- intermediate drivers WDK networking , po
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining Pool Handles





The following NDIS pool allocation functions require a handle to allocate resources:

-   [**NdisAllocateNetBufferPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferpool)

-   [**NdisAllocateNetBufferListPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlistpool)

NDIS 6.0 drivers obtain a handle as follows:

<a href="" id="protocol-drivers"></a>Protocol drivers  
Protocol drivers call the [**NdisRegisterProtocolDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) function to obtain a handle.

<a href="" id="miniport-drivers"></a>Miniport drivers  
NDIS calls the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function to pass the handle to the miniport driver.

<a href="" id="intermediate-drivers"></a>Intermediate drivers  
Intermediate drivers call the [**NdisRegisterProtocolDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) function to obtain a handle for pools used in send operations and NDIS calls *MiniportInitializeEx* to pass the handle to the intermediate driver for pools used in receive operations.

<a href="" id="filter-drivers"></a>Filter drivers  
NDIS calls the [*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach) function to pass the handle to the filter driver.

<a href="" id="other-drivers"></a>Other drivers  
If a driver cannot obtain a handle through one of the preceding methods, the driver can call the [**NdisAllocateGenericObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocategenericobject) function to get a handle.

 

