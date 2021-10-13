---
title: Sending and receiving data in CoNDIS
description: Sending and receiving data in CoNDIS
keywords:
- virtual connections WDK CoNDIS , data transfers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending and receiving data in CoNDIS





Transferring data involves sending or receiving packets over an established and activated VC.

**Note**  Protocol drivers must not call [**NdisCoSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscosendnetbufferlists) to send data to a VC after calling [**NdisClCloseCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclclosecall) for that VC.

 

The CoNDIS send and receive functions are similar to connectionless send and receive functions. The primary difference between the CoNDIS and connectionless interfaces is the management of virtual connections (VCs). For more information about connectionless send and receive operations, see [Send and Receive Operations](send-and-receive-operations.md).

In a single function call, CoNDIS drivers can send multiple [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures with multiple [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structures on each NET\_BUFFER\_LIST structure. Also, CoNDIS drivers can indicate completed send operations for multiple NET\_BUFFER\_LIST structures with multiple NET\_BUFFER structures on each NET\_BUFFER\_LIST structure.

In the receive path, CoNDIS miniport drivers can provide a list of NET\_BUFFER\_LIST structures to indicate receives. Each NET\_BUFFER\_LIST that a miniport driver provides contains one NET\_BUFFER structure. Because a different protocol binding can process each NET\_BUFFER\_LIST structure, NDIS can independently return each NET\_BUFFER\_LIST structure to the miniport driver.

To support NDIS 5.*x* and earlier drivers, CoNDIS provides a translation layer between legacy [**NDIS\_PACKET**](/previous-versions/windows/hardware/network/ff557086(v=vs.85)) structures and the NET\_BUFFER-based structures. CoNDIS performs the necessary conversion between NET\_BUFFER structures and NDIS\_PACKET structures. To avoid degrading performance because of the translation, CoNDIS drivers must be updated to support NET\_BUFFER structures and should support multiple NET\_BUFFER\_LIST structures in all data paths.

This section includes the following topics:

[Sending NET\_BUFFER Structures from CoNDIS Drivers](sending-net-buffer-structures-from-condis-drivers.md)

[Receiving NET\_BUFFER Structures in CoNDIS Drivers](receiving-net-buffer-structures-in-condis-drivers.md)

 

