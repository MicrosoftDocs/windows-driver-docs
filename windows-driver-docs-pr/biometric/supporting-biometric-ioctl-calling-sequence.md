---
title: Supporting Biometric IOCTL Calling Sequence
description: Supporting Biometric IOCTL Calling Sequence
keywords:
- biometric drivers WDK , supporting IOCTLs
- supporting IOCTLs WDK biometric
- IOCTLs WDK biometric
ms.date: 04/20/2017
---

# Supporting Biometric IOCTL Calling Sequence

WBDI is a Windows standard IOCTL-based interface. When you write a WBDI driver, you must support a set of mandatory IOCTLs. You may additionally choose to support optional IOCTLs. You can find a complete list of mandatory and optional IOCTLs in [Biometric IOCTLs](/windows-hardware/drivers/ddi/_biometric/#ioctls).

A vendor-supplied WBDI driver should be prepared to receive IOCTL requests in the following order from the Windows Biometric Service (WBS). You can review examples of handlers for these IOCTLs in Device.cpp in [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics/driver).

1. The Windows Biometric Service or the sensor adapter initializes the biometric device and verifies that it is ready for use. The service or adapter sends an [**IOCTL\_BIOMETRIC\_GET\_ATTRIBUTES**](/windows-hardware/drivers/ddi/winbio_ioctl/ni-winbio_ioctl-ioctl_biometric_get_attributes) request.

    The driver receives a pointer to a [**WINBIO\_SENSOR\_ATTRIBUTES**](/windows-hardware/drivers/ddi/winbio_ioctl/ns-winbio_ioctl-_winbio_sensor_attributes) structure. In the handler for this IOCTL, the driver should fill in the relevant members of this structure and complete the request by calling [**IWDFIoRequest::Complete**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-complete).

2. Next, the driver receives [**IOCTL\_BIOMETRIC\_GET\_SENSOR\_STATUS**](/windows-hardware/drivers/ddi/winbio_ioctl/ni-winbio_ioctl-ioctl_biometric_get_sensor_status). The driver should fill in the relevant members of the [**WINBIO\_DIAGNOSTICS**](/windows-hardware/drivers/ddi/winbio_ioctl/ns-winbio_ioctl-_winbio_diagnostics) structure and complete the request.

3. If the driver indicates that calibration is necessary in the **SensorStatus** member of the [**WINBIO\_DIAGNOSTICS**](/windows-hardware/drivers/ddi/winbio_ioctl/ns-winbio_ioctl-_winbio_diagnostics) structure that was returned from the IOCTL\_BIOMETRIC\_GET\_SENSOR\_STATUS request, the driver next receives an [**IOCTL\_BIOMETRIC\_CALIBRATE**](/windows-hardware/drivers/ddi/winbio_ioctl/ni-winbio_ioctl-ioctl_biometric_calibrate) request. The driver must provide a handler for this IOCTL. After calibrating the device, the callback should return a [**WINBIO\_CALIBRATION\_INFO**](/windows-hardware/drivers/ddi/winbio_ioctl/ns-winbio_ioctl-_winbio_calibration_info) structure.

4. The driver can now expect to receive [**IOCTL\_BIOMETRIC\_CAPTURE\_DATA**](/windows-hardware/drivers/ddi/winbio_ioctl/ni-winbio_ioctl-ioctl_biometric_capture_data) requests. Because only one capture can be pending at any time, the handler for this request should first confirm that no request is pending. If a request is pending, complete the request with WINBIO\_E\_DATA\_COLLECTION\_IN\_PROGRESS.

    The WinBio service or an application can request cancellation of an outstanding capture request at any time by calling Win32 cancellation routines such as [**CancelIo**](/windows/desktop/FileIO/cancelio), [**CancelIoEx**](/windows/desktop/FileIO/cancelioex-func), or [**CancelSynchronousIo**](/windows/desktop/FileIO/cancelsynchronousio-func). As such, WBDI drivers must also support cancellation.

    The driver handles cancellation by calling [**IWDFIoRequest::MarkCancelable**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-markcancelable) to register an [IRequestCallbackCancel](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-irequestcallbackcancel) interface.

    The handler then programs the device for capture mode and returns from the callback. The request should remain pending until canceled or the driver detects that capture is complete. After this I/O request is completed, the device can return to an idle state. A client may make an initial call to IOCTL\_BIOMETRIC\_CAPTURE\_DATA to determine the correct buffer size for an actual capture.

5. The handler for [**IOCTL\_BIOMETRIC\_RESET**](/windows-hardware/drivers/ddi/winbio_ioctl/ni-winbio_ioctl-ioctl_biometric_reset) should physically reset the device to a known or idle state. The handler for this request must also cancel any pending data collection I/O and fill out the [**WINBIO\_BLANK\_PAYLOAD**](/windows-hardware/drivers/ddi/winbio_ioctl/ns-winbio_ioctl-_winbio_blank_payload) structure. The handler then completes the request. Clients do not need to call reset between calls to IOCTL\_BIOMETRIC\_CAPTURE\_DATA.
