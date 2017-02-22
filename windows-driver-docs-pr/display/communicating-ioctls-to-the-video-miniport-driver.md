---
title: Communicating IOCTLs to the Video Miniport Driver
description: Communicating IOCTLs to the Video Miniport Driver
ms.assetid: 9f9ad20e-d8cf-485d-adad-c04eeb40b705
keywords: ["video miniport drivers WDK Windows 2000 , IOCTLs", "IOCTLs WDK Windows 2000 display"]
---

# Communicating IOCTLs to the Video Miniport Driver


## <span id="ddk_communicating_ioctls_to_the_video_miniport_driver_gg"></span><span id="DDK_COMMUNICATING_IOCTLS_TO_THE_VIDEO_MINIPORT_DRIVER_GG"></span>


The following figure shows how the display driver communicates with the video miniport driver using IOCTLs.

![diagram illustrating display driver/video miniport driver communication](images/dpy2.png)

The display driver calls [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) with an IOCTL to send a synchronous request to the video miniport driver. GDI uses a single buffer for both input and output to pass the request to the I/O subsystem. The I/O subsystem routes the request to the video port, which processes the request with the video miniport driver.

Some IOCTL requests require the miniport driver to access video registers, and others store or retrieve information from the miniport driver's data structures. Generally, no requests require the video miniport driver to perform actual drawing operations.

In general, and unless modularity dictates otherwise, the display driver handles drawing and other time-critical operations. Sending an IOCTL to the miniport driver to perform a time-critical function can degrade system performance.

See [Video Miniport Driver I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff570515) for descriptions of system-defined video IOCTLs. You can extend the interface between the display driver and the video miniport driver by adding a *private IOCTL*, which must be formatted as described in [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023). If you need to write a new IOCTL, you should first contact Microsoft Technical Support.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Communicating%20IOCTLs%20to%20the%20Video%20Miniport%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




