---
title: Irql\_Miniport\_Driver\_Function rule (ndis)
description: The Irql\_Miniport\_Driver\_Function rule specifies that the NDIS functions for miniport drivers must be called at correct IRQL levels.
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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>Irql_Miniport_Driver_Function</strong> rule.</p>
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

[**NdisMCreateLog**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcreatelog)
[**NdisMDeregisterDmaChannel**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterdmachannel)
[**NdisMDeregisterIoPortRange**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterioportrange)
[**NdisMDeregisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterminiportdriver)
[**NdisMFlushLog**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismflushlog)
[**NdisMFreePort**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreeport)
[**NdisMFreeSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreesharedmemory)
[**NdisMGetDeviceProperty**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetdeviceproperty)
[**NdisMGetDmaAlignment**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetdmaalignment)
[**NdisMMapIoSpace**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismmapiospace)
[**NdisMPauseComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismpausecomplete)
[**NdisMQueryAdapterInstanceName**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismqueryadapterinstancename)
[**NdisMReadDmaCounter**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismreaddmacounter)
[**NdisMRegisterDmaChannel**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterdmachannel)
[**NdisMRegisterIoPortRange**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterioportrange)
[**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver)
[**NdisMRemoveMiniport**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismremoveminiport)
[**NdisMResetComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismresetcomplete)
[**NdisMRestartComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismrestartcomplete)
[**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes)
[**NdisMSetupDmaTransfer**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetupdmatransfer)
[**NdisMSleep**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsleep)
[**NdisMUnmapIoSpace**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismunmapiospace)
[**NdisMWriteLogData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismwritelogdata)
