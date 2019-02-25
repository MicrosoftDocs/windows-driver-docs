---
Description: UCX extends the WDF object functionality to define its own USB-specific UCX objects. UCX uses these objects for queuing requests to any underlying host controller driver.
title: UCX objects and handles used by a host controller driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UCX objects and handles used by a host controller driver


**Summary**

-   UCX objects are used by the host controller driver to handle operations related to the controller, its root hub, and all endpoints.
-   UCX objects are created by the host controller driver and each object's lifetime is managed by UCX.

**Applies to**

-   Windows 10

**Last updated**

-   July 2015

**Important APIs**

-   [**UcxControllerCreate**](https://msdn.microsoft.com/library/windows/hardware/mt188033)
-   [**UcxRootHubCreate**](https://msdn.microsoft.com/library/windows/hardware/mt188048)
-   [**UcxUsbDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/mt188052)

UCX extends the WDF object functionality to define its own USB-specific UCX objects. UCX uses these objects for queuing requests to any underlying host controller driver.

For more details on WDF objects, see [Introduction to Framework Objects](https://msdn.microsoft.com/library/windows/hardware/ff544249).

## Host controller object


**UCXCONTROLLER**

Represents the host controller that is created by the host controller driver. The driver must create only one host controller object per host controller instance. Typically created within the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback by calling the [**UcxControllerCreate**](https://msdn.microsoft.com/library/windows/hardware/mt188033) method.

When the host controller driver creates the object, the driver registers its implementation of callback functions that are invoked by UCX. The driver should additionally identify the bus type over which the host controller is connected, such as ACPI or PCI. The driver also provides host controller device information by using the [**UCX\_CONTROLLER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/mt188057) structure that is passed to the [**UcxControllerCreate**](https://msdn.microsoft.com/library/windows/hardware/mt188033) call.

To handle I/O requests, the host controller driver must register a GUID\_DEVINTERFACE\_USB\_HOST\_CONTROLLER device interface. The driver is not required to implement the IOCTLs defined in this interface. Instead, the UCX client passes the IOCTL requests received on this interface to UCX by calling [**UcxIoDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/mt188047).

Here are the callback functions associated with the host controller object, which are invoked by UCX. These functions must be implemented by the host controller driver.

[*EVT\_UCX\_CONTROLLER\_USBDEVICE\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187823)  
Called when the hub driver has determined, via interaction with the root hub and/or external hub(s), that a new device is present on the bus.

[*EVT\_UCX\_CONTROLLER\_QUERY\_USB\_CAPABILITY*](https://msdn.microsoft.com/library/windows/hardware/mt187821)  
Called by UCX to gather information about various features supported by USB host controllers.

[*EVT\_UCX\_CONTROLLER\_RESET*](https://msdn.microsoft.com/library/windows/hardware/mt187822)  
Called by UCX to reset the controller hardware, possibly in response to a detected error.

[*EVT\_UCX\_CONTROLLER\_GET\_CURRENT\_FRAMENUMBER*](https://msdn.microsoft.com/library/windows/hardware/mt187820)  
Used to retrieve the current frame number from the host controller, which is used by the hub driver for scheduling isochronous transfers.

## Root hub object


**UCXROOTHUB**

Gets and controls the status of the root ports of the host controller. Created by the host controller driver typically within the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback by calling the [**UcxRootHubCreate**](https://msdn.microsoft.com/library/windows/hardware/mt188048) method after the host controller object is created. There should be only one root hub object per host controller instance. In the **UcxRootHubCreate** call, the driver registers its callback implementations.

[*EVT\_UCX\_ROOTHUB\_GET\_INFO*](https://msdn.microsoft.com/library/windows/hardware/mt187836)  
Returns the number of USB 2.0 and USB 3.0 ports of the root hub.

[*EVT\_UCX\_ROOTHUB\_GET\_20PORT\_INFO*](https://msdn.microsoft.com/library/windows/hardware/mt187834)  
Return information about the USB 2.0 or USB 3.0 ports ([*EVT\_UCX\_ROOTHUB\_GET\_30PORT\_INFO*](https://msdn.microsoft.com/library/windows/hardware/mt187835)) of the root hub.

After the root hub object is created and initialized, the hub driver interacts with the root hub ports by sending interrupt and control transfers. UCX assists with these transfers by invoking these callback functions implemented by the host controller driver.

[*EVT\_UCX\_ROOTHUB\_CONTROL\_URB*](https://msdn.microsoft.com/library/windows/hardware/mt187833)  
Handles feature control requests by the USB hub.

[*EVT\_UCX\_ROOTHUB\_INTERRUPT\_TX*](https://msdn.microsoft.com/library/windows/hardware/mt187837)  
Handles request for information about changed ports.

For more information, see [Root hub callback functions of a host controller driver](manage-the-root-hub-in-a-host-controller-driver.md).

## USB device object


**UCXUSBDEVICE**

Represents a physical USB device connected to the bus. Created by the host controller driver typically within the [*EVT\_UCX\_CONTROLLER\_USBDEVICE\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187823) callback by calling the [**UcxUsbDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/mt188052) method.

When the object is created, the host controller driver registers its implementation of the callback functions with the [**UcxUsbDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/mt188052) call.

These callback functions are meant to keep the controller and driver informed about the current status of USB devices.

[*EVT\_UCX\_USBDEVICE\_ENABLE*](https://msdn.microsoft.com/library/windows/hardware/mt187841)  
Prepares the controller for performing transfers to the device’s default endpoint.

[*EVT\_UCX\_USBDEVICE\_DISABLE*](https://msdn.microsoft.com/library/windows/hardware/mt187840)  
Releases controller resources associated with the device and its default endpoint.

[*EVT\_UCX\_USBDEVICE\_ADDRESS*](https://msdn.microsoft.com/library/windows/hardware/mt187838)  
Programs an address into the controller and sends a SET\_ADDRESS transfer to the device, to bring it to the addressed state.

[*EVT\_UCX\_USBDEVICE\_ENDPOINTS\_CONFIGURE*](https://msdn.microsoft.com/library/windows/hardware/mt187842)  
Programs non-default endpoints into the controller, and/or releases other non-default endpoints.

[*EVT\_UCX\_USBDEVICE\_RESET*](https://msdn.microsoft.com/library/windows/hardware/mt187845)  
A controller notification that a device has been reset, in which case the driver takes any necessary action to sync the controller with the USB device.

[*EVT\_UCX\_USBDEVICE\_UPDATE*](https://msdn.microsoft.com/library/windows/hardware/mt187846)  
Notifies the controller of various bits of information related to the device.

[*EVT\_UCX\_USBDEVICE\_HUB\_INFO*](https://msdn.microsoft.com/library/windows/hardware/mt187844)  
A notification about hub properties, if the UCXUSBDEVICE handle is for a hub device.

[*EVT\_UCX\_USBDEVICE\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187843)  
Notifies the driver to create an endpoint for the device. [*EVT\_UCX\_USBDEVICE\_DEFAULT\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187839) for default endpoint.

When an interface on a suspended USB 3.0 device has signaled wake up, the driver is expected to call [**UcxUsbDeviceRemoteWakeNotification**](https://msdn.microsoft.com/library/windows/hardware/mt188054) to notify UCX.

After the object is created, the lifetime of the object is managed by UCX, and the driver must not delete the object.

## Endpoint object


**UCXENDPOINT**

Represents an endpoint on a USB device object. Endpoint objects are created by the host controller during either an [*EVT\_UCX\_USBDEVICE\_DEFAULT\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187839) or an [*EVT\_UCX\_USBDEVICE\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187843) callback. When a endpoint object is created, the driver registers its callback functions.

The driver also creates a framework queue object for each endpoint, and passes the WDFQUEUE for that queue to UCX by calling [**UcxEndpointSetWdfIoQueue**](https://msdn.microsoft.com/library/windows/hardware/mt188045). After the endpoint is created, the lifetime of the object and its associated queues is managed by UCX, and the driver must not delete these objects itself.

The endpoint object implements several callback functions that allow the driver to assist UCX with operations related to the endpoint.

[*EVT\_UCX\_ENDPOINT\_ABORT*](https://msdn.microsoft.com/library/windows/hardware/mt187825)  
Abort the queue associated with the endpoint.

[*EVT\_UCX\_ENDPOINT\_OK\_TO\_CANCEL\_TRANSFERS*](https://msdn.microsoft.com/library/windows/hardware/mt187826)  
Notify the controller driver that it can complete cancelled transfers on the endpoint.

[*EVT\_UCX\_ENDPOINT\_PURGE*](https://msdn.microsoft.com/library/windows/hardware/mt187827)  
Complete all outstanding I/O requests on the endpoint.

[*EVT\_UCX\_ENDPOINT\_START*](https://msdn.microsoft.com/library/windows/hardware/mt187829)  
Start the queue associated with the endpoint.

[*EVT\_UCX\_ENDPOINT\_STATIC\_STREAMS\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187830)  
Create static streams.

[*EVT\_UCX\_ENDPOINT\_RESET*](https://msdn.microsoft.com/library/windows/hardware/mt187828)  
Notify the driver to reset the controller’s programming of the endpoint.

When the host controller driver receives a USB 3.0 No Ping Response Error on an endpoint, the driver must call [**UcxEndpointNoPingResponseError**](https://msdn.microsoft.com/library/windows/hardware/mt188043). That call results in the USB device object receiving [*EVT\_UCX\_USBDEVICE\_UPDATE*](https://msdn.microsoft.com/library/windows/hardware/mt187846).
For more information, see [Configuring USB endpoints in a host controller driver](configuring-usb-endpoints-in-a-host-controller-driver.md).

## Stream object


**UCXSTREAMS**

Represents a number of pipes to the device across a single endpoint. The host controller driver creates stream objects in the [*EVT\_UCX\_ENDPOINT\_STATIC\_STREAMS\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187830) callback by calling [**UcxStaticStreamsCreate**](https://msdn.microsoft.com/library/windows/hardware/mt188050).

During the [**UcxStaticStreamsCreate**](https://msdn.microsoft.com/library/windows/hardware/mt188050) call, the host controller driver registers its callback functions. For a specific endpoint object, the driver can determine whether it has created a streams object, and return the UCXSTREAMS handle by calling [**UcxEndpointGetStaticStreamsReferenced**](https://msdn.microsoft.com/library/windows/hardware/mt188040).

After the object is created, the driver creates a framework queue object for each stream and sends the WDFQUEUE handle to UCX by calling [**UcxStaticStreamsSetStreamInfo**](https://msdn.microsoft.com/library/windows/hardware/mt188051).

The stream object provides several callback functions for the host controller to assist UCX with managing the static streams.

[*EVT\_UCX\_ENDPOINT\_STATIC\_STREAMS\_DISABLE*](https://msdn.microsoft.com/library/windows/hardware/mt187831)  
Release controller resources for all streams for an endpoint.

[*EVT\_UCX\_ENDPOINT\_STATIC\_STREAMS\_ENABLE*](https://msdn.microsoft.com/library/windows/hardware/mt187832)  
Enable controller hardware of all streams for this endpoint.

The lifetime of the object and associated queues are managed by UCX, and the driver must not delete the objects.

## Related topics
[Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)  



