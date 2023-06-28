---
title: USB client drivers for media-agnostic (MA-USB)
description: USB device driver that sends MA-USB packets.
ms.date: 06/28/2023
---

# USB client drivers for media-agnostic (MA-USB)

> [!NOTE]
> Media-agnostic USB is not supported by Windows and is intended for evaluation only.

In Windows 10, version 1709, USB driver stack can send USB packets over non-USB physical mediums such as Wi-Fi by using the media-agnostic USB (MA-USB) protocol. The new feature has been designed in a way that the changes required to existing USB client drivers are minimal. That set of changes include additional information about the transport:

- For devices with isochronous/streaming endpoints, the client driver needs to know the delays associated with transfer programming and transfer completion so that the driver can make sure that the device gets the isochronous packets on time.

- The client driver can use that information to optimize their higher layer selection of protocols. For example, a display driver can use the  latency and bandwidth information to choose the best codecs and buffering schemes. Because those characteristics might change dynamically, the driver needs to determine the changes.

## Getting the delays for isochronous transfers

For isochronous endpoints, the client driver needs to know the maximum programming latency and maximum completion latency. That request must be targeted for a specific pipe because that latency can be different for different endpoints on the same device as MA-USB specification provides mechanisms for the host to calculate these values.

To build that request the driver must use the **_URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS** URB.

> [!NOTE]
> In this release, this feature is available to only KMDF and WDM-based drivers.

Here are some best practices for building this URB:

- The client driver must allocate this URB by calling [WdfUsbTargetDeviceCreateUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb) or [USBD_UrbAllocate](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urballocate).
- The URB can be sent at <= Dispatch Level.
- If the URB is targeted to a nonisochronous endpoint, the USB driver stack fails the request.
- The client driver must not assume the third-party USB stacks support this URB.

For a continuous isochronous IN streaming, client driver typically issues multiple outstanding read requests. The driver can use the round-trip time to calculate the number of isochronous packets that need to be in a read request based on the number of outstanding read requests.

For example, if the number of outstanding requests is two, the number of isochronous packets in an URB should be at least (Total Round Trip Time)/ (Length of Service Interval) where Total Round Trip Time = MaximumSendPathDelayInMilliSeconds + MaximumCompletionPathDelayInMilliSeconds

If Send delay = 10 ms, Completion delay = 15 ms, then Total round trip = 25 ms

If Length of Service Interval = 5 ms

Number of isochronous URBs = 2

For continuous streaming, the number of isochronous packets in each isochronous URB should be at least = 25 / 5 = 5 packets.

## Getting the host controller transport characteristics

A client driver can retrieve the transport characteristics by sending these IOCTLs requests:

- [IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_get_transport_characteristics)
- [IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_register_for_transport_characteristics_change)
- [IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_notify_on_transport_characteristics_change)
- [IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_unregister_for_transport_characteristics_change)

The transport characteristics may or may not be available in all cases because the USB driver stack is dependent on the underlying transport to expose those values. Therefore, the client driver must determine the information through other mechanisms when the IOCTL requests fail.

### Query for the current transport characteristics

The client driver can query the transport characteristics at a specific time by sending the   [IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_get_transport_characteristics) request. On receiving the request, the USB driver stack completes it immediately with the information about the current transport characteristics in a USB_TRANSPORT_CHARACTERISTICS structure. Given that the information doesn't always indicate changes, this request is used by the driver for the deciding the algorithm or starting a stream.

### Receive changes in transport characteristics

For MA-USB, the underlying transport could be wired, wireless￼. The transport characteristics of those mediums can vary significantly over time. The client driver can get notified on the ongoing changes.

1. Send an [IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_register_for_transport_characteristics_change) request
to register for notifications. If registration is successful, the client driver receives a handle and the initial values of the transport characteristics.

1. Send an [IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_notify_on_transport_characteristics_change) request with the registration handle obtained in step 1. The USB driver stack keeps the request pending. Whenever transport characteristics change, the pending request is completed with the new values of transport characteristics.

