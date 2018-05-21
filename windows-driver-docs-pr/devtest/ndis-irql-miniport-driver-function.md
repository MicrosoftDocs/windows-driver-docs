---
title: Irql\_Miniport\_Driver\_Function rule (ndis)
description: The Irql\_Miniport\_Driver\_Function rule specifies that the NDIS functions for miniport drivers must be called at correct IRQL levels.
ms.assetid: b82627db-63bd-413f-9d7f-dbb611cf2c50
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_Miniport_Driver_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Miniport_Driver_Function
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_Miniport_Driver_Function</strong> rule.</p>
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
 

 





