---
title: SerCx2 Custom-Transmit Transactions
description: Some serial controller hardware might implement a data-transfer mechanism other than PIO or system DMA for writing data to a serial controller.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SerCx2 Custom-Transmit Transactions

Some serial controller hardware might implement a data-transfer mechanism other than PIO or system DMA for writing data to a serial controller. A serial controller driver can support custom-transmit transactions to make this data-transfer mechanism available to be used by SerCx2.

To start a custom-transmit transaction, SerCx2 calls the driver's [*EvtSerCx2CustomTransmitTransactionStart*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_transmit_transaction_start) event callback function and supplies as parameters the write ([**IRP\_MJ\_WRITE**](/previous-versions/ff546904(v=vs.85))) request and a description of the write buffer for the transaction. In this call, the function initiates the transaction and returns. The driver is then responsible for finishing the transaction and completing the write request.

## Creating the custom-transmit object

Before SerCx2 can call any of the serial controller driver's *EvtSerCx2CustomTransmitTransaction*Xxx** functions, the driver must call the [**SerCx2CustomTransmitTransactionCreate**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmittransactioncreate) method to register these functions with SerCx2. This method accepts, as an input parameter, a pointer to a [**SERCX2\_CUSTOM\_TRANSMIT\_TRANSACTION\_CONFIG**](/windows-hardware/drivers/ddi/sercx/ns-sercx-_sercx2_custom_transmit_transaction_config) structure that contains pointers to the driver's *EvtSerCx2CustomTransmitTransaction*Xxx** functions.

The driver must implement the following function:

- [*EvtSerCx2CustomTransmitTransactionStart*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_transmit_transaction_start)

As an option, the driver can implement one or both of the following functions:

- [*EvtSerCx2CustomTransmitTransactionInitialize*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_transmit_transaction_initialize)
- [*EvtSerCx2CustomTransmitTransactionCleanup*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_transmit_transaction_cleanup)

The **SerCx2CustomTransmitTransactionCreate** method creates a custom-transmit object and supplies the calling driver with a [**SERCX2CUSTOMTRANSMITTRANSACTION**](./sercx2-object-handles.md#sercx2customtransmittransaction-object-handle) handle to this object. The driver's *EvtSerCx2CustomTransmitTransaction*Xxx** functions all take this handle as their first parameter. The following SerCx2 methods take this handle as their first parameter:

- [**SerCx2CustomTransmitTransactionInitializeComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmittransactioninitializecomplete)
- [**SerCx2CustomTransmitTransactionCleanupComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmittransactioncleanupcomplete)

## Hardware initialization and clean-up

Some serial controller drivers might need to initialize the serial controller hardware at the start of a custom-transmit transaction, or to clean up the hardware state of the serial controller at the end of the transaction.

If a driver implements an [*EvtSerCx2CustomTransmitTransactionInitialize*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_transmit_transaction_initialize) event callback function, SerCx2 calls this function to initialize the serial controller before starting the transaction. If implemented, the *EvtSerCx2CustomTransmitTransactionInitialize* function must call the [**SerCx2CustomTransmitTransactionInitializeComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmittransactioninitializecomplete) method to inform SerCx2 when the driver finishes initializing the serial controller.

If the driver implements an [*EvtSerCx2CustomTransmitTransactionCleanup*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_transmit_transaction_cleanup) event callback function, SerCx2 calls this function to clean up the hardware state after the transaction ends. If implemented, the *EvtSerCx2CustomTransmitTransactionInitialize* function must call the [**SerCx2CustomTransmitTransactionCleanupComplete**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmittransactioncleanupcomplete) method to inform SerCx2 when the driver finishes cleaning up the serial controller.

## Accessing the request object

To start a custom-transmit transaction, SerCx2 calls the driver's [*EvtSerCx2CustomTransmitTransactionStart*](/windows-hardware/drivers/ddi/sercx/nc-sercx-evt_sercx2_custom_transmit_transaction_start) function and passes the associated write request (encapsulated in a WDFREQUEST object handle) to this function as a parameter. The driver is responsible for calling a method such as [**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete) to complete this request when the transaction finishes. Unless the request can be completed immediately, before the *EvtSerCx2CustomTransmitTransactionStart* function returns, the driver must call a method such as [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex) to mark the request as cancelable.

The serial controller driver must not use a method such as [**WdfRequestRetrieveInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer) to access the data buffer in the write request. Instead, the driver should use the *Mdl*, *Offset*, and *Length* parameter values passed to the *EvtSerCx2CustomTransmitTransactionStart* function to access this buffer.

During a custom-transmit transaction, the driver might need to store information about the transaction in a context that is attached to the request object. If so, the driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) event callback function can call the [**WdfDeviceInitSetRequestAttributes**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetrequestattributes) method to set the attributes to use for request objects. These attributes include the name and allocation size to use for request contexts. The request attributes specified in this call must match the request attributes that the driver specifies in the call to the [**SerCx2InitializeDevice**](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2initializedevice) method. These attributes are specified in the **RequestAttributes** member of the **SERCX2\_CONFIG** structure that the driver passes to **SerCx2InitializeDevice**. For more information, see [**SERCX2\_CONFIG**](/windows-hardware/drivers/ddi/sercx/ns-sercx-_sercx2_config).

For a write request that the serial controller driver receives at the start of a custom-transmit transaction, the request context allocated by the driver framework is uninitialized. The driver should, as a best practice, call the [**RtlZeroMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlzeromemory) routine to initialize this request context to all zeros.