1. After the client is done and not interested in getting further notifications, it should ensure that there are no IOCTLs pending in the stack. Then the client should send the IOCTL with subcode [IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_unregister_for_transport_characteristics_change), passing in the registration handle. If the client unregisters with pending change request, USB Stack completes them before completing the unregister IOCTL.

### Query for device characteristics

To determine the general characteristics about a USB device, such as maximum send and receive delays for any request, the client driver can send the  [IOCTL_USB_GET_DEVICE_CHARACTERISTICS](/windows-hardware/drivers/ddi/usbioctl/ns-usbioctl-_usb_device_characteristics) request.

## Setting priority for a bulk endpoint

There may be cases when certain client drivers use bulk endpoint for carrying different types of data that doesn’t fit into the priority class of bulk transfers. For example,
a USB display driver can use a bulk endpoint for carrying display frames and cursor updates. A USB audio driver for MIDI can use bulk endpoint for carrying audio/voice data.
For a user good experience over MA-USB with such client drivers, the driver must prioritize bulk transfers based on type of data. For example, a bulk endpoint carrying a mouse cursor updates or audio/voice data should be marked highest priority whereas a bulk endpoint carrying display/video or storage data should be marked medium priority.

The client driver can set the options by defining the priorities of specific bulk endpoints in the Device Parameters subkey of the device's HW registry key.

The format of the registry value is a multistring named **EndpointPriorities**. Each string within the multi-string defines the priority for a specific endpoint. The format of the string is as follows:
    `<CONFIG>,<INTERFACE>,<ALTSETTING>,<TYPE>,<ORDER>,<PRIORITY>`

Where:

- CONFIG – A decimal value indicating the **bConfigurationValue** value for the configuration containing the endpoint, as defined in the configuration descriptor. A value of 0 isn't valid. A wildcard value of "*" may be specified to indicate it applies to all configurations.

- INTERFACE - A decimal value indicating the **bInterfaceNumber** for the interface within the configuration that contains the endpoint, as defined in the interface descriptor. A wildcard value of "*" may be specified to indicate it applies to all interfaces. In cases where the registry setting is being applied to a composite USB function rather than an entire USB device, the interface value indicates.

- ALTSETTING - A decimal value indicating the bAlternateSetting value for the interface's alternate setting. A wildcard value of "*" may be used to indicate it applies to all alternate settings within the interface.

- TYPE - Indicates the type and direction of endpoint being specified. Valid strings are **BULK_IN**, **BULK_OUT**, **INTERRUPT_IN**, **INTERRUPT_OUT**, **ISOCHRONOUS_IN**, **ISOCHRONOUS_OUT**, and **CONTROL**.

- POSITION - A zero-based decimal value indicating which endpoint within the interface the priority applies to. If an interface had three BULK_OUT endpoints, a position value of 0 specifies the first endpoint, a value of 1 specifies the second endpoint, and so on. For a function on a composite USB device, the interface numbers are relative to the interface(s) assigned to the composite function, not the parent USB device.

For example,

```cpp

REG_MULTI_SZ:"EndpointPriorities" = 
“"1,0,*,BULK_IN,0,VIDEO",   // BULK IN endpoint in interface 0, configuration 1, all alternate settings has VIDEO priority. 
"1,1,*,BULK_OUT,0,VOICE",  // First BULK OUT endpoint in interface 1, configuration 1, all alternate settings has VOICE priority. 
"2,1,0,BULK_OUT,1,INTERACTIVE"” // BULK OUT endpoint in configuration 2, interface 1, alt setting 1 has INTERACTIVE priority.
```

## See Also

- [WdfUsbTargetDeviceCreateUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)
- [USBD_UrbAllocate](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urballocate)
- [IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_get_transport_characteristics)
- [IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_register_for_transport_characteristics_change)
- [IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_notify_on_transport_characteristics_change)
- [IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_unregister_for_transport_characteristics_change)
