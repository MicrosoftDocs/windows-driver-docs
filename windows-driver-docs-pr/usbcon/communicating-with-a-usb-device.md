---
Description: Information about how a USB client driver can allocate, build, and submit URBs to the USB driver stack.
title: USB Request Blocks (URBs)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Request Blocks (URBs)


This section describes a USB Request Block (URB) and provides information about how a USB client driver can use Windows Driver Model (WDM) routines to allocate, build, and submit URBs to the USB driver stack.

A Universal Serial Bus (USB) client driver cannot communicate with its device directly. Instead, the client driver creates requests and submits them to the USB driver stack for processing. Within each request, the client driver provides a variable-length data structure called a *USB Request Block (URB)*. The [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) structure describes the details of the request and also contains information about the status of the completed request. The client driver performs all device-specific operations, including data transfers, through URBs. The client driver must initialize the URB with information about the request before submitting it to the USB driver stack. For certain types of requests, Microsoft provides helper routines and macros that allocate an **URB** structure and fill the necessary members of the **URB** structure with details provided by the client driver.

Each URB begins with a standard fixed-sized header ([**\_URB\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff540409)) whose purpose is to identify the type of operation requested. The **Length** member of **\_URB\_HEADER** specifies the size, in bytes, of the URB. The **Function** member, which must be one of a series of system-defined URB\_FUNCTION\_XXX constants, determines the type of operation that is requested. In the case of data transfers, for instance, this member indicates the type of transfer. Function codes URB\_FUNCTION\_CONTROL\_TRANSFER, URB\_FUNCTION\_BULK\_OR\_INTERRUPT\_TRANSFER, and URB\_FUNCTION\_ISOCH\_TRANSFER indicate control, bulk/interrupt, and isochronous transfers respectively. The USB driver stack uses the **Status** member to return a USB-specific status code.

To submit an URB, the client driver uses the [**IOCTL\_INTERNAL\_USB\_SUBMIT\_URB**](https://msdn.microsoft.com/library/windows/hardware/ff537271) request, which is delivered to the device by means of an I/O request packet (IRP) of type [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766).

After the USB driver stack is done processing the URB, the driver stack uses the **Status** member of the [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) structure to return a USB-specific status code.

**Note**  KMDF and UMDF driver developers should use the respective framework interfaces for communicating with a USB device. For more information, see [Working with USB Devices](https://msdn.microsoft.com/library/windows/hardware/ff553101) for KMDF drivers and [Working with USB Interfaces in UMDF](https://msdn.microsoft.com/library/windows/hardware/ff561478). These topics discuss the underlying WDM driver interfaces used for USB device communication.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="how-to-add-xrb-support-for-client-drivers.md" data-raw-source="[Allocating and Building URBs](how-to-add-xrb-support-for-client-drivers.md)">Allocating and Building URBs</a></p></td>
<td><p>This topic describes how a USB client driver can use Windows Driver Model (WDM) driver routines to allocate and format an URB before sending the request to the Microsoft-provided USB driver stack.</p></td>
</tr>
<tr class="even">
<td><p><a href="send-requests-to-the-usb-driver-stack.md" data-raw-source="[How to Submit an URB](send-requests-to-the-usb-driver-stack.md)">How to Submit an URB</a></p></td>
<td><p>This topic describes the steps that are required to submit an initialized URB to the USB driver stack to process a particular request.</p></td>
</tr>
<tr class="odd">
<td><p><a href="usb-client-driver-contract-in-windows-8.md" data-raw-source="[Best Practices: Using URBs](usb-client-driver-contract-in-windows-8.md)">Best Practices: Using URBs</a></p></td>
<td><p>This topic describes best practices for a client driver for allocating, building, and sending an URB to the USB driver stack included with Windows 8.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[USB Driver Development Guide](usb-driver-development-guide.md)  



