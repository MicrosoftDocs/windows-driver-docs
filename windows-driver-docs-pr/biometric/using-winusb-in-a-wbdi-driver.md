---
title: Using WinUSB in a WBDI Driver
description: Using WinUSB in a WBDI Driver
ms.assetid: a2f109cd-cb61-4c63-8e93-111f62a2c02d
keywords: ["biometric drivers WDK , WinUSB"]
---

# Using WinUSB in a WBDI Driver


Microsoft recommends that WBDI drivers use the [USB I/O target](https://msdn.microsoft.com/library/windows/hardware/ff561358) that is built into User-Mode Driver Framework (UMDF).

### <span id="setting_umdfdispatcher"></span><span id="SETTING_UMDFDISPATCHER"></span>Setting UmdfDispatcher

An INF file that installs a UMDF driver must contain a WDF-specific **DDInstall** section. If you use the USB I/O target in UMDF, you must set the UmdfDispatcher registry directive within this **DDInstall** section.

The following section from WudfBioUsbSample.inx in the [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics/driver) sample shows how to set this directive:

```
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
    ```
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

A WBDI driver should support [USB Selective Suspend](https://msdn.microsoft.com/library/windows/hardware/ff540144).

A device that supports system wake and device idle should enable the registry settings for selective suspend in WinUsb, as shown in this code example from WudfBioUsbSample.inx:

```
HKR,,"SystemWakeEnabled",0x00010001,1
HKR,,"DeviceIdleEnabled",0x00010001,1
```

The operating system USB stack cannot guarantee the timing between system wake and when the driver can start reading from the device.

Ideally, the device should be left in a state ready to capture a scan when the system is suspended. If a scan occurs while the system is suspended, the device should cache the input data for an entire fingerprint scan. When the system wakes up, the driver then reads in the data from the device. By supporting this scenario, you can enable system wake and unlock/login scenarios.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Using%20WinUSB%20in%20a%20WBDI%20Driver%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




