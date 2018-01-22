---
title: IrqlMmApcLte rule (wdm)
ms.assetid: 075f5710-b2bf-4546-9648-661a3c8521f8
description: 
keywords: ["IrqlMmApcLte rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlMmApcLte
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlMmApcLte</strong> rule.</p>
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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20IrqlMmApcLte%20%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




