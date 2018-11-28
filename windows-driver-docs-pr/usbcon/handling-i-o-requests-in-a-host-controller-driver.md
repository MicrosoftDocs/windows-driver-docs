---
Description: Best practices for a host controller driver for handling I/O requests sent by UCX.
title: Handle I/O requests in a USB host controller driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handle I/O requests in a USB host controller driver


Best practices for a host controller driver for handling I/O requests sent by UCX.

UCX keeps track of all the endpoints that have been created by the host controller driver for devices on the USB bus. Any data transfer requests sent by the hub driver, or by another driver that is higher up in the USB device stack, is first handled by UCX. UCX is responsible for forwarding the framework request object to the correct endpoint queue. The USB Request Block (URB) contained in the request may specify an endpoint handle. If an endpoint handle is specified, UCX checks for the corresponding endpoint among the endpoints present for the device. If the specified endpoint handle is present, the request is forwarded to the endpoint’s queue. If the specified endpoint handle is not found, the request is failed. If no handle is specified, then the request is for the default endpoint, and UCX forwards the request to the host controller driver’s default endpoint queue for that device.

To ensure compatibility with existing USB drivers, the host controller must comply with the following requirements when completing URB request:

-  [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) must be called at DISPATCH\_LEVEL.
-   If the URB was delivered to its framework queue and the driver began processing it synchronously on the calling driver’s thread or DPC, the request should not also be completed synchronously. The request must be completed on a separate DPC, which can be scheduled with a call to [**WdfDpcEnqueue**](https://msdn.microsoft.com/library/windows/hardware/ff547148).
-   Similar to the preceding requirement, upon receiving [**EVT_WDF_IO_QUEUE_IO_CANCELED_ON_QUEUE**](https://msdn.microsoft.com/library/windows/hardware/ff541756) or [**EVT_WDF_REQUEST_CANCEL**](https://msdn.microsoft.com/library/windows/hardware/ff541817), the host controller driver must complete the URB request on a separate DPC from the calling thread or DPC. By default, WDF completes canceled requests on the queue synchronously. That behavior might cause issues for URB requests. For this reason, the driver must provide an *EvtIoCanceledOnQueue* callback for its URB queues.

The framework request object for an [**IOCTL\_INTERNAL\_USB\_SUBMIT\_URB**](https://msdn.microsoft.com/library/windows/hardware/ff537271) contains an URB located at **Parameters.Others.Arg1** of the request. When the request is completed, the URB status must be set to either USBD\_STATUS\_SUCCESS, or to a failure status that indicates the nature of the failure. The failure status values are defined in the usb.h header file.

## Related topics
[Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)  



