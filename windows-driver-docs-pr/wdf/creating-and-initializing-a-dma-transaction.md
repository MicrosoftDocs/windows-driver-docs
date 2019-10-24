---
title: Creating and Initializing a DMA Transaction
description: Creating and Initializing a DMA Transaction
ms.assetid: 1982c3fa-9e4a-4b26-8902-321223d9159f
keywords:
- DMA transactions WDK KMDF , initializing
- DMA operations WDK KMDF , transactions
- bus-master DMA WDK KMDF , transactions
- DMA transactions WDK KMDF , creating
- initializing DMA transactions WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating and Initializing a DMA Transaction


\[Applies to KMDF only\]




Before your driver can send an I/O request to a DMA device, the driver must:

1.  Call [**WdfDmaTransactionCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncreate) to create a DMA transaction object for the request.

2.  Call [**WdfDmaTransactionInitializeUsingRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitializeusingrequest), [**WdfDmaTransactionInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitialize), or [**WdfDmaTransactionInitializeUsingOffset**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitializeusingoffset) to initialize the transaction object.

Typically, your driver creates a [DMA transaction](dma-transactions-and-dma-transfers.md) because a [request handler](request-handlers.md) has received a [framework request object](framework-request-objects.md) and must pass the request to the hardware. In this case, the driver should call [**WdfDmaTransactionInitializeUsingRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitializeusingrequest), which accepts a request object handle as input and extracts the request's address parameters from the request object.

If your driver must create a DMA transaction that is *not* based on a framework request object that the driver received, the driver can call either [**WdfDmaTransactionInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitialize) or [**WdfDmaTransactionInitializeUsingOffset**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitializeusingoffset). Both methods accept address parameters that the driver provides.

All three initialization methods require the address of an [*EvtProgramDma*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_program_dma) event callback function as an input parameter. This callback function programs the device, and the framework calls the callback function each time a [DMA transfer](dma-transactions-and-dma-transfers.md) is available.

When your driver calls [**WdfDmaEnablerCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablercreate) to create a DMA enabler object, the driver supplies a [**WDF\_DMA\_ENABLER\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmaenabler/ns-wdfdmaenabler-_wdf_dma_enabler_config) structure that contains the device's maximum transfer length. The framework uses this value as the default maximum length for all DMA transfers.

For some types of DMA transactions, you might need to specify a maximum transfer length that is different from the device's default maximum length. You can use [**WdfDmaTransactionSetMaximumLength**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetmaximumlength) to set a maximum transfer length for an individual transaction. The framework uses the specified maximum transfer length only while it processes the specified transaction.

Note that the maximum transfer length is limited by the number of [map registers](https://docs.microsoft.com/windows-hardware/drivers/kernel/map-registers) that the operating system makes available to the DMA enabler object. To determine the maximum transfer length that is available, your driver can call [**WdfDmaEnablerGetFragmentLength**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablergetfragmentlength). If the value that **WdfDmaEnablerGetFragmentLength** returns is less than the maximum transfer length that the driver supplied to [**WdfDmaEnablerCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablercreate), the framework uses the smaller value.

After your driver creates and initializes a DMA transaction, the driver must [start the transaction](starting-a-dma-transaction.md).

 

 





