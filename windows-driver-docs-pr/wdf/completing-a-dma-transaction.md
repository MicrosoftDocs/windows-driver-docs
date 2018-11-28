---
title: Completing a DMA Transaction
description: Completing a DMA Transaction
ms.assetid: 90531b72-e51d-451e-ae84-a9bbf0245665
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




Each time that a driver's device [completes a DMA transfer](completing-a-dma-transfer.md), the driver must call [**WdfDmaTransactionDmaCompleted**](https://msdn.microsoft.com/library/windows/hardware/ff547039), [**WdfDmaTransactionDmaCompletedWithLength**](https://msdn.microsoft.com/library/windows/hardware/ff547052), or [**WdfDmaTransactionDmaCompletedFinal**](https://msdn.microsoft.com/library/windows/hardware/ff547049) and then check the return value.

When the return value is **TRUE**, no more transfers are needed for the DMA transaction and the driver must complete the DMA transaction. Typically, the driver has not yet returned from its [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function. Therefore, this callback function completes the DMA transaction by:

1.  Calling [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete the transaction object, or calling [**WdfDmaTransactionRelease**](https://msdn.microsoft.com/library/windows/hardware/ff547114) if the driver [reuses DMA transaction objects](reusing-dma-transaction-objects.md).

2.  Calling [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) or [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), if the transaction is associated with a framework request object.

If the driver calls [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), it typically first calls [**WdfDmaTransactionGetBytesTransferred**](https://msdn.microsoft.com/library/windows/hardware/ff547072) to obtain the total length (number of bytes) of all of the transaction's transfers.

These steps are illustrated in the following code example, taken from the [PLX9x5x](http://go.microsoft.com/fwlink/p/?linkid=256157) sample’s [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function in the *Isrdpc.c* file:

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









