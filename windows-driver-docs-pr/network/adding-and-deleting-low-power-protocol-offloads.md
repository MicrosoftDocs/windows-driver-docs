---
title: Adding and Deleting Low Power Protocol Offloads
description: Adding and Deleting Low Power Protocol Offloads
ms.assetid: f00f13b4-9204-4480-884a-407684a4b2d4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding and Deleting Low Power Protocol Offloads





To add a low power protocol offload, NDIS protocol drivers issue an OID set request of [OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569763). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure.

**Note**  If an incoming packet matches both an offloaded protocol and a pattern (for example, because of a configuration error), the network adapter should respond to the packet and wake up the computer.

 

The [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566765) structure includes the following information:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Priority</strong></p></td>
<td align="left"><p>Contains the priority of the protocol offload. If an overlying driver adds a higher priority protocol offload when there are no resources available for more protocol offloads, NDIS might remove a lower priority protocol offload to free resources. Miniport drivers should ignore this member. Protocol drivers can provide any value within the predefined range from NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_LOWEST to NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_HIGHEST.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ProtocolOffloadType</strong></p></td>
<td align="left"><p>Contains an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566765" data-raw-source="[&lt;strong&gt;NDIS_PM_PROTOCOL_OFFLOAD_TYPE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566765)"><strong>NDIS_PM_PROTOCOL_OFFLOAD_TYPE</strong></a> value that specifies the type of protocol offload.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FriendlyName</strong></p></td>
<td align="left"><p>Contains an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566753" data-raw-source="[&lt;strong&gt;NDIS_PM_COUNTED_STRING&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566753)"><strong>NDIS_PM_COUNTED_STRING</strong></a> structure that contains the user-readable description of the low power protocol offload.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ProtocolOffloadId</strong></p></td>
<td align="left"><p>Contains an NDIS-provided value that identifies the offloaded protocol. Before NDIS sends the OID request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569763" data-raw-source="[OID_PM_ADD_PROTOCOL_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569763)">OID_PM_ADD_PROTOCOL_OFFLOAD</a> down to the underlying NDIS drivers or completes the request to the overlying driver, NDIS sets <strong>ProtocolOffloadId</strong> to a value that is unique among the protocol offloads on a network adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>NextProtocolOffloadOffset</strong></p></td>
<td align="left"><p>Contains the offset, the beginning of the OID request <em>InformationBuffer</em>, to the next <a href="https://msdn.microsoft.com/library/windows/hardware/ff566760" data-raw-source="[&lt;strong&gt;NDIS_PM_PROTOCOL_OFFLOAD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566760)"><strong>NDIS_PM_PROTOCOL_OFFLOAD</strong></a> structure in a list for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff569769" data-raw-source="[OID_PM_PROTOCOL_OFFLOAD_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569769)">OID_PM_PROTOCOL_OFFLOAD_LIST</a> OID. For more information about OID_PM_PROTOCOL_OFFLOAD_LIST, see <a href="obtaining-the-current-parameter-settings-of-low-power-protocol-offload.md" data-raw-source="[Obtaining the Current Parameter Settings of Low Power Protocol Offloads](obtaining-the-current-parameter-settings-of-low-power-protocol-offload.md)">Obtaining the Current Parameter Settings of Low Power Protocol Offloads</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ProtocolOffloadParameters</strong></p></td>
<td align="left"><p>Contains one of the <strong>IPv4ARPParameters</strong>, <strong>IPv6NSParameters</strong>, or <strong>Dot11RSNRekeyParameters</strong> structures in a union.</p>
<p></p>
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IPv4ARPParameters</p></td>
<td align="left"><p>Contains IPv4 ARP parameters.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IPv6NSParameters</p></td>
<td align="left"><p>Contains IPv6 Neighbor Solicitation (NS) parameters.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Dot11RSNRekeyParameters</p></td>
<td align="left"><p>Contains IEEE 802.11 robust secure network (RSN) handshake parameters</p></td>
</tr>
</tbody>
</table>
<p> </p></td>
</tr>
</tbody>
</table>

 

NDIS assigns an identifier that is unique for a network adapter to every offloaded protocol. The protocol offload identifier is a unique value for each of the protocols that are offloaded on a network adapter. However, the protocol offload identifier is not globally unique across all network adapters. NDIS passes this identifier to the underlying miniport driver when NDIS sends the [OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569763) OID request to the miniport driver. If offloading the protocol is successful, NDIS returns the identifier to the overlying driver that offloaded the protocol. The overlying driver uses the identifier to remove a previously offloaded protocol. The protocol offload identifier is also used in status indications to the upper layer drivers when an offloaded protocol is removed from a network adapter.

Protocol drivers must remove all of the offloaded protocols from a network adapter before closing the binding to that network adapter. To remove a low power protocol offload, a protocol driver sends an OID set request of [OID\_PM\_REMOVE\_PROTOCOL\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569770). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a protocol offload identifier.

NDIS allows multiple NDIS protocol drivers to add protocol offloads to the same network adapter. To ensure that the right set of protocols have been offloaded to a network adapter when the number of requested offloaded protocols is higher than what a network adapter can support, protocol drivers assign a priority to each offloaded protocol. When NDIS cannot offload a new high priority protocol because the network adapter is out of resources, NDIS deletes one of the lower priority offloaded protocols (if any) and attempts to offload the high priority protocol again.

**Note**  A miniport driver should fail a low power protocol offload add request and return the STATUS\_NDIS\_PM\_PROTOCOL\_OFFLOAD\_LIST\_FULL status code to allow NDIS to re-prioritize the protocol offloads.

 

If as a result of offloading a high priority protocol, one of the lower priority offloaded protocols is deleted, NDIS sends an [**NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED**](https://msdn.microsoft.com/library/windows/hardware/ff567412) status indication to notify the overlying driver that set the deleted protocol offload. The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains a protocol offload identifier of the rejected protocol offload. NDIS provided the protocol offload identifier in the **ProtocolOffloadId** member of the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure.

 

 





