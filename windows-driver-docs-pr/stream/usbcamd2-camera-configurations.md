---
title: USBCAMD2 Camera Configurations
author: windows-driver-content
description: USBCAMD2 Camera Configurations
ms.assetid: 9a0dd6f9-aefb-4134-8bd5-31420a16db4a
keywords:
- Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library
- Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library
- Kernel Streaming Model WDK , USBCAMD2 minidriver library
- USBCAMD2 camera configurations WDK Windows 2000 Kernel Streaming
- USB-based streaming cameras WDK USBCAMD2
- cameras WDK USBCAMD2
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# USBCAMD2 Camera Configurations


Minidrivers to support USB cameras can be clients of the *stream.sys* class driver on their upper end and the USB bus driver on their lower end, as shown in the following diagram.

![diagram illustrating usb camera minidriver models](images/usbimdev.png)

In the group **A** configuration of the diagram, the minidriver writer must interface to the *stream.sys* class driver, the camera, and the USB bus. In the goup **B** configuration, a minidriver written to use USBCAMD2 needs only to contain the code that is device-specific. That is, if you use USBCAMD2, you can focus on implementing support for video formats, property sets, image decompression, and color space conversion. The USBCAMD2 minidriver library controls the connection to the *stream.sys* class driver and the USB bus driver, thereby simplifying the process of developing a camera minidriver.

Although USBCAMD2 interfaces with the *stream.sys* class driver, which is now obsolete, developing a camera minidriver with USBCAMD2 can be easier than writing your own stand-alone *stream.sys* class or AVStream minidriver.

The primary purpose of USBCAMD2 is to support streaming video cameras, such as webcams. However, USBCAMD2 also provides support to use USB bulk and interrupt transfer pipes to capture still images sent from the camera. This feature supports USB cameras with snapshot capability to capture still frames.

If your camera primarily streams video, and optionally provides snapshot capability, then you need only to write a USBCAMD2 minidriver. Vendors of hybrid cameras (cameras that primarily take still photos, but that can also stream video) write a USBCAMD2 minidriver to support the streaming capability, and a separate Windows Image Acquisition (WIA) still camera driver to support still image storage and management. For more information about WIA and supporting digital cameras that capture still images, see [Windows Image Acquisition Drivers](https://msdn.microsoft.com/library/windows/hardware/ff553346).

The USBCAMD2 library supports cameras that use a combination of isochronous pipe(s), bulk I/O pipe(s) and/or an interrupt pipe to transfer data streams and control settings. USBCAMD2 supports cameras that implement the following USB pipe configurations:

-   A single isochronous pipe, with synchronization information, such as the start and end of video or still frames embedded in the data stream. These types of cameras can multiplex both video and still frames through the same isochronous pipe or reuse individual video frames as still frames.

-   Same as the previous configuration, with the addition of an interrupt pipe to signal notification of external trigger events to registered applications.

-   Same as the first configuration, with the addition of two bulk I/O pipes to control and retrieve still frames from the camera.

-   Two isochronous pipes. One pipe streams data and the other pipe contains synchronization information, such as the start and end of video or still frames. These cameras can also multiplex both video and still frames through the same isochronous pipe or reuse individual video frames as still frames.

-   Two bulk I/O pipes and an optional interrupt pipe. One bulk pipe streams video and the other bulk pipe transfers still images. The optional interrupt pipe signals notification of external trigger events to registered applications.

**Note**   USBCAMD2 supports cameras with a single USB interface that has multiple alternate settings. All alternate settings must have the same type and number of pipes. You specify this information in an array of type [**USBCAMD\_Pipe\_Config\_Descriptor**](https://msdn.microsoft.com/library/windows/hardware/ff568623) that you pass to [*CamConfigureEx*](https://msdn.microsoft.com/library/windows/hardware/ff557605) when you initialize and configure the camera.

 

Whereas USB 1.1 devices can be connected to a USB 2.0 bus, USBCAMD2 supports only USB 1.1 camera devices and is therefore limited to the maximum throughput of the USB 1.1 bus (for example, isochronous data transfer in *full*-speed mode). USBCAMD2 does not support the USB 2.0 *high*-speed mode for isochronous data transfer. However, if a camera implements bulk pipes only, then it could benefit from being connected to a USB 2.0 bus where there is more available bulk transfer bandwidth.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20USBCAMD2%20Camera%20Configurations%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


