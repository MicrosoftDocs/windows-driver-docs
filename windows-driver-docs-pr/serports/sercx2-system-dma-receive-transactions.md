---
title: SerCx2 System-DMA-Receive Transactions
description: Some serial controller drivers implement support for receive transactions that use the system DMA controller.
ms.date: 04/20/2017
---

# SerCx2 System-DMA-Receive Transactions

Some serial controller drivers implement support for receive transactions that use the system DMA controller. Such support is optional but can improve performance by relieving the main processor of the need to use programmed I/O (PIO) for long data transfers. SerCx2 performs a system-DMA-receive transaction by setting up the system DMA controller and initiating the necessary DMA transfers on behalf of the serial controller driver.

When the serial controller driver creates a system-DMA-receive object, the driver supplies the parameters that SerCx2 will use to set up the system DMA adapter for system-DMA-receive transactions.

Before the start of a system-DMA-receive transaction, the serial controller driver has the option to do any special set-up of the serial controller hardware or DMA adapter that might be required for the transaction. After the transaction finishes, the driver can, if necessary, do any clean-up of the serial controller hardware state that might be required.

## Creating the system-DMA-receive object

Before SerCx2 can call any of the serial controller driver's *EvtSerCx2SystemDmaReceive*Xxx** functions, the driver must call the [**SerCx2SystemDmaReceiveCreate**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivecreate) method to register these functions with SerCx2. This method accepts, as an input parameter, a pointer to a [**SERCX2\_SYSTEM\_DMA\_RECEIVE\_CONFIG**](/windows-hardware/drivers/ddi/sercx/ns-sercx-_sercx2_system_dma_receive_config) structure that contains pointers to the driver's *EvtSerCx2SystemDmaReceive*Xxx** functions.

As an option, the driver can implement any or all of the following functions:

- [*EvtSerCx2SystemDmaReceiveInitializeTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_receive_initialize_transaction)
- [*EvtSerCx2SystemDmaReceiveCleanupTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_receive_cleanup_transaction)
- [*EvtSerCx2SystemDmaReceiveConfigureDmaChannel*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_receive_configure_dma_channel)

As an option, the driver can implement the following two functions:

- [*EvtSerCx2SystemDmaReceiveEnableNewDataNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_receive_enable_new_data_notification)
- [*EvtSerCx2SystemDmaReceiveCancelNewDataNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_receive_cancel_new_data_notification)

A driver that implements one of the two functions in the preceding list must implement both.

The **SerCx2SystemDmaReceiveCreate** method creates a system-DMA-receive object and supplies the calling driver with a [**SERCX2SYSTEMDMARECEIVE**](./sercx2-object-handles.md) handle to this object. The driver's *EvtSerCx2SystemDmaReceive*Xxx** functions all take this handle as their first parameter. The following SerCx2 methods take this handle as their first parameter:

- [**SerCx2SystemDmaReceiveNewDataNotification**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivenewdatanotification)
- [**SerCx2SystemDmaReceiveInitializeTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceiveinitializetransactioncomplete)
- [**SerCx2SystemDmaReceiveCleanupTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivecleanuptransactioncomplete)
- [**SerCx2SystemDmaReceiveGetDmaEnabler**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivegetdmaenabler)

## Hardware initialization and clean-up

Some serial controller drivers might need to initialize the serial controller hardware at the start of a system-DMA-receive transaction, or to clean up the hardware state of the serial controller at the end of the transaction.

If a driver implements an [*EvtSerCx2SystemDmaReceiveInitializeTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_receive_initialize_transaction) event callback function, SerCx2 calls this function to initialize the serial controller before starting the first DMA transfer in the transaction. If implemented, the *EvtSerCx2SystemDmaReceiveInitializeTransaction* function must call the [**SerCx2SystemDmaReceiveInitializeTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceiveinitializetransactioncomplete) method to inform SerCx2 when the driver finishes initializing the serial controller.

If the driver implements an [*EvtSerCx2SystemDmaReceiveCleanupTransaction*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_receive_cleanup_transaction) event callback function, SerCx2 calls this function to clean up the hardware state after the end of the final DMA transfer in the transaction. If implemented, the *EvtSerCx2SystemDmaReceiveInitializeTransaction* function must call the [**SerCx2SystemDmaReceiveCleanupTransactionComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivecleanuptransactioncomplete) method to inform SerCx2 when the driver finishes cleaning up the serial controller.

