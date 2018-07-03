---
title: Irql\_IM\_Function rule (ndis)
description: The Irql\_IM\_Function rule specifies that the NDIS functions for Intermediate (IM) drivers must be called at correct IRQL levels.
ms.assetid: f13ee05d-41d5-48e1-aa53-8904d99f94da
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_IM_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_IM_Function
api_type:
- NA
---

# Irql\_IM\_Function rule (ndis)


The Irql\_IM\_Function rule specifies that the NDIS functions for Intermediate (IM) drivers must be called at correct IRQL levels.

This rule verifies the following NDIS functions:

**NdisIMAssociateMiniport**
**NdisIMCancelInitializeDeviceInstance**
**NdisIMDeInitializeDeviceInstance**
**NdisIMGetBindingContext**
**NdisIMInitializeDeviceInstanceEx**
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_IM_Function</strong> rule.</p>
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

[**NdisIMAssociateMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff562717)
[**NdisIMCancelInitializeDeviceInstance**](https://msdn.microsoft.com/library/windows/hardware/ff562719)
[**NdisIMDeInitializeDeviceInstance**](https://msdn.microsoft.com/library/windows/hardware/ff562721)
[**NdisIMGetBindingContext**](https://msdn.microsoft.com/library/windows/hardware/ff562724)
[**NdisIMInitializeDeviceInstanceEx**](https://msdn.microsoft.com/library/windows/hardware/ff562727)
 

 





