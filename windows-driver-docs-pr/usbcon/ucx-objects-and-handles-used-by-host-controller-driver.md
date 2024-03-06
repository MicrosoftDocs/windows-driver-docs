---
title: UCX Objects and Handles Used by a Host Controller Driver
description: UCX extends the WDF object functionality to define its own USB-specific UCX objects. UCX uses these objects for queuing requests to any underlying host controller driver.
ms.date: 01/17/2024
---

# UCX objects and handles used by a host controller driver

UCX extends the WDF object functionality to define its own USB-specific UCX objects. UCX uses these objects for queuing requests to any underlying host controller driver.

## Summary

- UCX objects are used by the host controller driver to handle operations related to the controller, its root hub, and all endpoints.
- UCX objects are created by the host controller driver and each object's lifetime is managed by UCX.

## Important APIs

- **[UcxControllerCreate](/windows-hardware/drivers/ddi/ucxcontroller/nf-ucxcontroller-ucxcontrollercreate)**
- **[UcxRootHubCreate](/windows-hardware/drivers/ddi/ucxroothub/nf-ucxroothub-ucxroothubcreate)**
- **[UcxUsbDeviceCreate](/windows-hardware/drivers/ddi/ucxusbdevice/nf-ucxusbdevice-ucxusbdevicecreate)**

UCX extends the WDF object functionality to define its own USB-specific UCX objects. UCX uses these objects for queuing requests to any underlying host controller driver.

For more details on WDF objects, see [Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md).

## UCXCONTROLLER: Host controller object

Represents the host controller that is created by the host controller driver. The driver must create only one host controller object per host controller instance. Typically created within the *[EvtDriverDeviceAdd](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add)* callback by calling the **[UcxControllerCreate](/windows-hardware/drivers/ddi/ucxcontroller/nf-ucxcontroller-ucxcontrollercreate)** method.

When the host controller driver creates the object, the driver registers its implementation of callback functions that are invoked by UCX. The driver should additionally identify the bus type over which the host controller is connected, such as ACPI or PCI. The driver also provides host controller device information by using the **[UCX_CONTROLLER_CONFIG](/windows-hardware/drivers/ddi/ucxcontroller/ns-ucxcontroller-_ucx_controller_config)** structure that is passed to the **[UcxControllerCreate](/windows-hardware/drivers/ddi/ucxcontroller/nf-ucxcontroller-ucxcontrollercreate)** call.

To handle I/O requests, the host controller driver must register a GUID_DEVINTERFACE_USB_HOST_CONTROLLER device interface. The driver is not required to implement the IOCTLs defined in this interface. Instead, the UCX client passes the IOCTL requests received on this interface to UCX by calling **[UcxIoDeviceControl](/windows-hardware/drivers/ddi/ucxcontroller/nf-ucxcontroller-ucxiodevicecontrol)**.

Here are the callback functions associated with the host controller object, which are invoked by UCX. These functions must be implemented by the host controller driver.

*[EVT_UCX_CONTROLLER_USBDEVICE_ADD](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_usbdevice_add)</br>
Called when the hub driver has determined, via interaction with the root hub and/or external hub(s), that a new device is present on the bus.

*[EVT_UCX_CONTROLLER_QUERY_USB_CAPABILITY](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_query_usb_capability)</br>
Called by UCX to gather information about various features supported by USB host controllers.

*[EVT_UCX_CONTROLLER_RESET](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_reset)</br>
Called by UCX to reset the controller hardware, possibly in response to a detected error.

*[EVT_UCX_CONTROLLER_GET_CURRENT_FRAMENUMBER](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_get_current_framenumber)</br>
Used to retrieve the current frame number from the host controller, which is used by the hub driver for scheduling isochronous transfers.

## UCXROOTHUB: Root hub object

