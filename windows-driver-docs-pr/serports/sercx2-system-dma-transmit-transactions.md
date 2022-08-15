---
title: SerCx2 System-DMA-Transmit Transactions
description: Some serial controller drivers implement support for transmit transactions that use the system DMA controller.
ms.date: 04/20/2017
---

# SerCx2 System-DMA-Transmit Transactions

Some serial controller drivers implement support for transmit transactions that use the system DMA controller. Such support is optional but can improve performance by relieving the main processor of the need to use programmed I/O (PIO) for long data transfers. SerCx2 performs a system-DMA-transmit transaction by setting up the system DMA controller and initiating the necessary DMA transfers on behalf of the serial controller driver.

When the serial controller driver creates a system-DMA-transmit object, the driver supplies the parameters that SerCx2 will use to set up the system DMA adapter for system-DMA-transmit transactions.

Before the start of the transaction, the serial controller driver has the option to do any special set-up of the serial controller hardware or DMA adapter that might be required for the transaction. After the transaction finishes, the driver has the option to drain the transmit FIFO, and, if necessary, to clean up the serial controller hardware state.

## Creating the system-DMA-transmit object

Before SerCx2 can call any of the serial controller driver's *EvtSerCx2SystemDmaTransmit*Xxx** functions, the driver must call the [**SerCx2SystemDmaTransmitCreate**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitcreate) method to register these functions with SerCx2. This method accepts, as an input parameter, a pointer to a [**SERCX2\_SYSTEM\_DMA\_TRANSMIT\_CONFIG**](/windows-hardware/drivers/ddi/sercx/ns-sercx-_sercx2_system_dma_transmit_config) structure that contains pointers to the driver's *EvtSerCx2SystemDmaTransmit*Xxx** functions.

As an option, the driver can implement any or all of the following functions:

- [*EvtSerCx2SystemDmaTransmitInitializeTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_initialize_transaction)
- [*EvtSerCx2SystemDmaTransmitCleanupTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_cleanup_transaction)
- [*EvtSerCx2SystemDmaTransmitConfigureDmaChannel*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_configure_dma_channel)

As an option, the driver can implement the following functions:

- [*EvtSerCx2SystemDmaTransmitDrainFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_drain_fifo)
- [*EvtSerCx2SystemDmaTransmitCancelDrainFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_cancel_drain_fifo)
- [*EvtSerCx2SystemDmaTransmitPurgeFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_purge_fifo)

A driver that implements any of the functions in the preceding list must implement all three.

