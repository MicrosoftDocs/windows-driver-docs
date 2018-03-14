---
title: NdisMNetPnPEventInOIDRequest rule (ndis)
description: This rule checks that NdisMNetPnPEvent is not called in the context of an OID request.
ms.assetid: BC069325-FFC4-452D-9B07-C39C2F942B64
keywords: ["NdisMNetPnPEventInOIDRequest rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisMNetPnPEventInOIDRequest
api_type:
- NA
---

# NdisMNetPnPEventInOIDRequest rule (ndis)


This rule checks that [**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616) is not called in the context of an OID request.

|              |      |
|--------------|------|
| Driver model | NDIS |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisMNetPnPEventInOIDRequest</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616)
[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
 

 





