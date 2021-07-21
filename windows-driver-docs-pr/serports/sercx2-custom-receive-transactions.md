---
title: SerCx2 Custom-Receive Transactions
description: Some serial controller hardware might implement a data-transfer mechanism other than PIO or system DMA for reading data from a serial controller.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SerCx2 Custom-Receive Transactions

Some serial controller hardware might implement a data-transfer mechanism other than PIO or system DMA for reading data from a serial controller. A serial controller driver can support custom-receive transactions to make this data-transfer mechanism available to be used by SerCx2.

To start a custom-receive transaction, SerCx2 calls the driver's [*EvtSerCx2CustomReceiveTransactionStart*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_receive_transaction_start) event callback function and supplies as parameters the read ([**IRP\_MJ\_READ**](/previous-versions/ff546883(v=vs.85))) request and a description of the read buffer for the transaction. In this call, the function initiates the transaction and returns. The driver is then responsible for finishing the transaction and completing the read request.

## Creating the custom-receive object

Before SerCx2 can call any of the serial controller driver's *EvtSerCx2CustomReceiveTransaction*Xxx** functions, the driver must call the [**SerCx2CustomReceiveTransactionCreate**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactioncreate) method to register these functions with SerCx2. This method accepts, as an input parameter, a pointer to a [**SERCX2\_CUSTOM\_RECEIVE\_TRANSACTION\_CONFIG**](/windows-hardware/drivers/ddi/sercx/ns-sercx-_sercx2_custom_receive_transaction_config) structure that contains pointers to the driver's *EvtSerCx2CustomReceiveTransaction*Xxx** functions.

The driver must implement the following two functions:

- [*EvtSerCx2CustomReceiveTransactionStart*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_receive_transaction_start)
- [*EvtSerCx2CustomReceiveTransactionQueryProgress*](/previous-versions/windows/hardware/drivers/dn265203(v=vs.85))

As an option, the driver can implement any or all of the following three functions:

- [*EvtSerCx2CustomReceiveTransactionEnableNewDataNotification*](/previous-versions/windows/hardware/drivers/dn265201(v=vs.85))
- [*EvtSerCx2CustomReceiveTransactionInitialize*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_receive_transaction_initialize)
- [*EvtSerCx2CustomReceiveTransactionCleanup*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_receive_transaction_cleanup)

