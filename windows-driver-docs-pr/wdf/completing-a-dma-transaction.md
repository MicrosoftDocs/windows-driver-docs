---
title: Completing a DMA Transaction
description: Completing a DMA Transaction
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 90531b72-e51d-451e-ae84-a9bbf0245665
keywords: ["DMA transactions WDK KMDF completing", "DMA operations WDK KMDF transactions", "bus master DMA WDK KMDF transactions", "completing DMA transactions WDK KMDF"]
---

# Completing a DMA Transaction


\[Applies to KMDF only\]

## <a href="" id="ddk-completing-a-dma-transaction-df"></a>


Each time that a driver's device [completes a DMA transfer](completing-a-dma-transfer.md), the driver must call [**WdfDmaTransactionDmaCompleted**](https://msdn.microsoft.com/library/windows/hardware/ff547039), [**WdfDmaTransactionDmaCompletedWithLength**](https://msdn.microsoft.com/library/windows/hardware/ff547052), or [**WdfDmaTransactionDmaCompletedFinal**](https://msdn.microsoft.com/library/windows/hardware/ff547049) and then check the return value.

When the return value is **TRUE**, no more transfers are needed for the DMA transaction and the driver must complete the DMA transaction. Typically, the driver has not yet returned from its [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function. Therefore, this callback function completes the DMA transaction by:

1.  Calling [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete the transaction object, or calling [**WdfDmaTransactionRelease**](https://msdn.microsoft.com/library/windows/hardware/ff547114) if the driver [reuses DMA transaction objects](reusing-dma-transaction-objects.md).

2.  Calling [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) or [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), if the transaction is associated with a framework request object.

If the driver calls [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), it typically first calls [**WdfDmaTransactionGetBytesTransferred**](https://msdn.microsoft.com/library/windows/hardware/ff547072) to obtain the total length (number of bytes) of all of the transaction's transfers.

These steps are illustrated in the following code example, taken from the [PLX9x5x](http://go.microsoft.com/fwlink/p/?linkid=256157) sample’s [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function in the *Isrdpc.c* file:

```
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
          WdfDmaTransactionDmaCompleted( dmaTransaction, &amp;status ); 
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Completing%20a%20DMA%20Transaction%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




