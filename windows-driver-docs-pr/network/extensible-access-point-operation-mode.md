---
title: Extensible Access Point Operation Mode
description: Extensible Access Point Operation Mode
ms.assetid: 38069e18-6a52-4b72-a51a-7a34f71a049a
keywords: ["extensible access point WDK Native 802.11", "extensible AP WDK Native 802.11", "ExtAP WDK Native 802.11"]
---

# Extensible Access Point Operation Mode


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

In the Extensible Access Point (ExtAP) operation mode, the 802.11 station operates as a wireless LAN (WLAN) access point. The ExtAP operation mode is available beginning with NDIS 6.20 in Windows 7. The ExtAP mode is optional. To take advantage of this mode, you must compile or recompile an 802.11 miniport driver with the NTDDI\_VERSION macro set to &gt;= NTDDI\_WIN7.

Note that a NIC must always support the [Extensible Station Operation Mode](extensible-station-operation-mode.md).

A miniport driver enters the ExtAP mode when it receives an [OID\_DOT11\_CURRENT\_OPERATION\_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569132) request with the **uCurrentOpMode** member of [**DOT11\_CURRENT\_OPERATION\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff547678) set to DOT11\_OPERATION\_MODE\_EXTENSIBLE\_AP. When the driver enters ExtAP mode, the NIC must disable any background scanning that it has implemented.

The 802.11 miniport driver completes a [**DOT11\_EXTAP\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff547687) structure to report the attributes of the driver and 802.11 station in the ExtAP mode. These attributes are reported through the **ExtAPAttributes** member of the [**NDIS\_MINIPORT\_ADAPTER\_NATIVE\_802\_11\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565926) structure.

To operate in ExtAP mode, the miniport driver must do the following:

-   Support the initialization (INIT) and operational (OP) states, and transitions between these states, as described in [Extensible Access Point Operating States](extensible-access-point-operating-states.md).

-   Support raw packet receive indications, as described in [Indicating Raw 802.11 Packets](indicating-raw-802-11-packets.md).

-   Support the promiscuous packet receive indications, as described in [Guidelines for 802.11 Promiscuous Receive Operations](guidelines-for-802-11-promiscuous-receive-operations.md).

-   Follow association guidelines given in [Association Operation Guidelines for Extensible Access Point (ExtAP) Mode](association-operation-guidelines-for-extensible-access-point--extap--m.md).

-   Follow power management guidelines given in [Extensible Access Point Power Management](extensible-access-point-power-management.md).

-   Enable the required support for Windows Protected Setup (WPS) in response to [OID\_DOT11\_WPS\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569436).

-   Support a set request on [OID\_DOT11\_BEACON\_PERIOD](https://msdn.microsoft.com/library/windows/hardware/ff569109).

-   Support all OIDs listed in [Native 802.11 Extensible AP OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560596).

-   Not send packets either on its own or through a call to its [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function. The driver can only receive packets based on the current packet filter settings. For more information about the 802.11 packet filter settings, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

### ExtAP OIDs

The following OIDs and their associated structures support the ExtAP operation mode.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Object identifier (OID)</th>
<th align="left">Associated structure</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_DOT11_ADDITIONAL_IE](https://msdn.microsoft.com/library/windows/hardware/ff569103)</p></td>
<td align="left"><p>[<strong>DOT11_ADDITIONAL_IE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547645)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_AVAILABLE_CHANNEL_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569107)</p></td>
<td align="left"><p>[<strong>DOT11_AVAILABLE_CHANNEL_LIST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547663)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_AVAILABLE_FREQUENCY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569108)</p></td>
<td align="left"><p>[<strong>DOT11_AVAILABLE_FREQUENCY_LIST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547664)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_DISASSOCIATE_PEER_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569146)</p></td>
<td align="left"><p>[<strong>DOT11_DISASSOCIATE_PEER_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547681)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_ENUM_PEER_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569361)</p></td>
<td align="left"><p>[<strong>DOT11_PEER_INFO_LIST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548719)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_INCOMING_ASSOCIATION_DECISION](https://msdn.microsoft.com/library/windows/hardware/ff569379)</p></td>
<td align="left"><p>[<strong>DOT11_INCOMING_ASSOC_DECISION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548654)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_START_AP_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569418)</p></td>
<td align="left"><p>(none)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_WPS_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569436)</p></td>
<td align="left"><p>(none)</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Native 802.11 Extensible AP OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560596).

### ExtAP Status Indications

The following NDIS status indications and their associated structures support the ExtAP operation mode.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">NDIS status indication</th>
<th align="left">Associated structure</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[NDIS_STATUS_DOT11_CAN_SUSTAIN_AP](https://msdn.microsoft.com/library/windows/hardware/ff567323)</p></td>
<td align="left"><p>[<strong>DOT11_CAN_SUSTAIN_AP_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547671)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[NDIS_STATUS_DOT11_INCOMING_ASSOC_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567338)</p></td>
<td align="left"><p>[<strong>DOT11_INCOMING_ASSOC_COMPLETION_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548650)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[NDIS_STATUS_DOT11_INCOMING_ASSOC_REQUEST_RECEIVED](https://msdn.microsoft.com/library/windows/hardware/ff567339)</p></td>
<td align="left"><p>[<strong>DOT11_INCOMING_ASSOC_REQUEST_RECEIVED_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548655)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[NDIS_STATUS_DOT11_INCOMING_ASSOC_STARTED](https://msdn.microsoft.com/library/windows/hardware/ff567342)</p></td>
<td align="left"><p>[<strong>DOT11_INCOMING_ASSOC_STARTED_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548663)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[NDIS_STATUS_DOT11_PHY_FREQUENCY_ADOPTED](https://msdn.microsoft.com/library/windows/hardware/ff567351)</p></td>
<td align="left"><p>[<strong>DOT11_PHY_FREQUENCY_ADOPTED_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548735)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[NDIS_STATUS_DOT11_STOP_AP](https://msdn.microsoft.com/library/windows/hardware/ff567366)</p></td>
<td align="left"><p>[<strong>DOT11_STOP_AP_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548783)</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Native 802.11 Extensible AP Status Indications](https://msdn.microsoft.com/library/windows/hardware/ff560598).

 

 





