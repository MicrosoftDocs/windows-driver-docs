---
Description: UCX performs root hub management. 
title: Root hub callback functions of a USB host controller driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Root hub callback functions of a USB host controller driver


UCX performs root hub management. It simulates and manages virtual control and interrupt endpoints. UCX creates those virtual endpoints when the host controller driver creates the root hub object.

The USB hub driver interacts with the root hub in the same way that it interacts with a regular hub device. However, the host controller driver doesn’t have to handle requests sent to the root hub for the control and interrupt endpoints directly. UCX handles those requests. UCX invokes callback functions implemented by the host controller driver so that it can return relevant information about the current state of the host controller’s ports. When these callback functions are completed, the underlying UCX requests are completed and returned to the hub driver.

On receiving an interrupt transfer for the root hub, UCX sets the request as pending. When a change is detected on one of the root hub ports, the host controller driver calls [**UcxRootHubPortChanged**](https://msdn.microsoft.com/library/windows/hardware/mt188049). UCX then invokes the driver’s [*EVT\_UCX\_ROOTHUB\_INTERRUPT\_TX*](https://msdn.microsoft.com/library/windows/hardware/mt187837) callback, and the driver indicates that the port that was changed. At this time, UCX completes the pending request back to the hub driver. The hub driver sends a control transfer to the root hub, to get the port status of the port that signaled a change. UCX sets that control transfer request to pending, and invokes the driver’s [*EVT\_UCX\_ROOTHUB\_CONTROL\_URB*](https://msdn.microsoft.com/library/windows/hardware/mt187833) callback function. In the implementation returns the current status of the root hub port, including the indication that a device is connected. UCX completes the control transfer request to the hub driver, and device enumeration continues.

## Related topics
[Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)  



