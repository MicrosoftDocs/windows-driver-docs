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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>Irql_Filter_Driver_Function</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
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








