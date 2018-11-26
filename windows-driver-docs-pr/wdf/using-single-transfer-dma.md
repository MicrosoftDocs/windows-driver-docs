---
title: Using Single Transfer DMA
description: This topic describes how a KMDF driver requests single transfer DMA.
ms.assetid: 57bf9988-6eed-42ca-a961-a6d16c5c19c1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Single Transfer DMA

By default, WDF sometimes splits a single DMA transaction into multiple DMA transfers. However, some devices cannot handle a fragmented transaction and must instead receive all data in a single DMA operation.  For example, some PCI network controllers require one network packet at a time because they do not have the hardware to cache and reassemble partial data.

Starting in KMDF version 1.19, a KMDF driver using DMA v3 can specify that it requires single transfer DMA transactions.  The driver can specify single transfer for a single DMA transaction only, or it can specify single transfer for all DMA transactions created using a specified DMA enabler.  

## Setting single transfer for a specific DMA transaction

To set single transfer for a single transaction, use the following sequence:

1. Call [**WdfDmaTransactionCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547027) or [**WdfDmaTransactionRelease**](https://msdn.microsoft.com/library/windows/hardware/ff547114).
2. Call [**WdfDmaTransactionSetSingleTransferRequirement**](https://msdn.microsoft.com/library/windows/hardware/988c7e70-3b2a-4a0f-91cf-dfab3ea07f05).
3. Call [**WdfDmaTransactionInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff547099).  
    If initialization fails due to transaction fragmentation, a driver can fail the I/O request or it can rearrange the transaction's memory buffers and reinitialize the transaction.
4. Call [**WdfDmaTransactionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff547062).

When debugging your driver, you can use the [**!wdfkd.wdfdmatransaction**](https://msdn.microsoft.com/library/windows/hardware/ff565721) extension to determine if single transfer is set for a given transaction object.

## Setting the single-transfer requirement for all DMA transactions created with a particular DMA enabler

To set single transfer for all transactions created with a given enabler, specify the **WDF_DMA_ENABLER_CONFIG_REQUIRE_SINGLE_TRANSFER** flag in [**WDF_DMA_ENABLER_CONFIG_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/hh439491) when calling [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/guid).  

A driver that uses this flag does not need to call [**WdfDmaTransactionSetSingleTransferRequirement**](https://msdn.microsoft.com/library/windows/hardware/988c7e70-3b2a-4a0f-91cf-dfab3ea07f05) each time it creates or reuses a transaction object.

This setting also persists if the driver [reuses the transaction object](reusing-dma-transaction-objects.md).

When debugging, use the [**!wdfkd.wdfdmaenabler**](https://msdn.microsoft.com/library/windows/hardware/ff565717) extension to determine if single transfer is set for a given DMA enabler object.

For information about the order in which WDF calls your driver's DMA event callback functions, see [Handling I/O Requests in a KMDF Driver for a Bus-Master DMA Device](handling-i-o-requests-in-a-kmdf-driver-for-a-bus-master-dma-device.md).
