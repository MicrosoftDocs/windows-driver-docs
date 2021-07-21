---
title: SerCx2 PIO-Transmit Transactions
description: SerCx2 requires all serial controller drivers to implement support for transmit transactions that use programmed I/O (PIO).
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SerCx2 PIO-Transmit Transactions

SerCx2 requires all serial controller drivers to implement support for transmit transactions that use programmed I/O (PIO). To start a PIO-transmit transaction, SerCx2 calls the driver's [*EvtSerCx2PioTransmitWriteBuffer*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_write_buffer) event callback function and supplies a write buffer as a parameter.

During this call, the *EvtSerCx2PioTransmitWriteBuffer* function transfers data from the write buffer to the transmit FIFO in the serial controller hardware. This data transfer continues until either the write buffer is empty or the transmit FIFO cannot immediately accept more data. When the transfer ends, the function returns the number of bytes that were successfully transferred from the write buffer to the FIFO.

## Creating the PIO-transmit object

Before SerCx2 can call any of the serial controller driver's *EvtSerCx2PioTransmit*Xxx** functions, the driver must call the [**SerCx2PioTransmitCreate**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitcreate) method to register these functions with SerCx2. This method accepts, as an input parameter, a pointer to a [**SERCX2\_PIO\_TRANSMIT\_CONFIG**](/windows-hardware/drivers/ddi/sercx/ns-sercx-_sercx2_pio_transmit_config) structure that contains pointers to the driver's *EvtSerCx2PioTransmit*Xxx** functions.

The driver is required to implement all three of the following functions:

- [*EvtSerCx2PioTransmitWriteBuffer*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_write_buffer)
- [*EvtSerCx2PioTransmitEnableReadyNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_enable_ready_notification)
- [*EvtSerCx2PioTransmitCancelReadyNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_cancel_ready_notification)

As an option, the driver can implement one or both of the following functions:

- [*EvtSerCx2PioTransmitInitializeTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_initialize_transaction)
- [*EvtSerCx2PioTransmitCleanupTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_cleanup_transaction)

As an option, the driver can implement the following three functions:

- [*EvtSerCx2PioTransmitDrainFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_drain_fifo)
- [*EvtSerCx2PioTransmitCancelDrainFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_cancel_drain_fifo)
- [*EvtSerCx2PioTransmitPurgeFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_purge_fifo)

If the driver implements any function in the preceding list, it must implement all three.

The **SerCx2PioTransmitCreate** method creates a PIO-transmit object and supplies the calling driver with a [**SERCX2PIOTRANSMIT**](./sercx2-object-handles.md) handle to this object. The driver's *EvtSerCx2PioTransmit*Xxx** functions all take this handle as their first parameter. The following SerCx2 methods take this handle as their first parameter:

- [**SerCx2PioTransmitReady**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitready)
- [**SerCx2PioTransmitInitializeTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitinitializetransactioncomplete)
- [**SerCx2PioTransmitCleanupTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitcleanuptransactioncomplete)
- [**SerCx2PioTransmitDrainFifoComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitdrainfifocomplete)
- [**SerCx2PioTransmitPurgeFifoComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitpurgefifocomplete)

## Hardware initialization and clean-up

Some serial controller drivers might need to initialize the serial controller hardware at the start of a PIO-transmit transaction, or to clean up the hardware state of the serial controller at the end of the transaction.

If a driver implements an [*EvtSerCx2PioTransmitInitializeTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_initialize_transaction) event callback function, SerCx2 calls this function to initialize the serial controller before the *EvtSerCx2PioTransmitWriteBuffer* call that starts the transaction. If implemented, the *EvtSerCx2PioTransmitInitializeTransaction* function must call the [**SerCx2PioTransmitInitializeTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitinitializetransactioncomplete) method to inform SerCx2 when the driver finishes initializing the serial controller.

If the driver implements an [*EvtSerCx2PioTransmitCleanupTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_cleanup_transaction) event callback function, SerCx2 calls this function to clean up the hardware state after the final *EvtSerCx2PioTransmitWriteBuffer* call in the transaction. If implemented, the *EvtSerCx2PioTransmitInitializeTransaction* function must call the [**SerCx2PioTransmitCleanupTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitcleanuptransactioncomplete) method to inform SerCx2 when the driver finishes cleaning up the serial controller.

