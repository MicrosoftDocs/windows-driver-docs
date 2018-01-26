---
title: Irql\_Interfaces\_Function rule (ndis)
description: The Irql\_Interfaces\_Function rule specifies that the NDIS network interface functions must be called at correct IRQL levels.
ms.assetid: cea79975-4b14-4c7e-acfe-0bb10679e25b
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Irql_Interfaces_Function%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




