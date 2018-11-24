---
title: Packet Indication Format
description: Packet Indication Format
ms.assetid: 37ee6db6-2f0e-4987-85e9-5362d23d7b27
keywords:
- packet indication WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Packet Indication Format


Network data is indicated in WFP as NDIS net buffer lists ([**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)). The **Next** member of the **NET\_BUFFER\_LIST** structure can be used to describe a *chain* of net buffer lists. WFP only indicates a single net buffer list to callouts (that is, netBufferList-&gt;Next == **NULL**), except for the following cases:

-   WFP can indicate net buffer list chains to callouts from the Stream layer.

-   WFP indicates net buffer list chains to callouts when it classifies IP packet fragment groups in the forward path to callouts. Each net buffer list inside the chain describes a single fragment.

Although a net buffer list can describe a whole packet, for different types of layers, WFP indicates net buffer lists to callouts at different offsets from the beginning of IP header. For example, at the incoming network layer, the net buffer list starts after the IP header, while at the incoming transport layer, the net buffer list starts after the transport header. IP and transport headers are always described by the first [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure inside a net buffer list.

Offsets into the net buffer lists are indicated to callouts by using the **ipHeaderSize** and **transportHeaderSize** members of the [**FWPS\_INCOMING\_METADATA\_VALUES0**](https://msdn.microsoft.com/library/windows/hardware/ff552397) structure. Callouts can use the NDIS functions [**NdisRetreatNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff564527) and [**NdisAdvanceNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff560703) to adjust the offset of the indicated net buffer lists. However in this case, the callout must undo the offset adjustment before it returns from the [*classifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff544890) function.

In a call to the *classifyFn* function for outgoing data, a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) can contain more than one [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure, each of which describes an IP packet. If some packets (for example, net buffers) in a net buffer list are acceptable, but others are not, a callout driver must do the following:

1.  Clone and block the whole net buffer list.

2.  Build a new net buffer list that describes the acceptable subset of net buffers.

3.  Inject the new net buffer list back into the send path.

Alternatively, the callout can unlink the unwanted net buffers from the net buffer list and inject the altered net buffer list back into the send path. However, in this case the callout driver must undo this modification to the cloned net buffer list before it calls the [**FwpsFreeCloneNetBufferList0**](https://msdn.microsoft.com/library/windows/hardware/ff551170) function. The callout driver must also save the original net buffer linkage information as part of its state data.

For more information about data offsets that are used by WFP, see [Data Offset Positions](https://msdn.microsoft.com/library/windows/hardware/ff546324).

**Note**  Callouts that work with decrypted IPSec ESP packets must use the data length of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure instead of MDL data to determine the packet length. To obtain the data length, use the [**NET\_BUFFER\_DATA\_LENGTH**](https://msdn.microsoft.com/library/windows/hardware/ff568382) macro. For more information, see [Developing IPsec-Compatible Callout Drivers](developing-ipsec-compatible-callout-drivers.md).

 

 

 





