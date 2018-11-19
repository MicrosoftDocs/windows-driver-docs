---
Description: MultiTransport Device Support
title: MultiTransport Device Support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MultiTransport Device Support


The WpdMultiTransportDriver sample is based on the WpdHelloWorldDriver, and most of the source code for the original driver remains unchanged. In particular, the code that supports object enumeration, properties, and capabilities contains very few changes or revisions.

The revisions to the code in the WpdMultiTransportDriver appear in two primary areas: device-arrival and I/O queues. The code that supports device arrival is found in two files, *Device.cpp* and *Driver.cpp*. The code that supports the I/O queues is found in *Driver.cpp* and *Queue.cpp*

## <span id="Multitransport_Device-Arrival"></span><span id="multitransport_device-arrival"></span><span id="MULTITRANSPORT_DEVICE-ARRIVAL"></span>Multitransport Device-Arrival


The device-arrival code is found in the **CDevice::OnPrepareHardware** method (in the *Device.cpp* file) and in the **CDriver::OnDeviceAdd** method (in the *Driver.cpp* file).

The code in the **CDevice::OnPrepareHardware** method completes the following tasks before it initializes the WPD class extension. (The last three tasks set the option parameters that are passed to the WPD class extension.)

The parallel queue is required so that the **IOCTL\_COMPOSITE\_TRANSPORT\_REQUEST IOCTLs** can be correctly received from the WPD class installer when the device interface state changes. The second queue allows a different (for example, non-parallel) dispatch mode to be used by the transport driver. Sequential queues are simpler to manage because WUDF only allows one request at a time. However, if your WPD driver is able to handle multiple requests in parallel, it does not require the secondary queue.

|                                                                       |                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                  | Description                                                                                                                                                                                                                      |
| Create a Functional Unique Identifier (FUID).                         | The FUID is a globally unique identifier (GUID) value that the driver passes to the WPD class extension during initialization. (The class extension associates this FUID with each transport.)                                   |
| Retrieve a pointer to an **IQueueCallbackDeviceIoControl** interface. | The driver forwards any non-WPD IOCTLs to the class extension by using this pointer.                                                                                                                                             |
| Enable the multitransport mode option.                                | This option informs the WPD class extension that it should set up the multitransport framework.                                                                                                                                  |
| Set the necessary Plug and Play (PnP) values.                         | These values are used to configure the multitransport framework.                                                                                                                                                                 |
| Set the current transport bandwidth.                                  | This value is used by the class extension and the composite driver (*WpdComp.dll*). The composite driver retrieves the value from the extension and uses it to determine the best transport when multiple transports are active. |

 

The following code example from the **CDevice::OnPrepareHardware** method shows how the sample driver created the Functional Unique Identifier (FUID). Make sure to review the comments, which precede the creation of this GUID.

```ManagedCPlusPlus
 // ATTENTION: The following GUID value is provided for illustrative
                // purposes only.
                //
                // Rather than hard-coding a GUID value in your driver, the driver
                // must obtain a GUID value from the device. The driver can provision the GUID value on the
                // device (upon first-connect) by
                // using CoCreateGUID and setting that value into non-volatile storage
                // on the device. The same GUID value is then  reported by each
                // of your device&#39;s transports. To avoid a provisioning race condition,
                // always read the value from the device after provisioning. Only
                // provision the GUID one time. Thereafter, always use the value that is provided
                // by the device.
                GUID guidFUID = { 0x245e5e81, 0x2c17, 0x40a4, { 0x8b, 0x10, 0xe9, 0x43, 0xc5, 0x4c, 0x97, 0xb2 } };
```

