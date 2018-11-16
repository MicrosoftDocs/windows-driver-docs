---
Description: This topic provides an overview of USB pipes and describes the steps required by a USB client driver to obtain pipe handles from the USB driver stack.
title: How to enumerate USB pipes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to enumerate USB pipes


This topic provides an overview of USB pipes and describes the steps required by a USB client driver to obtain pipe handles from the USB driver stack.

A *USB endpoint* is a buffer in the device that the client driver sends data to or receives data from. To send or receive data, the client driver submits an I/O transfer request to the USB driver stack, which presents the data to the host controller. The host controller then follows certain protocols (depending on the type of endpoint: bulk, interrupt, or isochronous) to build requests that transfer data to or from the device. All details of the data transfer are abstracted from the client driver. As long as the client driver submits a well-formed request, the USB driver stack processes the request and transfers data to the device.

During device configuration, the USB driver stack creates a *USB pipe* (on the host side) for each of the device's endpoints defined in the USB interface and its active alternate setting. A USB pipe is a communication channel between the host controller and endpoint. For the client driver, a pipe is a logical abstraction of the endpoint. In order to send data transfers, the driver must get the pipe handle associated with the endpoint that is the target for the transfer. Pipe handles are also required when the driver wants abort transfers or reset the pipe, in case of error conditions.

All attributes of a pipe are derived from the associated endpoint descriptor. For instance, depending on the type of the endpoint, the USB driver stack assigns a type for the pipe. For a bulk endpoint, the USB driver stack creates a bulk pipe; for an isochronous endpoint, an isochronous pipe is created, and so on. Another important attribute is the amount of data that the host controller can send to the endpoint point in a request. Depending on that value, the client driver must determine the layout of the transfer buffer.

Windows Driver Foundation (WDF) provides specialized I/O target objects in [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/) and [User-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/) that simplify many of the configuration tasks for the client driver. By using those objects, the client driver can retrieve information about the current configuration, such as the number of interfaces, alternate setting within each interface, and their endpoints. One of those objects, called the *target pipe object*, performs endpoint-related tasks. This topic describes how to obtain pipe information by using the target pipe object.

For Windows Driver Model (WDM) client drivers, the USB driver stack returns an array of [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) structures. The number of elements in the array depends on the number of endpoints defined for the active alternate setting of an interface in the selected configuration. Each element contains information about the pipe created for a particular endpoint. For information about selecting a configuration and getting the array of pipe information, see [How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md).

## What you need to know


### Technologies

-   [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)
-   [User-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)

### Prerequisites

Before the client driver can enumerate pipes, make sure these requirements are met:

-   The client driver must have created the framework USB target device object.

    If you are using the USB templates that are provided with Microsoft Visual Studio Professional 2012, the template code performs those tasks. The template code obtains the handle to the target device object and stores in the device context.

    **KMDF client driver:  **

    A KMDF client driver must obtain a WDFUSBDEVICE handle by calling the [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428) method. For more information, see "Device source code" in [Understanding the USB client driver code structure (KMDF)](understanding-the-kmdf-template-code-for-usb.md).

    **UMDF client driver:  **

    A UMDF client driver must obtain an [**IWDFUsbTargetDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560362) pointer by querying the framework target device object. For more information, see "[**IPnpCallbackHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556764) implementation and USB-specific tasks" in [Understanding the USB client driver code structure (UMDF)](understanding-the-umdf-template-code-for-usb.md).

-   The device must have an active configuration.

    If you are using USB templates, the code selects the first configuration and the default alternate setting in each interface. For information about how to change that default setting, see [How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md).

    **KMDF client driver:  **

    A KMDF client driver must call the [**WdfUsbTargetDeviceSelectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff550101) method.

    **UMDF client driver:  **

    For a UMDF client driver, the framework selects the first configuration and the default alternate setting for each interface in that configuration.

Instructions
------------

### Getting USB pipe handles - KMDF client driver

