---
title: Irql\_CallManager\_Function rule (ndis)
description: The Irql\_CallManager\_Function rule specifies that the NDIS functions for the NDIS CallManager must be called at correct IRQL levels.
ms.assetid: 3e026fb0-8c5f-40cc-affb-3b35f17f40f7
keywords: ["Irql_CallManager_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_CallManager_Function
api_type:
- NA
---

# Irql\_CallManager\_Function rule (ndis)


The **Irql\_CallManager\_Function** rule specifies that the NDIS functions for the NDIS CallManager must be called at correct IRQL levels.

This rule examines the following NDIS functions:

**NdisCmActivateVc**
**NdisCmAddPartyComplete**
**NdisCmCloseAddressFamilyComplete**
**NdisCmCloseCallComplete**
**NdisCmDeactivateVc**
**NdisCmDeregisterSapComplete**
**NdisCmDispatchCallConnected**
**NdisCmDispatchIncomingCall**
**NdisCmDispatchIncomingCallQoSChange**
**NdisCmDispatchIncomingCloseCall**
**NdisCmDispatchIncomingDropParty**
**NdisCmDropPartyComplete**
**NdisCmMakeCallComplete**
**NdisCmModifyCallQoSComplete**
**NdisCmNotifyCloseAddressFamily**
**NdisCmOpenAddressFamilyComplete**
**NdisCmRegisterAddressFamilyEx**
**NdisCmRegisterSapComplete**
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_CallManager_Function</strong> rule.</p>
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

[**NdisCmActivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff561649)
[**NdisCmAddPartyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561651)
[**NdisCmCloseAddressFamilyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561654)
[**NdisCmCloseCallComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561655)
[**NdisCmDeactivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff561657)
[**NdisCmDeregisterSapComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561659)
[**NdisCmDispatchCallConnected**](https://msdn.microsoft.com/library/windows/hardware/ff561661)
[**NdisCmDispatchIncomingCall**](https://msdn.microsoft.com/library/windows/hardware/ff561664)
[**NdisCmDispatchIncomingCallQoSChange**](https://msdn.microsoft.com/library/windows/hardware/ff561668)
[**NdisCmDispatchIncomingCloseCall**](https://msdn.microsoft.com/library/windows/hardware/ff561670)
[**NdisCmDispatchIncomingDropParty**](https://msdn.microsoft.com/library/windows/hardware/ff561672)
[**NdisCmDropPartyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561674)
[**NdisCmMakeCallComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561677)
[**NdisCmModifyCallQoSComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561679)
[**NdisCmNotifyCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff561680)
[**NdisCmOpenAddressFamilyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561682)
[**NdisCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff561685)
[**NdisCmRegisterSapComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561689)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Irql_CallManager_Function%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




