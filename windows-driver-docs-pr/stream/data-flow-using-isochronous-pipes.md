---
title: Data Flow Using Isochronous Pipes
author: windows-driver-content
description: Data Flow Using Isochronous Pipes
ms.assetid: a66f4191-53ce-4ca2-aae7-8fb24a1a9a16
keywords: ["isochronous pipes WDK USBCAMD2", "Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library", "Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library", "Kernel Streaming Model WDK , USBCAMD2 minidriver library", "USBCAMD2 minidriver library WDK Windows 2000 Kernel Streaming", "USB-based streaming cameras WDK USBCAMD2", "cameras WDK USBCAMD2", "data flow WDK USBCAMD2"]
---

# Data Flow Using Isochronous Pipes


## <a href="" id="ddk-data-flow-using-isochronous-pipes-ksg"></a>


USBCAMD2 begins streaming on the isochronous pipe by requesting two transfers of 32 packets. Each packet has a maximum size that corresponds to the maximum size in the selected alternate setting.

**Note**   Streaming on the isochronous pipe is independent of Microsoft DirectShow streaming.

 

Double-buffer isochronous transfer requests are continuously submitted to USBCAMD2 and stop only when one of the following two conditions occur:

1.  A stop DirectShow stream state is issued (KSSTATE\_STOP).

2.  The camera minidriver requests USBCAMD2 to stop isochronous streaming by passing the USBCAMD\_STOP\_STREAMING flag in the *PipeStateFlags* parameter in a call to [*USBCAMD\_SetIsoPipeState*](https://msdn.microsoft.com/library/windows/hardware/ff568629).

While streaming is in progress, USBCAMD2 and the camera minidriver repeat the following process until streaming stops:

1.  USBCAMD2 calls the camera minidriver's [*CamProcessUSBPacketEx*](https://msdn.microsoft.com/library/windows/hardware/ff557631) callback function (at IRQL = DISPATCH\_LEVEL) for every packet that USBCAMD2 receives from the USB bus driver. The camera minidriver must set the appropriate error flags in the case of error conditions. The minidriver must also set a new video frame flag if the beginning of a new video frame is detected using the *FrameComplete* parameter of **CamProcessUSBPacketEx**.

2.  After the camera minidriver has determined that a video frame is complete, USBCAMD2 calls the camera minidriver's [*CamProcessRawVideoFrameEx*](https://msdn.microsoft.com/library/windows/hardware/ff557625) callback function (from the context of a worker thread) to process the video frame if there is a need to perform a color space conversion or decompression. USBCAMD2 returns a completed raw frame to the *stream.sys* class driver to be processed by the camera minidriver at IRQL = PASSIVE\_LEVEL. If there is insufficient frame data or an error occurred during decompression due to bad data, for example, then the *BytesReturned* parameter to **CamProcessRawVideoFrameEx** must be set to 0.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Data%20Flow%20Using%20Isochronous%20Pipes%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


