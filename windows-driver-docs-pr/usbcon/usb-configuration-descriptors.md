---
title: USB Configuration Descriptors
description: A USB device exposes its capabilities in the form of a series of interfaces called a USB configuration.
ms.date: 01/17/2024
---

# USB configuration descriptors

A USB device exposes its capabilities in the form of a series of interfaces called a USB configuration. Each interface consists of one or more alternate settings, and each alternate setting is made up of a set of endpoints. This topic describes the various descriptors associated with a USB configuration.

A USB configuration is described in a configuration descriptor (see **[USB_CONFIGURATION_DESCRIPTOR](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_configuration_descriptor)** structure). A configuration descriptor contains information about the configuration and its interfaces, alternate settings, and their endpoints. Each interface descriptor or alternate setting is described in a **[USB_INTERFACE_DESCRIPTOR](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_interface_descriptor)** structure. In a configuration, each interface descriptor is followed in memory by all of the endpoint descriptors for the interface and alternate setting. Each endpoint descriptor is stored in a **[USB_ENDPOINT_DESCRIPTOR](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_endpoint_descriptor)** structure.

For example, consider a USB webcam device described in [USB Device Layout](usb-device-layout.md). The device supports a configuration with two interfaces, and the first interface (index 0) supports two alternate settings.

The following example shows the configuration descriptor for the USB webcam device:

```output
Configuration Descriptor:
wTotalLength:         0x02CA
bNumInterfaces:       0x02
bConfigurationValue:  0x01
iConfiguration:       0x00
bmAttributes:         0x80 (Bus Powered )
MaxPower:             0xFA (500 mA)
```

The **bConfigurationValue** field indicates the number for the configuration defined in the firmware of the device. The client driver uses that number value to select an active configuration. For more information about [USB device configuration](configuring-usb-devices.md), see [How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md). A USB configuration also indicates certain power characteristics. The **bmAttributes** contains a bitmask that indicates whether the configuration supports the remote wake-up feature, and whether the device is bus-powered or self-powered. The **MaxPower** field specifies the maximum power (in milliamp units) that the device can draw from the host, when the device is bus-powered. The configuration descriptor also indicates the total number of interfaces (**bNumInterfaces**) that the device supports.

The following example shows the interface descriptor for Alternate Setting 0 of Interface 0 for the webcam device:

```output
Interface Descriptor:
bInterfaceNumber:     0x00
bAlternateSetting:    0x00
bNumEndpoints:        0x01
bInterfaceClass:      0x0E
bInterfaceSubClass:   0x02
bInterfaceProtocol:   0x00
iInterface:           0x02
0x0409: "Microsoft LifeCam VX-5000"
0x0409: "Microsoft LifeCam VX-5000"
```

In the preceding example, note **bInterfaceNumber** and **bAlternateSetting** field values. Those fields contain index values that a client driver uses to activate the interface and one of its alternate settings. For activation, the driver sends a select-interface request to the USB driver stack. The driver stack then builds a standard control request (SET INTERFACE) and sends it to the device. Note the **bInterfaceClass** field. The interface descriptor or the descriptor for any of its alternate settings specifies a class code, subclass, and protocol. The value of 0x0E indicates that the interface is for the video device class. Also, notice the **iInterface** field. That value indicates that there are two string descriptors appended to the interface descriptor. String descriptors contain Unicode descriptions that are used during device enumeration to identify the functionality. For more information about string descriptors, see [USB String Descriptors](usb-string-descriptors.md).

Each endpoint, in an interface, describes a single stream of input or output for the device. A device that supports streams for different kinds of functions has multiple interfaces. A device that supports several streams that pertain to a function can support multiple endpoints on a single interface.

All types of endpoints (except the default endpoint) must provide endpoint descriptors so that the host can get information about endpoint. An endpoint descriptor includes information, such as its address, type, direction, and the amount of data the endpoint can handle. The data transfers to the endpoint are based on that information.

The following example shows an endpoint descriptor for the webcam device:

```output
Endpoint Descriptor:
bEndpointAddress:   0x82  IN
bmAttributes:       0x01
wMaxPacketSize:     0x0080 (128)
bInterval:          0x01
```

