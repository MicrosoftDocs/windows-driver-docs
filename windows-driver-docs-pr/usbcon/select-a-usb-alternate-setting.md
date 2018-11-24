---
Description: This topic describes the steps for issuing a select-interface request to activate an alternate setting in a USB interface.
title: How to select an alternate setting in a USB interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to select an alternate setting in a USB interface


This topic describes the steps for issuing a select-interface request to activate an alternate setting in a USB interface. The client driver must issue this request after selecting a USB configuration. Selecting a configuration, by default, also activates the first alternate setting in each interface in that configuration.

Each USB configuration must support one or more multiple USB interfaces. Each interface exposes one or more endpoints that are used to transfer data to and from the device. USB interfaces must have a device-defined, *interface index* that is used to identify the interface. The interface must also have one or more *alternate settings* that group the endpoints of the interface. As part of device configuration, the client driver must select one of the alternate settings in the interface. Because endpoints can be shared among alternate settings, only one setting can be active at a given time. After the alternate setting is active, its endpoints become available for data transfers.

For a multiple interface device, two interfaces can be active at a given time. The client driver must activate an alternate setting in each interface. Endpoints are not shared among interfaces and therefore, each simultaneous data transfers can be performed on each interface.

Alternate settings are device-defined and identified with a number called the *setting index*. The alternate setting at index 0 is called the *default alternate setting* in this documentation set. An alternate setting is described in a [**USB\_INTERFACE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff540065) structure. The structure contains the interface index with which the setting is associated and the number of endpoints defined by the setting. It also contains information about the class specification to which the functionality of the interface conforms. The way, in which endpoints are grouped, depends on the functionality of the device.

For example, an interface exposes two isochronous and two bulk endpoints through three alternate settings (index 0, 1, 2). The Alternate Setting 0 does not define any endpoint; Alternate Setting 1 defines the bulk endpoints; Alternate Setting 2 defines the isochronous endpoints. Because Alternate Setting 0 has no endpoint, the client driver can select this setting to disable data transfer in order to conserve bandwidth. When either of the other settings is active, the device is ready for data transfers. Alternate Setting 1 can be used to transfer bulk data. Alternate Setting 2 can be selected when the device is in streaming mode. Therefore, alternate settings give the client driver the flexibility of changing the device configuration as and when required. In this example, the client driver can switch the device functionality from a bulk transfer to streaming, just by selecting an alternate setting.

Alternate settings can also be used to set bandwidth requirements. For an example, see the [USB Device Layout](usb-device-layout.md).

Windows Driver Foundation (WDF) provides methods in [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/) and [User-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/) that the client driver can call to select a different alternate setting. KMDF client driver can select a setting by specifying the setting index, interface descriptor of the setting, or by submitting an URB that contains the request. UMDF client driver can only select an alternate setting by specifying its setting index.

After a select-configuration request completes successfully, the previously active alternate setting is deactivated.

## What you need to know


### Technologies

-   [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)
-   [User-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)

### Prerequisites

Before the client driver can select an alternate setting, make sure these requirements are met:

-   The client driver must have created the framework USB target device object.

    -   A KMDF client driver must obtain a WDFUSBDEVICE handle by calling the [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428) method. For more information, see "Device source code" in [Understanding the USB client driver code structure (KMDF)](understanding-the-kmdf-template-code-for-usb.md).
    -   A UMDF client driver must obtain an [**IWDFUsbTargetDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560362) pointer by querying the framework target device object. For more information, see "[**IPnpCallbackHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556764) implementation and USB-specific tasks" in [Understanding the USB client driver code structure (UMDF)](understanding-the-umdf-template-code-for-usb.md)

    If you are using the USB templates that are provided with Microsoft Visual Studio Professional 2012, the template code performs those tasks. The template code obtains the handle to the target device object and stores in the device context.

-   The device must have an active configuration.
    -   A KMDF client driver must call the [**WdfUsbTargetDeviceSelectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff550101) method.
    -   For a UMDF client driver, the framework selects the first configuration and the default alternate setting for each interface in that configuration.

    If you are using USB templates, the code selects the first configuration and the default alternate setting in each interface.

