---
title: Using Single Transfer DMA
description: This topic describes how a KMDF driver requests single transfer DMA.
ms.date: 04/20/2017
---

# Using Single Transfer DMA

By default, WDF sometimes splits a single DMA transaction into multiple DMA transfers. However, some devices cannot handle a fragmented transaction and must instead receive all data in a single DMA operation.  For example, some PCI network controllers require one network packet at a time because they do not have the hardware to cache and reassemble partial data.

Starting in KMDF version 1.19, a KMDF driver using DMA v3 can specify that it requires single transfer DMA transactions.  The driver can specify single transfer for a single DMA transaction only, or it can specify single transfer for all DMA transactions created using a specified DMA enabler.  

## Setting single transfer for a specific DMA transaction

To set single transfer for a single transaction, use the following sequence:

1. Call [**WdfDmaTransactionCreate**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncreate) or [**WdfDmaTransactionRelease**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionrelease).
2. Call [**WdfDmaTransactionSetSingleTransferRequirement**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetsingletransferrequirement).
3. Call [**WdfDmaTransactionInitialize**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitialize).  
    If initialization fails due to transaction fragmentation, a driver can fail the I/O request or it can rearrange the transaction's memory buffers and reinitialize the transaction.
4. Call [**WdfDmaTransactionExecute**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionexecute).

When debugging your driver, you can use the [**!wdfkd.wdfdmatransaction**](../debugger/-wdfkd-wdfdmatransaction.md) extension to determine if single transfer is set for a given transaction object.

## Setting the single-transfer requirement for all DMA transactions created with a particular DMA enabler

To set single transfer for all transactions created with a given enabler, specify the **WDF_DMA_ENABLER_CONFIG_REQUIRE_SINGLE_TRANSFER** flag in [**WDF_DMA_ENABLER_CONFIG_FLAGS**](/windows-hardware/drivers/ddi/wdfdmaenabler/ne-wdfdmaenabler-_wdf_dma_enabler_config_flags) when calling [**WdfDmaEnablerCreate**](/previous-versions/jj619276(v=technet.10)).  

A driver that uses this flag does not need to call [**WdfDmaTransactionSetSingleTransferRequirement**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetsingletransferrequirement) each time it creates or reuses a transaction object.

This setting also persists if the driver [reuses the transaction object](reusing-dma-transaction-objects.md).

When debugging, use the [**!wdfkd.wdfdmaenabler**](../debugger/-wdfkd-wdfdmaenabler.md) extension to determine if single transfer is set for a given DMA enabler object.

For information about the order in which WDF calls your driver's DMA event callback functions, see [Handling I/O Requests in a KMDF Driver for a Bus-Master DMA Device](handling-i-o-requests-in-a-kmdf-driver-for-a-bus-master-dma-device.md).
