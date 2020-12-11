---
title: WFP Layer Requirements and Restrictions
description: WFP Layer Requirements and Restrictions
keywords:
- processing packets WDK Windows Filtering Platform
- packet processing WDK Windows Filtering Platform
- layers for packet processing WDK Windows Filtering Platform
ms.date: 01/22/2019
ms.localizationpriority: medium
---

# WFP Layer Requirements and Restrictions


The following requirements and restrictions apply to WFP layers.

<a href="" id="forwarding-layer-------"></a>**Forwarding Layer**   
An IP packet will be delivered to the forwarding layer if IP forwarding is enabled for a packet that originates from, or is destined for, an address that is assigned to the computer and the packet is sent or received on a different interface than the interface on which the local address is assigned. By default, IP forwarding is disabled and can be enabled by using the **netsh interface ipv4 set interface** command for IPv4 forwarding or the **netsh interface ipv6 set interface** command for IPv6 forwarding.

The forwarding layer can forward each received fragment as it arrives or hold the fragments of an IP payload until all fragments have arrived and then forward them. This is known as *fragment grouping*. When fragment grouping is disabled (it is disabled by default), forwarded IP packet fragments are indicated to WFP one time. When fragment grouping is enabled, a fragment is indicated to WFP two times--first as the fragment itself, and again inside a fragment group that is described by a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) chain. WFP sets the **FWP\_CONDITION\_FLAG\_IS\_FRAGMENT\_GROUP** flag when it indicates fragment groups to forwarding layer callouts. You can enable fragment grouping by using the **netsh interface {ipv4|ipv6} set global groupforwardedfragments=enabled** command. Fragment grouping is different than reassembly, which is the reconstruction of the original IP packet at the destination host.

The [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure that is indicated at the forwarding layer can describe a full IP packet, an IP packet fragment, or an IP packet fragment group. While an IP packet fragment traverses the forwarding layer, it will be indicated two times to the callout: first as a fragment, and again, as a fragment inside a fragment group.

When a fragment group is indicated, the **FWP\_CONDITION\_FLAG\_IS\_FRAGMENT\_GROUP** flag is passed as an incoming value to the callout driver's [*classifyFn*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_classify_fn0) callout function. In this case, the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure pointed to by the *NetBufferList* parameter is the first node of a **NET\_BUFFER\_LIST** chain with each **NET\_BUFFER\_LIST** describing a packet fragment.

A forward injected packet will not be presented to any WFP layer. The injected packet can be indicated to the callout driver again. To prevent infinite looping, the driver should first call the [**FwpsQueryPacketInjectionState0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsquerypacketinjectionstate0) function before it continues with a call to the *classifyFn* callout function, and the driver should permit packets that have the injection state [**FWPS\_PACKET\_INJECTION\_STATE**](/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_packet_injection_state_) set to **FWPS\_PACKET\_INJECTED\_BY\_SELF** or **FWPS\_PACKET\_PREVIOUSLY\_INJECTED\_BY\_SELF** to pass through unaltered.

You can use the following command to view the current "Group Forwarded Fragments" setting for the system: **netsh interface {ipv4|ipv6} show global**.

<a href="" id="network-layer-------"></a>**Network Layer**   
IP packet fragments, which are indicated only for incoming paths, are indicated at three points at this layer: first as an IP packet, again as an IP fragment, and a third time as part of a reassembled IP packet. WFP sets the **FWP\_CONDITION\_FLAG\_IS\_FRAGMENT** flag when it indicates fragments to network layer callouts. 

For example, if a single IP packet is divided into four fragments, the indications for this packet occur as follows:

1. One indication for each "original" IP packet (4 classifications, or calls to the callout's classify function)
2. One indication for each "original fragment" (4 classifications)
3. One indication for the final reassembled IP packet (1 classification)

When adding filtering conditions, **FWP\_MATCH\_FLAGS\_NONE\_SET** can be used together with the **FWP\_CONDITION\_FLAG\_IS\_FRAGMENT** flag to avoid the second indication(s). These condition flags are meant to prevent classifications the callout driver does not care about. If the callout has to inspect only full packets (those that have not been fragmented and reassembled), it has to parse the IP header to avoid processing fragments that are indicated as IP packets. A callout might do the following steps to achieve this:

1. Skip the first indication(s) by checking if the More Fragments (MF) flag is set and/or the Fragment Offset field is not 0.
2. Write a filter that allows all classifications where **FWP_CONDITION_FLAG_IS_FRAGMENT** is set.
3. Perform whatever processing is needed on the reassembled packet.

 Alternatively, the callout can inspect packets at the transport layer.

<a href="" id="transport-layer-and-ale-------"></a>**Transport Layer and ALE**   
To be able to coexist with IPsec processing, callouts that inspect packets at the incoming transport layer must also register at the ALE receive and accept layer. Such a callout can inspect/modify most of the traffic at the transport layer, but it must also permit packets that are assigned to the ALE receive/accept layer. Such a callout must also inspect or modify the packets from the ALE layer. WFP sets the **FWPS\_METADATA\_FIELD\_ALE\_CLASSIFY\_REQUIRED** metadata flag when it indicates to the transport layer those packets that require ALE inspection. IPsec processing is deferred until those packets that create the initial "connection" and those that are required to re-authorize the connection reach the ALE layer.

Transport layer and ALE layer callouts must register themselves at a sublayer that is of lower weight than the universal sublayer. The built-in IPsec/ALE enforcement callouts reside at the universal sublayer.

The following table shows packet types that can be indicated at ALE layers. Be aware that some ALE layers do not always have a packet associated with their indication.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">ALE layer</th>
<th align="left">TCP packets</th>
<th align="left">UDP packets</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Bind (resource assignment)</p></td>
<td align="left"><p>not applicable</p></td>
<td align="left"><p>not applicable</p></td>
</tr>
<tr class="even">
<td align="left"><p>Connect</p></td>
<td align="left"><p>no packet</p></td>
<td align="left"><p>first UDP packet (outgoing)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Receive/Accept</p></td>
<td align="left"><p>SYN (incoming)</p></td>
<td align="left"><p>first UDP packet (incoming)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Flow Established</p></td>
<td align="left"><p>final ACK (incoming & outgoing)</p></td>
<td align="left"><p>first UDP packet (incoming & outgoing)</p></td>
</tr>
</tbody>
</table>

 

 

