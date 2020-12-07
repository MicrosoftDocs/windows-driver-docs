---
title: Completing a DMA Transaction
description: Completing a DMA Transaction
keywords:
- DMA transactions WDK KMDF , completing
- DMA operations WDK KMDF , transactions
- bus-master DMA WDK KMDF , transactions
- completing DMA transactions WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Completing a DMA Transaction


\[Applies to KMDF only\]




Each time that a driver's device [completes a DMA transfer](completing-a-dma-transfer.md), the driver must call [**WdfDmaTransactionDmaCompleted**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompleted), [**WdfDmaTransactionDmaCompletedWithLength**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompletedwithlength), or [**WdfDmaTransactionDmaCompletedFinal**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompletedfinal) and then check the return value.

When the return value is **TRUE**, no more transfers are needed for the DMA transaction and the driver must complete the DMA transaction. Typically, the driver has not yet returned from its [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function. Therefore, this callback function completes the DMA transaction by:

1.  Calling [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) to delete the transaction object, or calling [**WdfDmaTransactionRelease**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionrelease) if the driver [reuses DMA transaction objects](reusing-dma-transaction-objects.md).

2.  Calling [**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete) or [**WdfRequestCompleteWithInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation), if the transaction is associated with a framework request object.

If the driver calls [**WdfRequestCompleteWithInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation), it typically first calls [**WdfDmaTransactionGetBytesTransferred**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiongetbytestransferred) to obtain the total length (number of bytes) of all of the transaction's transfers.

These steps are illustrated in the following code example, taken from the [PLX9x5x](/samples/browse/) sample’s [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function in the *Isrdpc.c* file:

```cpp
if (readComplete) {
    BOOLEAN              transactionComplete;
    WDFDMATRANSACTION    dmaTransaction;
    size_t               bytesTransferred;

    // Get the current Read DmaTransaction.
    dmaTransaction = devExt->CurrentReadDmaTransaction;

    // Indicate that this DMA operation has completed:
    // This may start the transfer on the next packet if 
    // there is still data to be transferred.
    transactionComplete = 
          WdfDmaTransactionDmaCompleted( dmaTransaction, &status ); 
    if (transactionComplete) {
        // Complete the DmaTransaction and the request.
        devExt->CurrentReadDmaTransaction = NULL;
        bytesTransferred =  
               ((NT_SUCCESS(status)) ? 
               WdfDmaTransactionGetBytesTransferred(dmaTransaction): 0 );
        WdfDmaTransactionRelease(dmaTransaction);
        WdfRequestCompleteWithInformation(request, status, bytesTransferred);
    }
}
```