Gets and controls the status of the root ports of the host controller. Created by the host controller driver typically within the *[EvtDriverDeviceAdd](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add)* callback by calling the **[UcxRootHubCreate](/windows-hardware/drivers/ddi/ucxroothub/nf-ucxroothub-ucxroothubcreate)** method after the host controller object is created. There should be only one root hub object per host controller instance. In the **UcxRootHubCreate** call, the driver registers its callback implementations.

*[EVT_UCX_ROOTHUB_GET_INFO](/windows-hardware/drivers/ddi/ucxroothub/nc-ucxroothub-evt_ucx_roothub_get_info)*</br>
Returns the number of USB 2.0 and USB 3.0 ports of the root hub.

*[EVT_UCX_ROOTHUB_GET_20PORT_INFO](/windows-hardware/drivers/ddi/ucxroothub/nc-ucxroothub-evt_ucx_roothub_get_20port_info)*</br>
Return information about the USB 2.0 or USB 3.0 ports (*[EVT_UCX_ROOTHUB_GET_30PORT_INFO](/windows-hardware/drivers/ddi/ucxroothub/nc-ucxroothub-evt_ucx_roothub_get_30port_info)) of the root hub.

After the root hub object is created and initialized, the hub driver interacts with the root hub ports by sending interrupt and control transfers. UCX assists with these transfers by invoking these callback functions implemented by the host controller driver.

*[EVT_UCX_ROOTHUB_CONTROL_URB](/windows-hardware/drivers/ddi/ucxroothub/nc-ucxroothub-evt_ucx_roothub_control_urb)*</br>
Handles feature control requests by the USB hub.

*[EVT_UCX_ROOTHUB_INTERRUPT_TX](/windows-hardware/drivers/ddi/ucxroothub/nc-ucxroothub-evt_ucx_roothub_interrupt_tx)*</br>
Handles request for information about changed ports.

For more information, see [Root hub callback functions of a host controller driver](manage-the-root-hub-in-a-host-controller-driver.md).

## UCXUSBDEVICE: USB device object

Represents a physical USB device connected to the bus. Created by the host controller driver typically within the *[EVT_UCX_CONTROLLER_USBDEVICE_ADD](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_usbdevice_add)* callback by calling the **[UcxUsbDeviceCreate](/windows-hardware/drivers/ddi/ucxusbdevice/nf-ucxusbdevice-ucxusbdevicecreate)** method.

When the object is created, the host controller driver registers its implementation of the callback functions with the **[UcxUsbDeviceCreate](/windows-hardware/drivers/ddi/ucxusbdevice/nf-ucxusbdevice-ucxusbdevicecreate)** call.

These callback functions are meant to keep the controller and driver informed about the current status of USB devices.

*[EVT_UCX_USBDEVICE_ENABLE](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_enable)*</br>
Prepares the controller for performing transfers to the device's default endpoint.

*[EVT_UCX_USBDEVICE_DISABLE](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_disable)*</br>
Releases controller resources associated with the device and its default endpoint.

*[EVT_UCX_USBDEVICE_ADDRESS](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_address)*</br>
Programs an address into the controller and sends a SET_ADDRESS transfer to the device, to bring it to the addressed state.

*[EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_endpoints_configure)*</br>
Programs non-default endpoints into the controller, and/or releases other non-default endpoints.

*[EVT_UCX_USBDEVICE_RESET](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_reset)*</br>
A controller notification that a device has been reset, in which case the driver takes any necessary action to sync the controller with the USB device.

*[EVT_UCX_USBDEVICE_UPDATE](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_update)*</br>
Notifies the controller of various bits of information related to the device.

*[EVT_UCX_USBDEVICE_HUB_INFO](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_hub_info)*</br>
A notification about hub properties, if the UCXUSBDEVICE handle is for a hub device.

*[EVT_UCX_USBDEVICE_ENDPOINT_ADD](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_endpoint_add)*</br>
Notifies the driver to create an endpoint for the device. *[EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_default_endpoint_add)* for default endpoint.

