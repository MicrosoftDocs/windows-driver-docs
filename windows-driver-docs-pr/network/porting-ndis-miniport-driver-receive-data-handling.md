---
title: Porting NDIS Miniport Driver Receive Data Handling
description: Porting NDIS Miniport Driver Receive Data Handling
ms.assetid: d4c5ab42-049d-45ad-96d0-4563234410b5
keywords:
- receive operation porting WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting NDIS Miniport Driver Receive Data Handling





NDIS 6.0 miniport drivers indicate to NDIS a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures instead of [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures. NDIS forwards the NET\_BUFFER\_LIST structures to the appropriate overlying drivers.

With the exception of indicating the completion status of a receive operation in a NET\_BUFFER\_LIST structure, the semantics of indicating data is very similar to that of NDIS 5.*x* miniport drivers that call the [**NdisMIndicateReceivePacket**](https://msdn.microsoft.com/library/windows/hardware/ff553533) function. An NDIS 6.0 miniport driver calls the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function to indicate a linked list of NET\_BUFFER\_LIST structures.

If the miniport driver sets the **Status** member of the NET\_BUFFER\_LIST structure to NDIS\_STATUS\_RESOURCES, it can reclaim ownership of the NET\_BUFFER\_LIST structures as soon as **NdisMIndicateReceiveNetBufferLists** returns. If the miniport driver sets the **Status** member of the NET\_BUFFER\_LIST structure to NDIS\_STATUS\_SUCCESS, NDIS returns ownership of the NET\_BUFFER\_LIST structure by calling the miniport driver's [*MiniportReturnNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559437) function. This is analogous to calling an NDIS 5.*x* miniport driver's [**MiniportReturnPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550510) function.

For more information about miniport driver receive handling, see [Indicating Received Data from a Miniport Driver](indicating-received-data-from-a-miniport-driver.md).

 

 





