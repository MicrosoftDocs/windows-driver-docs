---
title: Managing Queues in a WBDI Driver
description: Managing Queues in a WBDI Driver
ms.assetid: f0434581-8492-42e1-ae50-4114e7b8b202
keywords: ["biometric drivers WDK , managing queues", "managing queues WDK biometric"]
---

# Managing Queues in a WBDI Driver


WBDI drivers should create at least one queue to handle multiple concurrent requests from the service. If you are using UMDF, you can take advantage of its queue management support.

In [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics/driver), the CBiometricIoQueue class implements the I/O queue interface.

In the method `CBiometricIoQueue::Initialize`, specifically, the driver queries the owning CBiometricIoQueue object for a pointer to the [IQueueCallbackDeviceIoControl](https://msdn.microsoft.com/library/windows/hardware/ff556852) interface that the framework uses to determine the event callback functions that the driver subscribes to on the queue:

```
if (SUCCEEDED(hr)) 
{
hr = this->QueryInterface(__uuidof(IUnknown), (void **)&unknown);
}
```

Then the driver calls [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020) to configure the default I/O queue:

```
hr = FxDevice->CreateIoQueue(unknown,
FALSE,
WdfIoQueueDispatchParallel,
FALSE,
FALSE,
&fxQueue);
BiometricSafeRelease(unknown);
```

The call specifies WdfIoQueueDispatchParallel so that the framework will present requests to the driver's I/O queue callback functions as soon as the requests are available.

Next, the driver calls [**IWDFDevice::ConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff557014) to configure the queue to filter all Device I/O requests:

```
hr = FxDevice->ConfigureRequestDispatching(fxQueue,
WdfRequestDeviceIoControl,
TRUE);
```

Because the driver specifies WdfRequestDeviceIoControl in this call, it provides an [**OnDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff556854) handler to process I/O notifications from the framework. It does this in the **IQueueCallbackDeviceIoControl::OnDeviceIoControl** method that is part of the "unknown" parameter in the call to CreateIoQueue previously.

There can only be one outstanding [**IOCTL\_BIOMETRIC\_CAPTURE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff536429) request at a time. The driver should track IOCTL\_BIOMETRIC\_CAPTURE\_DATA requests, either by internally keeping a pointer to the pending requests or by using another framework queue to handle those requests.

In the sample, if there is a pending I/O request, the sample maintains a pointer to the request in a member of the CBiometricDevice class, as defined in Device.h:

```
IWDFIoRequest *m_PendingRequest;
```

While one sensor data collection I/O is pending, subsequent calls to the data collection IOCTLs should fail:

```
FxRequest->Complete(WINBIO_E_DATA_COLLECTION_IN_PROGRESS);
```

When a capture request is completed or canceled, this value is set to **NULL**:

```
IWDFIoRequest *FxRequest = (IWDFIoRequest *)InterlockedExchangePointer((PVOID *)&m_PendingRequest, NULL);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Managing%20Queues%20in%20a%20WBDI%20Driver%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




