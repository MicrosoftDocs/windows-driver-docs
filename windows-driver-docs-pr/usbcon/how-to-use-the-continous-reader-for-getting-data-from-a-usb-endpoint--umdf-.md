---
Description: This topic describes the WDF-provided continuous reader object. The procedures in this topic provide step-by-step instructions about how to configure the object and use it to read data from a USB pipe.
title: How to use the continuous reader for reading data from a USB pipe
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to use the continuous reader for reading data from a USB pipe


This topic describes the WDF-provided continuous reader object. The procedures in this topic provide step-by-step instructions about how to configure the object and use it to read data from a USB pipe.

Windows Driver Framework (WDF) provides a specialized object called the *continuous reader*. This object enables a USB client driver to read data from bulk and interrupt endpoints continuously, as long as there is data available. In order to use the reader, the client driver must have a handle to a USB target pipe object that is associated with the endpoint from which the driver reads data. The endpoint must be in the active configuration. You can make a configuration active in one of two ways: by selecting a USB configuration or by changing the alternate setting in the current configuration. For more information about those operations, see [How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md) and [How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md).

After creating the continuous reader, the client driver can start and stop the reader as and when necessary. The continuous reader that ensures that a read request is always available on the target pipe object and the client driver is always ready to receive data from the endpoint.

The continuous reader is not automatically power managed by the framework. This means that the client driver must stop the reader when the device enters a lower power state and restart the reader when the device enters working state.

## What you need to know


### Technologies

-   [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)
-   [User-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)

### Prerequisites

Before the client driver can use the continuous reader, make sure that these requirements are met:

