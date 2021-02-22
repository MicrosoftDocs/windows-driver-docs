---
description: USB function class extension (UFX) uses the WDF object functionality to define these USB-specific UFX objects.
title: UFX objects and handles used by a USB function client driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UFX objects and handles used by a USB function client driver


**Summary**

-   UFX objects are used by the function controller driver to handle transfers to and from endpoints.
-   These objects are handles to WDF objects and are created by UFX at the request of client driver. Each object's lifetime is managed by UFX.

**Applies to**

-   Windows 10

**Last updated**

-   July 2015

**Important APIs**

-   [**UfxDeviceCreate**](/windows-hardware/drivers/ddi/ufxclient/nf-ufxclient-ufxdevicecreate)
-   [**UfxEndpointCreate**](/windows-hardware/drivers/ddi/ufxclient/nf-ufxclient-ufxendpointcreate)

USB function class extension (UFX) uses the WDF object functionality to define these USB-specific UFX objects.

These objects are handles to WDF objects and are created by UFX at the request of the function client driver. Optionally client driver can associate a context with these objects which can be passed at the time of the creation. Every WDF object created by UFX can potentially have two device contexts: One device context set by UFX at the object creation time; the other device context passed in by client driver and is set in UFX by using [**WdfObjectAllocateContext**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectallocatecontext) after the WDF object is created.

## USB device object


**UFXDEVICE**

Represents the USB device created by the controller. The object is responsible for managing USB states according to the USB protocol specification and managing one or more endpoints associated with the USB device. The function controller driver creates this object within the [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback by calling the [**UfxDeviceCreate**](/windows-hardware/drivers/ddi/ufxclient/nf-ufxclient-ufxdevicecreate) method.

[*EVT\_UFX\_DEVICE\_HOST\_CONNECT*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_host_connect)  
Initiates connection with the host.

[*EVT\_UFX\_DEVICE\_HOST\_DISCONNECT*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_host_disconnect)  
Disables the function controller's communication with the host.

[*EVT\_UFX\_DEVICE\_ADDRESSED*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_addressed)  
Assigns an address on the function controller.

[*EVT\_UFX\_DEVICE\_ENDPOINT\_ADD*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_endpoint_add)  
Creates a default endpoint object.

[*EVT\_UFX\_DEVICE\_DEFAULT\_ENDPOINT\_ADD*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_default_endpoint_add)  
Creates a default endpoint object.

[*EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_usb_state_change)  
Update the state of the USB device.

[*EVT\_UFX\_DEVICE\_PORT\_CHANGE*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_port_change)  
Update the type of the new port to which the USB device is connected.

[*EVT\_UFX\_DEVICE\_PORT\_DETECT*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_port_detect)  
Initiate port detection.

[*EVT\_UFX\_DEVICE\_REMOTE\_WAKEUP\_SIGNAL*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_remote_wakeup_signal)  
initiate remote wake-up on the function controller.

[*EVT\_UFX\_DEVICE\_DETECT\_PROPRIETARY\_CHARGER*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_proprietary_charger_detect)  
Initiates proprietary charger detection.

[*EVT\_UFX\_DEVICE\_PROPRIETARY\_CHARGER\_RESET*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_proprietary_charger_reset)  
Resets the proprietary charger.

[*EVT\_UFX\_DEVICE\_PROPRIETARY\_CHARGER\_SET\_PROPERTY*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_proprietary_charger_set_property)  
Sets charger information that it uses to enable charging over USB.

## USB endpoint object


**UFXENDPOINT**

Represents a logical connection between the host and the device. The object is responsible for transfer of data to/from the host. For every device object there can be one or more endpoints. The default endpoint is always the control endpoint and rest are class driver specific objects. The function controller driver creates the object in the [*EVT\_UFX\_DEVICE\_ENDPOINT\_ADD*](/windows-hardware/drivers/ddi/ufxclient/nc-ufxclient-evt_ufx_device_endpoint_add) callback by calling the [**UfxEndpointCreate**](/windows-hardware/drivers/ddi/ufxclient/nf-ufxclient-ufxendpointcreate) method.

## Related topics
[Developing Windows drivers for USB function controllers](developing-windows-drivers-for-usb-function-controllers.md)