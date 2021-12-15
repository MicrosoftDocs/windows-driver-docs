---
title: Completing a DMA Transfer
description: Completing a DMA Transfer
keywords:
- DMA operations WDK KMDF , transfers
- bus-master DMA WDK KMDF , transfers
- DMA transfers WDK KMDF , completing
- completing DMA transfers WDK KMDF
ms.date: 04/20/2017
---

# Completing a DMA Transfer


\[Applies to KMDF only\]




Typically, your driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function completes the processing of each DMA transfer.

First, because multiple DMA transactions can be in progress concurrently, the [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function must determine which DMA transaction the completed transfer is associated with. The callback function can do this by retrieving the transaction handle that the driver stored when it [started the DMA transaction](starting-a-dma-transaction.md). To retrieve the device extension, the [PLX9x5x](/samples/browse/) sample defines a function called **PLxGetDeviceContext** in its Private.h header file:

```cpp
WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(DEVICE_EXTENSION, PLxGetDeviceContext)
```

Then, in the driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback, it does the following:

```cpp
WDFDMATRANSACTION   dmaTransaction;
PDEVICE_EXTENSION   devExt;
...
devExt  = PLxGetDeviceContext(WdfInterruptGetDevice(Interrupt));
...
dmaTransaction = devExt->WriteDmaTransaction;
```

Next, the [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function must inform the framework that a transfer is complete, by calling one of the following transfer completion methods:

-   [**WdfDmaTransactionDmaCompleted**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompleted), if the transfer completed successfully and the hardware does not report a count of transferred bytes.

-   [**WdfDmaTransactionDmaCompletedWithLength**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompletedwithlength), if the transfer completed successfully and the hardware reports a count of transferred bytes (or a count of bytes not transferred), or if the driver detected an error and specifies a transfer count of zero to retry the transfer. If the driver specifies a transfer count of zero, the framework subtracts zero from the number of bytes that remain and thus sends the same transfer to the [*EvtProgramDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_program_dma) callback function.

-   [**WdfDmaTransactionDmaCompletedFinal**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompletedfinal), if the hardware reports an underrun or failure condition.

Your driver can call [**WdfDmaTransactionGetCurrentDmaTransferLength**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiongetcurrentdmatransferlength) to obtain the original length of the completed transfer. This call is useful if your device reports a count of bytes that were not transferred, because the driver can subtract the number of non-transferred bytes from the original transfer length and then call **WdfDmaTransactionGetCurrentDmaTransferLength** to report the actual transfer size.

Each of the preceding transfer completion methods informs the framework that a single [DMA transfer](dma-transactions-and-dma-transfers.md) (not the entire [DMA transaction](dma-transactions-and-dma-transfers.md)) is complete. After your driver calls one of these methods, the driver checks the method's return value to see if the transaction requires more transfers:

-   If the completion method's return value is **FALSE**, the framework has determined that additional DMA transfers are required to finish processing the DMA transaction.

    Typically, the driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function just returns. The framework calls the driver's [*EvtProgramDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_program_dma) callback function again, and the callback function can program the hardware for the next transfer.

    The transfer completion methods provide a status value, which is always STATUS\_MORE\_PROCESSING\_REQUIRED in this case.

-   If the return value is **TRUE**, no more transfers will occur for the DMA transaction.

    The transfer completion methods provide a status value. If the status value is STATUS\_SUCCESS, all transfers for the DMA transaction are complete and the driver must [complete the DMA transaction](completing-a-dma-transaction.md). If the status value is anything else, an error occurred and the DMA transaction might not have been completed.

If the [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function detects an error, typically due to a timer expiring or a hardware interrupt signaling a transfer error, the driver can restart the transaction's current transfer.

To restart the transaction's current transfer, the driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function can call [**WdfDmaTransactionDmaCompletedWithLength**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompletedwithlength) with the *TransferredLength* parameter set to zero.

