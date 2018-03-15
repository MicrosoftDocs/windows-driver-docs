---
title: StorPortStatusPending rule (storport)
description: This rule checks that an SRB is not completed with status SRB\_STATUS\_PENDING.
ms.assetid: 134BDADA-C475-4D82-A0AB-31410C994AAF
keywords: ["StorPortStatusPending rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortStatusPending
api_type:
- NA
---

# StorPortStatusPending rule (storport)


This rule checks that an SRB is not completed with status **SRB\_STATUS\_PENDING**.

|              |          |
|--------------|----------|
| Driver model | Storport |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortStatusPending</strong> rule.</p>
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

[**StorPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff567433)
 

 





