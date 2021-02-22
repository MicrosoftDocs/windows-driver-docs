---
description: UCX manages the creation of endpoint objects, and notifies the host controller to program or deprogram endpoints into the USB host controller.
title: Configure USB endpoints in a USB host controller driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configure USB endpoints in a USB host controller driver


UCX manages the creation of endpoint objects, and notifies the host controller to program or deprogram endpoints into the USB host controller.

While an endpoint is programmed, it is also managed by UCX. The state of an endpoint changes as devices are connected to and disconnect from the bus, experience power events such as suspend and reset, and undergo new endpoint creation such as alternate setting changes.

## Endpoint configuration


UCX invokes callback functions implemented by the host controller driver to notify the driver when endpoints must programmed into the USB host controller, or released. When [*EVT\_UCX\_USBDEVICE\_ENABLE*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_enable) is called, the driver prepares the controller for performing transfers to the device’s default endpoint. Preparing the controller includes programming the default endpoint. When [*EVT\_UCX\_USBDEVICE\_DISABLE*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_disable) is called, the driver deprograms the default endpoint and frees other controller resources associated with the device. When [*EVT\_UCX\_USBDEVICE\_ENDPOINTS\_CONFIGURE*](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_endpoints_configure) is called, the driver is given a list of non-default endpoints to program into the controller, and given another list of non-default endpoints to remove from the controller. The host controller driver then programs the specified non-default endpoints into the controller, and also removes the non-default endpoints (specified in the other list) from the controller.

## Queue state management


UCX invokes callback functions implemented by the host controller driver to perform changes to the endpoint queue state. The driver then takes the corresponding action on the endpoint queue given to UCX, and on any second level queues maintained within the driver. Endpoint queues are aborted or purged in these scenarios:

-   The USB device client driver sends an URB\_FUNCTION\_ABORT\_PIPE request.
-   During suspend.
-   When the hub that a device is attached to, detects a device disconnection.
-   During a select-interface setting request.

To notify the host controller driver about a queue abort or purge, UCX calls [*EVT\_UCX\_ENDPOINT\_ABORT*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_abort) or [*EVT\_UCX\_ENDPOINT\_PURGE*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_purge). If at some later point the endpoint queue is needed by UCX, then UCX invokes the [*EVT\_UCX\_ENDPOINT\_START*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_start) callback to notify the driver to start the queue.

## Transfer cancellation


For any controller for which the host controller driver declares GUID\_USB\_CAPABILITY\_CLEAR\_TT\_BUFFER\_ON\_ASYNC\_TRANSFER\_CANCEL, the driver must call [**UcxEndpointNeedToCancelTransfers**](/windows-hardware/drivers/ddi/ucxendpoint/nf-ucxendpoint-ucxendpointneedtocanceltransfers) and implement [*EVT\_UCX\_ENDPOINT\_OK\_TO\_CANCEL\_TRANSFERS*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_ok_to_cancel_transfers) for canceling asynchronous (Bulk or Control) USB transfers to a USB full or low speed device that is behind a Transaction Translator (TT) hub. In all other cases, the driver can optionally call **UcxEndpointNeedToCancelTransfers** to get a *EVT\_UCX\_ENDPOINT\_OK\_TO\_CANCEL\_TRANSFERS* notification that indicates that cancelling transfers is allowed on this endpoint and the driver can proceed to cancel the transfers. Alternatively, the driver can cancel transfers directly without calling **UcxEndpointNeedToCancelTransfers**.

If the host controller driver always fails the request for this GUID, it can ignore these two function calls entirely.

If the driver never calls [**UcxEndpointNeedToCancelTransfers**](/windows-hardware/drivers/ddi/ucxendpoint/nf-ucxendpoint-ucxendpointneedtocanceltransfers), the driver's [*EVT\_UCX\_ENDPOINT\_OK\_TO\_CANCEL\_TRANSFERS*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_ok_to_cancel_transfers) callback is not called and can be NULL during callback registration.

If the driver intends to use [**UcxEndpointNeedToCancelTransfers**](/windows-hardware/drivers/ddi/ucxendpoint/nf-ucxendpoint-ucxendpointneedtocanceltransfers), the driver must call the method when a transfer has been programmed into the controller and then canceled, and then waits for [*EVT\_UCX\_ENDPOINT\_OK\_TO\_CANCEL\_TRANSFERS*](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_ok_to_cancel_transfers) before completing it.

## Related topics
[Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)