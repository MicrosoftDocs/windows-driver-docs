---
title: MB / NDIS 6.20 Interfacing Overview
description: MB / NDIS 6.20 Interfacing Overview
keywords:
- NDIS 6.20 WDK , mobile broadband (MB) interfacing
- mobile broadband (MB) WDK
- mobile broadband (MB) WDK , NDIS 6.20 interfacing
ms.date: 03/02/2023
ms.custom: UpdateFrequency3
---

# MB / NDIS 6.20 Interfacing Overview


This topic is designed to provide enough background about the *NDIS 6.20 Specification* to put the MB driver model into perspective. It is not intended to be a reference for NDIS 6.20. In the case of discrepancies between this content and the *NDIS 6.20 Specification*, see the [NDIS 6.20](introduction-to-ndis-6-20.md) documentation for complete information.

In NDIS 6.20, the MB Service calls [**NdisOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisoidrequest) to issue OID requests to the miniport driver. Then, miniport drivers call [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) to return data back to the MB Service.

NDIS 6.20 supports the following types of OID operations:

-   *Set* operations that send data from the service to a miniport driver.

-   *Query* operations that request miniport drivers to return data to the service.

-   *Method* operations, equivalent to a function call, that have both input parameters and output parameters.

Finally, miniport drivers may send *indications* that contain data to notify the service about state changes in the MB device.

### Receiving *Set* and *Query* Requests

MB miniport drivers implement the [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) NDIS handler to respond to both *set* and *query* requests.

### Sending Status Indications

Miniport drivers provide status indications to the MB Service by calling [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex). See the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure for more details about status indications.

### Connection State Indications

NDIS 6.20 miniport drivers must use the [**NDIS\_STATUS\_LINK\_STATE**](./ndis-status-link-state.md) status indication to notify NDIS and overlying drivers that there has been a change in the physical characteristics of a transmission medium.

The **StatusBuffer** member of the NDIS\_STATUS\_INDICATION structure is an [**NDIS\_LINK\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_link_state) structure, which specifies the physical state of the transmission medium.

MB miniport drivers should avoid sending the NDIS\_STATUS\_LINK\_STATUS status indication if there have been no changes in the physical state of the medium. However, miniport drivers are not necessarily required to avoid sending this status indication.

MB miniport drivers must report the maximum data rate of the currently connected data-class. A change in data-class while connected must result in a Connection State Indication with the corresponding data rate reported. The following is a recommended implementation of this rule:

1.  MB miniport drivers that conform to this specification must use [**NDIS\_STATUS\_LINK\_STATE**](./ndis-status-link-state.md) to indicate connection status changes instead of NDIS\_STATUS\_MEDIA\_CONNECT, NDIS\_STATUS\_MEDIA\_DISCONNECT, or NDIS\_STATUS\_LINK\_SPEED\_CHANGE (as in NDIS 5.1) for connection status indications.

2.  The **XmitLinkSpeed** and **RcvLinkSpeed** members of the [**NDIS\_LINK\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_link_state) structure must not report NDIS\_LINK\_SPEED\_UNKNOWN. Miniport drivers must report the speed by using the information in the following tables.

**For GSM-based MB device speed links**

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Data class</th>
<th align="left">XmitLinkSpeed</th>
<th align="left">RcvLinkSpeed</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>GPRS</p></td>
<td align="left"><p>8 to 48 kbps</p></td>
<td align="left"><p>8 to 48 kbps</p></td>
</tr>
<tr class="even">
<td align="left"><p>EDGE</p></td>
<td align="left"><p>8 to 220 kbps</p></td>
<td align="left"><p>8 to 220 kbps</p></td>
</tr>
<tr class="odd">
<td align="left"><p>UMTS</p></td>
<td align="left"><p>64 to 384 kbps</p></td>
<td align="left"><p>64 to 384 kbps</p></td>
</tr>
<tr class="even">
<td align="left"><p>HSDPA</p></td>
<td align="left"><p>64 to 5.76 mbps</p></td>
<td align="left"><p>1.8 to 14.4 mbps</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HSUPA</p></td>
<td align="left"><p>1.4 to 5.76 mbps</p></td>
<td align="left"><p>64 kbps to 7.2 mbps</p></td>
</tr>
</tbody>
</table>

 

**For CDMA-based MB device speed links**

| Data Class     | XmitLinkSpeed            | RcvLinkSpeed            |
|----------------|--------------------------|-------------------------|
| 1xRTT          | 115.2 kbps to 307.2 kbps | 153.6 kbps to 3 mbps    |
| 3xRTT          | 614 kbps to 1.04 mbps    | 307.2 kbps to 1.04 mbps |
| 1xEV-DO        | 153.6 kbps               | 2.4 mbps                |
| 1xEvDO Rev. A. | 1.8 mbps                 | 3.1 mbps                |
| 1xEV-DV        | 1.8 mbps                 | 3.1 mbps                |
| 1xEvDO Rev. B. | 27 mbps                  | 3.1 mbps to 73.5 mbps   |

 

**Note**  MB devices should report the speed in the range of speed shown in the previous tables.

 

Unlike NDIS 5.1, different link state change indications are consolidated into a single NDIS\_STATUS\_LINK\_STATE indication by using the NDIS\_LINK\_STATE data structure. NDIS 5.1 indications can be mapped to this structure according to the information in the following table. In the case of link speed change, the consumer of the indication should compare the transmitting and receiving speed values with the ones it recorded for a previous indication to decide whether the link speed change has occurred or not.

**Connection status indication mapping from NDIS 5.1 to 6.x**

NDIS 5.1 indication
NDIS 6.x NDIS\_LINK\_STATE data structure
Parameter
Value
NDIS\_STATUS\_MEDIA\_CONNECT

MediaConnectState

MediaConnectStateConnected

NDIS\_STATUS\_MEDIA\_DISCONNECT

MediaConnectState

MediaConnectStateDisconnected

NDIS\_STATUS\_LINK\_SPEED\_CHANGE

XmitLinkSpeed

Transmitting speed (bps)

RcvLinkSpeed

Receiving speed (bps)

 

 