Instructions
------------

### Select an alternate setting - KMDF client driver

1.  Get a WDFUSBINTERFACE handle to the interface that has the alternate setting.

    To get handle, first get the number of the interfaces of the selected configuration by calling [**WdfUsbTargetDeviceGetNumInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff550094) and then enumerate interfaces in a loop. In each iteration call the [**WdfUsbTargetDeviceGetInterface**](https://msdn.microsoft.com/library/windows/hardware/ff550092) method and increment the index (starting at zero).

    **Note**  During device enumeration, the USB driver stack assigns numbers to the alternate settings. The interface numbers are zero-based and sequential. Those numbers might be different to the device-defined setting index. To obtain the device-defined setting index, call the [**WdfUsbInterfaceGetInterfaceNumber**](https://msdn.microsoft.com/library/windows/hardware/ff550065) method.

     

2.  Initiate a select-interface request by calling the [**WdfUsbInterfaceSelectSetting**](https://msdn.microsoft.com/library/windows/hardware/ff550073) method. In the *Params* parameter of the call, choose one of these options:

    -   Specify the alternate setting number assigned by the USB driver stack. Typically, you pass the same index that you used in step 1 to enumerate the settings.
    -   Specify a pointer the interface descriptor that describes the alternate setting. The driver can then get interface descriptors while enumerating alternate settings in the interface by calling the [**WdfUsbInterfaceGetDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff550060) method. After the enumeration completes, the driver gets information about all of the enumerated alternate settings in the [**USB\_INTERFACE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff540065) structure.
    -   Specify a pointer to an URB that contains all the information required for the select-interface request.

        1.  Allocate an array of [**USBD\_INTERFACE\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff539076) structures. The number of elements in this array depends on the number of interfaces in the selected configuration. For information about initializing this array, see [How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md).
        2.  Allocate an [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) for the select interface request by calling the [**USBD\_SelectInterfaceUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406245) routine. In this call specify the interface list array and the configuration handle that was obtained after selecting a configuration. You can get that handle by calling the [**WdfUsbTargetDeviceWdmGetConfigurationHandle**](https://msdn.microsoft.com/library/windows/hardware/ff551127) method.
        3.  Call [**WdfUsbInterfaceSelectSetting**](https://msdn.microsoft.com/library/windows/hardware/ff550073) and specify the URB.

        **WDM drivers:  **To submit the URB, associate the URB with an IRP, and submit the IRP to the USB driver stack. For more information, see [How to Submit an URB](send-requests-to-the-usb-driver-stack.md).

    The options in the list provide the client driver with the flexibility for specifying the selection criteria. If you are already aware of the endpoint capabilities of the alternate setting, choose the first option (with the alternate setting number) in the list. Otherwise, choose the second option that specifies the interface descriptor. Inspect [**USB\_INTERFACE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff540065) structures for all alternate settings. For each setting, enumerate its endpoints and their characteristics such as, the endpoint type, maximum packet size, and so on. When you find the set of endpoints that you need for data transfers, call [**WdfUsbInterfaceSelectSetting**](https://msdn.microsoft.com/library/windows/hardware/ff550073) by specifying a pointer to that interface descriptor. Typically, you will not require the third option unless you are a WDM-based client driver that can only send requests to the USB driver stack by submitting URBs.

    Based on the information supplied by the client driver, the USB driver stack then builds a standard control request (SET INTERFACE) and sends it to the device. If the request completes successfully, the USB driver stack obtains pipes handles to the endpoints of the alternate setting.

    After selecting an alternate setting, the client driver must always get the pipe handles for endpoints in the new setting. Failure to do so might cause the driver to send data transfer requests by using stale pipe handles. For information about retrieving pipe handles, see [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md).

```cpp
NTSTATUS  FX3SelectInterfaceSetting(  
    _In_ WDFDEVICE Device,
    _In_ UCHAR SettingIndex)

{
    NTSTATUS                 status;  
    PDEVICE_CONTEXT          pDeviceContext;  
    WDF_OBJECT_ATTRIBUTES               pipeAttributes;

    WDF_USB_INTERFACE_SELECT_SETTING_PARAMS settingParams;

    PAGED_CODE();  

    pDeviceContext = GetDeviceContext(Device);

    if (pDeviceContext->UsbInterface == NULL)
    {
        status = USBD_STATUS_BAD_NUMBER_OF_INTERFACES;
        goto Exit;
    }

    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&pipeAttributes, PIPE_CONTEXT);  

    pipeAttributes.EvtCleanupCallback = FX3EvtPipeContextCleanup;

    WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING (&settingParams, SettingIndex);

    status = WdfUsbInterfaceSelectSetting (
        pDeviceContext->UsbInterface,
        &pipeAttributes,
        &settingParams);

    if (status != STATUS_SUCCESS)
    {
        goto Exit;
    }

    if (WdfUsbInterfaceGetNumConfiguredPipes (pDeviceContext->UsbInterface) > 0)
    {
        status = FX3EnumeratePipes (Device);

        if (status != STATUS_SUCCESS)
        {
            goto Exit;
        }
    }

Exit:
    return status;
}
```

### Select an alternate setting - UMDF client driver

1.  Get the number of USB interfaces that the active configuration supports by calling the [**IWDFUsbTargetDevice::GetNumInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff560366) method.
2.  Get an [**IWDFUsbInterface**](https://msdn.microsoft.com/library/windows/hardware/ff560312) pointer for each interface in the configuration.

    Enumerate all interfaces by calling the [**IWDFUsbTargetDevice::RetrieveUsbInterface**](https://msdn.microsoft.com/library/windows/hardware/ff560381) method in a loop until the function returns NULL. With each iteration, increment the member index (zero-based). The loop retrieves [**IWDFUsbInterface**](https://msdn.microsoft.com/library/windows/hardware/ff560312) pointers to all the enumerated interfaces.

3.  For each interface, get the WinUSB handle by calling [**IWDFUsbInterface::GetWinUsbHandle**](https://msdn.microsoft.com/library/windows/hardware/ff560337). This handle is required by the next step.
4.  Call [**WinUsb\_GetAssociatedInterface**](https://msdn.microsoft.com/library/windows/hardware/ff540245) to obtain a handle to the interface. In the *AssociatedInterfaceIndex* parameter, specify the index in step 2.
5.  Determine the number of alternate settings in the interface.

    Call the [**WinUsb\_QueryInterfaceSettings**](https://msdn.microsoft.com/library/windows/hardware/ff540292) function in a loop and increment the index (zero-based) in each iteration. When all settings are enumerated, the function returns ERROR\_NO\_MORE\_ITEMS. The function also returns interface descriptors for each setting.

6.  By using the value received in the **bNumEndpoints** member of each interface descriptor, and enumerate its endpoints. Inspect the endpoint descriptors and determine which setting meets your requirement.
7.  Initiate a select-interface request by calling the [**WinUsb\_SetCurrentAlternateSetting**](https://msdn.microsoft.com/library/windows/hardware/ff540302) function. In the call, specify the alternate setting number associated with the index in step 4.
8.  Release the interface handle obtained in step 4 by calling the [**WinUsb\_Free**](https://msdn.microsoft.com/library/windows/hardware/ff540233) function.
9.  Release the WinUSB handle obtained in step 3 by calling the [**WinUsb\_Free**](https://msdn.microsoft.com/library/windows/hardware/ff540233) function.
10. If you are finished using [**IWDFUsbInterface**](https://msdn.microsoft.com/library/windows/hardware/ff560312) methods, release all interface pointers retrieved in step 2.

Remarks
-------

For a KMDF client driver, in its [**WdfUsbInterfaceSelectSetting**](https://msdn.microsoft.com/library/windows/hardware/ff550073) call, the driver can supply a pointer to a driver-defined pipe context. The client driver can store information about pipes in the pipe context. For more information about pipe information, see [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md).

## Related topics
[USB device configuration](configuring-usb-devices.md)  



