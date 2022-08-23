---
title: Bug Check 0x156 WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP
description: The WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP live dump has a value of 0x00000156. This indicates that Winsock detected a hung transport endpoint close request.
keywords: ["Bug Check 0x156 WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP", "WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP"]
ms.date: 04/18/2022
topic_type:
- apiref
api_name:
- WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x156: WINSOCK\_DETECTED\_HUNG\_CLOSESOCKET\_LIVEDUMP


The WINSOCK\_DETECTED\_HUNG\_CLOSESOCKET\_LIVEDUMP live dump has a value of 0x00000156. This indicates that Winsock detected a hung transport endpoint close request.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## WINSOCK\_DETECTED\_HUNG\_CLOSESOCKET\_LIVEDUMP Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">1</td>
<td align="left">AFD endpoint pointer (!afdkd.endp &lt;ptr&gt;) The !afdkd debugger extension is only available to hardware development partners. </td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left"><p>Transport endpoint type</p>
<p>0x1 : UDP datagram</p>
<p>0x2 : RAW datagram</p>
<p>0x3 : TCP listener</p>
<p>0x4 : TCP endpoint</p></td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Number of buffered send bytes for datagram endpoints</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">afd!NETIO_SUPER_TRIAGE_BLOCK</td>
</tr>
</tbody>
</table>

 

## Cause

While processing a closesocket request, Winsock detected a hung transport endpoint close request. The system generated a live dump for analysis, then the closesocket request was completed without waiting for the completion of hung transport endpoint close request.



 

 




