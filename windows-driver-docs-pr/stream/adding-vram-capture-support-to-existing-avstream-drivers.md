---
title: Adding VRAM Capture Support to Existing AVStream Drivers
author: windows-driver-content
description: Adding VRAM Capture Support to Existing AVStream Drivers
MS-HAID:
- 'gpucap\_1ddd738d-775b-4b4a-bea3-a3c1429eee06.xml'
- 'stream.adding\_vram\_capture\_support\_to\_existing\_avstream\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 10736533-3873-4f1d-91c5-d2e55163daaa
keywords: ["VRAM capture WDK AVStream , existing driver support"]
---

# Adding VRAM Capture Support to Existing AVStream Drivers


To add VRAM capture support to an existing pin-centric AVStream driver that uses DMA, follow these steps.

1.  Add VRAM capture support to your [*AVStrMiniPinProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556351) callback routine. The **CCapturePin::Process** method in *Capture.cpp* of the [AVStream Simulated Hardware Sample Driver (AVSHwS)](http://go.microsoft.com/fwlink/p/?linkid=256083) in the MSDN Code Gallery shows one way to do this.

2.  Handle VRAM capture property requests as described earlier in this section.

3.  Add support in either the child capture driver or the parent display miniport driver to map DX kernel handles to VRAM addresses.

4.  Implement StopCapture functionality. When the KMD sends a stop capture notification, the capture driver must stop all capture. To register for notification, the capture driver provides a [*DxgkDdiStopCapture*](https://msdn.microsoft.com/library/windows/hardware/ff560776) callback routine. The capture driver should fail any capture requests coming from user mode after receiving this notification.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Adding%20VRAM%20Capture%20Support%20to%20Existing%20AVStream%20Drivers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


