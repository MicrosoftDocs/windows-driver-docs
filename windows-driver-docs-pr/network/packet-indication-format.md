---
title: Packet Indication Format
description: Packet Indication Format
keywords:
- packet indication WDK Windows Filtering Platform
ms.date: 04/20/2017
---

# Packet Indication Format


Network data is indicated in WFP as NDIS net buffer lists ([**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list)). The **Next** member of the **NET\_BUFFER\_LIST** structure can be used to describe a *chain* of net buffer lists. WFP only indicates a single net buffer list to callouts (that is, netBufferList-&gt;Next == **NULL**), except for the following cases:

-   WFP can indicate net buffer list chains to callouts from the Stream layer.

-   WFP indicates net buffer list chains to callouts when it classifies IP packet fragment groups in the forward path to callouts. Each net buffer list inside the chain describes a single fragment.

Although a net buffer list can describe a whole packet, for different types of layers, WFP indicates net buffer lists to callouts at different offsets from the beginning of IP header. For example, at the incoming network layer, the net buffer list starts after the IP header, while at the incoming transport layer, the net buffer list starts after the transport header. IP and transport headers are always described by the first [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure inside a net buffer list.

Offsets into the net buffer lists are indicated to callouts by using the **ipHeaderSize** and **transportHeaderSize** members of the [**FWPS\_INCOMING\_METADATA\_VALUES0**](/windows-hardware/drivers/ddi/fwpsk/ns-fwpsk-fwps_incoming_metadata_values0_) structure. Callouts can use the NDIS functions [**NdisRetreatNetBufferDataStart**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisretreatnetbufferdatastart) and [**NdisAdvanceNetBufferDataStart**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisadvancenetbufferdatastart) to adjust the offset of the indicated net buffer lists. However in this case, the callout must undo the offset adjustment before it returns from the [*classifyFn*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_classify_fn0) function.

In a call to the *classifyFn* function for outgoing data, a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) can contain more than one [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure, each of which describes an IP packet. If some packets (for example, net buffers) in a net buffer list are acceptable, but others are not, a callout driver must do the following:

1.  Clone and block the whole net buffer list.

2.  Build a new net buffer list that describes the acceptable subset of net buffers.

3.  Inject the new net buffer list back into the send path.

Alternatively, the callout can unlink the unwanted net buffers from the net buffer list and inject the altered net buffer list back into the send path. However, in this case the callout driver must undo this modification to the cloned net buffer list before it calls the [**FwpsFreeCloneNetBufferList0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsfreeclonenetbufferlist0) function. The callout driver must also save the original net buffer linkage information as part of its state data.

For more information about data offsets that are used by WFP, see [Data Offset Positions](./data-offset-positions.md).

**Note**  Callouts that work with decrypted IPSec ESP packets must use the data length of the [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure instead of MDL data to determine the packet length. To obtain the data length, use the [**NET\_BUFFER\_DATA\_LENGTH**](/windows-hardware/drivers/ddi/nblaccessors/nf-nblaccessors-net_buffer_data_length) macro. For more information, see [Developing IPsec-Compatible Callout Drivers](developing-ipsec-compatible-callout-drivers.md).

 

 