The framework represents each pipe, that is opened by the USB driver stack, as a USB target pipe object. A KMDF client driver can access the methods of the target pipe object to get information about the pipe. To perform data transfers, the client driver must have WDFUSBPIPE pipe handles. To get the pipe handles, the driver must enumerate the active configuration's interfaces and alternate settings, and then enumerate the endpoints defined in each setting. Performing enumeration operations, for each data transfer, can be expensive. Therefore, one approach is to get pipe handles after the device is configured and store them in the driver-defined device context. When the driver receives data transfer requests, the driver can retrieve the required pipe handles from the device context, and use them to send the request. If the client driver changes the configuration of the device, for example, selects an alternate setting, the driver must also refresh the device context with the new pipe handles. Otherwise, the driver can erroneously send transfer requests on stale pipe handles.

**Note**  Pipe handles are not required for control transfers.
To send control transfer requests, a WDF client driver calls **WdfUsbDevicexxxx** methods exposed by the framework device object. Those methods require a WDFUSBDEVICE handle to initiate control transfers that target the default endpoint. For such transfers, the I/O target for the request is the default endpoint and is represented by the WDFIOTARGET handle, which is abstracted by the WDFUSBPIPE handle. At the device level, the WDFUSBDEVICE handle is an abstraction of the WDFUSBPIPE handle to the default endpoint.

For information about sending control transfers and the KMDF methods, see [How to send a USB control transfer](usb-control-transfer.md).



1.  Extend your device context structure to store pipe handles.

    If you know the endpoints in your device, extend your device context structure by adding WDFUSBPIPE members to store the associated USB pipe handles. For example, you can extend the device context structure as shown here:

    ```cpp
    typedef struct _DEVICE_CONTEXT {  
        WDFUSBDEVICE    UsbDevice;  
        WDFUSBINTERFACE UsbInterface;  
        WDFUSBPIPE      BulkReadPipe;   // Pipe opened for the bulk IN endpoint.
        WDFUSBPIPE      BulkWritePipe;  // Pipe opened for the bulk IN endpoint.
        WDFUSBPIPE      InterruptPipe;  // Pipe opened for the interrupt IN endpoint.
        WDFUSBPIPE      StreamInPipe;   // Pipe opened for stream IN endpoint.
        WDFUSBPIPE      StreamOutPipe;  // Pipe opened for stream OUT endpoint.
        UCHAR           NumberConfiguredPipes;  // Number of pipes opened.
        ...
        ...                                     // Other members. Not shown.

    } DEVICE_CONTEXT, *PDEVICE_CONTEXT;  
    ```