A serial controller driver that needs to do any special configuration of the system DMA controller at the start of a system-DMA-receive transaction should implement an [*EvtSerCx2SystemDmaReceiveConfigureDmaChannel*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_receive_configure_dma_channel) event callback function. This function can call the [**SerCx2SystemDmaReceiveGetDmaEnabler**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivegetdmaenabler) method to get the DMA enabler for the system DMA adapter used for the transaction. SerCx2 calls this function before starting the first DMA transfer in the transaction. For more information about DMA enablers, see [Enabling DMA Transactions](../wdf/enabling-dma-transactions.md).

## New-data notifications

As an option, the serial controller driver can implement an [*EvtSerCx2SystemDmaReceiveEnableNewDataNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_receive_enable_new_data_notification) event callback function. If implemented, SerCx2 uses this function to efficiently manage interval time-outs during the handling of read requests that are processed as system-DMA-receive transactions.

An interval time-out occurs if the interval between two successive bytes received by the serial controller exceeds a client-specified maximum time. After a peripheral driver sends a read request to SerCx2, an interval time-out cannot occur until after at least one byte of data is received from the serially connected peripheral device. The time between the arrival of a read request and the receipt of the first byte of data from the peripheral device might be significantly longer than the time required to receive the rest of the data for the read request after the first byte is received. For more information, see [**SERIAL\_TIMEOUTS**](/windows-hardware/drivers/ddi/ntddser/ns-ntddser-_serial_timeouts).

SerCx2 calls the *EvtSerCx2SystemDmaReceiveEnableNewDataNotification* function, if it is implemented, to enable a *new-data notification*. If this notification is enabled and the serial controller receives one or more bytes of new data from the peripheral device, or already has data in its receive FIFO, the serial controller driver must call the [**SerCx2SystemDmaReceiveNewDataNotification**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivenewdatanotification) method to notify SerCx2.

To detect a possible interval time-out, SerCx2 periodically calls the [**ReadDmaCounter**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pread_dma_counter) routine of the system DMA adapter to check whether any data was received during the preceding interval. How SerCx2 detects receipt of the first byte of data depends on whether the serial controller driver implements an *EvtSerCx2SystemDmaReceiveEnableNewDataNotification* function. If this function is implemented, SerCx2 calls the function to enable a new-data notification, and is notified by the driver when the first byte of data is received. Otherwise, SerCx2 periodically calls **ReadDmaCounter** to detect receipt of the first byte, and might need to periodically wake the processor to make these calls. Thus, a driver that implements an *EvtSerCx2SystemDmaReceiveEnableNewDataNotification* function can reduce power consumption by not requiring the processor to wake as often.

**Note**  SerCx2 relies on the **ReadDmaCounter** routine of the system DMA adapter to monitor time-outs during system-DMA-receive transactions and system-DMA-transmit transactions. The hardware abstraction layer (HAL) must implement a fully functional **ReadDmaCounter** routine for the system DMA controller used to transfer data to and from the serial controller.

A serial controller driver that supports new-data notifications for system-DMA-receive transactions must implement an [*EvtSerCx2SystemDmaReceiveCancelNewDataNotification*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_system_dma_receive_cancel_new_data_notification) event callback function so that SerCx2 can cancel a enabled new-data notification before it occurs. If a new-data notification is enabled when the pending read request is canceled, or when a total time-out occurs, SerCx2 calls the *EvtSerCx2SystemDmaReceiveCancelNewDataNotification* function to cancel the notification. If this function successfully cancels the pending notification, it returns **TRUE**. A return value of **TRUE** guarantees that the serial controller driver will not call **SerCx2SystemDmaReceiveNewDataNotification**. A return value of **FALSE** indicates that the driver has called or will soon call **SerCx2SystemDmaReceiveNewDataNotification**. For more information about total time-outs, see [**SERIAL\_TIMEOUTS**](/windows-hardware/drivers/ddi/ntddser/ns-ntddser-_serial_timeouts).
