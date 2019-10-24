---
title: Irql\_Filter\_Driver\_Function rule (ndis)
description: The Irql\_Filter\_Driver\_Function rule specifies that the NDIS functions for filter drivers must be called at correct IRQL levels.
ms.assetid: 1dd45962-151b-472c-88a6-6042ecb7491c
ms.date: 05/21/2018
keywords: ["Irql_Filter_Driver_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Filter_Driver_Function
api_type:
- NA
ms.localizationpriority: medium
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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>Irql_Filter_Driver_Function</strong> rule.</p>
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

[**NdisEnumerateFilterModules**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisenumeratefiltermodules)
[**NdisFCancelSendNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfcancelsendnetbufferlists)
[**NdisFDeregisterFilterDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfderegisterfilterdriver)
[**NdisFDevicePnPEventNotify**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfdevicepnpeventnotify)
[**NdisFIndicateReceiveNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatereceivenetbufferlists)
[**NdisFNetPnPEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfnetpnpevent)
[**NdisFPauseComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfpausecomplete)
[**NdisFRegisterFilterDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfregisterfilterdriver)
[**NdisFRestartComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfrestartcomplete)
[**NdisFRestartFilter**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfrestartfilter)
[**NdisFReturnNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreturnnetbufferlists)
[**NdisFSendNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfsendnetbufferlists)
[**NdisFSendNetBufferListsComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfsendnetbufferlistscomplete)
[**NdisFSetAttributes**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfsetattributes)








