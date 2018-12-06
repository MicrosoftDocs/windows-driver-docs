---
Description: In this topic, you will learn about the chained MDLs capability in the USB driver stack, and how a client driver can send a transfer buffer as a chain of MDL structure.
title: How to send chained MDLs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to send chained MDLs


In this topic, you will learn about the chained MDLs capability in the USB driver stack, and how a client driver can send a transfer buffer as a chain of [**MDL**](https://msdn.microsoft.com/library/windows/hardware/ff554414) structure.

Most USB host controllers require the transfer buffer to be virtually contiguous. Virtually contiguous means that the buffer can start and end anywhere in a page but the rest of the buffer must start and end on a page boundary. Many USB client drivers are able to meet that requirement. However, for certain client drivers, particularly those that need to add or remove additional data to or from the buffer, allocating virtually contiguous memory for the transfer buffer is not preferable.

For example, consider a networking stack of three drivers, a network protocol driver, an intermediate driver, and a miniport driver. The protocol driver initiates a transfer and sends a packet to the next driver in the stack: the intermediate driver. The intermediate driver wants to add a custom header (contained in a separate block of memory) to the packet. The intermediate driver sends that header and the received packet, to the next driver in the stack: the miniport driver. The miniport driver interfaces with the USB driver stack and therefore must prepare a virtually contiguous transfer buffer. To create such a buffer, the miniport driver allocates a large buffer, adds the custom header, and then copies the payload. Because payload is typically large, copying the entire payload can have a significant impact on performance.

The client driver can overcome that performance impact by sending the transfer buffer as a chain of *memory descriptor list* (MDLs). The new USB driver stack in Windows 8, is capable of accepting a chained MDL (see [**MDL**](https://msdn.microsoft.com/library/windows/hardware/ff554414)) from the client driver. By supplying a chained MDL, the client driver can reference discontiguous pages in memory instead of performing extraneous copy operations. The capability removes restrictions on the number, size, and alignment of buffers, allowing the transfer buffer to be segmented in physical memory.

In order to use chained MDLs, the client driver must detect whether the underlying USB driver stack, loaded by Windows, supports the capability and then build a chain of MDLs in a proper order.

### Prerequisites

The chained MDL capability is only supported for bulk, isochronous, and interrupt transfers. Before you query for the chained MDL capability, make sure that your client driver has a USBD handle for the driver's registration with the USB driver stack. To create a USBD handle, call [**USBD\_CreateHandle**](https://msdn.microsoft.com/library/windows/hardware/hh406241).Typically, the client driver creates the USBD handle in its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine.

You can query for the chained MDL capability in the client driver's [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) handler or anytime later. The client driver must not query for this capability in its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine.

Instructions
------------

1.  Call the [**USBD\_QueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh406230) routine to determine whether the USB driver stack supports the chained MDLs capability. To query for that capability, specify UsbCapabilityChainedMdls as the GUID. Set the *OutputBuffer* parameter to NULL and *OutputBufferSize* parameter to 0.
2.  Check the NTSTATUS value returned by [**USBD\_QueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh406230) and evaluate the result. If the routine completes successfully, the chained MDLs capability is supported. Any other value indicates that the capability is not supported.
3.  Create the chain of MDLs. Each [**MDL**](https://msdn.microsoft.com/library/windows/hardware/ff554414) has a **Next** pointer that points to another **MDL**.

    The driver can build a chain MDL by manually setting the **Next** pointer.

    In the preceding example, the protocol driver sends the packet as an MDL. The intermediate driver can create another [**MDL**](https://msdn.microsoft.com/library/windows/hardware/ff554414) that references the block of memory with the header data. To create a chain, the intermediate driver can point the header MDL's **Next** pointer to the MDL received from the protocol driver. The intermediate driver can then forward the chain of two MDLs to the miniport driver, which supplies a reference to the chained MDL in the URB for the request and submits the request to the USB driver stack. For more information, see [Using MDLs](https://msdn.microsoft.com/library/windows/hardware/ff565421).

4.  While building an URB for an I/O request that uses chained MDLs, set the **TransferBufferMDL** member of the associated [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) structure (such as [**\_URB\_BULK\_OR\_INTERRUPT\_TRANSFER**](https://msdn.microsoft.com/library/windows/hardware/ff540352) or [**\_URB\_ISOCH\_TRANSFER**](https://msdn.microsoft.com/library/windows/hardware/ff540414)) to the first MDL in the chain, and set the **TransferBufferLength** to the total number of bytes to transfer. The data may span more than one MDL entry in the MDL chain.

    In Windows 8, two new types of URB functions have been added that enable a client driver to use chained MDLs for data transfers. If you want to use this capability, make sure that set the **Function** member of the URB header is set to one of following URB functions:

    -   URB\_FUNCTION\_BULK\_OR\_INTERRUPT\_TRANSFER\_USING\_CHAINED\_MDL
    -   URB\_FUNCTION\_ISOCH\_TRANSFER\_USING\_CHAINED\_MDL

    For information about those URB functions, see [**\_URB\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff540409).

Remarks
-------

For code example that queries the underlying USB driver stack to determine whether the driver stack can accept chained MDLs, see [**USBD\_QueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh406230).

## Related topics
[USB I/O Operations](usb-device-i-o.md)  



