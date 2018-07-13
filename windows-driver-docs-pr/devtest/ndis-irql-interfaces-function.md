---
title: Irql\_Interfaces\_Function rule (ndis)
description: The Irql\_Interfaces\_Function rule specifies that the NDIS network interface functions must be called at correct IRQL levels.
ms.assetid: cea79975-4b14-4c7e-acfe-0bb10679e25b
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_Interfaces_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Interfaces_Function
api_type:
- NA
---

# Irql\_Interfaces\_Function rule (ndis)


The Irql\_Interfaces\_Function rule specifies that the NDIS network interface functions must be called at correct IRQL levels.

This rule verifies the following NDIS network interface functions:

**NdisIfAddIfStackEntry**
**NdisIfAllocateNetLuidIndex**
**NdisIfDeleteIfStackEntry**
**NdisIfDeregisterInterface**
**NdisIfDeregisterProvider**
**NdisIfFreeNetLuidIndex**
**NdisIfGetInterfaceIndexFromNetLuid**
**NdisIfGetNetLuidFromInterfaceIndex**
**NdisIfQueryBindingIfIndex**
**NdisIfRegisterInterface**
**NdisIfRegisterProvider**
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_Interfaces_Function</strong> rule.</p>
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

[**NdisIfAddIfStackEntry**](https://msdn.microsoft.com/library/windows/hardware/ff562693)
[**NdisIfAllocateNetLuidIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562695)
[**NdisIfDeleteIfStackEntry**](https://msdn.microsoft.com/library/windows/hardware/ff562698)
[**NdisIfDeregisterInterface**](https://msdn.microsoft.com/library/windows/hardware/ff562700)
[**NdisIfDeregisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff562703)
[**NdisIfFreeNetLuidIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562706)
[**NdisIfGetInterfaceIndexFromNetLuid**](https://msdn.microsoft.com/library/windows/hardware/ff562707)
[**NdisIfGetNetLuidFromInterfaceIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562711)
[**NdisIfQueryBindingIfIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562713)
[**NdisIfRegisterInterface**](https://msdn.microsoft.com/library/windows/hardware/ff562715)
[**NdisIfRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff562716)
 

 





