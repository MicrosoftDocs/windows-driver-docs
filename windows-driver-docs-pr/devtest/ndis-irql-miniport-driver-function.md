---
title: Irql\_Miniport\_Driver\_Function rule (ndis)
description: The Irql\_Miniport\_Driver\_Function rule specifies that the NDIS functions for miniport drivers must be called at correct IRQL levels.
ms.assetid: b82627db-63bd-413f-9d7f-dbb611cf2c50
ms.date: 05/21/2018
keywords: ["Irql_Miniport_Driver_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Miniport_Driver_Function
api_type:
- NA
ms.localizationpriority: medium
---

# Irql\_Miniport\_Driver\_Function rule (ndis)


The Irql\_Miniport\_Driver\_Function rule specifies that the NDIS functions for miniport drivers must be called at correct IRQL levels.

This rule verifies functions for NDIS miniport driver logging, NDIS ports, and NDIS DMA interface.

**NdisMCreateLog**
**NdisMDeregisterDmaChannel**
**NdisMDeregisterIoPortRange**
**NdisMDeregisterMiniportDriver**
**NdisMFlushLog**
**NdisMFreePort**
**NdisMFreeSharedMemory**
**NdisMGetDeviceProperty**
**NdisMGetDmaAlignment**
**NdisMMapIoSpace**
**NdisMPauseComplete**
**NdisMQueryAdapterInstanceName**
**NdisMReadDmaCounter**
**NdisMRegisterDmaChannel**
**NdisMRegisterIoPortRange**
**NdisMRegisterMiniportDriver**
**NdisMRemoveMiniport**
**NdisMResetComplete**
**NdisMRestartComplete**
**NdisMSetMiniportAttributes**
**NdisMSetupDmaTransfer**
**NdisMSleep**
**NdisMUnmapIoSpace**
**NdisMUpdateSharedMemory**
**NdisMWriteLogData**

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>Irql_Miniport_Driver_Function</strong> rule.</p>
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

[**NdisMCreateLog**](https://msdn.microsoft.com/library/windows/hardware/ff563572)
[**NdisMDeregisterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff563574)
[**NdisMDeregisterIoPortRange**](https://msdn.microsoft.com/library/windows/hardware/ff563577)
[**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578)
[**NdisMFlushLog**](https://msdn.microsoft.com/library/windows/hardware/ff563584)
[**NdisMFreePort**](https://msdn.microsoft.com/library/windows/hardware/ff563588)
[**NdisMFreeSharedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563589)
[**NdisMGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff563592)
[**NdisMGetDmaAlignment**](https://msdn.microsoft.com/library/windows/hardware/ff563593)
[**NdisMMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff563613)
[**NdisMPauseComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563628)
[**NdisMQueryAdapterInstanceName**](https://msdn.microsoft.com/library/windows/hardware/ff563630)
[**NdisMReadDmaCounter**](https://msdn.microsoft.com/library/windows/hardware/ff563641)
[**NdisMRegisterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff563646)
[**NdisMRegisterIoPortRange**](https://msdn.microsoft.com/library/windows/hardware/ff563651)
[**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654)
[**NdisMRemoveMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff563661)
[**NdisMResetComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563663)
[**NdisMRestartComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563665)
[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)
[**NdisMSetupDmaTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff563675)
[**NdisMSleep**](https://msdn.microsoft.com/library/windows/hardware/ff563677)
[**NdisMUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff563691)
[**NdisMWriteLogData**](https://msdn.microsoft.com/library/windows/hardware/ff563695)








