---
title: Supporting Biometric IOCTL Calling Sequence
description: Supporting Biometric IOCTL Calling Sequence
ms.assetid: e6555895-8936-4f5d-8f2b-05b5283edbee
keywords:
- biometric drivers WDK , supporting IOCTLs
- supporting IOCTLs WDK biometric
- IOCTLs WDK biometric
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Biometric IOCTL Calling Sequence


WBDI is a Windows standard IOCTL-based interface. When you write a WBDI driver, you must support a set of mandatory IOCTLs. You may additionally choose to support optional IOCTLs. You can find a complete list of mandatory and optional IOCTLs in [Biometric IOCTLs](https://msdn.microsoft.com/library/windows/hardware/ff536414).

A vendor-supplied WBDI driver should be prepared to receive IOCTL requests in the following order from the Windows Biometric Service (WBS). You can review examples of handlers for these IOCTLs in Device.cpp in [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics/driver).

1.  The Windows Biometric Service or the sensor adapter initializes the biometric device and verifies that it is ready for use. The service or adapter sends an [**IOCTL\_BIOMETRIC\_GET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff536431) request.

    The driver receives a pointer to a [**WINBIO\_SENSOR\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff536475) structure. In the handler for this IOCTL, the driver should fill in the relevant members of this structure and complete the request by calling [**IWDFIoRequest::Complete**](https://msdn.microsoft.com/library/windows/hardware/ff559070).

2.  Next, the driver receives [**IOCTL\_BIOMETRIC\_GET\_SENSOR\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff536436). The driver should fill in the relevant members of the [**WINBIO\_DIAGNOSTICS**](https://msdn.microsoft.com/library/windows/hardware/ff536470) structure and complete the request.

3.  If the driver indicates that calibration is necessary in the **SensorStatus** member of the [**WINBIO\_DIAGNOSTICS**](https://msdn.microsoft.com/library/windows/hardware/ff536470) structure that was returned from the IOCTL\_BIOMETRIC\_GET\_SENSOR\_STATUS request, the driver next receives an [**IOCTL\_BIOMETRIC\_CALIBRATE**](https://msdn.microsoft.com/library/windows/hardware/ff536427) request. The driver must provide a handler for this IOCTL. After calibrating the device, the callback should return a [**WINBIO\_CALIBRATION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536465) structure.

4.  The driver can now expect to receive [**IOCTL\_BIOMETRIC\_CAPTURE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff536429) requests. Because only one capture can be pending at any time, the handler for this request should first confirm that no request is pending. If a request is pending, complete the request with WINBIO\_E\_DATA\_COLLECTION\_IN\_PROGRESS.

    The WinBio service or an application can request cancellation of an outstanding capture request at any time by calling Win32 cancellation routines such as [**CancelIo**](https://msdn.microsoft.com/library/windows/desktop/aa363791), [**CancelIoEx**](https://msdn.microsoft.com/library/windows/desktop/aa363792), or [**CancelSynchronousIo**](https://msdn.microsoft.com/library/windows/desktop/aa363794). As such, WBDI drivers must also support cancellation.

    The driver handles cancellation by calling [**IWDFIoRequest::MarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff559146) to register an [IRequestCallbackCancel](https://msdn.microsoft.com/library/windows/hardware/ff556901) interface.

    The handler then programs the device for capture mode and returns from the callback. The request should remain pending until canceled or the driver detects that capture is complete. After this I/O request is completed, the device can return to an idle state. A client may make an initial call to IOCTL\_BIOMETRIC\_CAPTURE\_DATA to determine the correct buffer size for an actual capture.

5.  The handler for [**IOCTL\_BIOMETRIC\_RESET**](https://msdn.microsoft.com/library/windows/hardware/ff536439) should physically reset the device to a known or idle state. The handler for this request must also cancel any pending data collection I/O and fill out the [**WINBIO\_BLANK\_PAYLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff536464) structure. The handler then completes the request. Clients do not need to call reset between calls to IOCTL\_BIOMETRIC\_CAPTURE\_DATA.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Supporting%20Biometric%20IOCTL%20Calling%20Sequence%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




