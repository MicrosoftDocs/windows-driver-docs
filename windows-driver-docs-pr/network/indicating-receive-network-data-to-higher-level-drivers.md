---
title: Indicating Receive Network Data to Higher Level Drivers
description: Indicating Receive Network Data to Higher Level Drivers
ms.assetid: 27272427-86bc-4fd3-bd2f-12d94273fcd4
keywords:
- intermediate drivers WDK networking , receive operations
- NDIS intermediate drivers WDK , receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating Receive Network Data to Higher Level Drivers





A connectionless intermediate driver indicates receive network data to the next higher driver by calling the [**NdisMIndicateReceiveNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismindicatereceivenetbufferlists) function. A connection-oriented intermediate driver indicates receive network data to the next higher driver by calling the [**NdisMCoIndicateReceiveNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismcoindicatereceivenetbufferlists) function.

Before indicating the receive network data, the driver processes the data, perhaps converting it to the format expected by a higher-level driver, and if required, copying relevant data into MDLs that are associated with an intermediate-driver-allocated [**NET\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer) structure.

 

 





