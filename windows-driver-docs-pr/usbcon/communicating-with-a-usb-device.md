---
Description: This section describes a USB Request Block (URB) and provides information about how a USB client driver can use Windows Driver Model (WDM) routines to allocate, build, and submit URBs to the USB driver stack.
MS-HAID:
- 'usbvendor\_a54373f7-864d-460e-a193-8e9d7ad9dd08.xml'
- 'buses.communicating\_with\_a\_usb\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB Request Blocks (URBs)
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
<td><p>[Allocating and Building URBs](how-to-add-xrb-support-for-client-drivers.md)</p></td>
<td><p>This topic describes how a USB client driver can use Windows Driver Model (WDM) driver routines to allocate and format an URB before sending the request to the Microsoft-provided USB driver stack.</p></td>
</tr>
<tr class="even">
<td><p>[How to Submit an URB](send-requests-to-the-usb-driver-stack.md)</p></td>
<td><p>This topic describes the steps that are required to submit an initialized URB to the USB driver stack to process a particular request.</p></td>
</tr>
<tr class="odd">
<td><p>[Best Practices: Using URBs](usb-client-driver-contract-in-windows-8.md)</p></td>
<td><p>This topic describes best practices for a client driver for allocating, building, and sending an URB to the USB driver stack included with Windows 8.</p></td>
</tr>
</tbody>
</table>

 

## Related topics


[USB Driver Development Guide](usb-driver-development-guide.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20Request%20Blocks%20%28URBs%29%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