-   Your USB device must have an IN endpoint. Check the device configuration in [USBView](https://msdn.microsoft.com/library/ff560019(VS.85).aspx). Usbview.exe is an application that allows you to browse all USB controllers and the USB devices connected to them. Typically, USBView is installed in the **Debuggers** folder in the Windows Driver Kit (WDK).
-   The client driver must have created the framework USB target device object.

    If you are using the USB templates that are provided with Microsoft Visual Studio Professional 2012, the template code performs those tasks. The template code obtains the handle to the target device object and stores in the device context.

    **KMDF client driver:**

    A KMDF client driver must obtain a WDFUSBDEVICE handle by calling the [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428) method. For more information, see "Device source code" in [Understanding the USB client driver code structure (KMDF)](understanding-the-kmdf-template-code-for-usb.md).

    **UMDF client driver:**

    A UMDF client driver must obtain an [**IWDFUsbTargetDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560362) pointer by querying the framework target device object. For more information, see "[**IPnpCallbackHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556764) implementation and USB-specific tasks" in [Understanding the USB client driver code structure (UMDF)](understanding-the-umdf-template-code-for-usb.md).

-   The device must have an active configuration.

    If you are using USB templates, the code selects the first configuration and the default alternate setting in each interface. For information about how to change the alternate setting, see [How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md).

    **KMDF client driver:**

    A KMDF client driver must call the [**WdfUsbTargetDeviceSelectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff550101) method.

    **UMDF client driver:**

    For a UMDF client driver, the framework selects the first configuration and the default alternate setting for each interface in that configuration.

-   The client driver must have a handle to the framework target pipe object for the IN endpoint. For more information, see [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md).

Instructions
------------

### Using the continuous reader - KMDF client driver

1.  Configure the continuous reader.

    1.  Initialize a [**WDF\_USB\_CONTINUOUS\_READER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552561) structure by calling the [**WDF\_USB\_CONTINUOUS\_READER\_CONFIG\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552561_init) macro.
    2.  Specify its configuration options in the [**WDF\_USB\_CONTINUOUS\_READER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552561) structure.
    3.  Call the [**WdfUsbTargetPipeConfigContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff551130) method.

    The following example code configures the continuous reader for the specified target pipe object.

    ```cpp
    NTSTATUS FX3ConfigureContinuousReader(
        _In_ WDFDEVICE Device,
        _In_ WDFUSBPIPE Pipe)
    {
        NTSTATUS status;

        PDEVICE_CONTEXT                     pDeviceContext;       

        WDF_USB_CONTINUOUS_READER_CONFIG    readerConfig;

        PPIPE_CONTEXT                       pipeContext;  

        PAGED_CODE();

        pDeviceContext = WdfObjectGet_DEVICE_CONTEXT(Device);

        pipeContext = GetPipeContext (Pipe);

        WDF_USB_CONTINUOUS_READER_CONFIG_INIT(  
            &readerConfig,  
            FX3EvtReadComplete,  
            pDeviceContext,  
            pipeContext->MaxPacketSize);  

        readerConfig.EvtUsbTargetPipeReadersFailed=FX3EvtReadFailed;  

        status = WdfUsbTargetPipeConfigContinuousReader(  
            Pipe,  
            &readerConfig);  

        if (!NT_SUCCESS (status))
        {
            TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
                "%!FUNC! WdfUsbTargetPipeConfigContinuousReader failed 0x%x", status);

            goto Exit;
        }


    Exit:
        return status;
    }
    ```

Typically the client driver configures the continuous reader in the [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function after enumerating the target pipe objects in the active setting.

In the preceding example, the client driver specifies its configuration options in two ways. First by calling [**WDF\_USB\_CONTINUOUS\_READER\_CONFIG\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552566) and then by setting [**WDF\_USB\_CONTINUOUS\_READER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552561) members. Notice the parameters for **WDF\_USB\_CONTINUOUS\_READER\_CONFIG\_INIT**. These values are mandatory. In this example, the client driver specifies:

-   A pointer to a completion routine that the driver implements. The framework calls this routine when it completes a read request. In the completion routine, the driver can access the memory location that contains the data that was read. The implementation of the completion routine is discussed in step 2.
-   A pointer to the driver-defined context.
-   The number of bytes that can be read from the device in a single transfer. The client driver can obtain that information in a [**WDF\_USB\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff553037) structure by calling [**WdfUsbInterfaceGetConfiguredPipe**](https://msdn.microsoft.com/library/windows/hardware/ff550057)or [**WdfUsbTargetPipeGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff551142) method. For more information, see [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md).

[**WDF\_USB\_CONTINUOUS\_READER\_CONFIG\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552566) configures the continuous reader to use the default value for *NumPendingReads*. That value determines the number of read requests that the framework adds to the pending queue. The default value has been determined to provide reasonably good performance for many devices on many processor configurations.

In addition to the configuration parameters specified in [**WDF\_USB\_CONTINUOUS\_READER\_CONFIG\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552566), the example also sets a failure routine in [**WDF\_USB\_CONTINUOUS\_READER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552561). This failure routine is optional.

In addition to the failure routine, there are other members in [**WDF\_USB\_CONTINUOUS\_READER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552561) that the client driver can use to specify the layout of the transfer buffer. For example, consider a network driver that uses the continuous reader to receive network packets. Each packet contains header, payload, and footer data. To describe the packet, the driver must first specify the size of the packet in its call to [**WDF\_USB\_CONTINUOUS\_READER\_CONFIG\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552561_init). Then, the driver must specify the length of the header and footer by setting **HeaderLength** and **TrailerLength** members of **WDF\_USB\_CONTINUOUS\_READER\_CONFIG**. The framework uses those values to calculate the byte offsets on either side of the payload. When payload data is read from the endpoint, the framework stores that data in the part of the buffer between the offsets.

2.  Implement the completion routine.

    The framework invokes the client-driver implemented completion routine each time a request is completed. The framework passes the number of bytes read and a WDFMEMORY object whose buffer contains the data that is read from the pipe.

    The following example code shows the completion routine implementation.

    ```cpp
    EVT_WDF_USB_READER_COMPLETION_ROUTINE FX3EvtReadComplete;

    VOID FX3EvtReadComplete(
        __in  WDFUSBPIPE Pipe,
        __in  WDFMEMORY Buffer,
        __in  size_t NumBytesTransferred,
        __in  WDFCONTEXT Context
        )
    {

        PDEVICE_CONTEXT  pDeviceContext;  
        PVOID  requestBuffer;    

        pDeviceContext = (PDEVICE_CONTEXT)Context;

        if (NumBytesTransferred == 0)
        {
            return;
        }

        requestBuffer = WdfMemoryGetBuffer(Buffer, NULL);

        if (Pipe == pDeviceContext->InterruptPipe)
        {
            KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL,
                                    "Interrupt endpoint: %s.\n", 
                                    requestBuffer )); 
        }


        return;
    }

    ```

The framework invokes the client-driver implemented completion routine each time a request is completed. The framework allocates a memory object for each read operation. In the completion routine, the framework passes the number of bytes read and a WDFMEMORY handle to the memory object. The memory object buffer contains the data that is read from the pipe. The client driver must not free the memory object. The framework releases the object after each completion routine returns. If the client driver wants to store the received data, the driver must copy the contents of the buffer in the completion routine.

3.  Implement the failure routine.

    The framework invokes the client-driver implemented failure routine to inform the driver that the continuous reader has reported an error while processing a read request. The framework passes the pointer to the target pipe object on which the request failed and error code values. Based on those error code values the driver can implement its error recovery mechanism. The driver must also return an appropriate value that indicates to the framework whether the framework should restart the continuous reader.

    The following example code shows a failure routine implementation.

    ```cpp
    EVT_WDF_USB_READERS_FAILED FX3EvtReadFailed;  

    BOOLEAN  
    FX3EvtReadFailed(  
        WDFUSBPIPE      Pipe,  
        NTSTATUS        Status,  
        USBD_STATUS     UsbdStatus  
        )  
    {      
        UNREFERENCED_PARAMETER(Status);  

        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
                "%!FUNC! ReadersFailedCallback failed NTSTATUS 0x%x, UsbdStatus 0x%x\n", 
                     status,
                     UsbdStatus);

        return TRUE;  
    }  
    ```

In the preceding example, the driver returns TRUE. This value indicates to the framework that it must reset the pipe and then restart the continuous reader.

Alternatively, the client driver can return FALSE and provide an error recovery mechanism if a stall condition occurs on the pipe. For example, the driver can check the USBD status and issue a reset-pipe request to clear the stall condition.

For information about error recovery in pipes, see [How to recover from USB pipe errors](how-to-recover-from-usb-pipe-errors.md).

4.  Instruct the framework to start the continuous reader when the device enters working state; stop the reader when the device leaves working state. Call these methods and specify the target pipe object as the I/O target object.

    -   [**WdfIoTargetStart**](https://msdn.microsoft.com/library/windows/hardware/ff548677)
    -   [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680)

    The continuous reader is not automatically power managed by the framework. Therefore, the client driver must explicitly start or stop the target pipe object when the power state of the device changes. The driver calls [**WdfIoTargetStart**](https://msdn.microsoft.com/library/windows/hardware/ff548677) in the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) implementation. This call ensures that the queue delivers requests only when the device is in working state. Conversely, the driver calls [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680) in the drivers [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) implementation so that the queue stops delivering requests when the device enters a lower power state.

The following example code configures the continuous reader for the specified target pipe object.

```cpp

EVT_WDF_DEVICE_D0_ENTRY FX3EvtDeviceD0Entry;

NTSTATUS FX3EvtDeviceD0Entry(
    __in  WDFDEVICE Device,
    __in  WDF_POWER_DEVICE_STATE PreviousState
    )
{
    PDEVICE_CONTEXT  pDeviceContext;

    NTSTATUS status;

    PAGED_CODE();

    pDeviceContext = WdfObjectGet_DEVICE_CONTEXT(Device);


    status = WdfIoTargetStart (WdfUsbTargetPipeGetIoTarget (pDeviceContext->InterruptPipe));

    if (!NT_SUCCESS (status))
    {
        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE, 
            "%!FUNC! Could not start interrupt pipe failed 0x%x", status);
    }

}

EVT_WDF_DEVICE_D0_EXIT FX3EvtDeviceD0Exit;

NTSTATUS FX3EvtDeviceD0Exit(
    __in  WDFDEVICE Device,
    __in  WDF_POWER_DEVICE_STATE TargetState
    )
{
    PDEVICE_CONTEXT  pDeviceContext;      

    NTSTATUS status;

    PAGED_CODE();

    pDeviceContext = WdfObjectGet_DEVICE_CONTEXT(Device);


    WdfIoTargetStop (WdfUsbTargetPipeGetIoTarget (pDeviceContext->InterruptPipe), WdfIoTargetCancelSentIo));

}
```

The preceding example shows the implementation for [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) and [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback routines. The Action parameter of [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680) allows the client driver to decide the action for the pending requests in the queue when the device leaves working state. In the example, the driver specifies **WdfIoTargetCancelSentIo**. That option instructs the framework to cancel all pending requests in the queue. Alternatively, the driver can instruct the framework to wait for pending requests to get completed before stopping the I/O target or keep the pending requests and resume when the I/O target restarts.

### Using the continuous reader - UMDF client driver

Before you start using the continuous reader, you must configure the reader in your implementation of [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766) method. After you get a pointer to [**IWDFUsbTargetPipe**](https://msdn.microsoft.com/library/windows/hardware/ff560391) interface of the target pipe object associated with the IN endpoint, perform these steps:

**Configure the continuous reader**

1.  Call **QueryInterface** on the target pipe object ([**IWDFUsbTargetPipe**](https://msdn.microsoft.com/library/windows/hardware/ff560391)) and query for the [**IWDFUsbTargetPipe2**](https://msdn.microsoft.com/library/windows/hardware/ff560394) interface.
2.  Call **QueryInterface** on the device callback object and query for the [**IUsbTargetPipeContinuousReaderCallbackReadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff556908) interface. In order to use the continuous reader, you must implement IUsbTargetPipeContinuousReaderCallbackReadComplete. The implementation is described later in this topic.
3.  Call **QueryInterface** on the device callback object and query for the [IUsbTargetPipeContinuousReaderCallbackReadersFailed](https://msdn.microsoft.com/library/windows/hardware/ff556914) interface if you have implemented a failure callback. The implementation is described later in this topic.
4.  Call the [**IWDFUsbTargetPipe2::ConfigureContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff560395) method and specify the configuration parameters, such as header, trailer, number of pending requests, and references to the completion and failure callback methods.

    The method configures the continuous reader for the target pipe object. The continuous reader creates queues that manage a set of read requests as they are sent and received from the target pipe object.

The following example code configures the continuous reader for the specified target pipe object. The example assumes that the target pipe object specified by the caller is associated with an IN endpoint. The continuous reader is configured to read USBD\_DEFAULT\_MAXIMUM\_TRANSFER\_SIZE bytes; to use the default number of pending requests using by the framework; to invoke the client driver-supplied completion and failure callback methods. Buffer received will not contain any header or trailer data.

```cpp
HRESULT CDeviceCallback::ConfigureContinuousReader (IWDFUsbTargetPipe* pFxPipe)
{
    if (!pFxPipe)
    {
        return E_INVALIDARG;
    }

    IUsbTargetPipeContinuousReaderCallbackReadComplete *pOnCompletionCallback = NULL;
    IUsbTargetPipeContinuousReaderCallbackReadersFailed *pOnFailureCallback = NULL;
    IWDFUsbTargetPipe2* pFxUsbPipe2 = NULL;

    HRESULT hr = S_OK;

    // Set up the continuous reader to read from the target pipe object.

    //Get a pointer to the target pipe2 object.
    hr = pFxPipe->QueryInterface(IID_PPV_ARGS(&pFxUsbPipe2));
    if (FAILED(hr))
    {   
        goto ConfigureContinuousReaderExit;
    }

    //Get a pointer to the completion callback.
    hr = QueryInterface(IID_PPV_ARGS(&pOnCompletionCallback));
    if (FAILED(hr))
    {   
        goto ConfigureContinuousReaderExit;
    }

    //Get a pointer to the failure callback.
    hr = QueryInterface(IID_PPV_ARGS(&pOnFailureCallback));
    if (FAILED(hr))
    {   
        goto ConfigureContinuousReaderExit;
    }

    //Get a pointer to the target pipe2 object.
    hr = pFxUsbPipe2->ConfigureContinuousReader (    
        USBD_DEFAULT_MAXIMUM_TRANSFER_SIZE, //size of data to be read
        0, //Header
        0, //Trailer
        0, // Number of pending requests queued by WDF
        NULL, // Cleanup callback. Not provided.
        pOnCompletionCallback, //Completion routine.
        NULL, //Completion routine context. Not provided.
        pOnFailureCallback); //Failure routine. Not provided

    if (FAILED(hr))
    {   
        goto ConfigureContinuousReaderExit;
    }

ConfigureContinuousReaderExit:

    if (pOnFailureCallback)
    {
        pOnFailureCallback->Release();
        pOnFailureCallback = NULL;
    }

    if (pOnCompletionCallback)
    {
        pOnCompletionCallback->Release();
        pOnCompletionCallback = NULL;
    }

    if (pFxUsbPipe2)
    {
        pFxUsbPipe2->Release();
        pFxUsbPipe2 = NULL;
    }

    return hr;
}
```

Next, specify the state of the target pipe object, when the device enters and exits a working state (**D0**).

If a client driver uses a power-managed queue to send requests to a pipe, the queue delivers requests only when the device is in the **D0** state. If the power state of the device changes from **D0** to a lower power state (on **D0** exit), the target pipe object completes the pending requests and the queue stops submitting requests to the target pipe object. Therefore, the client driver is not required to start and stop the target pipe object.

The continuous reader does not use power-managed queues to submit requests. Therefore, you must explicitly start or stop the target pipe object when the power state of the device changes. For changing the state of the target pipe object, you can use the [**IWDFIoTargetStateManagement**](https://msdn.microsoft.com/library/windows/hardware/ff559198) interface implemented by the framework. After you get a pointer to [**IWDFUsbTargetPipe**](https://msdn.microsoft.com/library/windows/hardware/ff560391) interface of the target pipe object associated with the IN endpoint, perform the following steps:

**Implement state management**

1.  In your implementation of [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766), call[**QueryInterface** on the target pipe object ([**IWDFUsbTargetPipe**](https://msdn.microsoft.com/library/windows/hardware/ff560391)) and query for the [**IWDFIoTargetStateManagement**](https://msdn.microsoft.com/library/windows/hardware/ff559198) interface. Store the reference in a member variable of your device callback class.
2.  Implement the [**IPnpCallback**](https://msdn.microsoft.com/library/windows/hardware/ff556762) interface on the device callback object.
3.  In the implementation of the [**IPnpCallback::OnD0Entry**](https://msdn.microsoft.com/library/windows/hardware/ff556799) method, call [**IWDFIoTargetStateManagement::Start**](https://msdn.microsoft.com/library/windows/hardware/ff559213) to start the continuous reader.
4.  In the implementation of the [**IPnpCallback::OnD0Exit**](https://msdn.microsoft.com/library/windows/hardware/ff556803) method, call [**IWDFIoTargetStateManagement::Stop**](https://msdn.microsoft.com/library/windows/hardware/ff559217) to stop the continuous reader.

After the device enters a working state (**D0**), the framework calls the client-driver supplied D0-entry callback method that starts the target pipe object. When the device leaves the **D0** state, the framework calls the D0-exit callback method. The target pipe object completes the number of pending read requests, configured by the client driver, and stops accepting new requests.
The following example code implements the [IPnpCallback](https://msdn.microsoft.com/library/windows/hardware/ff556762) interface on the device callback object.

```cpp
class CDeviceCallback : 
    public IPnpCallbackHardware, 
    public IPnpCallback,
{
public:
    CDeviceCallback();
    ~CDeviceCallback();
    virtual HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, VOID** ppvObject);
    virtual ULONG STDMETHODCALLTYPE AddRef();
    virtual ULONG STDMETHODCALLTYPE Release();

    virtual HRESULT STDMETHODCALLTYPE OnPrepareHardware(IWDFDevice* pDevice);
    virtual HRESULT STDMETHODCALLTYPE OnReleaseHardware(IWDFDevice* pDevice); 

    virtual HRESULT STDMETHODCALLTYPE OnD0Entry(IWDFDevice*  pWdfDevice, WDF_POWER_DEVICE_STATE  previousState);
    virtual HRESULT STDMETHODCALLTYPE OnD0Exit(IWDFDevice*  pWdfDevice, WDF_POWER_DEVICE_STATE  previousState);
    virtual void STDMETHODCALLTYPE OnSurpriseRemoval(IWDFDevice*  pWdfDevice);
    virtual HRESULT STDMETHODCALLTYPE OnQueryRemove(IWDFDevice*  pWdfDevice);
    virtual HRESULT STDMETHODCALLTYPE OnQueryStop(IWDFDevice*  pWdfDevice);    

private:
    LONG m_cRefs;
    IWDFUsbTargetPipe* m_pFxUsbPipe;
    IWDFIoTargetStateManagement* m_pFxIoTargetInterruptPipeStateMgmt;

    HRESULT CreateUSBTargetDeviceObject (IWDFDevice* pFxDevice, IWDFUsbTargetDevice** ppUSBTargetDevice);
    HRESULT ConfigureContinuousReader (IWDFUsbTargetPipe* pFxPipe);
};
```

The following example code shows how to get a pointer to the IWDFIoTargetStateManagement interface of the target pipe object in the IPnpCallback::OnPrepareHardware method

```cpp
   //Enumerate the endpoints and get the interrupt pipe.

    for (UCHAR index = 0; index < NumEndpoints; index++)
    {
        hr = pFxInterface->RetrieveUsbPipeObject(index, &pFxPipe);

        if (SUCCEEDED (hr) && pFxPipe)
        {
            if ((pFxPipe->IsInEndPoint()) && (pFxPipe->GetType()==UsbdPipeTypeInterrupt))
            {
                //Pipe is for an interrupt IN endpoint.

                hr = pFxPipe->QueryInterface(IID_PPV_ARGS(&m_pFxIoTargetInterruptPipeStateMgmt));

                if (m_pFxIoTargetInterruptPipeStateMgmt)
                {               
                    m_pFxUsbPipe = pFxPipe;

                    break;
                }

            }
            else
            {
                //Pipe is NOT for an interrupt IN endpoint.

                pFxPipe->Release();
                pFxPipe = NULL;
            }
        }
        else
        {
             //Pipe not found.
        }
    }
```

The following example code shows how to get a pointer to the [**IWDFIoTargetStateManagement**](https://msdn.microsoft.com/library/windows/hardware/ff559198) interface of the target pipe object in the [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766) method.

```cpp
 HRESULT CDeviceCallback::OnD0Entry(
    IWDFDevice*  pWdfDevice,
    WDF_POWER_DEVICE_STATE  previousState
    )
{

    if (!m_pFxIoTargetInterruptPipeStateMgmt)
    {
        return E_FAIL;
    }

    HRESULT hr = m_pFxIoTargetInterruptPipeStateMgmt->Start();

    if (FAILED (hr))
    {
        goto OnD0EntryExit;
    }

OnD0EntryExit:
    return hr;
}

HRESULT CDeviceCallback::OnD0Exit(
    IWDFDevice*  pWdfDevice,
    WDF_POWER_DEVICE_STATE  previousState
    )
{
    if (!m_pFxIoTargetInterruptPipeStateMgmt)
    {
        return E_FAIL;
    }

    // Stop the I/O target always succeeds.

    (void)m_pFxIoTargetInterruptPipeStateMgmt->Stop(WdfIoTargetCancelSentIo);

    return S_OK;
}
```

After the continuous reader completes a read request, the client driver must provide a way to get notified when the request completes a read request successfully. The client driver must add this code to the device callback object.

**Provide a completion callback by implementing IUsbTargetPipeContinuousReaderCallbackReadComplete**

1.  Implement the [**IUsbTargetPipeContinuousReaderCallbackReadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff556908) interface on the device callback object.
2.  Make sure the **QueryInterface** implementation of the device callback object increments the reference count of the callback object and then returns the [**IUsbTargetPipeContinuousReaderCallbackReadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff556908) interface pointer.
3.  In the implementation of the [**IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556910) method, access the data read that was read from the pipe. The *pMemory* parameter points to the memory allocated by the framework that contains the data. You can call [**IWDFMemory::GetDataBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff562631) to get the buffer that contains the data. The buffer includes the header however the length of data indicated by the *NumBytesTransferred* parameter of **OnReaderCompletion** does not include the header length. The header length is specified by the client driver while configuring the continuous reader in the driver's call to [**IWDFUsbTargetPipe2::ConfigureContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff560395).
4.  Supply a pointer to the completion callback in the *pOnCompletion* parameter of the [**IWDFUsbTargetPipe2::ConfigureContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff560395) method.

Each time that data is available on the endpoint on the device, the target pipe object completes a read request. If the read request completed successfully, the framework notifies the client driver by calling [**IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556910). Otherwise, the framework calls a client driver-supplied failure callback when the target pipe object reports an error on the read request.

The following example code implements the [**IUsbTargetPipeContinuousReaderCallbackReadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff556908) interface on the device callback object.

```cpp
class CDeviceCallback : 
    public IPnpCallbackHardware, 
    public IPnpCallback,   
    public IUsbTargetPipeContinuousReaderCallbackReadComplete

{
public:
    CDeviceCallback();
    ~CDeviceCallback();
    virtual HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, VOID** ppvObject);
    virtual ULONG STDMETHODCALLTYPE AddRef();
    virtual ULONG STDMETHODCALLTYPE Release();

    virtual HRESULT STDMETHODCALLTYPE OnPrepareHardware(IWDFDevice* pDevice);
    virtual HRESULT STDMETHODCALLTYPE OnReleaseHardware(IWDFDevice* pDevice); 

    virtual HRESULT STDMETHODCALLTYPE OnD0Entry(IWDFDevice*  pWdfDevice, WDF_POWER_DEVICE_STATE  previousState);
    virtual HRESULT STDMETHODCALLTYPE OnD0Exit(IWDFDevice*  pWdfDevice, WDF_POWER_DEVICE_STATE  previousState);
    virtual void STDMETHODCALLTYPE OnSurpriseRemoval(IWDFDevice*  pWdfDevice);
    virtual HRESULT STDMETHODCALLTYPE OnQueryRemove(IWDFDevice*  pWdfDevice);
    virtual HRESULT STDMETHODCALLTYPE OnQueryStop(IWDFDevice*  pWdfDevice);    

    virtual VOID STDMETHODCALLTYPE OnReaderCompletion(IWDFUsbTargetPipe* pPipe, IWDFMemory* pMemory, SIZE_T NumBytesTransferred, PVOID Context);    


private:
    LONG m_cRefs;
    IWDFUsbTargetPipe* m_pFxUsbPipe;
    IWDFIoTargetStateManagement* m_pFxIoTargetInterruptPipeStateMgmt;

    HRESULT CreateUSBTargetDeviceObject (IWDFDevice* pFxDevice, IWDFUsbTargetDevice** ppUSBTargetDevice);
    HRESULT ConfigureContinuousReader (IWDFUsbTargetPipe* pFxPipe);
};
```

The following example code shows the QueryInterface implementation of the device callback object.

```cpp
HRESULT CDeviceCallback::QueryInterface(REFIID riid, LPVOID* ppvObject)
{
    if (ppvObject == NULL)
    {
        return E_INVALIDARG;
    }

    *ppvObject = NULL;

    HRESULT hr = E_NOINTERFACE;

    if(  IsEqualIID(riid, __uuidof(IPnpCallbackHardware))   ||  IsEqualIID(riid, __uuidof(IUnknown))  )
    {  
        *ppvObject = static_cast<IPnpCallbackHardware*>(this);
        reinterpret_cast<IUnknown*>(*ppvObject)->AddRef();
        hr = S_OK;

    }

    if(  IsEqualIID(riid, __uuidof(IPnpCallback)))
    {  
        *ppvObject = static_cast<IPnpCallback*>(this);
        reinterpret_cast<IUnknown*>(*ppvObject)->AddRef();
        hr = S_OK;

    }

    if(  IsEqualIID(riid, __uuidof(IUsbTargetPipeContinuousReaderCallbackReadComplete)))
    {  
        *ppvObject = static_cast<IUsbTargetPipeContinuousReaderCallbackReadComplete*>(this);
        reinterpret_cast<IUnknown*>(*ppvObject)->AddRef();
        hr = S_OK;

    }

    return hr;
}
```

The following example code shows how to get data from the buffer returned by [**IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556910). Each time the target pipe object completes a read request successfully, the framework calls **OnReaderCompletion**. The example gets the buffer that containsng data and prints the contents on the debugger output.

```cpp
 VOID CDeviceCallback::OnReaderCompletion(
    IWDFUsbTargetPipe* pPipe,
    IWDFMemory* pMemory,
    SIZE_T NumBytesTransferred,
    PVOID Context)
{        
    if (pPipe != m_pFxUsbInterruptPipe)
    {
        return;
    }

    if (NumBytesTransferred == 0) 
    {
        // NumBytesTransferred is zero.

        return;
    }

    PVOID pBuff = NULL;
    LONG CurrentData = 0;
    char data[20];

    pBuff = pMemory->GetDataBuffer(NULL);

    if (pBuff)
    {
        CopyMemory(&CurrentData, pBuff, sizeof(CurrentData));
        sprintf_s(data, 20, "%d\n", CurrentData);
        OutputDebugString(data);
        pBuff = NULL;
    }
    else
    {
        OutputDebugString(TEXT("Unable to get data buffer."));
    }
}
```

The client driver can get notifications from the framework when a failure occurs in the target pipe object while completing a read request. To get notifications, the client driver must implement a failure callback and supply a pointer to the callback while configuring the continuous reader. The following procedure describes how to implement the failure callback.

**Provide a failure callback by implementing IUsbTargetPipeContinuousReaderCallbackReadersFailed**

1.  Implement the [**IUsbTargetPipeContinuousReaderCallbackReadersFailed**](https://msdn.microsoft.com/library/windows/hardware/ff556914) interface on the device callback object.
2.  Make sure the **QueryInterface** implementation of the device callback object increments the reference count of the callback object and then returns the [**IUsbTargetPipeContinuousReaderCallbackReadersFailed**](https://msdn.microsoft.com/library/windows/hardware/ff556914) interface pointer.
3.  In the implementation of the [**IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure**](https://msdn.microsoft.com/library/windows/hardware/ff556915) method, provide error handling of the failed read request.

    If the continuous reader fails to complete a read request and the client driver provides a failure callback, the framework invokes the [**IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure**](https://msdn.microsoft.com/library/windows/hardware/ff556915) method. The framework provides an HRESULT value in the *hrStatus* parameter that indicates the error code that occurred in the target pipe object. Based on that error code you might provide certain error handling. For example, if you want the framework to reset the pipe and then restart the continuous reader, make sure that the callback returns TRUE.

    **Note**  Do not call [**IWDFIoTargetStateManagement::Start**](https://msdn.microsoft.com/library/windows/hardware/ff559213) and [**IWDFIoTargetStateManagement::Stop**](https://msdn.microsoft.com/library/windows/hardware/ff559217) within the failure callback.



4.  Supply a pointer to the failure callback in the *pOnFailure* parameter of the [**IWDFUsbTargetPipe2::ConfigureContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff560395) method.

The following example code implements the [**IUsbTargetPipeContinuousReaderCallbackReadersFailed**](https://msdn.microsoft.com/library/windows/hardware/ff556914) interface on the device callback object.

```cpp
class CDeviceCallback : 
    public IPnpCallbackHardware, 
    public IPnpCallback,
    public IUsbTargetPipeContinuousReaderCallbackReadComplete,
    public IUsbTargetPipeContinuousReaderCallbackReadersFailed
{
public:
    CDeviceCallback();
    ~CDeviceCallback();
    virtual HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, VOID** ppvObject);
    virtual ULONG STDMETHODCALLTYPE AddRef();
    virtual ULONG STDMETHODCALLTYPE Release();

    virtual HRESULT STDMETHODCALLTYPE OnPrepareHardware(IWDFDevice* pDevice);
    virtual HRESULT STDMETHODCALLTYPE OnReleaseHardware(IWDFDevice* pDevice); 

    virtual HRESULT STDMETHODCALLTYPE OnD0Entry(IWDFDevice*  pWdfDevice, WDF_POWER_DEVICE_STATE  previousState);
    virtual HRESULT STDMETHODCALLTYPE OnD0Exit(IWDFDevice*  pWdfDevice, WDF_POWER_DEVICE_STATE  previousState);
    virtual void STDMETHODCALLTYPE OnSurpriseRemoval(IWDFDevice*  pWdfDevice);
    virtual HRESULT STDMETHODCALLTYPE OnQueryRemove(IWDFDevice*  pWdfDevice);
    virtual HRESULT STDMETHODCALLTYPE OnQueryStop(IWDFDevice*  pWdfDevice);    

    virtual VOID STDMETHODCALLTYPE OnReaderCompletion(IWDFUsbTargetPipe* pPipe, IWDFMemory* pMemory, SIZE_T NumBytesTransferred, PVOID Context);    
    virtual BOOL STDMETHODCALLTYPE OnReaderFailure(IWDFUsbTargetPipe * pPipe, HRESULT hrCompletion);

private:
    LONG m_cRefs;
    IWDFUsbTargetPipe* m_pFxUsbInterruptPipe;
    IWDFIoTargetStateManagement* m_pFxIoTargetInterruptPipeStateMgmt;

    HRESULT CreateUSBTargetDeviceObject (IWDFDevice* pFxDevice, IWDFUsbTargetDevice** ppUSBTargetDevice);
    HRESULT RetrieveUSBDeviceDescriptor (IWDFUsbTargetDevice* pUSBTargetDevice, PUSB_DEVICE_DESCRIPTOR DescriptorHeader, PULONG cbDescriptor);
    HRESULT ConfigureContinuousReader (IWDFUsbTargetPipe* pFxPipe);
};
```

The following example code shows the QueryInterface implementation of the device callback object.

```cpp
HRESULT CDeviceCallback::QueryInterface(REFIID riid, LPVOID* ppvObject)
{
    if (ppvObject == NULL)
    {
        return E_INVALIDARG;
    }

    *ppvObject = NULL;

    HRESULT hr = E_NOINTERFACE;

    if(  IsEqualIID(riid, __uuidof(IPnpCallbackHardware))   ||  IsEqualIID(riid, __uuidof(IUnknown))  )
    {  
        *ppvObject = static_cast<IPnpCallbackHardware*>(this);
        reinterpret_cast<IUnknown*>(*ppvObject)->AddRef();
        hr = S_OK;

    }

    if(  IsEqualIID(riid, __uuidof(IPnpCallback)))
    {  
        *ppvObject = static_cast<IPnpCallback*>(this);
        reinterpret_cast<IUnknown*>(*ppvObject)->AddRef();
        hr = S_OK;

    }

    if(  IsEqualIID(riid, __uuidof(IUsbTargetPipeContinuousReaderCallbackReadComplete)))
    {  
        *ppvObject = static_cast<IUsbTargetPipeContinuousReaderCallbackReadComplete*>(this);
        reinterpret_cast<IUnknown*>(*ppvObject)->AddRef();
        hr = S_OK;
    }

    if(  IsEqualIID(riid, __uuidof(IUsbTargetPipeContinuousReaderCallbackReadersFailed)))
    {  
        *ppvObject = static_cast<IUsbTargetPipeContinuousReaderCallbackReadersFailed*>(this);
        reinterpret_cast<IUnknown*>(*ppvObject)->AddRef();
        hr = S_OK;
    }

    return hr;
}
```

The following example code shows an implementation of a failure callback. If a read request fails, the method prints the error code reported by the framework in the debugger and instructs the framework to reset the pipe and then restart the continuous reader.

```cpp
 BOOL CDeviceCallback::OnReaderFailure(
    IWDFUsbTargetPipe * pPipe,
    HRESULT hrCompletion
    )
{
    UNREFERENCED_PARAMETER(pPipe);  
    UNREFERENCED_PARAMETER(hrCompletion);     

    return TRUE;
}
```

If the client driver does not provide a failure callback and an error occurs, the framework resets the USB pipe and restarts the continuous reader.

## Related topics
[USB I/O Transfers](usb-device-i-o.md)  
[How to enumerate USB pipes](how-to-get-usb-pipe-handles.md)  
[How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md)  
[How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md)  
[Common tasks for USB client drivers](wdk-resources-for-usb-driver-development.md)  



