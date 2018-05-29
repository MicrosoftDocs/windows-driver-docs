---
title: Irql\_CallManager\_Function rule (ndis)
description: The Irql\_CallManager\_Function rule specifies that the NDIS functions for the NDIS CallManager must be called at correct IRQL levels.
ms.assetid: 3e026fb0-8c5f-40cc-affb-3b35f17f40f7
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
 

 