The **bEndpointAddress** field specifies the unique endpoint address that contains the endpoint number (Bits 3..0) and the direction of the endpoint (Bit 7). By reading those values in the preceding example, we can determine that the descriptor describes an IN endpoint whose endpoint number is 2. The **bmAttributes** attribute indicates that the endpoint type is isochronous. The **wMaxPacketSizefield** indicates the maximum number of bytes that the endpoint can send or receive in a single transaction. Bits 12..11 indicate the total number of transactions that can be sent per microframe. The **bInterval** indicates how often the endpoint can send or receive data.

## How to get the configuration descriptor

The configuration descriptor is obtained from the device through a standard device request (GET_DESCRIPTOR), which is sent as a control transfer by the USB driver stack. A USB client driver can initiate the request in one of the following ways:

- If the device supports only one configuration, the easiest way is to call the framework-provided **[WdfUsbTargetDeviceRetrieveConfigDescriptor](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor)** method.
- For a device that supports multiple configurations, if the client driver wants to get the descriptor of the configuration other than the first, the driver must submit an URB. To submit an URB, the driver must allocate, format, and then submit the URB to the USB driver stack.

  To allocate the URB, the client driver must call the **[WdfUsbTargetDeviceCreateUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)** method. The method receives a pointer to an URB allocated by the USB driver stack.

  To format the URB, the client driver can use the **[UsbBuildGetDescriptorRequest](/previous-versions/ff538943(v=vs.85))** macro. The macro sets all the necessary information in the URB, such as the device-defined configuration number for which to retrieve the descriptor. The URB function is set to URB_FUNCTION_GET_DESCRIPTOR_FROM_DEVICE (see **[_URB_CONTROL_DESCRIPTOR_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_control_descriptor_request)**) and the type of descriptor is set to USB_CONFIGURATION_DESCRIPTOR_TYPE. By using the information contained in the URB, the USB driver stack builds a standard control request and sends it to the device.

  To submit the URB, the client driver must use a WDF request object. To send the request object to the USB driver stack asynchronously, the driver must call the **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)**method. To send it synchronously, call the **[WdfUsbTargetDeviceSendUrbSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendurbsynchronously)** method.

  **WDM drivers:** A Windows Driver Model (WDM) client driver can only get the configuration descriptor by submitting an URB. To allocate the URB, the driver must call the **[USBD_UrbAllocate](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urballocate)** routine. To format the URB, the driver must call the **[UsbBuildGetDescriptorRequest](/previous-versions//ff538943(v=vs.85))** macro. To submit the URB, the driver must associate the URB with an IRP, and submit the IRP to the USB driver stack. For more information, see [How to Submit an URB](send-requests-to-the-usb-driver-stack.md).

Within a USB configuration, the number of interfaces and their alternate settings are variable. Therefore, it's difficult to predict the size of buffer required to hold the configuration descriptor. The client driver must collect all that information in two steps. First, determine what size buffer required to hold all of the configuration descriptor, and then issue a request to retrieve the entire descriptor. A client driver can get the size in one of the following ways:

To obtain the configuration descriptor by calling WdfUsbTargetDeviceRetrieveConfigDescriptor, perform these steps:

1. Get the size of buffer required to hold all of the configuration information by calling **[WdfUsbTargetDeviceRetrieveConfigDescriptor](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor)**. The driver must pass NULL in the buffer, and a variable to hold the size of the buffer.
1. Allocate a larger buffer based on the size received through the previous **[WdfUsbTargetDeviceRetrieveConfigDescriptor](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor)** call.
1. Call **[WdfUsbTargetDeviceRetrieveConfigDescriptor](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor)** again and specify a pointer to the new buffer allocated in step 2.

```cpp
 NTSTATUS RetrieveDefaultConfigurationDescriptor (
    _In_  WDFUSBDEVICE  UsbDevice,
    _Out_ PUSB_CONFIGURATION_DESCRIPTOR *ConfigDescriptor 
    )
{
    NTSTATUS ntStatus = -1;

    USHORT sizeConfigDesc;

    PUSB_CONFIGURATION_DESCRIPTOR fullConfigDesc = NULL;

    PAGED_CODE();

    *ConfigDescriptor  = NULL;

    ntStatus = WdfUsbTargetDeviceRetrieveConfigDescriptor (
        UsbDevice, 
        NULL,
        &sizeConfigDesc);

    if (sizeConfigDesc == 0)
    {
        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
            "%!FUNC! Could not retrieve the configuration descriptor size.");

        goto Exit;
    }
    else
    {
        fullConfigDesc = (PUSB_CONFIGURATION_DESCRIPTOR) ExAllocatePoolWithTag (
            NonPagedPool, 
            sizeConfigDesc,
            USBCLIENT_TAG);

        if (!fullConfigDesc)
        {
            ntStatus = STATUS_INSUFFICIENT_RESOURCES;
            goto Exit;
        }  
    }

    RtlZeroMemory (fullConfigDesc, sizeConfigDesc);

    ntStatus = WdfUsbTargetDeviceRetrieveConfigDescriptor (
        UsbDevice, 
        fullConfigDesc,
        &sizeConfigDesc);

    if (!NT_SUCCESS(ntStatus))
    {           
        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
            "%!FUNC! Could not retrieve the configuration descriptor.");

        goto Exit;
    }

    *ConfigDescriptor = fullConfigDesc;

Exit:

    return ntStatus;   
}
```

To obtain the configuration descriptor by submitting an URB, perform these steps:

1. Allocate an URB by calling the **[WdfUsbTargetDeviceCreateUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)** method.
1. Format the URB by calling the **[UsbBuildGetDescriptorRequest](/previous-versions/ff538943(v=vs.85))** macro. The transfer buffer of the URB must point to a buffer large enough to hold a **[USB_CONFIGURATION_DESCRIPTOR](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_configuration_descriptor)** structure.
1. Submit the URB as a WDF request object by calling **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)** or **[WdfUsbTargetDeviceSendUrbSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendurbsynchronously)**.
1. After the request completes, check the **wTotalLength** member of **[USB_CONFIGURATION_DESCRIPTOR](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_configuration_descriptor)**. That value indicates the size of the buffer required to contain a full configuration descriptor.
1. Allocate a larger buffer based on the size retrieved in **wTotalLength**.
1. Issue the same request with the larger buffer.

