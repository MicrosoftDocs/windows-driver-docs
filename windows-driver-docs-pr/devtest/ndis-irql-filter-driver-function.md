---
title: Irql\_Filter\_Driver\_Function rule (ndis)
description: The Irql\_Filter\_Driver\_Function rule specifies that the NDIS functions for filter drivers must be called at correct IRQL levels.
ms.assetid: 1dd45962-151b-472c-88a6-6042ecb7491c
keywords: ["Irql_Filter_Driver_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Filter_Driver_Function
api_type:
- NA
---

# Irql\_Filter\_Driver\_Function rule (ndis)


The Irql\_Filter\_Driver\_Function rule specifies that the NDIS functions for filter drivers must be called at correct IRQL levels.

The NDIS functions for filter drivers include the following:

**NdisFRegisterFilterDriver**
**NdisFDeregisterFilterDriver**
**NdisFSetAttributes**
**NdisFRestartFilter**
**NdisFRestartComplete**
**NdisFPauseComplete**
**NdisFSendNetBufferLists**
**NdisFReturnNetBufferLists**
**NdisFSendNetBufferListsComplete**
**NdisFCancelSendNetBufferLists**
**NdisFIndicateReceiveNetBufferLists**
**NdisFNetPnPEvent**
**NdisFDevicePnPEventNotify**
**NdisEnumerateFilterModules**
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_Filter_Driver_Function</strong> rule.</p>
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

[**NdisEnumerateFilterModules**](https://msdn.microsoft.com/library/windows/hardware/ff561758)
[**NdisFCancelSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561794)
[**NdisFDeregisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561800)
[**NdisFDevicePnPEventNotify**](https://msdn.microsoft.com/library/windows/hardware/ff561804)
[**NdisFIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561820)
[**NdisFNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561828)
[**NdisFPauseComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561839)
[**NdisFRegisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562608)
[**NdisFRestartComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562610)
[**NdisFRestartFilter**](https://msdn.microsoft.com/library/windows/hardware/ff562611)
[**NdisFReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562613)
[**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616)
[**NdisFSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562618)
[**NdisFSetAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff562619)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Irql_Filter_Driver_Function%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




