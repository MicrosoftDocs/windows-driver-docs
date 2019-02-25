---
Description: 'USB device driver that sends MA-USB packets.'
title: USB client drivers for Media-Agnostic (MA-USB)
ms.date: 09/26/2017
ms.localizationpriority: medium
---

# USB client drivers for Media-Agnostic (MA-USB)

In Windows 10, version 1709, USB driver stack can send USB packets over non-USB physical mediums such as Wi-Fi by using the Media Agnostic USB (MA-USB) protocol. The new feature has been designed in a way that the changes required to exisitng USB client drivers are minimal. That set of changes include additional information about the transport:

-   For devices with isochronous/streaming endpoints, the client driver needs to know the delays associated with transfer programming and transfer completion so that the driver can make sure that the device gets the isochronous packets on time.

-   The client driver can use that informationf to optimize their higher layer selection of protocols. For example, a display driver can use the  latency and bandwidth information to choose the best codecs and buffering schemes. Because those characteristics might change dynamically, the driver needs to determine the changes.

## Getting the delays for isochronous transfers

For isochronous endpoints, the client driver needs to know the maximum programming latency and maximum completion latency. That request must be targeted for a specific pipe because that latency can be different for different endpoints on the same device as MA-USB specification provides mechanisms for the host to calculate these values. 

To build that request the driver must use the **_URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS** URB.

> [!NOTE]
> In this release, this feature is available to only KMDF and WDM-based drivers. 

Here are some best practices for building this URB:


