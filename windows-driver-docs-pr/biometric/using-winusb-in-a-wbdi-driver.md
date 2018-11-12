---
title: Using WinUSB in a WBDI Driver
description: Using WinUSB in a WBDI Driver
ms.assetid: a2f109cd-cb61-4c63-8e93-111f62a2c02d
keywords:
- biometric drivers WDK , WinUSB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using WinUSB in a WBDI Driver


Microsoft recommends that WBDI drivers use the [USB I/O target](https://msdn.microsoft.com/library/windows/hardware/ff561358) that is built into User-Mode Driver Framework (UMDF).

### <span id="setting_umdfdispatcher"></span><span id="SETTING_UMDFDISPATCHER"></span>Setting UmdfDispatcher

An INF file that installs a UMDF driver must contain a WDF-specific **DDInstall** section. If you use the USB I/O target in UMDF, you must set the UmdfDispatcher registry directive within this **DDInstall** section.

The following section from WudfBioUsbSample.inx in the [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics/driver) sample shows how to set this directive:

```cpp
[Biometric_Install.NT.Wdf]
KmdfService=WINUSB, WinUsb_Install
UmdfDispatcher=WinUsb
UmdfService=WudfBioUsbSample, WudfBioUsbSample_Install
UmdfServiceOrder=WudfBioUsbSample
```

For specific information about UmdfDispatcher, see [Specifying the UmdfDispatcher INF Directive](https://msdn.microsoft.com/library/windows/hardware/ff560526). For general information about WDF registry directives, see [Specifying WDF Directives](https://msdn.microsoft.com/library/windows/hardware/ff560526).

### <span id="pending_asynchronous_read_requests"></span><span id="PENDING_ASYNCHRONOUS_READ_REQUESTS"></span>Pending Asynchronous Read Requests

WinUsb can handle multiple outstanding read requests. Devices that require minimal latency between read operations during a scan should keep some number of outstanding asynchronous read requests pending. If the driver makes asynchronous requests, WinUsb issues these requests before the transfer back to user mode for the completion routines of earlier read requests.

You can refer to the `CBiometricDevice::InitiatePendingRead` method in Device.cpp in [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics/driver) to see a code example of how to pend a read request.

The code to pend a read request should be a loop of the following steps:

1.  Create a pre-allocated framework memory object by calling [**IWDFDriver::CreatePreallocatedWdfMemory**](https://msdn.microsoft.com/library/windows/hardware/ff558902).

2.  Provide callback code in an [**OnCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556905) routine. See `CBiometricDevice::OnCompletion` in the sample.

3.  Acquire a pointer to the [**IRequestCallbackRequestCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556904) interface of the owning object.

4.  Register callback function by calling [**IWDFIoRequest::SetCompletionCallback**](https://msdn.microsoft.com/library/windows/hardware/ff559153) and passing in the pointer to [**IRequestCallbackRequestCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556904) that was obtained in the previous step. The framework will now call the callback when an I/O request completes.

5.  Call [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) to send the read request to the device.

6.  Process read request when callback completion occurs. Before the [**OnCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556905) routine initiates a new pending read request, it should check the state of the I/O target. To do this, query [IWDFUsbTargetPipe](https://msdn.microsoft.com/library/windows/hardware/ff560391) for a pointer to its [IWDFIoTargetStateManagement](https://msdn.microsoft.com/library/windows/hardware/ff559198) interface. Then call [**IWDFIoTargetStateManagement::GetState**](https://msdn.microsoft.com/library/windows/hardware/ff559202):
    ```cpp
    IWDFIoTarget * pTarget
    IWDFIoTargetStateManagement * pStateMgmt = NULL;
    WDF_IO_TARGET_STATE state;

    HRESULT hrQI = pTarget->QueryInterface(IID_PPV_ARGS(&pStateMgmt));
    WUDF_TEST_DRIVER_ASSERT((SUCCEEDED(hrQI) && pStateMgmt));

    state = pStateMgmt->GetState();
    ```

When the scan is complete, cancel any pending read requests.

If you use the UMDF-USB target, you can allow read requests to remain pending across power-down and power-up.

If you do not use the UMDF-USB target, the driver should stop sending pending read requests at D0Exit and restart at D0Entry.

### <span id="selective_suspend"></span><span id="SELECTIVE_SUSPEND"></span>Selective Suspend

A WBDI driver should support [USB selective suspend](../usbcon/usb-selective-suspend.md).

A device that supports system wake and device idle should enable the registry settings for selective suspend in WinUsb, as shown in this code example from WudfBioUsbSample.inx:

```cpp
HKR,,"SystemWakeEnabled",0x00010001,1
HKR,,"DeviceIdleEnabled",0x00010001,1
```

The operating system USB stack cannot guarantee the timing between system wake and when the driver can start reading from the device.

Ideally, the device should be left in a state ready to capture a scan when the system is suspended. If a scan occurs while the system is suspended, the device should cache the input data for an entire fingerprint scan. When the system wakes up, the driver then reads in the data from the device. By supporting this scenario, you can enable system wake and unlock/login scenarios.

 

 





