---
title: Indicating Received Data from a Miniport Driver
description: Indicating Received Data from a Miniport Driver
ms.assetid: da5d31e9-5212-4c6c-bac2-81432a46c303
keywords:
- receiving data WDK networking
- NdisMIndicateReceiveNetBufferLists
- indicatings WDK NDIS miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating Received Data from a Miniport Driver





The following figure illustrates a miniport driver receive indication.

![diagram illustrating a miniport driver receive indication](images/miniportreceive.png)

Miniport drivers call the [**NdisMIndicateReceiveNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismindicatereceivenetbufferlists) function to indicate the receipt of data from the network. The **NdisMIndicateReceiveNetBufferLists** function passes the indicated list of [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structures up the stack to overlying drivers.

If a miniport driver sets the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of [**NdisMIndicateReceiveNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismindicatereceivenetbufferlists), this indicates that the miniport driver must regain ownership of the [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structures immediately. In this case, NDIS does not call the miniport driver's [*MiniportReturnNetBufferLists*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_return_net_buffer_lists) function to return the **NET\_BUFFER\_LIST** structures. The miniport driver regains ownership immediately after **NdisMIndicateReceiveNetBufferLists** returns.

If a miniport driver does not set the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of [**NdisMIndicateReceiveNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismindicatereceivenetbufferlists), NDIS returns the indicated [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structures to the miniport driver's [*MiniportReturnNetBufferLists*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_return_net_buffer_lists) function. In this case, the miniport driver relinquishes ownership of the indicated structures until NDIS returns them to *MiniportReturnNetBufferLists*.

 

 





