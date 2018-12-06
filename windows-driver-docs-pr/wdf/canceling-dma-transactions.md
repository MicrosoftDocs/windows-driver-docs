---
title: Canceling DMA Transactions
description: Canceling DMA Transactions
ms.assetid: 1E1D659D-80C9-45B1-B96F-78E5A1EE4F6B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Canceling DMA Transactions


\[Applies to KMDF only\]

If your driver has been built with version 1.11 or a later version of KMDF and is running on Windows 8 or later using direct memory access (DMA) version 3, the driver can attempt to cancel a pending DMA transaction by calling the [**WdfDmaTransactionCancel**](https://msdn.microsoft.com/library/windows/hardware/hh451127) method.

When calling [**WdfDmaTransactionCancel**](https://msdn.microsoft.com/library/windows/hardware/hh451127), the driver must ensure that the specified DMA transaction is not completed during the call. The driver can use the following technique to safely cancel a transaction, either before DMA channel allocation or after some number of transfer operations have already completed:

1.  In one of the driver's [request handlers](request-handlers.md), the driver calls [**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984) and provides an [*EvtRequestCancel*](https://msdn.microsoft.com/library/windows/hardware/ff541817) callback function for the I/O request. The request handler then calls [**WdfDmaTransactionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff547062).
2.  The driver's [*EvtRequestCancel*](https://msdn.microsoft.com/library/windows/hardware/ff541817) callback function (which may begin running in a separate thread immediately after the call to [**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)) calls [**WdfDmaTransactionCancel**](https://msdn.microsoft.com/library/windows/hardware/hh451127).
3.  If the call to [**WdfDmaTransactionCancel**](https://msdn.microsoft.com/library/windows/hardware/hh451127) occurs after the call to [**WdfDmaTransactionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff547062), but before the **WdfDmaTransactionExecute** method has started DMA allocation, transaction cancellation succeeds and **WdfDmaTransactionCancel** returns TRUE. In this case, the driver's [*EvtRequestCancel*](https://msdn.microsoft.com/library/windows/hardware/ff541817) callback function must [complete the DMA transaction](completing-a-dma-transaction.md). **WdfDmaTransactionExecute** returns an error value.
4.  If the driver calls [**WdfDmaTransactionCancel**](https://msdn.microsoft.com/library/windows/hardware/hh451127) after the [**WdfDmaTransactionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff547062) method has started DMA allocation, the attempt to cancel the transaction fails and **WdfDmaTransactionCancel** returns FALSE. In this case, **WdfDmaTransactionExecute** returns STATUS\_SUCCESS and the driver's request handler must [complete the DMA transaction](completing-a-dma-transaction.md).

    At this point, if the driver is using system-mode DMA, the [*EvtRequestCancel*](https://msdn.microsoft.com/library/windows/hardware/ff541817) callback function might call [**WdfDmaTransactionStopSystemTransfer**](https://msdn.microsoft.com/library/windows/hardware/hh439264) to attempt to stop the in-progress system-mode DMA transfer. For a code example that shows how to do this, see [**WdfDmaTransactionStopSystemTransfer**](https://msdn.microsoft.com/library/windows/hardware/hh439264).

5.  After the [**WdfDmaTransactionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff547062) method finishes DMA allocation, the framework calls the driver's [*EvtProgramDma*](https://msdn.microsoft.com/library/windows/hardware/ff541816) callback function (which may begin running in a separate thread immediately after the call to **WdfDmaTransactionExecute**). At this point, a call to the [**WdfDmaTransactionCancel**](https://msdn.microsoft.com/library/windows/hardware/hh451127) method would return FALSE.

    In [*EvtProgramDma*](https://msdn.microsoft.com/library/windows/hardware/ff541816), the driver can call [**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035) to end the possibility of request cancellation. If **WdfRequestUnmarkCancelable** returns STATUS\_SUCCESS, the callback function must program the hardware to start the transfer. If **WdfRequestUnmarkCancelable** returns STATUS\_CANCELLED, the request has been canceled. In this case, *EvtProgramDma* must call [**WdfDmaTransactionDmaCompletedFinal**](https://msdn.microsoft.com/library/windows/hardware/ff547049) to [complete the DMA transaction](completing-a-dma-transaction.md).

    The driver can use the same technique to cancel a DMA transaction after some number of transfer operations have already completed. In this case, the driver calls [**WdfDmaTransactionCancel**](https://msdn.microsoft.com/library/windows/hardware/hh451127) after it calls [**WdfDmaTransactionDmaCompleted**](https://msdn.microsoft.com/library/windows/hardware/ff547039), but before the framework calls [*EvtProgramDma*](https://msdn.microsoft.com/library/windows/hardware/ff541816) to program the next transfer operation. If the driver happens to call **WdfDmaTransactionCancel** before it calls **WdfDmaTransactionDmaCompleted**, **WdfDmaTransactionDmaCompleted** returns **TRUE**, indicating that the DMA transaction has been completed.

 

 





