---
title: USB Request Blocks (URBs)
description: Information about how a USB client driver can allocate, build, and submit URBs to the USB driver stack.
ms.date: 01/12/2024
---

# USB request blocks (URBs)

This article describes a USB Request Block (URB) and provides information about how a USB client driver can use Windows Driver Model (WDM) routines to allocate, build, and submit URBs to the USB driver stack.

A Universal Serial Bus (USB) client driver cannot communicate with its device directly. Instead, the client driver creates requests and submits them to the USB driver stack for processing. Within each request, the client driver provides a variable-length data structure called a *USB Request Block (URB)*. The **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure describes the details of the request and also contains information about the status of the completed request. The client driver performs all device-specific operations, including data transfers, through URBs. The client driver must initialize the URB with information about the request before submitting it to the USB driver stack. For certain types of requests, Microsoft provides helper routines and macros that allocate an **URB** structure and fill the necessary members of the **URB** structure with details provided by the client driver.

Each URB begins with a standard fixed-sized header (**[_URB_HEADER](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_header)**) whose purpose is to identify the type of operation requested. The **Length** member of **_URB_HEADER** specifies the size, in bytes, of the URB. The **Function** member, which must be one of a series of system-defined URB_FUNCTION_XXX constants, determines the type of operation that is requested. In the case of data transfers, for instance, this member indicates the type of transfer. Function codes URB_FUNCTION_CONTROL_TRANSFER, URB_FUNCTION_BULK_OR_INTERRUPT_TRANSFER, and URB_FUNCTION_ISOCH_TRANSFER indicate control, bulk/interrupt, and isochronous transfers respectively. The USB driver stack uses the **Status** member to return a USB-specific status code.

To submit an URB, the client driver uses the **[IOCTL_INTERNAL_USB_SUBMIT_URB](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_urb)** request, which is delivered to the device by means of an I/O request packet (IRP) of type **[IRP_MJ_INTERNAL_DEVICE_CONTROL](../kernel/irp-mj-internal-device-control.md)**.

After the USB driver stack is done processing the URB, the driver stack uses the **Status** member of the [**URB**](/windows-hardware/drivers/ddi/usb/ns-usb-_urb) structure to return a USB-specific status code.

> [!NOTE]
> KMDF and UMDF driver developers should use the respective framework interfaces for communicating with a USB device. For more information, see [Working with USB Devices](../wdf/working-with-usb-devices.md) for KMDF drivers and [Working with USB Interfaces in UMDF](../wdf/working-with-usb-interfaces-in-umdf-1-x-drivers.md). These topics discuss the underlying WDM driver interfaces used for USB device communication.

## In this section

| Topic | Description |
|---|---|
| [Allocating and Building URBs](how-to-add-xrb-support-for-client-drivers.md) | This topic describes how a USB client driver can use Windows Driver Model (WDM) driver routines to allocate and format an URB before sending the request to the Microsoft-provided USB driver stack. |
| [How to Submit an URB](send-requests-to-the-usb-driver-stack.md) | This topic describes the steps that are required to submit an initialized URB to the USB driver stack to process a particular request. |
| [Best Practices: Using URBs](usb-client-driver-contract-in-windows-8.md) | This topic describes best practices for a client driver for allocating, building, and sending an URB to the USB driver stack included with Windows 8. |

## Related topics

- [USB Driver Development Guide](usb-driver-development-guide.md)
