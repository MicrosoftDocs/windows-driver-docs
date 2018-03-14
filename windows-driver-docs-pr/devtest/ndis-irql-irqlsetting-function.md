---
title: Irql\_IrqlSetting\_Function rule (ndis)
description: The Irql\_IrqlSetting\_Function rule specifies that the NDIS interrupt macros must be called at correct IRQL levels.
ms.assetid: 47e62c7c-bd43-4b4a-b7d6-3f64a4b8a6c8
keywords: ["Irql_IrqlSetting_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_IrqlSetting_Function
api_type:
- NA
---

# Irql\_IrqlSetting\_Function rule (ndis)


The Irql\_IrqlSetting\_Function rule specifies that the NDIS interrupt macros must be called at correct IRQL levels.

This rule verifies the following NDIS macros:

**NDIS\_LOWER\_IRQL**
**NDIS\_RAISE\_IRQL\_TO\_DISPATCH**
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_IrqlSetting_Function</strong> rule.</p>
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

[**NDIS\_LOWER\_IRQL**](https://msdn.microsoft.com/library/windows/hardware/ff565882)
[**NDIS\_RAISE\_IRQL\_TO\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff566854)
 

 





