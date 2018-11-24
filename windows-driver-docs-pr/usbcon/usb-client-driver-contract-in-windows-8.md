---
Description: This topic describes best practices for a client driver for allocating, building, and sending an URB to the USB driver stack included with Windows 8.
title: Best Practices - Using URBs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Best Practices: Using URBs


This topic describes best practices for a client driver for allocating, building, and sending an URB to the USB driver stack included with Windows 8.

Windows 8 includes a new USB driver stack to support Universal Serial Bus (USB) 3.0 devices. The new USB 3.0 driver stack implements several new capabilities, as per the USB 3.0 specification. In addition, the driver stack includes other capabilities that enable a client driver to perform common tasks efficiently. For instance, the new driver stack accepts chained-MDLs that allows the client driver to send a transfer buffer in discontiguous pages in physical memory.

Before a client driver can use the new capabilities of the USB driver stack for Windows 8, the driver must register itself with the underlying USB driver stack that is loaded by Windows for the device. To register the client driver, call [**USBD\_CreateHandle**](https://msdn.microsoft.com/library/windows/hardware/hh406241) and specify a *contract version*. If the client driver is intended to build, run, and use the improvements and the new capabilities on Windows 8, the client contract version is USBD\_CLIENT\_CONTRACT\_VERSION\_602.

For a USBD\_CLIENT\_CONTRACT\_VERSION\_602 version client driver, the USB driver stack assumes that the client driver conforms to the following set of rules:

-   [Do not send I/O requests by using stale or invalid pipe handles](#do-not-send-i-o-requests-by-using-stale-or-invalid-pipe-handles)
-   [Allocate URBs by calling allocation routines in Windows 8](#allocate-urbs-by-calling-allocation-routines-in-windows-8)
-   [Do not reuse active URBs associated with pending requests](#do-not-reuse-active-urbs-associated-with-pending-requests)
-   [Do not use polling period greater than 8 for high speed and SuperSpeed isochronous transfers](#do-not-use-polling-period-greater-than-8-for-high-speed-and-superspeed-isochronous-transfers)
-   [Make sure that the number of isochronous packets that is a multiple of number of packets per frame](#make-sure-that-the-number-of-isochronous-packets-that-is-a-multiple-of-number-of-packets-per-frame)
-   [Call the routine at the documented IRQL level](#call-the-routine-at-the-documented-irql-level)
-   [Related topics](#related-topics)

The USB driver stack performs validations on the received requests and handles the violations whenever possible. Failure to do so might lead to an undefined behavior.

## Do not send I/O requests by using stale or invalid pipe handles


The client driver must *not* use stale pipe handles to send I/O requests to the USB driver stack. A *stale pipe handle* refers to a pipe handle that was obtained in a request to select a configuration, an interface, or an alternate setting that is no longer selected in the device. To avoid stale pipe handles, every time the client driver selects a configuration or an interface, the driver must refresh its cache of pipe handles (usually stored in the device context). Certain race conditions can also result in stale pipe handles. For instance, the client driver sends an I/O request by using a pipe handle on the selected interface. Before the request completes, the client driver selects an alternate setting that does not use the same endpoint associated with the pipe handle in use. Both of those pending requests might cause a race condition making the pipe handle invalid.

## Allocate URBs by calling allocation routines in Windows 8


Windows 8 provides new routines for allocating, building, and releasing USB Request Blocks (URBs). To allocate URBs, a Windows Driver Model (WDM) client driver must always use the new routines shown in the following list:

-   [**USBD\_UrbAllocate**](https://msdn.microsoft.com/library/windows/hardware/hh406250)
-   [**USBD\_IsochUrbAllocate**](https://msdn.microsoft.com/library/windows/hardware/hh406231)
-   [**USBD\_SelectConfigUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406243)
-   [**USBD\_SelectInterfaceUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406245)
-   [**USBD\_UrbFree**](https://msdn.microsoft.com/library/windows/hardware/hh406252)
-   [**USBD\_AssignUrbToIoStackLocation**](https://msdn.microsoft.com/library/windows/hardware/hh406228)

The routines in the preceding list might attach an opaque URB context to the allocated URB in order to improve tracking and processing. The client driver cannot view or modify the contents of the URB context. For more information about URB allocation in Windows 8, see [Allocating and Building URBs](how-to-add-xrb-support-for-client-drivers.md).

If a Windows Driver Framework (WDF) client driver that identifies its version as USBD\_CLIENT\_CONTRACT\_VERSION\_602 during registration (see **WdfUsbTargetDeviceCreateWithParameters**), the USB driver stack expects the client driver to allocate memory for the URB by calling the new **WdfUsbTargetDeviceCreateUrb**.

## Do not reuse active URBs associated with pending requests


The USB driver stack deliberately bugchecks if it detects that an active URB that has been resubmitted before the request associated with the URB. An URB is active as long as the request is pending, and the client driver's IRP completion routine has not been called. Do not perform the following tasks on an active URB.

-   Do *not* resubmit an active URB for another request (associate the URB with another IRP).
-   Do *not* modify the contents of an active URB.
-   Do *not* free an active URB.

After the client driver's completion routine is called, the drivers can resubmit URBs for the certain types of request within the completion routine. The following rules apply for resubmissions:

-   The client driver must not reuse an URB that is allocated by [**USBD\_SelectConfigUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406243) for any type of request other than a select-configuration request to select the same configuration.
-   The client driver must not reuse an URB that is allocated by [**USBD\_SelectInterfaceUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406245) for any type of request other than a select-interface request to select the same alternate setting in an interface. For an example, see Remarks in **USBD\_SelectInterfaceUrbAllocateAndBuild**.
-   An URB that is allocated by [**USBD\_IsochUrbAllocate**](https://msdn.microsoft.com/library/windows/hardware/hh406231) must be reused only for isochronous transfer requests. Conversely, an URB that is allocated for other types of I/O requests (control, bulk, or interrupt) must not be used for an isochronous request.

    For instance, a client driver allocates and builds an [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) structure for a bulk transfer request. The client driver also wants to send data to isochronous endpoints in the device. After a bulk transfer request completes, the client driver must *not* reformat and submit the URB for an isochronous request. That is because an URB associated with an isochronous request, has a variable length depending on the number of packets. In addition, the packets are required to start and end on a frame boundary. The allocated URB (for the bulk transfer) might not fit the buffer layout required for an isochronous transfer and the request might fail.

-   An URB that is allocated by [**USBD\_UrbAllocate**](https://msdn.microsoft.com/library/windows/hardware/hh406250) must not be reused for an isochronous, a select-configuration, or a select-interface request. The URB can be reused for selecting a NULL configuration to disable the selected configuration in the device. The URB must not be active and the client driver must reformat the URB by calling the [**UsbBuildSelectConfigurationRequest**](https://msdn.microsoft.com/library/windows/hardware/ff538968) macro and passing NULL in the *ConfigurationDescriptor* parameter.
-   Before resubmitting an URB, the client driver must reformat the URB by using the appropriate **UsbBuildXxx** macro defined for the type of request. It is important for the driver to format the URB, because the USB stack might have altered some of its contents.

    For instance, suppose a driver calls [**UsbBuildInterruptOrBulkTransferRequest**](https://msdn.microsoft.com/library/windows/hardware/ff538953) to initialize an URB for a bulk transfer request (see [**\_URB\_BULK\_OR\_INTERRUPT\_TRANSFER**](https://msdn.microsoft.com/library/windows/hardware/ff540352)). If the driver initializes the **TransferBufferMDL** member of the [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) structure to NULL, the USB driver stack uses the transfer buffer, specified **TransferBuffer**, in to exchange data with the device instead of an MDL. However, internally, the USB driver stack might create an MDL, store a pointer to the MDL in **TransferBufferMDL**, and use the MDL to pass data down the stack. Even though the USB driver stack frees the MDL memory, **TransferBufferMDL** might not be NULL when the client driver is processing the URB in the completion routine. To ensure that the members of the URB are properly formatted, the driver must call **UsbBuildInterruptOrBulkTransferRequest** again to reformat the URB before submitting the request,

## Do not use polling period greater than 8 for high speed and SuperSpeed isochronous transfers


The USB driver stack supports high speed and SuperSpeed isochronous pipes with a polling period numbers of 1, 2, 4, or 8. A client driver must not send IO to an endpoint that has a period of greater than 8. Doing so might lead to a bugcheck.

## Make sure that the number of isochronous packets that is a multiple of number of packets per frame


For high speed and SuperSpeed isochronous transfers, the number of isochronous packets per frame is calculated as 8 / polling period. The client driver must make sure that the **NumberOfPackets** value specified in the URB (see [**\_URB\_ISOCH\_TRANSFER**](https://msdn.microsoft.com/library/windows/hardware/ff540414)) is a multiple of number of packets per frame.

The USB driver stack does not support isochronous transfer URBs in which the **NumberOfPackets** is not a multiple of number of packets per frame.

## Call the routine at the documented IRQL level


If you register your client driver with USBD\_CLIENT\_CONTRACT\_VERSION\_602 as the contract version, the USB driver stack assumes that the client driver sent the request at the appropriate IRQL level. If a client driver sends a request at DISPATCH\_LEVEL, which should be sent at PASSIVE\_LEVEL. Upon receiving the request, in some cases, the USB driver stack validates the IRQL value and fails the request. However, in other cases, the USB driver stack might generate a bugcheck.

## Related topics
[Sending Requests to a USB Device](communicating-with-a-usb-device.md)  



