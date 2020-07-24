---
title: Irql\_Protocol\_Driver\_Function rule (ndis)
description: The Irql\_Protocol\_Driver\_Function rule specifies that the NDIS functions for CoNDIS clients must be called at correct IRQL levels.
ms.assetid: 9461c3d9-cb31-4ffd-b057-fd9978808c2f
ms.date: 05/21/2018
keywords: ["Irql_Protocol_Driver_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Protocol_Driver_Function
api_type:
- NA
ms.localizationpriority: medium
---

# Irql\_Protocol\_Driver\_Function rule (ndis)


The Irql\_Protocol\_Driver\_Function rule specifies that the NDIS functions for CoNDIS clients must be called at correct IRQL levels.

This rule verifies the following NDIS functions:

**NdisClAddParty**
**NdisClCloseAddressFamily**
**NdisClCloseCall**
**NdisClDeregisterSap**
**NdisClDropParty**
**NdisClGetProtocolVcContextFromTapiCallId**
**NdisClIncomingCallComplete**
**NdisClMakeCall**
**NdisClModifyCallQoS**
**NdisClNotifyCloseAddressFamilyComplete**
**NdisClOpenAddressFamilyEx**
**NdisCloseAdapterEx**
**NdisClRegisterSap**
**NdisCompleteBindAdapterEx**
**NdisCompleteNetPnPEvent**
**NdisCompleteUnbindAdapterEx**
**NdisDeregisterProtocolDriver**
**NdisMNetPnPEvent**
**NdisOpenAdapterEx**
**NdisRegisterProtocolDriver**
**NdisUnbindAdapter**

**Driver model: NDIS**

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>Irql_Protocol_Driver_Function</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**NdisClAddParty**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscladdparty)
[**NdisClCloseAddressFamily**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclcloseaddressfamily)
[**NdisClCloseCall**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclclosecall)
[**NdisClDeregisterSap**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclderegistersap)
[**NdisClDropParty**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscldropparty)
[**NdisClGetProtocolVcContextFromTapiCallId**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclgetprotocolvccontextfromtapicallid)
[**NdisClIncomingCallComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclincomingcallcomplete)
[**NdisClMakeCall**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclmakecall)
[**NdisClModifyCallQoS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclmodifycallqos)
[**NdisClNotifyCloseAddressFamilyComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclnotifycloseaddressfamilycomplete)
[**NdisClOpenAddressFamilyEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclopenaddressfamilyex)
[**NdisCloseAdapterEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscloseadapterex)
[**NdisClRegisterSap**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclregistersap)
[**NdisCompleteBindAdapterEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscompletebindadapterex)
[**NdisCompleteNetPnPEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscompletenetpnpevent)
[**NdisCompleteUnbindAdapterEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscompleteunbindadapterex)
[**NdisDeregisterProtocolDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisderegisterprotocoldriver)
[**NdisMNetPnPEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismnetpnpevent)
[**NdisOpenAdapterEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenadapterex)
[**NdisRegisterProtocolDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver)
[**NdisUnbindAdapter**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisunbindadapter)








