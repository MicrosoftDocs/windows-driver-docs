---
Description: 'USB function class extension (UFX) uses the WDF object functionality to define these USB-specific UFX objects.'
MS-HAID: 'buses.ufx\_objects\_and\_handles\_used\_by\_a\_usb\_function\_controller'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: UFX objects and handles used by a USB function client driver
author: windows-driver-content
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

-   [**UfxDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/mt187951)
-   [**UfxEndpointCreate**](https://msdn.microsoft.com/library/windows/hardware/mt187965)

USB function class extension (UFX) uses the WDF object functionality to define these USB-specific UFX objects.

These objects are handles to WDF objects and are created by UFX at the request of the function client driver. Optionally client driver can associate a context with these objects which can be passed at the time of the creation. Every WDF object created by UFX can potentially have two device contexts: One device context set by UFX at the object creation time; the other device context passed in by client driver and is set in UFX by using [**WdfObjectAllocateContext**](wdf-wdfobjectallocatecontext) after the WDF object is created.

## USB device object


**UFXDEVICE**

Represents the USB device created by the controller. The object is responsible for managing USB states according to the USB protocol specification and managing one or more endpoints associated with the USB device. The function controller driver creates this object within the [*EvtDriverDeviceAdd*](wdf-evtdriverdeviceadd) callback by calling the [**UfxDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/mt187951) method.

[*EVT\_UFX\_DEVICE\_HOST\_CONNECT*](https://msdn.microsoft.com/library/windows/hardware/mt187852)  
Initiates connection with the host.

[*EVT\_UFX\_DEVICE\_HOST\_DISCONNECT*](https://msdn.microsoft.com/library/windows/hardware/mt187853)  
Disables the function controller's communication with the host.

[*EVT\_UFX\_DEVICE\_ADDRESSED*](https://msdn.microsoft.com/library/windows/hardware/mt187847)  
Assigns an address on the function controller.

[*EVT\_UFX\_DEVICE\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187851)  
Creates a default endpoint object.

[*EVT\_UFX\_DEVICE\_DEFAULT\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187849)  
Creates a default endpoint object.

[*EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187863)  
Update the state of the USB device.

[*EVT\_UFX\_DEVICE\_PORT\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187854)  
Update the type of the new port to which the USB device is connected.

[*EVT\_UFX\_DEVICE\_PORT\_DETECT*](https://msdn.microsoft.com/library/windows/hardware/mt187855)  
Initiate port detection.

[*EVT\_UFX\_DEVICE\_REMOTE\_WAKEUP\_SIGNAL*](https://msdn.microsoft.com/library/windows/hardware/mt187859)  
initiate remote wake-up on the function controller.

[*EVT\_UFX\_DEVICE\_DETECT\_PROPRIETARY\_CHARGER*](https://msdn.microsoft.com/library/windows/hardware/mt187850)  
Initiates proprietary charger detection.

[*EVT\_UFX\_DEVICE\_PROPRIETARY\_CHARGER\_RESET*](https://msdn.microsoft.com/library/windows/hardware/mt187857)  
Resets the proprietary charger.

[*EVT\_UFX\_DEVICE\_PROPRIETARY\_CHARGER\_SET\_PROPERTY*](https://msdn.microsoft.com/library/windows/hardware/mt187858)  
Sets charger information that it uses to enable charging over USB.

## USB endpoint object


**UFXENDPOINT**

Represents a logical connection between the host and the device. The object is responsible for transfer of data to/from the host. For every device object there can be one or more endpoints. The default endpoint is always the control endpoint and rest are class driver specific objects. The function controller driver creates the object in the [*EVT\_UFX\_DEVICE\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187851) callback by calling the [**UfxEndpointCreate**](https://msdn.microsoft.com/library/windows/hardware/mt187965) method.

## Related topics
[Developing Windows drivers for USB function controllers](developing-windows-drivers-for-usb-function-controllers.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20UFX%20objects%20and%20handles%20used%20by%20a%20USB%20function%20client%20driver%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


