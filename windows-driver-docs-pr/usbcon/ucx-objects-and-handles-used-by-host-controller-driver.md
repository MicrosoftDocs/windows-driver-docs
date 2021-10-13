---
description: UCX extends the WDF object functionality to define its own USB-specific UCX objects. UCX uses these objects for queuing requests to any underlying host controller driver.
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

-   [**UcxControllerCreate**](/previous-versions/windows/hardware/drivers/mt188033(v=vs.85))
-   [**UcxRootHubCreate**](/previous-versions/windows/hardware/drivers/mt188048(v=vs.85))
-   [**UcxUsbDeviceCreate**](/windows-hardware/drivers/ddi/ucxusbdevice/nf-ucxusbdevice-ucxusbdevicecreate)

UCX extends the WDF object functionality to define its own USB-specific UCX objects. UCX uses these objects for queuing requests to any underlying host controller driver.

For more details on WDF objects, see [Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md).

## Host controller object


**UCXCONTROLLER**

Represents the host controller that is created by the host controller driver. The driver must create only one host controller object per host controller instance. Typically created within the [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback by calling the [**UcxControllerCreate**](/previous-versions/windows/hardware/drivers/mt188033(v=vs.85)) method.

When the host controller driver creates the object, the driver registers its implementation of callback functions that are invoked by UCX. The driver should additionally identify the bus type over which the host controller is connected, such as ACPI or PCI. The driver also provides host controller device information by using the [**UCX\_CONTROLLER\_CONFIG**](/windows-hardware/drivers/ddi/ucxcontroller/ns-ucxcontroller-_ucx_controller_config) structure that is passed to the [**UcxControllerCreate**](/previous-versions/windows/hardware/drivers/mt188033(v=vs.85)) call.

To handle I/O requests, the host controller driver must register a GUID\_DEVINTERFACE\_USB\_HOST\_CONTROLLER device interface. The driver is not required to implement the IOCTLs defined in this interface. Instead, the UCX client passes the IOCTL requests received on this interface to UCX by calling [**UcxIoDeviceControl**](/windows-hardware/drivers/ddi/ucxcontroller/nf-ucxcontroller-ucxiodevicecontrol).

Here are the callback functions associated with the host controller object, which are invoked by UCX. These functions must be implemented by the host controller driver.

[*EVT\_UCX\_CONTROLLER\_USBDEVICE\_ADD*](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_usbdevice_add)  
Called when the hub driver has determined, via interaction with the root hub and/or external hub(s), that a new device is present on the bus.

[*EVT\_UCX\_CONTROLLER\_QUERY\_USB\_CAPABILITY*](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_query_usb_capability)  
Called by UCX to gather information about various features supported by USB host controllers.

[*EVT\_UCX\_CONTROLLER\_RESET*](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_reset)  
Called by UCX to reset the controller hardware, possibly in response to a detected error.

[*EVT\_UCX\_CONTROLLER\_GET\_CURRENT\_FRAMENUMBER*](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_get_current_framenumber)  
Used to retrieve the current frame number from the host controller, which is used by the hub driver for scheduling isochronous transfers.

## Root hub object


**UCXROOTHUB**

Gets and controls the status of the root ports of the host controller. Created by the host controller driver typically within the [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback by calling the [**UcxRootHubCreate**](/previous-versions/windows/hardware/drivers/mt188048(v=vs.85)) method after the host controller object is created. There should be only one root hub object per host controller instance. In the **UcxRootHubCreate** call, the driver registers its callback implementations.

[*EVT\_UCX\_ROOTHUB\_GET\_INFO*](/windows-hardware/drivers/ddi/ucxroothub/nc-ucxroothub-evt_ucx_roothub_get_info)  
Returns the number of USB 2.0 and USB 3.0 ports of the root hub.

[*EVT\_UCX\_ROOTHUB\_GET\_20PORT\_INFO*](/windows-hardware/drivers/ddi/ucxroothub/nc-ucxroothub-evt_ucx_roothub_get_20port_info)  
Return information about the USB 2.0 or USB 3.0 ports ([*EVT\_UCX\_ROOTHUB\_GET\_30PORT\_INFO*](/windows-hardware/drivers/ddi/ucxroothub/nc-ucxroothub-evt_ucx_roothub_get_30port_info)) of the root hub.

After the root hub object is created and initialized, the hub driver interacts with the root hub ports by sending interrupt and control transfers. UCX assists with these transfers by invoking these callback functions implemented by the host controller driver.

[*EVT\_UCX\_ROOTHUB\_CONTROL\_URB*](/windows-hardware/drivers/ddi/ucxroothub/nc-ucxroothub-evt_ucx_roothub_control_urb)  
Handles feature control requests by the USB hub.

[*EVT\_UCX\_ROOTHUB\_INTERRUPT\_TX*](/windows-hardware/drivers/ddi/ucxroothub/nc-ucxroothub-evt_ucx_roothub_interrupt_tx)  
Handles request for information about changed ports.

For more information, see [Root hub callback functions of a host controller driver](manage-the-root-hub-in-a-host-controller-driver.md).

## USB device object


**UCXUSBDEVICE**

Represents a physical USB device connected to the bus. Created by the host controller driver typically within the [*EVT\_UCX\_CONTROLLER\_USBDEVICE\_ADD*](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_usbdevice_add) callback by calling the [**UcxUsbDeviceCreate**](/windows-hardware/drivers/ddi/ucxusbdevice/nf-ucxusbdevice-ucxusbdevicecreate) method.

When the object is created, the host controller driver registers its implementation of the callback functions with the [**UcxUsbDeviceCreate**](/windows-hardware/drivers/ddi/ucxusbdevice/nf-ucxusbdevice-ucxusbdevicecreate) call.

These callback functions are meant to keep the controller and driver informed about the current status of USB devices.

[*EVT\_UCX\_USBDEVICE\_ENABLE*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_enable)  
Prepares the controller for performing transfers to the device’s default endpoint.

[*EVT\_UCX\_USBDEVICE\_DISABLE*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_disable)  
Releases controller resources associated with the device and its default endpoint.

[*EVT\_UCX\_USBDEVICE\_ADDRESS*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_address)  
Programs an address into the controller and sends a SET\_ADDRESS transfer to the device, to bring it to the addressed state.

[*EVT\_UCX\_USBDEVICE\_ENDPOINTS\_CONFIGURE*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_endpoints_configure)  
Programs non-default endpoints into the controller, and/or releases other non-default endpoints.

[*EVT\_UCX\_USBDEVICE\_RESET*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_reset)  
A controller notification that a device has been reset, in which case the driver takes any necessary action to sync the controller with the USB device.

[*EVT\_UCX\_USBDEVICE\_UPDATE*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_update)  
Notifies the controller of various bits of information related to the device.

[*EVT\_UCX\_USBDEVICE\_HUB\_INFO*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_hub_info)  
A notification about hub properties, if the UCXUSBDEVICE handle is for a hub device.

[*EVT\_UCX\_USBDEVICE\_ENDPOINT\_ADD*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_endpoint_add)  
Notifies the driver to create an endpoint for the device. [*EVT\_UCX\_USBDEVICE\_DEFAULT\_ENDPOINT\_ADD*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_default_endpoint_add) for default endpoint.

When an interface on a suspended USB 3.0 device has signaled wake up, the driver is expected to call [**UcxUsbDeviceRemoteWakeNotification**](/windows-hardware/drivers/ddi/ucxusbdevice/nf-ucxusbdevice-ucxusbdeviceremotewakenotification) to notify UCX.

After the object is created, the lifetime of the object is managed by UCX, and the driver must not delete the object.

## Endpoint object


**UCXENDPOINT**

Represents an endpoint on a USB device object. Endpoint objects are created by the host controller during either an [*EVT\_UCX\_USBDEVICE\_DEFAULT\_ENDPOINT\_ADD*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_default_endpoint_add) or an [*EVT\_UCX\_USBDEVICE\_ENDPOINT\_ADD*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_endpoint_add) callback. When a endpoint object is created, the driver registers its callback functions.

The driver also creates a framework queue object for each endpoint, and passes the WDFQUEUE for that queue to UCX by calling [**UcxEndpointSetWdfIoQueue**](/windows-hardware/drivers/ddi/ucxendpoint/nf-ucxendpoint-ucxendpointsetwdfioqueue). After the endpoint is created, the lifetime of the object and its associated queues is managed by UCX, and the driver must not delete these objects itself.

The endpoint object implements several callback functions that allow the driver to assist UCX with operations related to the endpoint.

[*EVT\_UCX\_ENDPOINT\_ABORT*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_abort)  
Abort the queue associated with the endpoint.

[*EVT\_UCX\_ENDPOINT\_OK\_TO\_CANCEL\_TRANSFERS*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_ok_to_cancel_transfers)  
Notify the controller driver that it can complete cancelled transfers on the endpoint.

[*EVT\_UCX\_ENDPOINT\_PURGE*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_purge)  
Complete all outstanding I/O requests on the endpoint.

[*EVT\_UCX\_ENDPOINT\_START*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_start)  
Start the queue associated with the endpoint.

[*EVT\_UCX\_ENDPOINT\_STATIC\_STREAMS\_ADD*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_static_streams_add)  
Create static streams.

[*EVT\_UCX\_ENDPOINT\_RESET*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_reset)  
Notify the driver to reset the controller’s programming of the endpoint.

When the host controller driver receives a USB 3.0 No Ping Response Error on an endpoint, the driver must call [**UcxEndpointNoPingResponseError**](/windows-hardware/drivers/ddi/ucxendpoint/nf-ucxendpoint-ucxendpointnopingresponseerror). That call results in the USB device object receiving [*EVT\_UCX\_USBDEVICE\_UPDATE*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_update).
For more information, see [Configuring USB endpoints in a host controller driver](configuring-usb-endpoints-in-a-host-controller-driver.md).

## Stream object


**UCXSTREAMS**

Represents a number of pipes to the device across a single endpoint. The host controller driver creates stream objects in the [*EVT\_UCX\_ENDPOINT\_STATIC\_STREAMS\_ADD*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_static_streams_add) callback by calling [**UcxStaticStreamsCreate**](/windows-hardware/drivers/ddi/ucxsstreams/nf-ucxsstreams-ucxstaticstreamscreate).

During the [**UcxStaticStreamsCreate**](/windows-hardware/drivers/ddi/ucxsstreams/nf-ucxsstreams-ucxstaticstreamscreate) call, the host controller driver registers its callback functions. For a specific endpoint object, the driver can determine whether it has created a streams object, and return the UCXSTREAMS handle by calling [**UcxEndpointGetStaticStreamsReferenced**](/windows-hardware/drivers/ddi/ucxendpoint/nf-ucxendpoint-ucxendpointgetstaticstreamsreferenced).

After the object is created, the driver creates a framework queue object for each stream and sends the WDFQUEUE handle to UCX by calling [**UcxStaticStreamsSetStreamInfo**](/windows-hardware/drivers/ddi/ucxsstreams/nf-ucxsstreams-ucxstaticstreamssetstreaminfo).

The stream object provides several callback functions for the host controller to assist UCX with managing the static streams.

[*EVT\_UCX\_ENDPOINT\_STATIC\_STREAMS\_DISABLE*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_static_streams_disable)  
Release controller resources for all streams for an endpoint.

[*EVT\_UCX\_ENDPOINT\_STATIC\_STREAMS\_ENABLE*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_static_streams_enable)  
Enable controller hardware of all streams for this endpoint.

The lifetime of the object and associated queues are managed by UCX, and the driver must not delete the objects.

## Related topics
[Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)