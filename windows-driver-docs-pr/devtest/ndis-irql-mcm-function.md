---
title: Irql\_MCM\_Function rule (ndis)
description: The Irql\_MCM\_Function rule specifies that the NDIS MCM functions for drivers must be called at correct IRQL levels.
ms.assetid: 8cd71bf0-92ee-409d-90e3-6bb0c14ebda4
keywords: ["Irql_MCM_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_MCM_Function
api_type:
- NA
---

# Irql\_MCM\_Function rule (ndis)


The **Irql\_MCM\_Function** rule specifies that the NDIS MCM functions for drivers must be called at correct IRQL levels.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_MCM_Function</strong> rule.</p>
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

[**NdisMCmActivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562792)
[**NdisMCmAddPartyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562798)
[**NdisMCmCloseAddressFamilyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562800)
[**NdisMCmCloseCallComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562803)
[**NdisMCmCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562812)
[**NdisMCmDeactivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562818)
[**NdisMCmDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff562819)
[**NdisMCmDeregisterSapComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562821)
[**NdisMCmDispatchCallConnected**](https://msdn.microsoft.com/library/windows/hardware/ff562826)
[**NdisMCmDispatchIncomingCall**](https://msdn.microsoft.com/library/windows/hardware/ff562830)
[**NdisMCmDispatchIncomingCallQoSChange**](https://msdn.microsoft.com/library/windows/hardware/ff563540)
[**NdisMCmDispatchIncomingCloseCall**](https://msdn.microsoft.com/library/windows/hardware/ff563541)
[**NdisMCmDispatchIncomingDropParty**](https://msdn.microsoft.com/library/windows/hardware/ff563542)
[**NdisMCmDropPartyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563543)
[**NdisMCmMakeCallComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563544)
[**NdisMCmModifyCallQoSComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563545)
[**NdisMCmNotifyCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff563546)
[**NdisMCmOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563548)
[**NdisMCmOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563551)
[**NdisMCmOpenAddressFamilyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563552)
[**NdisMCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff563554)
[**NdisMCmRegisterSapComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563557)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Irql_MCM_Function%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




