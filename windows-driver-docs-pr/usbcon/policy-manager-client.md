---
title: Write a USB Type-C Policy Manager Client Driver
description:  The client driver can participate in the policy decisions for USB Type-C connectors.
ms.date: 01/17/2024
---

# Write a USB Type-C Policy Manager client driver

The Microsoft-provided USB Type-C Policy Manager monitors the activities of USB Type-C connectors. Windows, version 1809, introduces a set of programming interfaces that you can use to write a client driver to Policy Manager (called a _PM client driver_ in this topic). The client driver can participate in the policy decisions for USB Type-C connectors. With this set, you can choose to write a kernel-mode export driver or a user-mode driver.

The Policy Manager gets and coordinates the information from the USB Connector Manager (UCM), USB host controller, and USB function, and your PM client driver. When UI notification is required, the Policy Manager sends the request to system Shell.

![Architechtural block diagram for USB Policy Manager.](images/pmclient.png)

For a full view of the drivers, see [Architecture: USB Type-C design for a Windows system](./architecture--usb-type-c-in-a-windows-system.md).

## Important APIs

The PM APIs are declared in the [Usbpmapi.h](/windows-hardware/drivers/ddi/usbpmapi) header.

## 1: Client Registration

1. The client driver calls **[UsbPm_Register](/windows-hardware/drivers/ddi/usbpmapi/nf-usbpmapi-usbpm_register)** to register the driver's callback functions.
1. The client driver waits for an event from the Policy Manager.
    > A successful **UsbPm_Register** call doesn't guarantee that the client driver has requested access. When the Policy Manager is ready, the driver's **[EVT_USBPM_EVENT_CALLBACK](/windows-hardware/drivers/ddi/usbpmapi/nc-usbpmapi-evt_usbpm_event_callback)** gets invoked with **PolicyManagerArrival** as the event data that indicates the actual access granted.
1. The **UsbPm_Register** call returns the registration handle.
    > The client driver may receive **EVT_USBPM_EVENT_CALLBACK** even before **UsbPm_Register** returns.

## 2: Hub Arrival

1. When a UCMCX device arrives, the POlicy Manager is notified and keeps track of all the hub handles along with properties and states of all the connectors on each hub.
1. The client driver's **[EVT_USBPM_EVENT_CALLBACK](/windows-hardware/drivers/ddi/usbpmapi/nc-usbpmapi-evt_usbpm_event_callback)** gets invoked with **HubArrivalRemoval** as the event data. The call also contains the hub handles.
1. In the client driver's implementation of **EVT_USBPM_EVENT_CALLBACK**, the driver calls **[UsbPm_RetrieveHubProperties](/windows-hardware/drivers/ddi/usbpmapi/nf-usbpmapi-usbpm_retrievehubproperties)** to get the number of connectors on the hub, and then calls **[UsbPm_RetrieveConnectorProperties](/windows-hardware/drivers/ddi/usbpmapi/nf-usbpmapi-usbpm_retrieveconnectorproperties)** and **[UsbPm_RetrieveConnectorState](/windows-hardware/drivers/ddi/usbpmapi/nf-usbpmapi-usbpm_retrieveconnectorstate)** to get more information about each connector.

## 3: Connector State Change

1. Due to a connector state change, for example, Type-C attach/detach, PD contract negotiated, Policy Manager updates the per-connector state information.
1. The client driver's **[EVT_USBPM_EVENT_CALLBACK](/windows-hardware/drivers/ddi/usbpmapi/nc-usbpmapi-evt_usbpm_event_callback)** gets invoked with **ConnectorStateChange** as the event data. The call also contains the connector handles.
1. The client driver's completion routine also gets called, and takes action accordingly.
1. In the client driver's implementation of **EVT_USBPM_EVENT_CALLBACK**, the driver calls **[UsbPm_RetrieveConnectorProperties](/windows-hardware/drivers/ddi/usbpmapi/nf-usbpmapi-usbpm_retrieveconnectorproperties)**. By using the given connector handle, the driver gets the latest connector state, inspects it, and may decide to update its local copy.  

## 4: Change initiated by the client driver

1. To request a change the client driver calls  **[UsbPm_AssignConnectorPowerLevel](/windows-hardware/drivers/ddi/usbpmapi/nf-usbpmapi-usbpm_assignconnectorpowerlevel)**.
    > The client driver may call this function within the **EVT_USBPM_EVENT_CALLBACK** callback registered using **UsbPm_Register**.

1. The Policy Manager forwards the request to USB Connector Manager (UCM). The client driver for UcmCx takes the appropriate action to change the requested state.
1. The client driver's **[EVT_USBPM_EVENT_CALLBACK](/windows-hardware/drivers/ddi/usbpmapi/nc-usbpmapi-evt_usbpm_event_callback)** gets invoked with **ConnectorStateChange** as the event data. The call also contains the connector handle.
1. The client driver's completion routine also gets called, and takes action accordingly.
1. Within the callback, client driver calls **[UsbPm_RetrieveConnectorState](/windows-hardware/drivers/ddi/usbpmapi/nf-usbpmapi-usbpm_retrieveconnectorproperties)** with the given connector handle to get the latest connector state, inspects it and may decide to update its local copy.

## 5: Hub Removal

1. UCM notifies the Policy Manager when a UcmCx device (not an individual connector on a UcmCx device) is removed. The Policy Manager removes the hub from its hub collection.
1. The client driver's **[EVT_USBPM_EVENT_CALLBACK](/windows-hardware/drivers/ddi/usbpmapi/nc-usbpmapi-evt_usbpm_event_callback)** implementation gets invoked with **HubRemoval** as the event data. The call also contains the hub handle.
1. In the client driver's implementation of **EVT_USBPM_EVENT_CALLBACK**, the client driver performs clean-up tasks for the hub and connectors being removed. The driver can call **[UsbPm_RetrieveHubProperties](/windows-hardware/drivers/ddi/usbpmapi/nf-usbpmapi-usbpm_retrievehubproperties)** and **[UsbPm_RetrieveConnectorProperties](/windows-hardware/drivers/ddi/usbpmapi/nf-usbpmapi-usbpm_retrieveconnectorproperties)** to get the properties of hub and connectors.

## 6: Client Deregistration

1. The client driver calls **[UsbPm_Deregister](/windows-hardware/drivers/ddi/usbpmapi/nf-usbpmapi-usbpm_register)** when the driver no longer needs any notifications.
1. The Policy Manager marks the client handle registration as deregistered and does not invoke **EVT_USBPM_EVENT_CALLBACK** callback.

## See Also

- [Write a USB Type-C connector driver](./bring-up-a-usb-type-c-connector-on-a-windows-system.md)
- [Write a USB Type-C port controller driver](./write-a-usb-type-c-port-controller-driver.md)
- [Write a USB function controller client driver](./function-client-driver.md)
