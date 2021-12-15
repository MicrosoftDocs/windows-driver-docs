---
title: Reserving DMA Resources
description: Reserving DMA Resources
ms.date: 04/20/2017
---

# Reserving DMA Resources


\[Applies to KMDF only\]

Typically, framework-based drivers do not reserve map registers ahead of time. However, in certain circumstances, drivers may need to reserve these resources in advance.

Framework-based drivers running on Windows 8 or later can reserve a specified number of map registers for a DMA enabler that specifies a packet or system profile. To do so, the driver calls [**WdfDmaTransactionAllocateResources**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionallocateresources) and registers an [*EvtReserveDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_reserve_dma) callback function.

The framework calls the driver's [*EvtReserveDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_reserve_dma) function when it has reserved the map registers and the WDM DMA adapter's lock. The driver can then initialize and initiate the transaction multiple times using the same transaction object before finally releasing the transaction object. To release the DMA resources back to the system, the driver calls [**WdfDmaTransactionFreeResources**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionfreeresources).

To determine the number of map registers required for a transaction, the driver can call [**WdfDmaTransactionGetTransferInfo**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiongettransferinfo) before calling [**WdfDmaTransactionAllocateResources**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionallocateresources). The driver must initialize the transaction before calling **WdfDmaTransactionGetTransferInfo**.

The following steps demonstrate how a driver can reserve and release a DMA enabler for exclusive use with a specified transaction:

1.  The driver receives an I/O request.

2.  The driver's [request handler](request-handlers.md) calls [**WdfDmaTransactionCreate**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncreate) to create a DMA transaction object for the request.

3.  The driver's [request handler](request-handlers.md) calls [**WdfDmaTransactionAllocateResources**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionallocateresources) to reserve resources.

4.  The framework calls [*EvtReserveDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_reserve_dma) when it has reserved the requested resources.

5.  In [*EvtReserveDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_reserve_dma), the driver calls [**WdfDmaTransactionInitializeUsingRequest**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitializeusingrequest) or [**WdfDmaTransactionInitialize**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitialize) to initialize the transaction object.

6.  In [*EvtReserveDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_reserve_dma), the driver calls the [**WdfDmaTransactionExecute**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionexecute) method to start the transaction. Because the transaction has reserved resources, the framework immediately calls the driver's [*EvtProgramDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_program_dma) callback function.

7.  From [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtDmaTransactionDmaTransferComplete*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_dma_transaction_dma_transfer_complete), the driver calls [**WdfDmaTransactionDmaCompleted**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompleted), [**WdfDmaTransactionDmaCompletedWithLength**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompletedwithlength), or [**WdfDmaTransactionDmaCompletedFinal**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompletedfinal), followed by [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) or [**WdfDmaTransactionRelease**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionrelease). The driver must not delete or release the transaction until the transaction has been completed or canceled. After the completion of this step, the map registers remain reserved.

8.  The driver can repeat steps 5–7 as many times as necessary.

    When the driver no longer needs the reservation, the driver calls [**WdfDmaTransactionFreeResources**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionfreeresources) from [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtDmaTransactionDmaTransferComplete*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_dma_transaction_dma_transfer_complete). Alternatively, the driver can call **WdfDmaTransactionFreeResources** from its [*EvtReserveDma*](/windows-hardware/drivers/ddi/wdfdmatransaction/nc-wdfdmatransaction-evt_wdf_reserve_dma) event callback function.

 

