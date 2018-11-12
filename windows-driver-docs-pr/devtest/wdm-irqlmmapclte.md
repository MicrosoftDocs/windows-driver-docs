---
title: IrqlMmApcLte rule (wdm)
ms.assetid: 075f5710-b2bf-4546-9648-661a3c8521f8
ms.date: 05/21/2018
description: 
keywords: ["IrqlMmApcLte rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlMmApcLte
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlMmApcLte rule (wdm)


The **IrqlMmApcLte** rule specifies that the driver calls the following memory manager routines only when it is executing at IRQL &lt;= APC\_LEVEL:

-   [**MmAllocateNonCachedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554479)

-   [**MmFreeNonCachedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554516)

-   [**MmAllocatePagesForMdl**](https://msdn.microsoft.com/library/windows/hardware/ff554482)

-   [**MmFreePagesFromMdl**](https://msdn.microsoft.com/library/windows/hardware/ff554521)

-   [**MmLockPagableDataSection**](https://msdn.microsoft.com/library/windows/hardware/ff554607)

-   [**MmLockPagableSectionByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff554610)

-   [**MmPageEntireDriver**](https://msdn.microsoft.com/library/windows/hardware/ff554650)

-   [**MmResetDriverPaging**](https://msdn.microsoft.com/library/windows/hardware/ff554680)

-   [**MmSecureVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff556374)

-   [**MmUnlockPagableImageSection**](https://msdn.microsoft.com/library/windows/hardware/ff556377)

-   [**MmUnsecureVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff556395)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020019) |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IrqlMmApcLte</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a> and select the <a href="https://msdn.microsoft.com/library/windows/hardware/hh454208" data-raw-source="[DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**MmAllocateNonCachedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554479)
[**MmAllocatePagesForMdl**](https://msdn.microsoft.com/library/windows/hardware/ff554482)
[**MmAllocatePagesForMdlEx**](https://msdn.microsoft.com/library/windows/hardware/ff554489)
[**MmFreeNonCachedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554516)
[**MmFreePagesFromMdl**](https://msdn.microsoft.com/library/windows/hardware/ff554521)
[**MmLockPagableDataSection**](https://msdn.microsoft.com/library/windows/hardware/ff554607)
[**MmLockPagableSectionByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff554610)
[**MmPageEntireDriver**](https://msdn.microsoft.com/library/windows/hardware/ff554650)
[**MmResetDriverPaging**](https://msdn.microsoft.com/library/windows/hardware/ff554680)
[**MmSecureVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff556374)
[**MmUnlockPagableImageSection**](https://msdn.microsoft.com/library/windows/hardware/ff556377)
[**MmUnsecureVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff556395)
 

 





