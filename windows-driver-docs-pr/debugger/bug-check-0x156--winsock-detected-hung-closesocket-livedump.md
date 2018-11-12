---
title: Bug Check 0x156 WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP
description: The WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP bug check has a value of 0x00000156. This indicates that Winsock detected a hung transport endpoint close request.
ms.assetid: F5B53149-3051-459C-834A-6AE17C56AEE6
keywords: ["Bug Check 0x156 WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP", "WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x156: WINSOCK\_DETECTED\_HUNG\_CLOSESOCKET\_LIVEDUMP


The WINSOCK\_DETECTED\_HUNG\_CLOSESOCKET\_LIVEDUMP bug check has a value of 0x00000156. This indicates that Winsock detected a hung transport endpoint close request.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

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
<td align="left">AFD endpoint pointer (!afdkd.endp &lt;ptr&gt;)</td>
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

 

Cause
-----

While processing a closesocket request, Winsock detected a hung transport endpoint close request. The system generated a live dump for analysis, then the closesocket request was completed without waiting for the completion of hung transport endpoint close request.

 

 