2.  Declare a pipe context structure.

    Each pipe can store endpoint-related characteristics in another structure called the *pipe context*. Similar to a device context, a pipe context is a data structure (defined by the client driver) for storing information about pipes associated with endpoints. During device configuration, the client driver passes a pointer to its pipe context to the framework. The framework allocates a block of memory based on the size of the structure, and stores a pointer to that memory location with the framework USB target pipe object. The client driver can use the pointer to access and store pipe information in members of the pipe context.

    ```cpp
    typedef struct _PIPE_CONTEXT {  

        ULONG MaxPacketSize;
        ULONG MaxStreamsSupported;
        PUSBD_STREAM_INFORMATION StreamInfo;
    } PIPE_CONTEXT, *PPIPE_CONTEXT;  

    WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(PIPE_CONTEXT, GetPipeContext)  

    ```

    In this example, the pipe context stores the maximum number of bytes that can be sent in one transfer. The client driver can use that value to determine the size of the transfer buffer. The declaration also includes the [**WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551252) macro, which generates an inline function, GetPipeContext. The client driver can call that function to retrieve a pointer to the block of memory that stores the pipe context.

    For more information about contexts, see [Framework Object Context Space](https://msdn.microsoft.com/library/windows/hardware/ff542873).

    To pass a pointer to the framework, the client driver first initializes its pipe context by calling [**WDF\_OBJECT\_ATTRIBUTES\_INIT\_CONTEXT\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff552404). Then, passes a pointer to the pipe context while calling [**WdfUsbTargetDeviceSelectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff550101) (for selecting a configuration) or [**WdfUsbInterfaceSelectSetting**](https://msdn.microsoft.com/library/windows/hardware/ff550073) (for selecting an alternate setting).

3.  After the device configuration request completes, enumerate the interface and get the pipe handles for the configured pipes. You will need this set of information:

    -   WDFUSBINTERFACE handle to the interface that contains the current setting. You can get that handle by enumerating the interfaces in the active configuration. Alternately, if you supplied a pointer to a [**WDF\_USB\_DEVICE\_SELECT\_CONFIG\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552600) structure in [**WdfUsbTargetDeviceSelectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff550101), you can get the handle from **Type.SingleInterface.ConfiguredUsbInterface** member (for single interface devices) or **Type.MultiInterface.Pairs.UsbInterface** member (for multi-interface device).
    -   Number of pipes opened for the endpoints in the current setting. You can get that number on a particular interface by calling the [**WdfUsbInterfaceGetNumConfiguredPipes**](https://msdn.microsoft.com/library/windows/hardware/ff550066) method.
    -   WDFUSBPIPE handles for all configured pipe. You can get the handle by calling the [**WdfUsbInterfaceGetConfiguredPipe**](https://msdn.microsoft.com/library/windows/hardware/ff550057) method.

    After getting the pipe handle, the client driver can call methods to determine the type and direction of the pipe. The driver can obtain information about the endpoint, in a [**WDF\_USB\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff553037) structure. The driver can obtain the populated structure by calling the [**WdfUsbTargetPipeGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff551142) method. Alternatively, the driver can supply a pointer to the structure in the [**WdfUsbInterfaceGetConfiguredPipe**](https://msdn.microsoft.com/library/windows/hardware/ff550057) call.

The following code example enumerates the pipes in the current setting. It obtains pipe handles for the device's bulk and interrupt endpoints and stores them in the driver's device context structure. It stores the maximum packet size of each endpoint in the associated pipe context. If the endpoint supports streams, it opens static streams by calling OpenStreams routine. The implementation of OpenStreams is shown in [How to open and close static streams in a USB bulk endpoint](how-to-open-streams-in-a-usb-endpoint.md).

To determine whether a particular bulk endpoint supports static streams, the client driver examines the endpoint descriptor. That code is implemented in a helper routine named, RetrieveStreamInfoFromEndpointDesc, shown in the next code block.

```cpp
NTSTATUS  
    FX3EnumeratePipes(  
    _In_ WDFDEVICE Device)

{  

    NTSTATUS                    status;  
    PDEVICE_CONTEXT             pDeviceContext;  

    UCHAR                       i; 

    PPIPE_CONTEXT               pipeContext;

    WDFUSBPIPE                  pipe; 

    WDF_USB_PIPE_INFORMATION    pipeInfo;  

    PAGED_CODE();  

    pDeviceContext = GetDeviceContext(Device);

    // Get the number of pipes in the current altenrate setting.
    pDeviceContext->NumberConfiguredPipes = WdfUsbInterfaceGetNumConfiguredPipes(
        pDeviceContext->UsbInterface);

    if (pDeviceContext->NumberConfiguredPipes == 0)
    {
        status = USBD_STATUS_BAD_NUMBER_OF_ENDPOINTS;
        goto Exit;
    }
    else
    {
        status = STATUS_SUCCESS;
    }

    // Enumerate the pipes and get pipe information for each pipe.
    for (i = 0; i < pDeviceContext->NumberConfiguredPipes; i++) 
    {
        WDF_USB_PIPE_INFORMATION_INIT(&pipeInfo); 

        pipe =  WdfUsbInterfaceGetConfiguredPipe(
            pDeviceContext->UsbInterface,  
            i, 
            &pipeInfo); 

        if (pipe == NULL)
        {
            continue;
        }

        pipeContext = GetPipeContext (pipe);

        // If the pipe is a bulk endpoint that supports streams, 
        // If the host controller supports streams, open streams.
        // Use the endpoint as an IN bulk endpoint.
        // Store the maximum packet size.

        if ((WdfUsbPipeTypeBulk == pipeInfo.PipeType) &&
            WdfUsbTargetPipeIsInEndpoint (pipe))
        {

            // Check if this is a streams IN endpoint. If it is,
            // Get the maximum number of streams and store
            // the value in the pipe context.
            RetrieveStreamInfoFromEndpointDesc (
                Device,
                pipe);

            if ((pipeContext->IsStreamsCapable) &&
                (pipeContext->MaxStreamsSupported > 0))
            {           
                status = OpenStreams (
                    Device,
                    pipe);

                if (status != STATUS_SUCCESS)
                {
                    TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
                        "%!FUNC! Could not open streams.");

                    pDeviceContext->StreamInPipe = NULL;
                }
                else
                {
                    pDeviceContext->StreamInPipe = pipe;

                    pipeContext->MaxPacketSize = pipeInfo.MaximumPacketSize;

                }
            }
            else
            {
                pDeviceContext->BulkReadPipe = pipe;

                pipeContext->MaxPacketSize = pipeInfo.MaximumPacketSize;

            }

            continue;
        }

        if ((WdfUsbPipeTypeBulk == pipeInfo.PipeType) &&
            WdfUsbTargetPipeIsOutEndpoint (pipe))
        {
            // Check if this is a streams IN endpoint. If it is,
            // Get the maximum number of streams and store
            // the value in the pipe context.
            RetrieveStreamInfoFromEndpointDesc (
                Device,
                pipe);

            if ((pipeContext->IsStreamsCapable) &&
                (pipeContext->MaxStreamsSupported > 0))
            {           
                status = OpenStreams (
                    Device,
                    pipe);

                if (status != STATUS_SUCCESS)
                {
                    TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
                        "%!FUNC! Could not open streams.");

                    pDeviceContext->StreamOutPipe = NULL;
                }
                else
                {
                    pDeviceContext->StreamOutPipe = pipe;

                    pipeContext->MaxPacketSize = pipeInfo.MaximumPacketSize;

                }
            }
            else
            {
                pDeviceContext->BulkWritePipe = pipe;

                pipeContext->MaxPacketSize = pipeInfo.MaximumPacketSize;

            }

            continue;
        }

        if ((WdfUsbPipeTypeInterrupt == pipeInfo.PipeType) &&
            WdfUsbTargetPipeIsInEndpoint (pipe))
        {
            pDeviceContext->InterruptPipe = pipe;

            pipeContext->MaxPacketSize = pipeInfo.MaximumPacketSize;

            continue;
        }

    }  


Exit:
    return status;

}
```

The following code example shows a helper routine named, RetrieveStreamInfoFromEndpointDesc, that the client driver calls while enumerating pipes.

In following code example, the client driver calls the preceding helper routine, RetrieveStreamInfoFromEndpointDesc, while enumerating pipes. The routine examines first gets the configuration descriptor and parses it to retrieve endpoint descriptors. If the endpoint descriptor for the pipe contains a USB\_SUPERSPEED\_ENDPOINT\_COMPANION\_DESCRIPTOR\_TYPE descriptor, the driver retrieves the maximum number of streams supported by the endpoint.

```cpp
/*++

Routine Description:

This routine parses the configuration descriptor and finds the endpoint
with which the specified pipe is associated.
It then retrieves the maximum number of streams supported by the endpoint.
It stores maximum number of streams in the pipe context.

Arguments:

Device - WDFUSBDEVICE handle to the target device object. 
The driver obtained that handle in a previous call to
WdfUsbTargetDeviceCreateWithParameters.

Pipe - WDFUSBPIPE handle to the target pipe object.

Return Value:

NTSTATUS
++*/

VOID RetrieveStreamInfoFromEndpointDesc (
    WDFDEVICE Device,
    WDFUSBPIPE Pipe)
{
    PDEVICE_CONTEXT                                 deviceContext                = NULL;
    PUSB_CONFIGURATION_DESCRIPTOR                   configDescriptor             = NULL;
    WDF_USB_PIPE_INFORMATION                        pipeInfo;
    PUSB_COMMON_DESCRIPTOR                          pCommonDescriptorHeader      = NULL;
    PUSB_INTERFACE_DESCRIPTOR                       pInterfaceDescriptor         = NULL;
    PUSB_ENDPOINT_DESCRIPTOR                        pEndpointDescriptor          = NULL;
    PUSB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR   pEndpointCompanionDescriptor = NULL;
    ULONG                                           maxStreams;
    ULONG                                           index;
    BOOLEAN                                         found                        = FALSE;
    UCHAR                                           interfaceNumber = 0;
    UCHAR                                           alternateSetting = 1;
    PPIPE_CONTEXT                                   pipeContext = NULL;
    NTSTATUS                                        status;

    PAGED_CODE();

    deviceContext = GetDeviceContext (Device);

    pipeContext = GetPipeContext (Pipe);


    // Get the configuration descriptor of the currently selected configuration
    status = FX3RetrieveConfigurationDescriptor (
        deviceContext->UsbDevice,
        &deviceContext->ConfigurationNumber,
        &configDescriptor);

    if (!NT_SUCCESS (status))
    {
        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
            "%!FUNC! Could not retrieve the configuration descriptor.");

        status = USBD_STATUS_INAVLID_CONFIGURATION_DESCRIPTOR;

        goto Exit;
    }

    if (deviceContext->ConfigurationNumber == 1)
    {
        alternateSetting = 1;
    }
    else
    {
        alternateSetting = 0;
    }

    // Get the Endpoint Address of the pipe
    WDF_USB_PIPE_INFORMATION_INIT(&pipeInfo);  
    WdfUsbTargetPipeGetInformation (Pipe, &pipeInfo);


    // Parse the ConfigurationDescriptor (including all Interface and
    // Endpoint Descriptors) and locate a Interface Descriptor which
    // matches the InterfaceNumber, AlternateSetting, InterfaceClass,
    // InterfaceSubClass, and InterfaceProtocol parameters.  

    pInterfaceDescriptor = USBD_ParseConfigurationDescriptorEx(
        configDescriptor,
        configDescriptor,
        interfaceNumber,  //Interface number is 0.
        alternateSetting,  // Alternate Setting is 1
        -1, // InterfaceClass, ignore
        -1, // InterfaceSubClass, ignore
        -1  // InterfaceProtocol, ignore
        );

    if (pInterfaceDescriptor == NULL ) 
    {
        // USBD_ParseConfigurationDescriptorEx failed to retrieve Interface Descriptor.
        goto Exit;
    }

    pCommonDescriptorHeader = (PUSB_COMMON_DESCRIPTOR) pInterfaceDescriptor;

    for(index = 0; index < pInterfaceDescriptor->bNumEndpoints; index++) 
    {

        pCommonDescriptorHeader = USBD_ParseDescriptors(
            configDescriptor,
            configDescriptor->wTotalLength,
            pCommonDescriptorHeader,
            USB_ENDPOINT_DESCRIPTOR_TYPE);

        if (pCommonDescriptorHeader == NULL) 
        {
            // USBD_ParseDescriptors failed to retrieve Endpoint Descriptor unexpectedly.
            goto Exit;

        }

        pEndpointDescriptor = (PUSB_ENDPOINT_DESCRIPTOR) pCommonDescriptorHeader;

        // Search an Endpoint Descriptor that matches the EndpointAddress
        if (pEndpointDescriptor->bEndpointAddress == pipeInfo.EndpointAddress)
        {

            found = TRUE;

            break;

        }

        // Skip the current Endpoint Descriptor and search for the next.
        pCommonDescriptorHeader = (PUSB_COMMON_DESCRIPTOR)(((PUCHAR)pCommonDescriptorHeader) 
            + pCommonDescriptorHeader->bLength);

    }

    if (found) 
    {
        // Locate the SuperSpeed Endpoint Companion Descriptor 
        // associated with the endpoint descriptor
        pCommonDescriptorHeader = USBD_ParseDescriptors (
            configDescriptor,
            configDescriptor->wTotalLength,
            pEndpointDescriptor,
            USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR_TYPE);

        if (pCommonDescriptorHeader != NULL) 
        {
            pEndpointCompanionDescriptor = 
                (PUSB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR) pCommonDescriptorHeader;

            maxStreams = pEndpointCompanionDescriptor->bmAttributes.Bulk.MaxStreams;

            if (maxStreams == 0) 
            {

                pipeContext->MaxStreamsSupported = 0;

                pipeContext->IsStreamsCapable = FALSE;
            } 
            else 
            {
                pipeContext->IsStreamsCapable = TRUE;

                pipeContext->MaxStreamsSupported = 1 << maxStreams;

            }

        } 
        else 
        {
            KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, 
                "USBD_ParseDescriptors failed to retrieve SuperSpeed Endpoint Companion Descriptor unexpectedly.\n" ));        
        }

    }
    else
    {
        pipeContext->MaxStreamsSupported = 0;

        pipeContext->IsStreamsCapable = FALSE;
    }

Exit:
    if (configDescriptor)
    {
        ExFreePoolWithTag (configDescriptor, USBCLIENT_TAG);
    }

    return;
}
```

### Getting pipe handles - UMDF client driver

A UMDF client driver uses COM infrastructure and implements COM callback classes that pair with framework device objects. Similar to a KMDF driver, a UMDF client driver can only get pipe information after the device is configured. To get pipe information the client driver must obtain a pointer to the [**IWDFUsbTargetPipe**](https://msdn.microsoft.com/library/windows/hardware/ff560391) interface of the framework interface object that contains the active setting. By using the interface pointer, the driver can enumerate the pipes in that setting to obtain **IWDFUsbTargetPipe** interface pointers exposed by the framework target pipe objects.

Before the driver starts enumerating the pipes, the driver must know about the device configuration and the supported endpoints. Based on that information, the driver can store pipe objects as class member variables.

The following code example extends the USB UMDF template that is provided with Visual Studio Professional 2012. For an explanation of the starter code, see "[**IPnpCallbackHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556764) implementation and USB-specific tasks" in [Understanding the USB client driver code structure (UMDF)](understanding-the-umdf-template-code-for-usb.md).

Extend the CDevice class declaration as shown here. This example code assumes that the device is the OSR FX2 board. For information about its descriptor layout, see [USB Device Layout](usb-device-layout.md).

```cpp
class CMyDevice :
    public CComObjectRootEx<CComMultiThreadModel>,
    public IPnpCallbackHardware
{

public:

    DECLARE_NOT_AGGREGATABLE(CMyDevice)

    BEGIN_COM_MAP(CMyDevice)
        COM_INTERFACE_ENTRY(IPnpCallbackHardware)
    END_COM_MAP()

    CMyDevice() :
        m_FxDevice(NULL),
        m_IoQueue(NULL),
        m_FxUsbDevice(NULL)
    {
    }

    ~CMyDevice()
    {
    }

private:

    IWDFDevice *            m_FxDevice;

    CMyIoQueue *            m_IoQueue;

    IWDFUsbTargetDevice *   m_FxUsbDevice;

    IWDFUsbInterface *      m_pIUsbInterface;  //Pointer to the target interface object.

    IWDFUsbTargetPipe *     m_pIUsbInputPipe;  // Pointer to the target pipe object for the bulk IN endpoint.

    IWDFUsbTargetPipe *     m_pIUsbOutputPipe; // Pointer to the target pipe object for the bulk OUT endpoint.

    IWDFUsbTargetPipe *     m_pIUsbInterruptPipe; // Pointer to the target pipe object for the interrupt endpoint.

private:

    HRESULT
    Initialize(
        __in IWDFDriver *FxDriver,
        __in IWDFDeviceInitialize *FxDeviceInit
        );

public:

    static
    HRESULT
    CreateInstanceAndInitialize(
        __in IWDFDriver *FxDriver,
        __in IWDFDeviceInitialize *FxDeviceInit,
        __out CMyDevice **Device
        );

    HRESULT
    Configure(
        VOID
        );

    HRESULT                     // Declare a helper function to enumerate pipes.
    ConfigureUsbPipes(  
        );
public:

    // IPnpCallbackHardware methods

    virtual
    HRESULT
    STDMETHODCALLTYPE
    OnPrepareHardware(
            __in IWDFDevice *FxDevice
            );

    virtual
    HRESULT
    STDMETHODCALLTYPE
    OnReleaseHardware(
        __in IWDFDevice *FxDevice
        );

};
```

In the CDevice class definition, implement a helper method called CreateUsbIoTargets. This method is called from the IPnpCallbackHardware::OnPrepareHardware implementation after the driver has obtained a pointer to the target device object.

```cpp

HRESULT  CMyDevice::CreateUsbIoTargets()  

    HRESULT                 hr;  
    UCHAR                   NumEndPoints = 0;  

    IWDFUsbInterface *      pIUsbInterface = NULL;  
    IWDFUsbTargetPipe *     pIUsbPipe = NULL;  


    if (SUCCEEDED(hr))   
    {  
        UCHAR NumInterfaces = pIUsbTargetDevice->GetNumInterfaces();  

        WUDF_TEST_DRIVER_ASSERT(1 == NumInterfaces);  

        hr = pIUsbTargetDevice->RetrieveUsbInterface(0, &pIUsbInterface);  
        if (FAILED(hr))  
        {  
            TraceEvents(TRACE_LEVEL_ERROR,   
                        TEST_TRACE_DEVICE,   
                        "%!FUNC! Unable to retrieve USB interface from USB Device I/O Target %!HRESULT!",  
                        hr  
                        );          
        }  
        else  
        {  
            m_pIUsbInterface = pIUsbInterface;  

            DriverSafeRelease (pIUsbInterface); //release creation reference                                
        }
     }  

    if (SUCCEEDED(hr))   
    {  
        NumEndPoints = pIUsbInterface->GetNumEndPoints();  

        if (NumEndPoints != NUM_OSRUSB_ENDPOINTS) 
        {  
            hr = E_UNEXPECTED;  
            TraceEvents(TRACE_LEVEL_ERROR,   
                        TEST_TRACE_DEVICE,   
                        "%!FUNC! Has %d endpoints, expected %d, returning %!HRESULT! ",   
                        NumEndPoints,  
                        NUM_OSRUSB_ENDPOINTS,  
                        hr  
                        );  
        }  
    }  

    if (SUCCEEDED(hr))   
    {  
        for (UCHAR PipeIndex = 0; PipeIndex < NumEndPoints; PipeIndex++)  
        {  
            hr = pIUsbInterface->RetrieveUsbPipeObject(PipeIndex,   
                                                  &pIUsbPipe);  

            if (FAILED(hr))  
            {  
                TraceEvents(TRACE_LEVEL_ERROR,   
                            TEST_TRACE_DEVICE,   
                            "%!FUNC! Unable to retrieve USB Pipe for PipeIndex %d, %!HRESULT!",  
                            PipeIndex,  
                            hr  
                            );          
            }  
            else  
            {  
                if ( pIUsbPipe->IsInEndPoint() )  
                {  
                    if ( UsbdPipeTypeInterrupt == pIUsbPipe->GetType() )  
                    {  
                        m_pIUsbInterruptPipe = pIUsbPipe;  
                    }  
                    else if ( UsbdPipeTypeBulk == pIUsbPipe->GetType() )  
                    {  
                        m_pIUsbInputPipe = pIUsbPipe;  
                    }  
                    else  
                    {  
                        pIUsbPipe->DeleteWdfObject();  
                    }                        
                }  
                else if ( pIUsbPipe->IsOutEndPoint() && (UsbdPipeTypeBulk == pIUsbPipe->GetType()) )  
                {  
                    m_pIUsbOutputPipe = pIUsbPipe;  
                }  
                else  
                {  
                    pIUsbPipe->DeleteWdfObject();  
                }  

                DriverSafeRelease(pIUsbPipe);  //release creation reference
            }  
        }  

        if (NULL == m_pIUsbInputPipe || NULL == m_pIUsbOutputPipe)  
        {  
            hr = E_UNEXPECTED;  
            TraceEvents(TRACE_LEVEL_ERROR,   
                        TEST_TRACE_DEVICE,   
                        "%!FUNC! Input or output pipe not found, returning %!HRESULT!",  
                        hr  
                        );          
        }  
    }  

    return hr;  
}  
```

In UMDF, the client driver uses a pipe index to send data transfer requests. A pipe index is a number assigned by the USB driver stack when it opens pipes for the endpoints in a setting. To obtain the pipe index, call the[**IWDFUsbTargetPipe::GetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff560403) method. The method populates a [**WINUSB\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540285) structure. The **PipeId** value indicates the pipe index.

One way of performing read and write operations on the target pipe is to call [**IWDFUsbInterface::GetWinUsbHandle**](https://msdn.microsoft.com/library/windows/hardware/ff560337) to obtain a WinUSB handle and then call [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb). For example, the driver can call the [**WinUsb\_ReadPipe**](https://msdn.microsoft.com/library/windows/hardware/ff540297) or [**WinUsb\_WritePipe**](https://msdn.microsoft.com/library/windows/hardware/ff540322) function. In those function calls, the driver must specify the pipe index. For more information, see [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md).

Remarks
-------

### Pipe handles for WDM-based client drivers

After a configuration is selected, the USB driver stack sets up a pipe to each of the device's endpoints. The USB driver stack returns an array of [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) structures. The number of elements in the array depends on the number of endpoints defined for the active alternate setting of an interface in the selected configuration. Each element contains information about the pipe created for a particular endpoint. For more information about obtaining pipe handles, see [How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md).

To build an I/O transfer request, the client driver must have a handle to the pipe associated with that endpoint. The client driver can obtain the pipe handle from the **PipeHandle** member of [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) in the array.

In addition to the pipe handle, the client driver also requires the pipe type. The client driver can determine the pipe type by examining the **PipeType** member.

Based on the endpoint type, the USB driver stack supports different types of pipes. The client driver can determine the pipe type by examining the **PipeType** member of [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114). The different pipe types require different types of USB request blocks (URBs) to perform I/O transactions.

The client driver then submits the URB to the USB driver stack. The USB driver stack processes the request and sends the specified data to the requested target pipe.

The URB contains information about the request such as the target pipe handle, transfer buffer, and its length. Each structure within the [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) union shares certain members: **TransferFlags**, **TransferBuffer**, **TransferBufferLength**, and **TransferBufferMDL**. There are type-specific flags in the **TransferFlags** member that correspond to each URB type. For all data transfer URBs, the USBD\_TRANSFER\_DIRECTION\_IN flag in **TransferFlags** specifies the direction of the transfer. Client drivers set the USBD\_TRANSFER\_DIRECTION\_IN flag to read data from the device. Drivers clear this flag to send data to the device. Data may be read from or written to either a buffer resident in memory or an MDL. In either case, the driver specifies the size of the buffer in the **TransferBufferLength** member. The driver provides a resident buffer in the **TransferBuffer** member and an MDL in the **TransferBufferMDL** member. Whichever one the driver provides, the other must be NULL.

## Related topics
[USB I/O Transfers](usb-device-i-o.md)  
[How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md)  
[How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md)  
[Common tasks for USB client drivers](wdk-resources-for-usb-driver-development.md)  