The following example code shows the **[UsbBuildGetDescriptorRequest](/previous-versions/ff538943(v=vs.85))** call for a request to get configuration information for the i-th configuration:

```cpp
NTSTATUS FX3_RetrieveConfigurationDescriptor (
    _In_ WDFUSBDEVICE  UsbDevice,
    _In_ PUCHAR ConfigurationIndex,
    _Out_ PUSB_CONFIGURATION_DESCRIPTOR *ConfigDescriptor 
    )
{
    NTSTATUS ntStatus = STATUS_SUCCESS;

    USB_CONFIGURATION_DESCRIPTOR configDesc;
    PUSB_CONFIGURATION_DESCRIPTOR fullConfigDesc = NULL;

    PURB urb = NULL;

    WDFMEMORY urbMemory = NULL;

    PAGED_CODE();

    RtlZeroMemory (&configDesc, sizeof(USB_CONFIGURATION_DESCRIPTOR));
    *ConfigDescriptor = NULL;

    // Allocate an URB for the get-descriptor request. 
    // WdfUsbTargetDeviceCreateUrb returns the address of the 
    // newly allocated URB and the WDFMemory object that 
    // contains the URB.

    ntStatus = WdfUsbTargetDeviceCreateUrb (
        UsbDevice,
        NULL,
        &urbMemory,
        &urb);

    if (!NT_SUCCESS (ntStatus))
    {
        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
            "%!FUNC! Could not allocate URB for an open-streams request.");

        goto Exit;
    }

       // Format the URB.
    UsbBuildGetDescriptorRequest (
        urb,                                                        // Points to the URB to be formatted
        (USHORT) sizeof( struct _URB_CONTROL_DESCRIPTOR_REQUEST ),  // Size of the URB.
        USB_CONFIGURATION_DESCRIPTOR_TYPE,                          // Type of descriptor
        *ConfigurationIndex,                                        // Index of the configuration
        0,                                                          // Not used for configuration descriptors
        &configDesc,                                                // Points to a USB_CONFIGURATION_DESCRIPTOR structure
        NULL,                                                       // Not required because we are providing a buffer not MDL
        sizeof(USB_CONFIGURATION_DESCRIPTOR),                       // Size of the USB_CONFIGURATION_DESCRIPTOR structure.
        NULL                                                        // Reserved.
        );

       // Send the request synchronously.
    ntStatus = WdfUsbTargetDeviceSendUrbSynchronously (
        UsbDevice,
        NULL,
        NULL,
        urb);

    if (configDesc.wTotalLength == 0)
    {
        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
            "%!FUNC! Could not retrieve the configuration descriptor size.");

        ntStatus = USBD_STATUS_INAVLID_CONFIGURATION_DESCRIPTOR;

        goto Exit;
    }

    // Allocate memory based on the retrieved size. 
       // The allocated memory is released by the caller.
    fullConfigDesc = (PUSB_CONFIGURATION_DESCRIPTOR) ExAllocatePoolWithTag (
        NonPagedPool, 
        configDesc.wTotalLength,
        USBCLIENT_TAG);

    RtlZeroMemory (fullConfigDesc, configDesc.wTotalLength);

    if (!fullConfigDesc)
    {
        ntStatus = STATUS_INSUFFICIENT_RESOURCES;

        goto Exit;
    }

       // Format the URB.
    UsbBuildGetDescriptorRequest (
        urb,                                                        
        (USHORT) sizeof( struct _URB_CONTROL_DESCRIPTOR_REQUEST ),  
        USB_CONFIGURATION_DESCRIPTOR_TYPE,                          
        *ConfigurationIndex,                                         
        0,                                                          
        fullConfigDesc,                                                 
        NULL,                                                       
        configDesc.wTotalLength,                       
        NULL                                                        
        );

       // Send the request again.
    ntStatus = WdfUsbTargetDeviceSendUrbSynchronously (
        UsbDevice,
        NULL,
        NULL,
        urb);

    if ((fullConfigDesc->wTotalLength == 0) || !NT_SUCCESS (ntStatus))
    {
        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
            "%!FUNC! Could not retrieve the configuration descriptor.");

        ntStatus = USBD_STATUS_INAVLID_CONFIGURATION_DESCRIPTOR;

        goto Exit;
    }

       // Return to the caller.
    *ConfigDescriptor = fullConfigDesc;

Exit:

    if (urbMemory)
    {
        WdfObjectDelete (urbMemory);
    }

    return ntStatus;
}
```

