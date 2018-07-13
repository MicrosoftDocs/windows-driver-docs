---
title: NdisOpenConfigurationEx rule (ndis)
description: This rule checks that NdisOpenConfigurationEx and NdisCloseConfiguration are called in alternate order. The ultimate goal is to make sure that configuration handles are closed when MiniportHaltEx exits.
ms.assetid: 3E23D8AE-5EBC-4C2F-9EE3-42718D86B97C
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["NdisOpenConfigurationEx rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisOpenConfigurationEx
api_type:
- NA
---

# NdisOpenConfigurationEx rule (ndis)


This rule checks that [**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717) and [**NdisCloseConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff561642) are called in alternate order. The ultimate goal is to make sure that configuration handles are closed when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) exits.

The rule uses three different states. The state changes when a configuration is opened or closed. If a configuration handle is still open when the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) exits, a defect is reported.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisOpenConfigurationEx</strong> rule.</p>
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

[**NdisCloseConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff561642)
[**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717)
 

 





