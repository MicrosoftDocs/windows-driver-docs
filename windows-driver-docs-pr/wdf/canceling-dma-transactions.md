---
title: Canceling DMA Transactions
description: Canceling DMA Transactions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Canceling DMA Transactions


\[Applies to KMDF only\]

If your driver has been built with version 1.11 or a later version of KMDF and is running on Windows 8 or later using direct memory access (DMA) version 3, the driver can attempt to cancel a pending DMA transaction by calling the [**WdfDmaTransactionCancel**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncancel) method.

When calling [**WdfDmaTransactionCancel**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncancel), the driver must ensure that the specified DMA transaction is not completed during the call. The driver can use the following technique to safely cancel a transaction, either before DMA channel allocation or after some number of transfer operations have already completed:

1.  In one of the driver's [request handlers](request-handlers.md), the driver calls [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex) and provides an [*EvtRequestCancel*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel) callback function for the I/O request. The request handler then calls [**WdfDmaTransactionExecute**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionexecute).
2.  The driver's [*EvtRequestCancel*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel) callback function (which may begin running in a separate thread immediately after the call to [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex)) calls [**WdfDmaTransactionCancel**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncancel).
3.  If the call to [**WdfDmaTransactionCancel**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncancel) occurs after the call to [**WdfDmaTransactionExecute**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionexecute), but before the **WdfDmaTransactionExecute** method has started DMA allocation, transaction cancellation succeeds and **WdfDmaTransactionCancel** returns TRUE. In this case, the driver's [*EvtRequestCancel*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel) callback function must [complete the DMA transaction](completing-a-dma-transaction.md). **WdfDmaTransactionExecute** returns an error value.
4.  If the driver calls [**WdfDmaTransactionCancel**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncancel) after the [**WdfDmaTransactionExecute**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionexecute) method has started DMA allocation, the attempt to cancel the transaction fails and **WdfDmaTransactionCancel** returns FALSE. In this case, **WdfDmaTransactionExecute** returns STATUS\_SUCCESS and the driver's request handler must [complete the DMA transaction](completing-a-dma-transaction.md).

    At this point, if the driver is using system-mode DMA, the [*EvtRequestCancel*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel) callback function might call [**WdfDmaTransactionStopSystemTransfer**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionstopsystemtransfer) to attempt to stop the in-progress system-mode DMA transfer. For a code example that shows how to do this, see [**WdfDmaTransactionStopSystemTransfer**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionstopsystemtransfer).

5.  After the [**WdfDmaTransactionExecute**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionexecute) method finishes DMA allocation, the framework calls the driver's [*EvtProgramDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_program_dma) callback function (which may begin running in a separate thread immediately after the call to **WdfDmaTransactionExecute**). At this point, a call to the [**WdfDmaTransactionCancel**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncancel) method would return FALSE.

    In [*EvtProgramDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_program_dma), the driver can call [**WdfRequestUnmarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestunmarkcancelable) to end the possibility of request cancellation. If **WdfRequestUnmarkCancelable** returns STATUS\_SUCCESS, the callback function must program the hardware to start the transfer. If **WdfRequestUnmarkCancelable** returns STATUS\_CANCELLED, the request has been canceled. In this case, *EvtProgramDma* must call [**WdfDmaTransactionDmaCompletedFinal**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompletedfinal) to [complete the DMA transaction](completing-a-dma-transaction.md).

    The driver can use the same technique to cancel a DMA transaction after some number of transfer operations have already completed. In this case, the driver calls [**WdfDmaTransactionCancel**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncancel) after it calls [**WdfDmaTransactionDmaCompleted**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompleted), but before the framework calls [*EvtProgramDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_program_dma) to program the next transfer operation. If the driver happens to call **WdfDmaTransactionCancel** before it calls **WdfDmaTransactionDmaCompleted**, **WdfDmaTransactionDmaCompleted** returns **TRUE**, indicating that the DMA transaction has been completed.

 

