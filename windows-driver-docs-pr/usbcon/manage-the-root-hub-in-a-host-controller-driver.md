---
Description: 'UCX performs root hub management. It simulates and manages virtual control and interrupt endpoints. UCX creates those virtual endpoints when the host controller driver creates the root hub object.'
MS-HAID: 'buses.manage\_the\_root\_hub\_in\_a\_host\_controller\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Root hub callback functions of a USB host controller driver
author: windows-driver-content
---

# Root hub callback functions of a USB host controller driver


UCX performs root hub management. It simulates and manages virtual control and interrupt endpoints. UCX creates those virtual endpoints when the host controller driver creates the root hub object.

The USB hub driver interacts with the root hub in the same way that it interacts with a regular hub device. However, the host controller driver doesn’t have to handle requests sent to the root hub for the control and interrupt endpoints directly. UCX handles those requests. UCX invokes callback functions implemented by the host controller driver so that it can return relevant information about the current state of the host controller’s ports. When these callback functions are completed, the underlying UCX requests are completed and returned to the hub driver.

On receiving an interrupt transfer for the root hub, UCX sets the request as pending. When a change is detected on one of the root hub ports, the host controller driver calls [**UcxRootHubPortChanged**](https://msdn.microsoft.com/library/windows/hardware/mt188049). UCX then invokes the driver’s [*EVT\_UCX\_ROOTHUB\_INTERRUPT\_TX*](https://msdn.microsoft.com/library/windows/hardware/mt187837) callback, and the driver indicates that the port that was changed. At this time, UCX completes the pending request back to the hub driver. The hub driver sends a control transfer to the root hub, to get the port status of the port that signaled a change. UCX sets that control transfer request to pending, and invokes the driver’s [*EVT\_UCX\_ROOTHUB\_CONTROL\_URB*](https://msdn.microsoft.com/library/windows/hardware/mt187833) callback function. In the implementation returns the current status of the root hub port, including the indication that a device is connected. UCX completes the control transfer request to the hub driver, and device enumeration continues.

## Related topics
[Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Root%20hub%20callback%20functions%20of%20a%20USB%20host%20controller%20driver%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