The following code example from the **CDevice::OnPrepareHardware** method shows the three remaining tasks from the previous table (retrieval of the **IQueueCallbackDeviceIoControl** pointer, enabling the multitransport mode, setting the PnP values and the current bandwidth.

```ManagedCPlusPlus
     if (hr == S_OK)
                {
                    m_pWpdBaseDriver->m_pQueueCallback = NULL;

                    HRESULT hrTemp = m_pPortableDeviceClassExtension->QueryInterface(
                        __uuidof(IQueueCallbackDeviceIoControl),
                        (void**)&m_pWpdBaseDriver->m_pQueueCallback
                        );
                    CHECK_HR(hrTemp, "Failed to obtain IQueueCallbackDeviceIoControl interface from class extension");

                    if (hrTemp == S_OK)
                    {
                        // Enable the Multi-Transport Mode option
                        hr = pOptions->SetBoolValue(WPD_CLASS_EXTENSION_OPTIONS_MULTITRANSPORT_MODE, TRUE);
                        CHECK_HR(hr, "Failed to enable multi-transport mode");

                        // Create a PnP ID value collection
                        if (hr == S_OK)
                        {
                            hr = CreateIDValues(DEVICE_MANUFACTURER_VALUE,
                                                DEVICE_MODEL_VALUE,
                                                DEVICE_FIRMWARE_VERSION_VALUE,
                                                &guidFUID,
                                                &pIDs);
                            CHECK_HR(hr, "Failed to Create the ID value collection");
                        }

                        // Add the PnP ID value collection to the options
                        if (hr == S_OK)
                        {
                            hr = pOptions->SetIPortableDeviceValuesValue(WPD_CLASS_EXTENSION_OPTIONS_DEVICE_IDENTIFICATION_VALUES, pIDs);
                            CHECK_HR(hr, "Failed to set WPD_CLASS_EXTENSION_OPTIONS_DEVICE_IDENTIFICATION_VALUES");
                        }

                        // Add the transport bandwidth (in kilobits per second units) to the options
                        // (0 indicates bandwidth unknown)
                        if (hr == S_OK)
                        {
                            // Set the transport bandwidth (optional)
                            hr = pOptions->SetUnsignedIntegerValue(WPD_CLASS_EXTENSION_OPTIONS_TRANSPORT_BANDWIDTH, 0L);
                            CHECK_HR(hr, "Failed to set WPD_CLASS_EXTENSION_OPTIONS_TRANSPORT_BANDWIDTH");
                        }
                    }
                }
```

## <span id="MultiTransport_Queues"></span><span id="multitransport_queues"></span><span id="MULTITRANSPORT_QUEUES"></span>MultiTransport Queues


The WpdHelloWorld driver sample supports a single, sequential queue to process IOCTLs from the WPD serializer. The WpdMultiTransportDriver driver supports two queues: a parallel queue and a sequential queue. The parallel queue handles multiple, simultaneous I/O requests, while a sequential queue handles only one request at a time.

The device-arrival code in the **CDriver::OnDeviceAdd** method prepares both queues. The first (or default) queue is a parallel queue that processes each IOCTL and then forwards it to either the second (sequential) queue in the driver, or to another queue that is supported by the WPD class extension.

The following code example contains the code that creates both the parallel and sequential queues:

```ManagedCPlusPlus
        //
        // Create the default queue callback object
        //
        CComPtr<IUnknown> pIUnknown;
        if(S_OK == hr)
        {
            hr = CDefaultQueue::CreateInstance(&pIUnknown);
        }

        //
        // Configure the default queue.
        //
        if(S_OK == hr)
        {
            CComPtr<IWDFIoQueue> pDefaultQueue;
            hr = pIWDFDevice->CreateIoQueue(
                              pIUnknown,
                              TRUE,                         // bDefaultQueue
                              WdfIoQueueDispatchParallel,
                              TRUE,                         // bPowerManaged
                              FALSE,                        // bAllowZeroLengthRequests
                              &pDefaultQueue);
        }
        pIUnknown = NULL;

        //
        // Create the WPD queue callback object
        //
        if(S_OK == hr)
        {
            hr = CQueue::CreateInstance(&pIUnknown);
        }

        //
        // Configure the WPD queue.
        //
        if(S_OK == hr)
        {
            hr = pIWDFDevice->CreateIoQueue(
                              pIUnknown,
                              FALSE,                        // bDefaultQueue
                              WdfIoQueueDispatchSequential,
                              TRUE,                         // bPowerManaged
                              FALSE,                        // bAllowZeroLengthRequests
                              &pWpdBaseDriver->m_pWpdQueue);
        }
```

While the **CDriver::OnDeviceAdd** method handles the creation of the I/O queues, the code that supports the functionality in both queues is found in the *Queue.cpp* file.

## <span id="related_topics"></span>Related topics


[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