When the device returns the configuration descriptor, the request buffer is filled with interface descriptors for all alternate settings, and endpoint descriptors for all endpoints within a particular alternate setting. For the device described in [USB Device Layout](usb-device-layout.md), the following diagram illustrates how configuration information is laid out in memory.

:::image type="content" source="images/usbconfig.png" alt-text="Diagram of a configuration descriptor layout.":::

The zero-based **bInterfaceNumber** member of **[USB_INTERFACE_DESCRIPTOR](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_interface_descriptor)** distinguishes interfaces within a configuration. For a given interface, the zero-based **bAlternateSetting** member distinguishes between alternate settings of the interface. The device returns interface descriptors in order of **bInterfaceNumber** values and then in order of **bAlternateSetting** values.

To search for a given interface descriptor within the configuration, the client driver can call **[USBD_ParseConfigurationDescriptorEx](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_parseconfigurationdescriptorex)**. In the call, the client driver provides a starting position within the configuration. Optionally the driver can specify an interface number, an alternate setting, a class, a subclass, or a protocol. The routine returns a pointer to the next matching interface descriptor.

To examine a configuration descriptor for an endpoint or string descriptor, use the **[USBD_ParseDescriptors](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_parsedescriptors)** routine. The caller provides a starting position within the configuration and a descriptor type, such as USB_STRING_DESCRIPTOR_TYPE or USB_ENDPOINT_DESCRIPTOR_TYPE. The routine returns a pointer to the next matching descriptor.

## Related topics

- [How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md)
- [USB Descriptors](usb-descriptors.md)
