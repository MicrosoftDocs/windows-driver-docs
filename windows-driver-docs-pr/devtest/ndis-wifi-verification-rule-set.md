---
title: NDIS/WIFI verification rule set
description: Note  You can test NDIS/WIFI drivers with these rules starting with Windows 8.1. .
ms.assetid: B856F42E-E4AD-4178-AF71-3E68A23209C9
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# NDIS/WIFI verification rule set


> [!NOTE]
> You can test NDIS/WIFI drivers with these rules starting with Windows 8.1.

 

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="ndisfiltertimeddatareceive.md" data-raw-source="[&lt;strong&gt;NdisFilterTimedDataReceive&lt;/strong&gt;](ndisfiltertimeddatareceive.md)"><strong>NdisFilterTimedDataReceive</strong></a></p></td>
<td align="left"><p>The <a href="ndisfiltertimeddatareceive.md" data-raw-source="[&lt;strong&gt;NdisFilterTimedDataReceive&lt;/strong&gt;](ndisfiltertimeddatareceive.md)"><strong>NdisFilterTimedDataReceive</strong></a> rule verifies that an NDIS filter driver completes a receive request by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549960" data-raw-source="[&lt;em&gt;FilterReceiveNetBufferLists&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549960)"><em>FilterReceiveNetBufferLists</em></a> function before timing out.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndisfiltertimeddatasend.md" data-raw-source="[&lt;strong&gt;NdisFilterTimedDataSend&lt;/strong&gt;](ndisfiltertimeddatasend.md)"><strong>NdisFilterTimedDataSend</strong></a></p></td>
<td align="left"><p>The <a href="ndisfiltertimeddatasend.md" data-raw-source="[&lt;strong&gt;NdisFilterTimedDataSend&lt;/strong&gt;](ndisfiltertimeddatasend.md)"><strong>NdisFilterTimedDataSend</strong></a> rule verifies that an NDIS filter driver completes a send request by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549966" data-raw-source="[&lt;em&gt;FilterSendNetBufferLists&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549966)"><em>FilterSendNetBufferLists</em></a> function before timing out.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndisfiltertimedpausecomplete-.md" data-raw-source="[&lt;strong&gt;NdisFilterTimedPauseComplete&lt;/strong&gt;](ndisfiltertimedpausecomplete-.md)"><strong>NdisFilterTimedPauseComplete</strong></a></p></td>
<td align="left"><p>The <a href="ndisfiltertimedpausecomplete-.md" data-raw-source="[&lt;strong&gt;NdisFilterTimedPauseComplete&lt;/strong&gt;](ndisfiltertimedpausecomplete-.md)"><strong>NdisFilterTimedPauseComplete</strong></a> verifies three things:</p>
<ul>
<li><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff549957" data-raw-source="[&lt;em&gt;FilterPause&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549957)"><em>FilterPause</em></a> function will be completed in 10 seconds or less.</p></li>
<li><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff549957" data-raw-source="[&lt;em&gt;FilterPause&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549957)"><em>FilterPause</em></a> function must not fail.</p></li>
<li><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff549957" data-raw-source="[&lt;em&gt;FilterPause&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549957)"><em>FilterPause</em></a> function must not complete twice.</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-ndisoidcomplete.md" data-raw-source="[&lt;strong&gt;NdisOidComplete&lt;/strong&gt;](ndis-ndisoidcomplete.md)"><strong>NdisOidComplete</strong></a></p></td>
<td align="left"><p>The <a href="ndis-ndisoidcomplete.md" data-raw-source="[&lt;strong&gt;NdisOidComplete&lt;/strong&gt;](ndis-ndisoidcomplete.md)"><strong>NdisOidComplete</strong></a> rule verifies that an NDIS miniport driver completes an OID correctly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-ndisoiddoublecomplete.md" data-raw-source="[&lt;strong&gt;NdisOidDoubleComplete&lt;/strong&gt;](ndis-ndisoiddoublecomplete.md)"><strong>NdisOidDoubleComplete</strong></a></p></td>
<td align="left"><p>The <a href="ndis-ndisoiddoublecomplete.md" data-raw-source="[&lt;strong&gt;NdisOidDoubleComplete&lt;/strong&gt;](ndis-ndisoiddoublecomplete.md)"><strong>NdisOidDoubleComplete</strong></a> rule specifies that an NDIS miniport driver must not call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563622" data-raw-source="[&lt;strong&gt;NdisMOidRequestComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563622)"><strong>NdisMOidRequestComplete</strong></a> routine twice for the same OID.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-ndisoiddoublerequest.md" data-raw-source="[&lt;strong&gt;NdisOidDoubleRequest&lt;/strong&gt;](ndis-ndisoiddoublerequest.md)"><strong>NdisOidDoubleRequest</strong></a></p></td>
<td align="left"><p>This <a href="ndis-ndisoiddoublerequest.md" data-raw-source="[&lt;strong&gt;NdisOidDoubleRequest&lt;/strong&gt;](ndis-ndisoiddoublerequest.md)"><strong>NdisOidDoubleRequest</strong></a> rule verifies that:</p>
<ul>
<li><p>Minport driver must complete the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> that is currently pending.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-ndistimeddatahang.md" data-raw-source="[&lt;strong&gt;NdisTimedDataHang&lt;/strong&gt;](ndis-ndistimeddatahang.md)"><strong>NdisTimedDataHang</strong></a></p></td>
<td align="left"><p>The <a href="ndis-ndistimeddatahang.md" data-raw-source="[&lt;strong&gt;NdisTimedDataHang&lt;/strong&gt;](ndis-ndistimeddatahang.md)"><strong>NdisTimedDataHang</strong></a> rule verifies that an NDIS miniport driver processes any pending send requests for <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388" data-raw-source="[&lt;strong&gt;NET_BUFFER_LIST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568388)"><strong>NET_BUFFER_LIST</strong></a> structures within 22 seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-ndistimeddatasend.md" data-raw-source="[&lt;strong&gt;NdisTimedDataSend&lt;/strong&gt;](ndis-ndistimeddatasend.md)"><strong>NdisTimedDataSend</strong></a></p></td>
<td align="left"><p>The <a href="ndis-ndistimeddatasend.md" data-raw-source="[&lt;strong&gt;NdisTimedDataSend&lt;/strong&gt;](ndis-ndistimeddatasend.md)"><strong>NdisTimedDataSend</strong></a> rule verifies that when an NDIS driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559440" data-raw-source="[&lt;em&gt;MiniportSendNetBufferLists&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559440)"><em>MiniportSendNetBufferLists</em></a>, the miniport driver completes the send request within 30 seconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-ndistimedoidcomplete.md" data-raw-source="[&lt;strong&gt;NdisTimedOidComplete&lt;/strong&gt;](ndis-ndistimedoidcomplete.md)"><strong>NdisTimedOidComplete</strong></a></p></td>
<td align="left"><p>The <a href="ndis-ndistimedoidcomplete.md" data-raw-source="[&lt;strong&gt;NdisTimedOidComplete&lt;/strong&gt;](ndis-ndistimedoidcomplete.md)"><strong>NdisTimedOidComplete</strong></a> rule specifies that the NDIS miniport driver completes an OID request within 12 seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-wlanassociation.md" data-raw-source="[&lt;strong&gt;WlanAssociation&lt;/strong&gt;](ndis-wlanassociation.md)"><strong>WlanAssociation</strong></a></p></td>
<td align="left"><p>The <a href="ndis-wlanassociation.md" data-raw-source="[&lt;strong&gt;WlanAssociation&lt;/strong&gt;](ndis-wlanassociation.md)"><strong>WlanAssociation</strong></a> rule verifies the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) association sequence.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-wlanconnectionroaming.md" data-raw-source="[&lt;strong&gt;WlanConnectionRoaming&lt;/strong&gt;](ndis-wlanconnectionroaming.md)"><strong>WlanConnectionRoaming</strong></a></p></td>
<td align="left"><p>The <a href="ndis-wlanconnectionroaming.md" data-raw-source="[&lt;strong&gt;WlanConnectionRoaming&lt;/strong&gt;](ndis-wlanconnectionroaming.md)"><strong>WlanConnectionRoaming</strong></a> rule verifies the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) connection and roaming sequence.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-wlandisassociation.md" data-raw-source="[&lt;strong&gt;WlanDisassociation&lt;/strong&gt;](ndis-wlandisassociation.md)"><strong>WlanDisassociation</strong></a></p></td>
<td align="left"><p>The <a href="ndis-wlandisassociation.md" data-raw-source="[&lt;strong&gt;WlanDisassociation&lt;/strong&gt;](ndis-wlandisassociation.md)"><strong>WlanDisassociation</strong></a> rule verifies that the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) disassociation sequence.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-wlantimedassociation.md" data-raw-source="[&lt;strong&gt;WlanTimedAssociation&lt;/strong&gt;](ndis-wlantimedassociation.md)"><strong>WlanTimedAssociation</strong></a></p></td>
<td align="left"><p>The <a href="ndis-wlantimedassociation.md" data-raw-source="[&lt;strong&gt;WlanTimedAssociation&lt;/strong&gt;](ndis-wlantimedassociation.md)"><strong>WlanTimedAssociation</strong></a> rule specifies that the NDIS miniport driver finishes the wireless LAN (WLAN) association operation in 10 seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-wlantimedconnectionroaming.md" data-raw-source="[&lt;strong&gt;WlanTimedConnectionRoaming&lt;/strong&gt;](ndis-wlantimedconnectionroaming.md)"><strong>WlanTimedConnectionRoaming</strong></a></p></td>
<td align="left"><p>The <a href="ndis-wlantimedconnectionroaming.md" data-raw-source="[&lt;strong&gt;WlanTimedConnectionRoaming&lt;/strong&gt;](ndis-wlantimedconnectionroaming.md)"><strong>WlanTimedConnectionRoaming</strong></a> rule specifies that the NDIS miniport driver finishes the wireless LAN (WLAN) connection/roaming operations within 10 seconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-wlantimedconnectrequest.md" data-raw-source="[&lt;strong&gt;WlanTimedConnectRequest&lt;/strong&gt;](ndis-wlantimedconnectrequest.md)"><strong>WlanTimedConnectRequest</strong></a></p></td>
<td align="left"><p>The <a href="ndis-wlantimedconnectrequest.md" data-raw-source="[&lt;strong&gt;WlanTimedConnectRequest&lt;/strong&gt;](ndis-wlantimedconnectrequest.md)"><strong>WlanTimedConnectRequest</strong></a> rule verifies that an OID_DOT11_CONNECT_REQUEST is followed by a NDIS_STATUS_DOT11_CONNECTION_START within 10 seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-wlantimedscan.md" data-raw-source="[&lt;strong&gt;WlanTimedScan&lt;/strong&gt;](ndis-wlantimedscan.md)"><strong>WlanTimedScan</strong></a></p></td>
<td align="left"><p>The <a href="ndis-wlantimedscan.md" data-raw-source="[&lt;strong&gt;WlanTimedScan&lt;/strong&gt;](ndis-wlantimedscan.md)"><strong>WlanTimedScan</strong></a> rule verifies that a WLAN scan operation is completed within 15 seconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-wlantimedlinkquality.md" data-raw-source="[&lt;strong&gt;WlanTimedLinkQuality&lt;/strong&gt;](ndis-wlantimedlinkquality.md)"><strong>WlanTimedLinkQuality</strong></a></p></td>
<td align="left"><p>The <a href="ndis-wlantimedlinkquality.md" data-raw-source="[&lt;strong&gt;WlanTimedLinkQuality&lt;/strong&gt;](ndis-wlantimedlinkquality.md)"><strong>WlanTimedLinkQuality</strong></a> rule specifies the NDIS_STATUS_DOT11_LINK_QUALITY indication is made in 15 seconds after a successful NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION.</p></td>
</tr>
</tbody>
</table>

 

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a> and select the <a href="https://msdn.microsoft.com/library/windows/hardware/dn312128" data-raw-source="[NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/dn312128)">NDIS/WIFI verification</a> option.</p></td>
</tr>
</tbody>
</table>

 

 

 





