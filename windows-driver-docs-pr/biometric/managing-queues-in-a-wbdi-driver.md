---
title: Managing Queues in a WBDI Driver
description: Managing Queues in a WBDI Driver
keywords:
- biometric drivers WDK , managing queues
- managing queues WDK biometric
ms.date: 03/03/2023
---

# Managing Queues in a WBDI Driver


WBDI drivers should create at least one queue to handle multiple concurrent requests from the service. If you are using UMDF, you can take advantage of its queue management support.

In [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/main/biometrics/driver), the CBiometricIoQueue class implements the I/O queue interface.

In the method `CBiometricIoQueue::Initialize`, specifically, the driver queries the owning CBiometricIoQueue object for a pointer to the [IQueueCallbackDeviceIoControl](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iqueuecallbackdeviceiocontrol) interface that the framework uses to determine the event callback functions that the driver subscribes to on the queue:

```cpp
if (SUCCEEDED(hr)) 
{
hr = this->QueryInterface(__uuidof(IUnknown), (void **)&unknown);
}
```

Then the driver calls [**IWDFDevice::CreateIoQueue**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createioqueue) to configure the default I/O queue:

```cpp
hr = FxDevice->CreateIoQueue(unknown,
FALSE,
WdfIoQueueDispatchParallel,
FALSE,
FALSE,
&fxQueue);
BiometricSafeRelease(unknown);
```

The call specifies WdfIoQueueDispatchParallel so that the framework will present requests to the driver's I/O queue callback functions as soon as the requests are available.

Next, the driver calls [**IWDFDevice::ConfigureRequestDispatching**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-configurerequestdispatching) to configure the queue to filter all Device I/O requests:

```cpp
hr = FxDevice->ConfigureRequestDispatching(fxQueue,
WdfRequestDeviceIoControl,
TRUE);
```

Because the driver specifies WdfRequestDeviceIoControl in this call, it provides an [**OnDeviceIoControl**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackdeviceiocontrol-ondeviceiocontrol) handler to process I/O notifications from the framework. It does this in the **IQueueCallbackDeviceIoControl::OnDeviceIoControl** method that is part of the "unknown" parameter in the call to CreateIoQueue previously.

There can only be one outstanding [**IOCTL\_BIOMETRIC\_CAPTURE\_DATA**](/windows-hardware/drivers/ddi/winbio_ioctl/ni-winbio_ioctl-ioctl_biometric_capture_data) request at a time. The driver should track IOCTL\_BIOMETRIC\_CAPTURE\_DATA requests, either by internally keeping a pointer to the pending requests or by using another framework queue to handle those requests.

In the sample, if there is a pending I/O request, the sample maintains a pointer to the request in a member of the CBiometricDevice class, as defined in Device.h:

```cpp
IWDFIoRequest *m_PendingRequest;
```

While one sensor data collection I/O is pending, subsequent calls to the data collection IOCTLs should fail:

```cpp
FxRequest->Complete(WINBIO_E_DATA_COLLECTION_IN_PROGRESS);
```

When a capture request is completed or canceled, this value is set to **NULL**:

```cpp
IWDFIoRequest *FxRequest = (IWDFIoRequest *)InterlockedExchangePointer((PVOID *)&m_PendingRequest, NULL);
```

 

