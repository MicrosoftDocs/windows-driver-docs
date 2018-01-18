---
title: NDIS/WIFI verification rule set
description: Note  You can test NDIS/WIFI drivers with these rules starting with Windows 8.1. .
ms.assetid: B856F42E-E4AD-4178-AF71-3E68A23209C9
---

# NDIS/WIFI verification rule set


> \[!Note\]
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
<td align="left"><p>[<strong>NdisFilterTimedDataReceive</strong>](ndisfiltertimeddatareceive.md)</p></td>
<td align="left"><p>The [<strong>NdisFilterTimedDataReceive</strong>](ndisfiltertimeddatareceive.md) rule verifies that an NDIS filter driver completes a receive request by the [<em>FilterReceiveNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff549960) function before timing out.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisFilterTimedDataSend</strong>](ndisfiltertimeddatasend.md)</p></td>
<td align="left"><p>The [<strong>NdisFilterTimedDataSend</strong>](ndisfiltertimeddatasend.md) rule verifies that an NDIS filter driver completes a send request by the [<em>FilterSendNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff549966) function before timing out.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisFilterTimedPauseComplete</strong>](ndisfiltertimedpausecomplete-.md)</p></td>
<td align="left"><p>The [<strong>NdisFilterTimedPauseComplete</strong>](ndisfiltertimedpausecomplete-.md) verifies three things:</p>
<ul>
<li><p>The [<em>FilterPause</em>](https://msdn.microsoft.com/library/windows/hardware/ff549957) function will be completed in 10 seconds or less.</p></li>
<li><p>The [<em>FilterPause</em>](https://msdn.microsoft.com/library/windows/hardware/ff549957) function must not fail.</p></li>
<li><p>The [<em>FilterPause</em>](https://msdn.microsoft.com/library/windows/hardware/ff549957) function must not complete twice.</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisOidComplete</strong>](ndis-ndisoidcomplete.md)</p></td>
<td align="left"><p>The [<strong>NdisOidComplete</strong>](ndis-ndisoidcomplete.md) rule verifies that an NDIS miniport driver completes an OID correctly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisOidDoubleComplete</strong>](ndis-ndisoiddoublecomplete.md)</p></td>
<td align="left"><p>The [<strong>NdisOidDoubleComplete</strong>](ndis-ndisoiddoublecomplete.md) rule specifies that an NDIS miniport driver must not call the [<strong>NdisMOidRequestComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563622) routine twice for the same OID.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisOidDoubleRequest</strong>](ndis-ndisoiddoublerequest.md)</p></td>
<td align="left"><p>This [<strong>NdisOidDoubleRequest</strong>](ndis-ndisoiddoublerequest.md) rule verifies that:</p>
<ul>
<li><p>Minport driver must complete the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) that is currently pending.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisTimedDataHang</strong>](ndis-ndistimeddatahang.md)</p></td>
<td align="left"><p>The [<strong>NdisTimedDataHang</strong>](ndis-ndistimeddatahang.md) rule verifies that an NDIS miniport driver processes any pending send requests for [<strong>NET_BUFFER_LIST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures within 22 seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisTimedDataSend</strong>](ndis-ndistimeddatasend.md)</p></td>
<td align="left"><p>The [<strong>NdisTimedDataSend</strong>](ndis-ndistimeddatasend.md) rule verifies that when an NDIS driver calls [<em>MiniportSendNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/ff559440), the miniport driver completes the send request within 30 seconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisTimedOidComplete</strong>](ndis-ndistimedoidcomplete.md)</p></td>
<td align="left"><p>The [<strong>NdisTimedOidComplete</strong>](ndis-ndistimedoidcomplete.md) rule specifies that the NDIS miniport driver completes an OID request within 12 seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WlanAssociation</strong>](ndis-wlanassociation.md)</p></td>
<td align="left"><p>The [<strong>WlanAssociation</strong>](ndis-wlanassociation.md) rule verifies the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) association sequence.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WlanConnectionRoaming</strong>](ndis-wlanconnectionroaming.md)</p></td>
<td align="left"><p>The [<strong>WlanConnectionRoaming</strong>](ndis-wlanconnectionroaming.md) rule verifies the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) connection and roaming sequence.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WlanDisassociation</strong>](ndis-wlandisassociation.md)</p></td>
<td align="left"><p>The [<strong>WlanDisassociation</strong>](ndis-wlandisassociation.md) rule verifies that the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) disassociation sequence.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WlanTimedAssociation</strong>](ndis-wlantimedassociation.md)</p></td>
<td align="left"><p>The [<strong>WlanTimedAssociation</strong>](ndis-wlantimedassociation.md) rule specifies that the NDIS miniport driver finishes the wireless LAN (WLAN) association operation in 10 seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WlanTimedConnectionRoaming</strong>](ndis-wlantimedconnectionroaming.md)</p></td>
<td align="left"><p>The [<strong>WlanTimedConnectionRoaming</strong>](ndis-wlantimedconnectionroaming.md) rule specifies that the NDIS miniport driver finishes the wireless LAN (WLAN) connection/roaming operations within 10 seconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WlanTimedConnectRequest</strong>](ndis-wlantimedconnectrequest.md)</p></td>
<td align="left"><p>The [<strong>WlanTimedConnectRequest</strong>](ndis-wlantimedconnectrequest.md) rule verifies that an OID_DOT11_CONNECT_REQUEST is followed by a NDIS_STATUS_DOT11_CONNECTION_START within 10 seconds.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WlanTimedScan</strong>](ndis-wlantimedscan.md)</p></td>
<td align="left"><p>The [<strong>WlanTimedScan</strong>](ndis-wlantimedscan.md) rule verifies that a WLAN scan operation is completed within 15 seconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WlanTimedLinkQuality</strong>](ndis-wlantimedlinkquality.md)</p></td>
<td align="left"><p>The [<strong>WlanTimedLinkQuality</strong>](ndis-wlantimedlinkquality.md) rule specifies the NDIS_STATUS_DOT11_LINK_QUALITY indication is made in 15 seconds after a successful NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION.</p></td>
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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/dn312128) option.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20NDIS/WIFI%20verification%20rule%20set%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




