---
title: Irql\_OID\_Function rule (ndis)
description: The Irql\_OID\_Function rule specifies that the NDIS OID request DDIs must be called at correct IRQL levels.
ms.assetid: 450afd4e-ba01-45e8-a866-6cd9b3190bb7
keywords: ["Irql_OID_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_OID_Function
api_type:
- NA
---

# Irql\_OID\_Function rule (ndis)


The **Irql\_OID\_Function** rule specifies that the NDIS OID request DDIs must be called at correct IRQL levels.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_OID_Function</strong> rule.</p>
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

[**NdisAllocateCloneOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff560706)
[**NdisCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561622)
[**NdisFCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561792)
[**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830)
[**NdisFOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561833)
[**NdisFreeCloneOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561845)
[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
[**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Irql_OID_Function%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