## Draining and purging the transmit FIFO

A serial controller driver should implement an [*EvtSerCx2PioTransmitDrainFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_drain_fifo) event callback function if the driver can detect when the transmit FIFO empties. If implemented, SerCx2 calls this function after the last byte of data in a PIO-transmit transaction has been written to the transmit FIFO. During this call, the *EvtSerCx2PioTransmitDrainFifo* function typically enables an interrupt to be triggered when the transmit FIFO empties, and then returns without waiting. When the FIFO empties, the driver calls the [**SerCx2PioTransmitDrainFifoComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitdrainfifocomplete) method to notify SerCx2. Only after receiving this notification does SerCx2 complete the pending write ([**IRP\_MJ\_WRITE**](/previous-versions/ff546904(v=vs.85))) request that is associated with the PIO-transmit transaction.

If the serial controller driver does not implement an *EvtSerCx2PioTransmitDrainFifo* function, SerCx2 must complete the pending write request without first verifying that the transmit FIFO has emptied. There can be no guarantee that data written to the FIFO will be transmitted without a significant delay. Any data that remains in the FIFO after a write request is completed might be lost before it can be transmitted. This unexpected data loss in a successfully completed write request can create reliability problems for the peripheral driver that sent the request.

A driver that implements an *EvtSerCx2PioTransmitDrainFifo* function must also implement [*EvtSerCx2PioTransmitCancelDrainFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_cancel_drain_fifo) and [*EvtSerCx2PioTransmitPurgeFifo*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_drain_fifo) event callback functions.

The *EvtSerCx2PioTransmitCancelDrainFifo* function enables SerCx2 to cancel an ongoing FIFO-drain operation before it finishes. SerCx2 might cancel this operation if the write request times out or is canceled. If the *EvtSerCx2PioTransmitCancelDrainFifo* function successfully cancels the FIFO-drain operation, this function returns **TRUE**. A return value of **TRUE** guarantees that the serial controller driver has not called and will not call **SerCx2PioTransmitDrainFifoComplete**. A return value of **FALSE** indicates that the *EvtSerCx2PioTransmitDrainFifo* function has called or will soon call **SerCx2PioTransmitDrainFifoComplete**.

If the write request associated with a PIO-transmit transaction is canceled or times out before it completes, SerCx2 calls the *EvtSerCx2PioTransmitPurgeFifo* function, if it is implemented, to discard any unsent data that might remain the transmit FIFO. SerCx2 uses the information it gets from this function to tell the peripheral driver exactly how many bytes of data were successfully transmitted to the peripheral device by the write request.

## Ready notifications

When a *EvtSerCx2PioTransmitWriteBuffer* call ends because the transmit FIFO cannot immediately accept more data, SerCx2 has to wait to finish the PIO-receive transaction until, at some later time, the FIFO is ready to accept more data. In this case, SerCx2 calls the [*EvtSerCx2PioTransmitEnableReadyNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_enable_ready_notification) event callback function to enable the serial controller driver to send a ready notification. If this notification is enabled, the serial controller driver calls the [**SerCx2PioTransmitReady**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitready) method to notify SerCx2 when the driver detects that the transmit FIFO is ready accept more data. In response to this notification, SerCx2 calls the *EvtSerCx2PioTransmitWriteBuffer* function to write more data to the FIFO.

If the ready notification is enabled when the write request times out or is canceled, SerCx2 calls the [*EvtSerCx2PioTransmitCancelReadyNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_transmit_cancel_ready_notification) event callback function to cancel the pending notification. If this function successfully cancels the pending notification, it returns **TRUE**. A return value of **TRUE** guarantees that the serial controller driver will not call **SerCx2PioTransmitReady**. A return value of **FALSE** indicates that the *EvtSerCx2PioTransmitDrainFifo* function has called or will call **SerCx2PioTransmitReady**.