When an interface on a suspended USB 3.0 device has signaled wake up, the driver is expected to call **[UcxUsbDeviceRemoteWakeNotification](/windows-hardware/drivers/ddi/ucxusbdevice/nf-ucxusbdevice-ucxusbdeviceremotewakenotification)** to notify UCX.

After the object is created, the lifetime of the object is managed by UCX, and the driver must not delete the object.

## UCXENDPOINT: Endpoint object

Represents an endpoint on a USB device object. Endpoint objects are created by the host controller during either an *[EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_default_endpoint_add)* or an *[EVT_UCX_USBDEVICE_ENDPOINT_ADD](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_endpoint_add)* callback. When a endpoint object is created, the driver registers its callback functions.

The driver also creates a framework queue object for each endpoint, and passes the WDFQUEUE for that queue to UCX by calling **[UcxEndpointSetWdfIoQueue](/windows-hardware/drivers/ddi/ucxendpoint/nf-ucxendpoint-ucxendpointsetwdfioqueue)**. After the endpoint is created, the lifetime of the object and its associated queues is managed by UCX, and the driver must not delete these objects itself.

The endpoint object implements several callback functions that allow the driver to assist UCX with operations related to the endpoint.

*[EVT_UCX_ENDPOINT_ABORT](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_abort)*</br>
Abort the queue associated with the endpoint.

*[EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_ok_to_cancel_transfers)*</br>
Notify the controller driver that it can complete cancelled transfers on the endpoint.

*[EVT_UCX_ENDPOINT_PURGE](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_purge)*</br>
Complete all outstanding I/O requests on the endpoint.

*[EVT_UCX_ENDPOINT_START](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_start)*</br>
Start the queue associated with the endpoint.

*[EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_static_streams_add)*</br>
Create static streams.

*[EVT_UCX_ENDPOINT_RESET](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_reset)*</br>
Notify the driver to reset the controller's programming of the endpoint.

When the host controller driver receives a USB 3.0 No Ping Response Error on an endpoint, the driver must call **[UcxEndpointNoPingResponseError](/windows-hardware/drivers/ddi/ucxendpoint/nf-ucxendpoint-ucxendpointnopingresponseerror)**. That call results in the USB device object receiving *[EVT_UCX_USBDEVICE_UPDATE](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_update)*.
For more information, see [Configuring USB endpoints in a host controller driver](configuring-usb-endpoints-in-a-host-controller-driver.md).

## UCXSTREAMS: Stream object

Represents a number of pipes to the device across a single endpoint. The host controller driver creates stream objects in the *[EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_static_streams_add)* callback by calling **[UcxStaticStreamsCreate](/windows-hardware/drivers/ddi/ucxsstreams/nf-ucxsstreams-ucxstaticstreamscreate)**.

During the **[UcxStaticStreamsCreate](/windows-hardware/drivers/ddi/ucxsstreams/nf-ucxsstreams-ucxstaticstreamscreate)** call, the host controller driver registers its callback functions. For a specific endpoint object, the driver can determine whether it has created a streams object, and return the UCXSTREAMS handle by calling **[UcxEndpointGetStaticStreamsReferenced](/windows-hardware/drivers/ddi/ucxendpoint/nf-ucxendpoint-ucxendpointgetstaticstreamsreferenced)**.

After the object is created, the driver creates a framework queue object for each stream and sends the WDFQUEUE handle to UCX by calling **[UcxStaticStreamsSetStreamInfo](/windows-hardware/drivers/ddi/ucxsstreams/nf-ucxsstreams-ucxstaticstreamssetstreaminfo)**.

The stream object provides several callback functions for the host controller to assist UCX with managing the static streams.

*[EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_static_streams_disable)*</br>
Release controller resources for all streams for an endpoint.

*[EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_static_streams_enable)*</br>
Enable controller hardware of all streams for this endpoint.

The lifetime of the object and associated queues are managed by UCX, and the driver must not delete the objects.

## Related topics

- [Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)
