---
title: Porting I/O Dispatch Routines to I/O Event Callback Functions
description: Porting I/O Dispatch Routines to I/O Event Callback Functions
ms.assetid: 0BD65185-C358-4E28-8E31-255AF8D77F93
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting I/O Dispatch Routines to I/O Event Callback Functions


The core of a WDM driver’s I/O dispatch routines maps to the WDF driver’s I/O event callback functions. However, the I/O event callback functions differ in several important ways from a WDM driver’s I/O dispatch routines:

-   When the framework invokes a WDF driver’s I/O event callback, the callback receives the request in a noncancelable state. The request cannot be canceled unless the driver explicitly marks it as cancelable.
-   The driver specifies whether the framework synchronizes calls to the I/O event callbacks so that only one such callback runs concurrently for each queue or for each device object, or whether the framework applies no synchronization at all. For more information about selecting synchronization options, see [Using Automatic Synchronization](using-automatic-synchronization.md).

These differences mean that most I/O event callback functions contain significantly less code to synchronize access and to prevent race conditions than the corresponding WDM **DispatchXxx** routines.

Aside from synchronization, the primary differences between a WDM driver’s I/O dispatch routines and a WDF driver’s I/O event callback functions lie in how the driver retrieves parameters and how it accesses I/O buffers.

## Parameters for I/O Requests


Depending on the types of requests that a WDF driver handles and the way it configures its I/O queues, a driver might not be required to parse the parameters to an I/O request as a WDM driver does. When the framework calls the I/O event callbacks for read, write, and device I/O control requests ([*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776), [*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813), [*EvtIoDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541758), [*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768)), it extracts the most commonly used parameters from the IRP and passes them as parameters to the callback. For example, the framework calls a driver’s *EvtIoRead* callback with a handle to the WDFREQUEST object and the number of bytes to read. If the driver does not require a device offset or a sort key, it can simply retrieve the buffer from the WDFREQUEST object by calling one of the **WdfRequestRetrieveOutputXxx** methods; it does not need to retrieve additional parameters.

In an **EvtIoDefault** callback, however, the framework passes only a handle to the queue and a handle to the request object. Consequently, the driver must call **WdfRequestGetParameters** to get the parameters, including the type of request (**WdfRequestTypeXxx**). [**WdfRequestGetParameters**](https://msdn.microsoft.com/library/windows/hardware/ff549969) returns a [**WDF\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff552472) structure that contains the parameters that were passed with a create, read, write, device I/O control, or internal device I/O control request.

## Access to Buffers for Buffered and Direct I/O


When the framework receives a request for I/O, it creates a WDFREQUEST object that encapsulates the underlying WDM IRP. It then queues the WDFREQUEST object and eventually dispatches it according to the driver’s [dispatch specification](dispatching-methods-for-i-o-requests.md) for the queue. The driver uses WDF methods to retrieve parameters and buffers for the I/O request. A driver can get the underlying WDM IRP at any time by calling [**WdfRequestWdmGetIrp**](https://msdn.microsoft.com/library/windows/hardware/ff550037).

Like WDM drivers, WDF drivers can support [buffered, direct, or neither I/O](https://msdn.microsoft.com/library/windows/hardware/ff540701). A driver sets the type of I/O that is supported for each device object by calling [**WdfDeviceInitSetIoType**](https://msdn.microsoft.com/library/windows/hardware/ff546128) in the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback before creating the device object. Unlike a WDM driver, however, a KMDF driver accesses the buffers in the same way whether it performs buffered or direct I/O and uses the same methods for each.

Although a WDF driver accesses buffers in the same way for both buffered and direct I/O, it uses different methods to retrieve the buffers depending on the type of I/O request. The following sections describe how the driver handles each type of I/O request:

-   [Create Requests](#create-requests)
-   [Read Requests](#read-requests)
-   [Write Requests](#write-requests)
-   [Device I/O Control Requests](#device-i-o-requests)
-   [Internal Device I/O Control Requests](#int-dev-i-o)

## Create Requests


A WDF driver can handle create requests ([**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729)) in one of two ways:

-   Bypass queuing and instead supply an [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback.
-   Have the framework queue create requests and implement an [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) callback to handle such requests from the queue.

For detailed information about handling file creation requests, see [Framework File Objects](framework-file-objects.md#creating-or-opening-a-file).

## Read Requests


To retrieve a buffer for a read request ([**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794)), a WDF driver calls one of the **WdfRequestRetrieveOutputXxx** methods. The buffer that each of these methods returns depends on whether the driver performs [buffered, direct, or neither I/O](https://msdn.microsoft.com/library/windows/hardware/ff540701).

For information about WDM equivalents for buffer pointers, see [WDM Equivalents for KMDF Buffer Pointers](wdm-equivalents-for-kmdf-buffer-pointers.md#read).

## Write Requests


To retrieve a buffer for a write request ([**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819)), a WDF driver calls one of the **WdfRequestRetrieveInputXxx** methods. The buffer that each of these methods returns depends on whether the driver performs [buffered, direct, or neither I/O](https://msdn.microsoft.com/library/windows/hardware/ff540701).

For information about WDM equivalents for buffer pointers, see [WDM Equivalents for KMDF Buffer Pointers](wdm-equivalents-for-kmdf-buffer-pointers.md#write).

## Device I/O Control Requests


To handle a device I/O control request ([**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744)), a WDF driver calls either **WdfRequestRetrieveInputXxx** methods or **WdfRequestRetrieveOutputXxx** methods to get buffers for buffered and direct I/O. The corresponding input and output methods return the same buffer, so the driver can use either one. The buffer that each of these methods returns depends on whether the driver performs [buffered, direct, or neither I/O](https://msdn.microsoft.com/library/windows/hardware/ff540701), just as in read and write requests.

If the driver handles device I/O control requests that originate in another device stack or use the **Parameters.Other** fields, the driver should call [**WdfRequestGetParameters**](https://msdn.microsoft.com/library/windows/hardware/ff549969) to get a buffer pointer instead of calling [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014) and [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018). Because the source of these requests is guaranteed to be a kernel-mode component, the driver can trust the returned buffer pointer. However, it must still validate the buffer lengths and any other parameters.

For information about WDM equivalents for buffer pointers, see [WDM Equivalents for KMDF Buffer Pointers](wdm-equivalents-for-kmdf-buffer-pointers.md#device-control).

## Internal Device I/O Control Requests


Internal device I/O control requests ([**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766)) are issued only by kernel-mode components and are used internally by some operating system components to pass request blocks (xRB protocols such as SCSI request blocks \[SRBs\] or universal request blocks \[URBs\]). Many different types of buffers can accompany such requests.

Retrieving and interpreting parameters for internal device I/O control requests can be problematic. The problem occurs because some such requests pass the length in the **InputBufferLength** and **OutputBufferLength** fields of the **Parameters.DeviceIoControl** structure of the WDM IRP, but some do not. Nevertheless, the framework extracts whatever values are in the **InputBufferLength** and **OutputBufferLength** fields and passes them as parameters to the [*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback. It does not perform any internal validation on these values.

To get the buffers themselves, the driver calls one of the following methods:

-   [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014), which returns the **Parameters.DeviceIoControl.Type3InputBuffer** field of the IRP.
-   [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018), which returns the **UserBuffer** field of the IRP.

 

 