-    The client dirver must allocate this URB by calling [WdfUsbTargetDeviceCreateUrb](https://msdn.microsoft.com/library/windows/hardware/hh439423) or [USBD_UrbAllocate](https://msdn.microsoft.com/library/windows/hardware/hh406250). 
- The URB can be sent at <= Dispatch Level.
- If the URB is targeted to a non-isochronous endpoint, the USB driver stack fails the request.
- The client driver must not assume this URB is supported by third-party USB stacks. It will be supported by all Microsoft=provided inbox USB client drivers.

For a continuous isochronous IN streaming, client driver typically issues multiple outstanding read requests. The driver can use the round-trip time to calculate the number of isochronous packets that need to be in a read request based on the number of outstanding read requests.

For Example, if the number of outstanding requests is two, the number of isochronous packets in an URB should be at least (Total Round Trip Time)/ (Length of Service Interval) where Total Round Trip Time = MaximumSendPathDelayInMilliSeconds + MaximumCompletionPathDelayInMilliSeconds

If Send delay = 10 msec, Completion delay = 15msec, then Total round trip = 25msec.
If Length of Service Interval = 5 msec
Number of isochronous URBs = 2
For continuous streaming, the number of isochronous packets in each isochronous URBs should be at least = 25 / 5 = 5 packets.

## Getting the host controller transport characteristics
A client driver can retrieve the transport characteristics by sending these IOCTLs requests:

-    [IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS](https://msdn.microsoft.com/Library/Windows/Hardware/36CF2034-C816-421A-8B59-A4DC4EFFEB70)
-    [IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](https://msdn.microsoft.com/Library/Windows/Hardware/4192501F-5A30-463C-924D-CD4F2C8C3764)
-    [IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE](https://msdn.microsoft.com/Library/Windows/Hardware/1B71794C-EBAD-4F6C-A71C-C0D419D486BE) 
-    [IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](https://msdn.microsoft.com/Library/Windows/Hardware/A6D17761-4E5F-42FC-AB40-C2BCE7769243)

The transport characteristics may or may not be available in all cases because the USB driver stack is dependent on the underlying transport to expose those values. Therefore, the client driver must determine the information through other mechanisms when the IOCTL requests fail. 

### Query for the current transport characterisctics

The client driver can query the transport characteristics at a specific time by sending the   [IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS](https://msdn.microsoft.com/Library/Windows/Hardware/36CF2034-C816-421A-8B59-A4DC4EFFEB70) request. On receiving the request, the USB driver stack completes it immediately with the information about the current transport characteristics in a USB_TRANSPORT_CHARACTERISTICS structure. Given that the information does not indicate changes at all times, this request can be used by the driver for the deciding the algorithm or starting a stream. 

### Receive changes in trasport characteristics
For MA-USB, the underlying transport could be wired, wireless￼. The transport characteristics of those mediums can vary significantly over time. The client driver can get notified on the ongoing changes.

1.    Send an [IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](https://msdn.microsoft.com/Library/Windows/Hardware/4192501F-5A30-463C-924D-CD4F2C8C3764) request 
to register for notifications. If registration is successful, the client driver receives a handle and the initial values of the transport characteristics.

2.  Send an [IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE](https://msdn.microsoft.com/Library/Windows/Hardware/1B71794C-EBAD-4F6C-A71C-C0D419D486BE) request with the registration handle obtained in step 1. The USB driver stack keeps the request pending. Whenever transport characteristics change, the pending request is completed with the new values of transport characteristics.

3.  After the client is done and not interested in getting further notifications, it should ensure that there are no IOCTLs pending in the stack and then send the IOCTL with sub-code [IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](https://msdn.microsoft.com/Library/Windows/Hardware/A6D17761-4E5F-42FC-AB40-C2BCE7769243), passing in the registration handle. If the client unregisters with pending change request, USB Stack will complete them before completing the unregister IOCTL.

### Query for device characteristics

To determione the eneral characteristics about a USB device, such as maximum send and receive delays for any request, the client driver can send the  [IOCTL_USB_GET_DEVICE_CHARACTERISTICS](https://msdn.microsoft.com/Library/Windows/Hardware/D4A8DE43-3E81-4A1C-B1C0-ABE6000D9F11) request.

## Setting priority for a bulk endpoint

There may be cases when certain client drivers use bulk endpoint for carrying different types of data that doesn’t fit into the priority class of bulk transfers. For example, 
a USB display driver can use a bulk endpoint for carrying display frames and cursor updates. A USB audio driver for MIDI can use bulk endpoint for carrying audio/voice data.
For a user good experience over MA-USB with such client drivers, the driver must prioritize bulk transfers based on type of data. For example, a bulk endpoint carrying a mouse cursor updates or audio/voice data should be marked highest priority whereas a bulk endpoint carrying display/video or storage data should be marked medium priority.

The client driver can set the options by defining the priorties of specific bulk endpoints in the Device Parameters subkey of the device's HW registry key.  

The format of the registry value is a multistring named **EndpointPriorities**.  Each string within the multi-string defines the priority for a specific endpoint.  The format of the string is as follows:
    "<CONFIG>,<INTERFACE>,<ALTSETTING>,<TYPE>,<ORDER>,<PRIORITY>"

Where:

-    CONFIG – A decimal value indicating the **bConfigurationValue** value for the configuration containing the endpoint, as defined in the configuration descriptor.  A value of 0 is not valid.  A wildcard value of "*" may be specified to indicate it applies to all configurations.

-    INTERFACE - A decimal value indicating the **bInterfaceNumber** for the interface within the configuration that contains the endpoint, as defined in the interface descriptor.  A wildcard value of "*" may be specified to indicate it applies to all interfaces.  In cases where the registry setting is being applied to a composite USB function rather than an entire USB device, the interface value will indicate.

-    ALTSETTING - A decimal value indicating the bAlternateSetting value for the interface's alternate setting.  A wildcard value of "*" may be used to indicate it applies to all alternate settings within the interface.

-    TYPE - Indicates the type and direction of endpoint being specified.  Valid strings are **BULK_IN**, **BULK_OUT**, **INTERRUPT_IN**, **INTERRUPT_OUT**, **ISOCHRONOUS_IN**, **ISOCHRONOUS_OUT**, and **CONTROL**.  

-    POSITION - A zero-based decimal value indicating which endpoint within the interface the priority applies to.  For instance, if an interface had three BULK_OUT endpoints the first endpoint is specified by a position value of 0, the second endpoint by 1, and so on.  For a function on a composite USB device the interface numbers are relative to the interface(s) assigned to the composite function, not the parent USB device.

For example,

```cpp

REG_MULTI_SZ:"EndpointPriorities" = 
“"1,0,*,BULK_IN,0,VIDEO",   // BULK IN endpoint in interface 0, configuration 1, all alternate settings has VIDEO priority. 
"1,1,*,BULK_OUT,0,VOICE",  // First BULK OUT endpoint in interface 1, configuration 1, all alternate settings has VOICE priority. 
"2,1,0,BULK_OUT,1,INTERACTIVE"” // BULK OUT endpoint in configuration 2, interface 1, alt setting 1 has INTERACTIVE priority.
```
## See Also
[WdfUsbTargetDeviceCreateUrb](https://msdn.microsoft.com/library/windows/hardware/hh439423)

[USBD_UrbAllocate](https://msdn.microsoft.com/library/windows/hardware/hh406250)
[IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS](https://msdn.microsoft.com/Library/Windows/Hardware/36CF2034-C816-421A-8B59-A4DC4EFFEB70)

[IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](https://msdn.microsoft.com/Library/Windows/Hardware/4192501F-5A30-463C-924D-CD4F2C8C3764)

[IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE](https://msdn.microsoft.com/Library/Windows/Hardware/1B71794C-EBAD-4F6C-A71C-C0D419D486BE)

[IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](https://msdn.microsoft.com/Library/Windows/Hardware/A6D17761-4E5F-42FC-AB40-C2BCE7769243)
