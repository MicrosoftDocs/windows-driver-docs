---
title: Implementing IPv6 NS Offload
description: This section describes how to implement IPv6 neighbor solicitation (NS) offload
ms.assetid: 48AACE46-4D39-49ED-90AD-F73E27D0CDBE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing IPv6 NS Offload


An NDIS protocol driver sends an IPv6 neighbor solicitation (NS) offload request as an [OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569763) OID request. To support these NS offload requests, miniports should do the following.

## Indicating How Many Offload Requests the Miniport Adapter Supports


A miniport driver sets the **NumNSOffloadIPv6Addresses** member of the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure to indicate how many NS offload requests the miniport adapter supports.

**Note**  Despite its name, the **NumNSOffloadIPv6Addresses** member contains the number of supported requests, not the number of addresses.

 

**Note**  Some Windows Hardware Certification requirements, such as **Device.Network.LAN.PM.PowMgmtNDIS** and **Device.Network.WLAN.WoWLAN.ImplementWakeOnWLAN**, specify that the miniport adapter must support at least 2 NS offload requests. (In other words, to meet these requirements, the value of **NumNSOffloadIPv6Addresses** must be at least 2.) For more information, see the [Windows 8 Hardware Certification Requirements](http://go.microsoft.com/fwlink/p/?linkid=268621).

 

Each NS offload request can contain 1 or 2 target addresses.

In addition, there are 2 types of NS messages: unicast and multicast. Miniport drivers must be prepared to match both types of NS message for each target address.

### Example

If a miniport driver sets the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) member of the **NumNSOffloadIPv6Addresses** structure to 3, then NDIS may send up to 3 [OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569763) requests of type **NdisPMProtocolOffloadIdIPv6NS**. Each OID\_PM\_ADD\_PROTOCOL\_OFFLOAD request may have exactly 1 or 2 addresses in the **TargetIPv6Addresses** member of the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure. Therefore, the miniport must support a 3 x 2 = 6 target addresses.

Because the miniport must match both unicast and multicast NS messages for each target address, the miniport should be able to match a total of 6 x 2 = 12 NS message patterns.

## Matching the NS Message


The NS message format is specified in [RFC 4861](http://go.microsoft.com/fwlink/p/?linkid=268370) section 4.3, "Neighbor Solicitation Message Format". The miniport should match the fields in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Match value</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Ethernet.EtherType</strong></td>
<td align="left"><p>0x86dd (IPv6)</p></td>
<td align="left"><p>Adjust as needed for non-Ethernet media types.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>IPv6.Version</strong></td>
<td align="left"><p>6</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>IPv6.NextHeader</strong></td>
<td align="left"><p>58 (ICMPv6)</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>IPv6.HopLimit</strong></td>
<td align="left"><p>255</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>IPv6.Destination</strong></td>
<td align="left"><p><strong>OID.TargetIPv6Addresses[x]</strong> or <strong>OID.SolicitedNodeIPv6Address</strong></p></td>
<td align="left"><p>The miniport must match both options for this field: <strong>OID.TargetIPv6Addresses[x]</strong> and <strong>OID.SolicitedNodeIPv6Address</strong>.</p>
<p>If this field is <strong>OID.TargetIPv6Addresses[x]</strong>, the NS message is a unicast message.</p>
<p>If this field is <strong>OID.SolicitedNodeIPv6Address</strong>, the NS message is a multicast message.</p>
<p><strong>OID.TargetIPv6Addresses</strong> is an array that can contain 1 or 2 addresses. If it contains 2 addresses, the miniport must match both of them. If the second address is &quot;0::0&quot;, it must be ignored, and a second match pattern must not be created.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>IPv6.ICMPv6.Type</strong></td>
<td align="left"><p>135 (NS)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>IPv6.ICMPv6.Code</strong></td>
<td align="left"><p>0</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>IPv6.ICMPv6.TargetAddress</strong></td>
<td align="left"><p><strong>OID.TargetIPv6Addresses[x]</strong></p></td>
<td align="left"><p><strong>OID.TargetIPv6Addresses[x]</strong> is an array that can contain 1 or 2 addresses.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>IPv6.Source</strong></td>
<td align="left"><p><strong>OID.RemoteIPv6Address</strong></p></td>
<td align="left"><p>If <strong>OID.RemoteIPv6Address</strong> is &quot;0::0&quot;, this field should be ignored.</p></td>
</tr>
</tbody>
</table>

 

## Sending the NA Message


Upon receiving the NS message, device firmware should perform the validation steps called out in [RFC 4861](http://go.microsoft.com/fwlink/p/?linkid=268370) section 7.1, "Message Validation", including validating checksums. If the incoming NS message passes all validation, then an NA message must be generated and sent as a reply. Its format is specified in [RFC 4861](http://go.microsoft.com/fwlink/p/?linkid=268370) section 4.4, "Neighbor Advertisement Message Format". The miniport should set the fields in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Value</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Ethernet.Destination</strong></td>
<td align="left"><strong>Ethernet.Source</strong></td>
<td align="left"><p>Copy this value from the NS frame. Adjust as needed for non-Ethernet media types.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Ethernet.Source</strong></td>
<td align="left"><p>The miniport’s current MAC address</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>IPv6.HopLimit</strong></td>
<td align="left"><p>255</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>IPv6.Source</strong></td>
<td align="left"><strong>IPv6.ICMPv6.TargetAddress</strong></td>
<td align="left"><p>Copy this value from the NS frame.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>IPv6.Destination</strong></td>
<td align="left"><strong>IPv6.Source</strong></td>
<td align="left"><p>Copy this value from the NS frame, unless the value of <strong>IPv6.Source</strong> was &quot;0::0&quot;. If the value of <strong>IPv6.Source</strong> was &quot;0::0&quot; set this field to &quot;FF02::1&quot;.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>IPv6.ICMPv6.Type</strong></td>
<td align="left"><p>136 (NA)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>IPv6.ICMPv6.Code</strong></td>
<td align="left"><p>0</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>IPv6.ICMPv6.RouterFlag</strong></td>
<td align="left"><p>0</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>IPv6.ICMPv6.SolicitedFlag</strong></td>
<td align="left"><p>0</p></td>
<td align="left"><p>If the value of <strong>IPv6.Source</strong> in the NS frame was &quot;0::0&quot;, set this field to 1.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>IPv6.ICMPv6.OverrideFlag</strong></td>
<td align="left"><p>1</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>IPv6.ICMPv6.TargetAddress</strong></td>
<td align="left"><strong>IPv6.ICMPv6.TargetAddress</strong></td>
<td align="left"><p>Copy this value from the NS frame.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>IPv6.ICMPv6.TLLAOption.Type</strong></td>
<td align="left"><p>2 (Target Link-layer Address)</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><strong>IPv6.ICMPv6.TLLAOption.Length</strong></td>
<td align="left"><p>1</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><strong>IPv6.ICMPv6.TLLAOption.LinkLayerAddress</strong></td>
<td align="left"><strong>OID.MacAddress</strong></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

 

 





