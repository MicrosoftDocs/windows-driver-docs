---
title: SerCx2 PIO-Receive Transactions
description: SerCx2 requires all serial controller drivers to implement support for receive transactions that use programmed I/O (PIO).
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SerCx2 PIO-Receive Transactions

SerCx2 requires all serial controller drivers to implement support for receive transactions that use programmed I/O (PIO). To start a PIO-receive transaction, SerCx2 calls the driver's [*EvtSerCx2PioReceiveReadBuffer*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_receive_read_buffer) event callback function and supplies a read buffer as a parameter.

During this call, the *EvtSerCx2PioReceiveReadBuffer* function transfers data to the read buffer from the receive FIFO in the serial controller hardware. This data transfer continues until either the read buffer is full or no more data is immediately available from the receive FIFO. When the transfer ends, the function returns the number of bytes that were successfully transferred to the read buffer from the FIFO. This function never waits for more data to be received.

## Creating the PIO-receive object

Before SerCx2 can call any of the serial controller driver's *EvtSerCx2PioReceive*Xxx** functions, the driver must call the [**SerCx2PioReceiveCreate**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceivecreate) method to register these functions with SerCx2. This method accepts, as an input parameter, a pointer to a [**SERCX2\_PIO\_RECEIVE\_CONFIG**](/windows-hardware/drivers/ddi/sercx/ns-sercx-_sercx2_pio_receive_config) structure that contains pointers to the driver's *EvtSerCx2PioReceive*Xxx** functions.

The driver is required to implement all three of the following functions:

- [*EvtSerCx2PioReceiveReadBuffer*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_receive_read_buffer)
- [*EvtSerCx2PioReceiveEnableReadyNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_receive_enable_ready_notification)
- [*EvtSerCx2PioReceiveCancelReadyNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_receive_cancel_ready_notification)

As an option, the driver can implement one or both of the following functions:

- [*EvtSerCx2PioReceiveInitializeTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_receive_initialize_transaction)
- [*EvtSerCx2PioReceiveCleanupTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_receive_cleanup_transaction)

The **SerCx2PioReceiveCreate** method creates a PIO-receive object and supplies the calling driver with a [**SERCX2PIORECEIVE**](./sercx2-object-handles.md) handle to this object. The driver's *EvtSerCx2PioReceive*Xxx** functions all take this handle as their first parameter. The following SerCx2 methods take this handle as their first parameter:

- [**SerCx2PioReceiveReady**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceiveready)
- [**SerCx2PioReceiveInitializeTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceiveinitializetransactioncomplete)
- [**SerCx2PioReceiveCleanupTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceivecleanuptransactioncomplete)

## Hardware initialization and clean-up

Some serial controller drivers might need to initialize the serial controller hardware at the start of a PIO-receive transaction, or to clean up the hardware state of the serial controller at the end of the transaction.

If a driver implements an [*EvtSerCx2PioReceiveInitializeTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_receive_initialize_transaction) event callback function, SerCx2 calls this function to initialize the serial controller before the *EvtSerCx2PioReceiveReadBuffer* call that starts the transaction. If implemented, the *EvtSerCx2PioReceiveInitializeTransaction* function must call the [**SerCx2PioReceiveInitializeTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceiveinitializetransactioncomplete) method to inform SerCx2 when the driver finishes initializing the serial controller.

If the driver implements an [*EvtSerCx2PioReceiveCleanupTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_receive_cleanup_transaction) event callback function, SerCx2 calls this function to clean up the hardware state after the final *EvtSerCx2PioReceiveReadBuffer* call in the transaction. If implemented, the *EvtSerCx2PioReceiveInitializeTransaction* function must call the [**SerCx2PioReceiveCleanupTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceivecleanuptransactioncomplete) method to inform SerCx2 when the driver finishes cleaning up the serial controller.

## Ready notifications

When an *EvtSerCx2PioReceiveReadBuffer* call ends because no more data is immediately available to read from the receive FIFO, SerCx2 cannot finish the PIO-receive transaction until, at some later time, the serial controller receives more data. In this case, SerCx2 calls the [*EvtSerCx2PioReceiveEnableReadyNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_receive_enable_ready_notification) event callback function to enable a ready notification. This function typically enables an interrupt to be triggered when one or more bytes of data are available to be read from the receive FIFO. If and only if this notification is enabled, the serial controller driver calls the [**SerCx2PioReceiveReady**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceiveready) method to notify SerCx2 when the driver detects that the receive FIFO is no longer empty. In response to this notification, SerCx2 calls the *EvtSerCx2PioReceiveReadBuffer* function to read the newly received data.

SerCx2 additionally uses ready notifications to efficiently manage time-outs during the handling of read requests that are processed as PIO-receive transactions. For more information about these time-outs, see [**SERIAL\_TIMEOUTS**](/windows-hardware/drivers/ddi/ntddser/ns-ntddser-_serial_timeouts).

If the ready notification is enabled when the read request times out or is canceled, SerCx2 calls the [*EvtSerCx2PioReceiveCancelReadyNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_pio_receive_cancel_ready_notification) event callback function to cancel the pending notification. If this function successfully cancels the pending notification, it returns **TRUE**. A return value of **TRUE** guarantees that the serial controller driver will not call [**SerCx2PioReceiveReady**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceiveready). A return value of **FALSE** indicates that the controller driver has already called or will soon call **SerCx2PioReceiveReady**.
