---
title: Data Flow Using Isochronous Pipes
description: Data Flow Using Isochronous Pipes
keywords:
- isochronous pipes WDK USBCAMD2
- Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library
- Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library
- Kernel Streaming Model WDK , USBCAMD2 minidriver library
- USBCAMD2 minidriver library WDK Windows 2000 Kernel Streaming
- USB-based streaming cameras WDK USBCAMD2
- cameras WDK USBCAMD2
- data flow WDK USBCAMD2
ms.date: 04/20/2017
---

# Data Flow Using Isochronous Pipes





USBCAMD2 begins streaming on the isochronous pipe by requesting two transfers of 32 packets. Each packet has a maximum size that corresponds to the maximum size in the selected alternate setting.

**Note**   Streaming on the isochronous pipe is independent of Microsoft DirectShow streaming.

 

Double-buffer isochronous transfer requests are continuously submitted to USBCAMD2 and stop only when one of the following two conditions occur:

1.  A stop DirectShow stream state is issued (KSSTATE\_STOP).

2.  The camera minidriver requests USBCAMD2 to stop isochronous streaming by passing the USBCAMD\_STOP\_STREAMING flag in the *PipeStateFlags* parameter in a call to [*USBCAMD\_SetIsoPipeState*](/windows-hardware/drivers/ddi/usbcamdi/nc-usbcamdi-pfnusbcamd_setisopipestate).

While streaming is in progress, USBCAMD2 and the camera minidriver repeat the following process until streaming stops:

1.  USBCAMD2 calls the camera minidriver's [*CamProcessUSBPacketEx*](/windows-hardware/drivers/ddi/usbcamdi/nc-usbcamdi-pcam_process_packet_routine_ex) callback function (at IRQL = DISPATCH\_LEVEL) for every packet that USBCAMD2 receives from the USB bus driver. The camera minidriver must set the appropriate error flags in the case of error conditions. The minidriver must also set a new video frame flag if the beginning of a new video frame is detected using the *FrameComplete* parameter of **CamProcessUSBPacketEx**.

2.  After the camera minidriver has determined that a video frame is complete, USBCAMD2 calls the camera minidriver's [*CamProcessRawVideoFrameEx*](/windows-hardware/drivers/ddi/usbcamdi/nc-usbcamdi-pcam_process_raw_frame_routine_ex) callback function (from the context of a worker thread) to process the video frame if there is a need to perform a color space conversion or decompression. USBCAMD2 returns a completed raw frame to the *stream.sys* class driver to be processed by the camera minidriver at IRQL = PASSIVE\_LEVEL. If there is insufficient frame data or an error occurred during decompression due to bad data, for example, then the *BytesReturned* parameter to **CamProcessRawVideoFrameEx** must be set to 0.

 