The **SerCx2CustomReceiveTransactionCreate** method creates a custom-receive object and supplies the calling driver with a [**SERCX2CUSTOMRECEIVETRANSACTION**](./sercx2-object-handles.md#sercx2customreceivetransaction-object-handle) handle to this object. The driver's *EvtSerCx2CustomReceiveTransaction*Xxx** functions all take this handle as their first parameter. The following SerCx2 methods take this handle as their first parameter:

- [**SerCx2CustomReceiveTransactionNewDataNotification**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactionnewdatanotification)
- [**SerCx2CustomReceiveTransactionReportProgress**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactionreportprogress)
- [**SerCx2CustomReceiveTransactionInitializeComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactioninitializecomplete)
- [**SerCx2CustomReceiveTransactionCleanupComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactioncleanupcomplete)

## Hardware initialization and clean-up

Some serial controller drivers might need to initialize the serial controller hardware at the start of a custom-receive transaction, or to clean up the hardware state of the serial controller at the end of the transaction.

If a driver implements an [*EvtSerCx2CustomReceiveTransactionInitialize*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_receive_transaction_initialize) event callback function, SerCx2 calls this function to initialize the serial controller before starting the transaction. If implemented, the *EvtSerCx2CustomReceiveTransactionInitialize* function must call the [**SerCx2CustomReceiveTransactionInitializeComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactioninitializecomplete) method to inform SerCx2 when the driver finishes initializing the serial controller.

If the driver implements an [*EvtSerCx2CustomReceiveTransactionCleanup*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_receive_transaction_cleanup) event callback function, SerCx2 calls this function to clean up the hardware state after the transaction ends. If implemented, the *EvtSerCx2CustomReceiveTransactionInitialize* function must call the [**SerCx2CustomReceiveTransactionCleanupComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactioncleanupcomplete) method to inform SerCx2 when the driver finishes cleaning up the serial controller.

## New-data notifications

As an option, the serial controller driver can implement an [*EvtSerCx2CustomReceiveTransactionEnableNewDataNotification*](/previous-versions/windows/hardware/drivers/dn265201(v=vs.85)) event callback function. If implemented, SerCx2 uses this function to efficiently manage interval time-outs that occur during the handling of read requests that are processed as custom-receive transactions.

An interval time-out occurs if the interval between two successive bytes received by the serial controller exceeds a client-specified maximum time. After a peripheral driver sends a read request to SerCx2, an interval time-out cannot occur until after at least one byte of data is received from the serially connected peripheral device. The time between the arrival of a read request and the receipt of the first byte of data from the peripheral device might be significantly longer than the time required to receive the rest of the data for the read request after the first byte is received. For more information, see [**SERIAL\_TIMEOUTS**](/windows-hardware/drivers/ddi/ntddser/ns-ntddser-_serial_timeouts).

SerCx2 calls the *EvtSerCx2CustomReceiveTransactionEnableNewDataNotification* function, if it is implemented, to enable a new-data notification. If this notification is enabled and the serial controller receives one or more bytes of new data from the peripheral device, or already has data in its receive FIFO, the serial controller driver must call the [**SerCx2CustomReceiveTransactionNewDataNotification**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactionnewdatanotification) method to notify SerCx2.

To detect a possible interval time-out, SerCx2 periodically calls the [*EvtSerCx2CustomReceiveTransactionQueryProgress*](/previous-versions/windows/hardware/drivers/dn265203(v=vs.85)) event callback function to check whether any data was received during the preceding interval. How SerCx2 detects receipt of the first byte of data depends on whether the serial controller driver implements an *EvtSerCx2CustomReceiveTransactionEnableNewDataNotification* function. If this function is implemented, SerCx2 calls the function to enable a new-data notification, and is notified by the driver when the first byte of data is received. Otherwise, SerCx2 periodically calls the *EvtSerCx2CustomReceiveTransactionQueryProgress* function to detect receipt of the first byte, and might need to periodically wake the processor to make these calls. Thus, a driver that implements an *EvtSerCx2CustomReceiveTransactionEnableNewDataNotification* function can reduce power consumption by not requiring the processor to wake as often.

SerCx2 does not explicitly cancel a pending new-data notification for a custom-receive transaction. However, the serial controller driver might need to implicitly cancel a new-data notification if the notification is enabled and the driver must complete the associated read request for one of the following reasons:

- The read request times out or is canceled.
- The serial controller is about to exit the D0 device power state to enter a low-power state.

The driver typically calls a method such as [**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete) to complete the request. The driver must never call **SerCx2CustomReceiveTransactionNewDataNotification** after the request is completed.

## Accessing the request object

To start a custom-receive transaction, SerCx2 calls the driver's [*EvtSerCx2CustomReceiveTransactionStart*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_receive_transaction_start) function and passes the associated read request (encapsulated in a WDFREQUEST object handle) to this function as a parameter. The driver is responsible for calling a method such as [**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete) to complete this request when the transaction finishes. Unless the request can be completed immediately, before the *EvtSerCx2CustomReceiveTransactionStart* function returns, the driver must call a method such as [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex) to mark the request as cancelable.

The serial controller driver must not use a method such as [**WdfRequestRetrieveOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer) to access the data buffer in the read request. Instead, the driver should use the *Mdl*, *Offset*, and *Length* parameter values passed to the *EvtSerCx2CustomReceiveTransactionStart* function to access this buffer.

During a custom-receive transaction, the driver might need to store information about the transaction in a context that is attached to the request object. If so, the driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) event callback function can call the [**WdfDeviceInitSetRequestAttributes**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetrequestattributes) method to set the attributes to use for request objects. These attributes include the name and allocation size to use for request contexts. The request attributes specified in this call must match the request attributes that the driver specifies in the call to the [**SerCx2InitializeDevice**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2initializedevice) method. These attributes are specified in the **RequestAttributes** member of the **SERCX2\_CONFIG** structure that the driver passes to **SerCx2InitializeDevice**. For more information, see [**SERCX2\_CONFIG**](/windows-hardware/drivers/ddi/sercx/ns-sercx-_sercx2_config).

For a read request that the serial controller driver receives at the start of a custom-receive transaction, the request context allocated by the driver framework is uninitialized. The driver should, as a best practice, call the [**RtlZeroMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlzeromemory) routine to initialize this request context to all zeros.
