---
title: Irql\_MCM\_Function rule (ndis)
description: The Irql\_MCM\_Function rule specifies that the NDIS MCM functions for drivers must be called at correct IRQL levels.
ms.date: 05/21/2018
keywords: ["Irql_MCM_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_MCM_Function
api_type:
- NA
ms.localizationpriority: medium
---

# Irql\_MCM\_Function rule (ndis)


The **Irql\_MCM\_Function** rule specifies that the NDIS MCM functions for drivers must be called at correct IRQL levels.

**Driver model: NDIS**

## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>Irql_MCM_Function</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

## Applies to

[**NdisMCmActivateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmactivatevc)
[**NdisMCmAddPartyComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmaddpartycomplete)
[**NdisMCmCloseAddressFamilyComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmcloseaddressfamilycomplete)
[**NdisMCmCloseCallComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmclosecallcomplete)
[**NdisMCmCreateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmcreatevc)
[**NdisMCmDeactivateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdeactivatevc)
[**NdisMCmDeleteVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdeletevc)
[**NdisMCmDeregisterSapComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmderegistersapcomplete)
[**NdisMCmDispatchCallConnected**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdispatchcallconnected)
[**NdisMCmDispatchIncomingCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdispatchincomingcall)
[**NdisMCmDispatchIncomingCallQoSChange**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdispatchincomingcallqoschange)
[**NdisMCmDispatchIncomingCloseCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdispatchincomingclosecall)
[**NdisMCmDispatchIncomingDropParty**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdispatchincomingdropparty)
[**NdisMCmDropPartyComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdroppartycomplete)
[**NdisMCmMakeCallComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmmakecallcomplete)
[**NdisMCmModifyCallQoSComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmmodifycallqoscomplete)
[**NdisMCmNotifyCloseAddressFamily**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmnotifycloseaddressfamily)
[**NdisMCmOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmoidrequest)
[**NdisMCmOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmoidrequestcomplete)
[**NdisMCmOpenAddressFamilyComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmopenaddressfamilycomplete)
[**NdisMCmRegisterAddressFamilyEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmregisteraddressfamilyex)
[**NdisMCmRegisterSapComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmregistersapcomplete)
