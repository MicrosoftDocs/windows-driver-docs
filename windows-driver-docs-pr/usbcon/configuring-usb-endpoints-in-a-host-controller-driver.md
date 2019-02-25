---
Description: UCX manages the creation of endpoint objects, and notifies the host controller to program or deprogram endpoints into the USB host controller.
title: Configure USB endpoints in a USB host controller driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configure USB endpoints in a USB host controller driver


UCX manages the creation of endpoint objects, and notifies the host controller to program or deprogram endpoints into the USB host controller.

While an endpoint is programmed, it is also managed by UCX. The state of an endpoint changes as devices are connected to and disconnect from the bus, experience power events such as suspend and reset, and undergo new endpoint creation such as alternate setting changes.

## Endpoint configuration


UCX invokes callback functions implemented by the host controller driver to notify the driver when endpoints must programmed into the USB host controller, or released. When [*EVT\_UCX\_USBDEVICE\_ENABLE*](https://msdn.microsoft.com/library/windows/hardware/mt187841) is called, the driver prepares the controller for performing transfers to the device’s default endpoint. Preparing the controller includes programming the default endpoint. When [*EVT\_UCX\_USBDEVICE\_DISABLE*](https://msdn.microsoft.com/library/windows/hardware/mt187840) is called, the driver deprograms the default endpoint and frees other controller resources associated with the device. When [*EVT\_UCX\_USBDEVICE\_ENDPOINTS\_CONFIGURE*](https://msdn.microsoft.com/library/windows/hardware/mt187842) is called, the driver is given a list of non-default endpoints to program into the controller, and given another list of non-default endpoints to remove from the controller. The host controller driver then programs the specified non-default endpoints into the controller, and also removes the non-default endpoints (specified in the other list) from the controller.

## Queue state management


UCX invokes callback functions implemented by the host controller driver to perform changes to the endpoint queue state. The driver then takes the corresponding action on the endpoint queue given to UCX, and on any second level queues maintained within the driver. Endpoint queues are aborted or purged in these scenarios:

-   The USB device client driver sends an URB\_FUNCTION\_ABORT\_PIPE request.
-   During suspend.
-   When the hub that a device is attached to, detects a device disconnection.
-   During a select-interface setting request.

To notify the host controller driver about a queue abort or purge, UCX calls [*EVT\_UCX\_ENDPOINT\_ABORT*](https://msdn.microsoft.com/library/windows/hardware/mt187825) or [*EVT\_UCX\_ENDPOINT\_PURGE*](https://msdn.microsoft.com/library/windows/hardware/mt187827). If at some later point the endpoint queue is needed by UCX, then UCX invokes the [*EVT\_UCX\_ENDPOINT\_START*](https://msdn.microsoft.com/library/windows/hardware/mt187829) callback to notify the driver to start the queue.

## Transfer cancellation


For any controller for which the host controller driver declares GUID\_USB\_CAPABILITY\_CLEAR\_TT\_BUFFER\_ON\_ASYNC\_TRANSFER\_CANCEL, the driver must call [**UcxEndpointNeedToCancelTransfers**](https://msdn.microsoft.com/library/windows/hardware/mt188042) and implement [*EVT\_UCX\_ENDPOINT\_OK\_TO\_CANCEL\_TRANSFERS*](https://msdn.microsoft.com/library/windows/hardware/mt187826) for canceling asynchronous (Bulk or Control) USB transfers to a USB full or low speed device that is behind a Transaction Translator (TT) hub. In all other cases, the driver can optionally call **UcxEndpointNeedToCancelTransfers** to get a *EVT\_UCX\_ENDPOINT\_OK\_TO\_CANCEL\_TRANSFERS* notification that indicates that cancelling transfers is allowed on this endpoint and the driver can proceed to cancel the transfers. Alternatively, the driver can cancel transfers directly without calling **UcxEndpointNeedToCancelTransfers**.

If the host controller driver always fails the request for this GUID, it can ignore these two function calls entirely.

If the driver never calls [**UcxEndpointNeedToCancelTransfers**](https://msdn.microsoft.com/library/windows/hardware/mt188042), the driver's [*EVT\_UCX\_ENDPOINT\_OK\_TO\_CANCEL\_TRANSFERS*](https://msdn.microsoft.com/library/windows/hardware/mt187826) callback is not called and can be NULL during callback registration.

If the driver intends to use [**UcxEndpointNeedToCancelTransfers**](https://msdn.microsoft.com/library/windows/hardware/mt188042), the driver must call the method when a transfer has been programmed into the controller and then canceled, and then waits for [*EVT\_UCX\_ENDPOINT\_OK\_TO\_CANCEL\_TRANSFERS*](https://msdn.microsoft.com/library/windows/hardware/mt187826) before completing it.

## Related topics
[Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)  