The **SerCx2SystemDmaTransmitCreate** method creates a system-DMA-transmit object and supplies the calling driver with a [**SERCX2SYSTEMDMATRANSMIT**](./sercx2-object-handles.md#sercx2systemdmatransmit-object-handle) handle to this object. The driver's *EvtSerCx2SystemDmaTransmit*Xxx** functions all take this handle as their first parameter. The following SerCx2 methods take this handle as their first parameter:

- [**SerCx2SystemDmaTransmitDrainFifoComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitdrainfifocomplete)
- [**SerCx2SystemDmaTransmitPurgeFifoComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitpurgefifocomplete)
- [**SerCx2SystemDmaTransmitInitializeTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitinitializetransactioncomplete)
- [**SerCx2SystemDmaTransmitCleanupTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitcleanuptransactioncomplete)
- [**SerCx2SystemDmaTransmitGetDmaEnabler**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitgetdmaenabler)

## Hardware initialization and clean-up

Some serial controller drivers might need to initialize the serial controller hardware at the start of a system-DMA-transmit transaction, or to clean up the hardware state of the serial controller at the end of the transaction.

If a driver implements an [*EvtSerCx2SystemDmaTransmitInitializeTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_initialize_transaction) event callback function, SerCx2 calls this function to initialize the serial controller before starting the first DMA transfer in the transaction. If implemented, the *EvtSerCx2SystemDmaTransmitInitializeTransaction* function must call the [**SerCx2SystemDmaTransmitInitializeTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitinitializetransactioncomplete) method to inform SerCx2 when the driver finishes initializing the serial controller.

If the driver implements an [*EvtSerCx2SystemDmaTransmitCleanupTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_cleanup_transaction) event callback function, SerCx2 calls this function to clean up the hardware state after the end of the final DMA transfer in the transaction. If implemented, the *EvtSerCx2SystemDmaTransmitInitializeTransaction* function must call the [**SerCx2SystemDmaTransmitCleanupTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitcleanuptransactioncomplete) method to inform SerCx2 when the driver finishes cleaning up the serial controller.

A serial controller driver that needs to do any special configuration of the system DMA controller at the start of a system-DMA-transmit transaction should implement an [*EvtSerCx2SystemDmaTransmitConfigureDmaChannel*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_configure_dma_channel) event callback function. This function can call the [**SerCx2SystemDmaTransmitGetDmaEnabler**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitgetdmaenabler) method to get the DMA enabler for the system DMA adapter used for the transaction. SerCx2 calls this function before starting the first DMA transfer in the transaction. For more information about DMA enablers, see [Enabling DMA Transactions](../wdf/enabling-dma-transactions.md).

## Draining and purging the transmit FIFO

A serial controller driver that supports system-DMA-transmit transactions should implement an [*EvtSerCx2SystemDmaTransmitDrainFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_drain_fifo) event callback function if the driver can detect when the transmit FIFO empties. If implemented, SerCx2 calls this function after the last byte of data in a system-DMA-transmit transaction has been written to the transmit FIFO. During this call, the *EvtSerCx2SystemDmaTransmitDrainFifo* function typically enables an interrupt that's triggered when the transmit FIFO empties, and then returns without waiting for the interrupt. When the FIFO empties, the driver calls the [**SerCx2SystemDmaTransmitDrainFifoComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitdrainfifocomplete) method to notify SerCx2. Only after receiving this notification does SerCx2 complete the pending write ([**IRP\_MJ\_WRITE**](/previous-versions/ff546904(v=vs.85))) request that is associated with the system-DMA-transmit transaction.

If the serial controller driver does not implement an *EvtSerCx2SystemDmaTransmitDrainFifo* function, SerCx2 must complete the pending write request without first verifying that the transmit FIFO has emptied. There can be no guarantee that data written to the FIFO will be transmitted without a significant delay. Any data that remains in the FIFO after a write request is completed might be lost before it can be transmitted. This unexpected data loss in a successfully completed write request can create reliability problems for the peripheral driver that sent the request.

A driver that implements an *EvtSerCx2SystemDmaTransmitDrainFifo* function must also implement [*EvtSerCx2SystemDmaTransmitCancelDrainFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_cancel_drain_fifo) and [*EvtSerCx2SystemDmaTransmitPurgeFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_transmit_purge_fifo) event callback functions.

The *EvtSerCx2SystemDmaTransmitCancelDrainFifo* function enables SerCx2 to cancel an ongoing FIFO-drain operation before it finishes. SerCx2 might cancel this operation if the write request is canceled, or if the serial controller is about to exit the D0 device power state to enter a low-power state. If the *EvtSerCx2SystemDmaTransmitCancelDrainFifo* function successfully cancels the FIFO-drain operation, this function returns **TRUE**. A return value of **TRUE** guarantees that the *EvtSerCx2SystemDmaTransmitDrainFifo* function will return without first calling **SerCx2SystemDmaTransmitDrainFifoComplete**. A return value of **FALSE** indicates that the *EvtSerCx2SystemDmaTransmitDrainFifo* function has called or will call **SerCx2SystemDmaTransmitDrainFifoComplete**.

If the write request associated with a system-DMA-transmit transaction is canceled or times out before it completes, SerCx2 calls the *EvtSerCx2SystemDmaTransmitPurgeFifo* function, if it is implemented, to discard any unsent data that might remain the transmit FIFO. When the FIFO is purged, the *EvtSerCx2SystemDmaTransmitPurgeFifo* function calls the [**SerCx2SystemDmaTransmitPurgeFifoComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitpurgefifocomplete) method to notify SerCx2. Only after receiving this notification does SerCx2 start a new I/O transaction.
