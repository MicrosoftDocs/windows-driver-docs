---
title: NdisAllocateGenericObject rule (ndis)
description: The NdisAllocateGenericObject rule specifies that NdisAllocateGenericObject and NdisFreeGenericObject are called in alternate order. The ultimate goal is to make sure all generic objects are freed when MiniportHaltEx ends.
ms.assetid: A247B43F-1958-4A57-AA60-37C995A96DF7
keywords: ["NdisAllocateGenericObject rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisAllocateGenericObject
api_type:
- NA
---

# NdisAllocateGenericObject rule (ndis)


The **NdisAllocateGenericObject** rule specifies that [**NdisAllocateGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561603) and [**NdisFreeGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561850) are called in alternate order. The ultimate goal is to make sure all generic objects are freed when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) ends.

The rule uses three different states. The state changes when an NDIS generic object is allocated or freed. If an NDIS generic object is still allocated when the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) exits, the rule will fail.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisAllocateGenericObject</strong> rule.</p>
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

[**NdisAllocateGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561603)
[**NdisFreeGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561850)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20NdisAllocateGenericObject%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




