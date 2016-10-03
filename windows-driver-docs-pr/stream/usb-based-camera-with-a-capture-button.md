---
title: USB-Based Camera with a Capture Button
author: windows-driver-content
description: USB-Based Camera with a Capture Button
MS-HAID:
- 'vidcapds\_bd0effd9-1b5d-4d1b-92ef-4e5ce3b9f8d9.xml'
- 'stream.usb\_based\_camera\_with\_a\_capture\_button'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: abbd824c-1ade-4dbc-8807-e558c444a3ea
keywords: ["filter graph configurations WDK video capture , USB-based cameras with capture button", "still pins WDK video capture", "capture buttons WDK AVStream", "USB-based cameras with capture button WDK video capture", "capturing still images WDK video capture", "still image capturing WDK video capture", "cameras WDK video capture"]
---

# USB-Based Camera with a Capture Button


A slightly more complex filter graph, compared to a [USB or 1394 based conferencing camera](usb-or-1394-based-conferencing-camera.md), is created for a conferencing camera whose minidriver exposes a still pin that supports a button to capture a still image. The still pin can provide a higher resolution image when the user pushes a button on the camera.

Vendors do not need to write a minidriver for their USB-based camera if it conforms to the UVC specification. Microsoft provides the [USB Video Class Driver](usb-video-class-driver.md) for such cameras. Microsoft recommends that any new USB based conferencing camera hardware be developed to follow the UVC specification.

Microsoft also provides the [USBCAMD Minidriver Library](usbcamd-minidriver-library.md) for backward compatibility. USBCAMD supports cameras with still pins. However, the USBCAMD interface is obsolete, and Microsoft has discontinued further its development.

The following diagram demonstrates a possible filter graph configuration for a USB-based camera with a still pin.

![diagram illustrating a possible filter graph configuration for a usb-based camera with a still pin](images/usb-camera-still.gif)

In the diagram, the still pin streams only a single image when the user pushes the button on the camera. Alternatively, the still pin can be triggered by programmatic control.

The Windows Image Acquisition (WIA) technology built on the Still Image Architecture (STI) complements the functionality provided by USBCAMD. See [Windows Image Acquisition Drivers](https://msdn.microsoft.com/library/windows/hardware/ff553346) and [Still Image Drivers](https://msdn.microsoft.com/library/windows/hardware/ff548278) for more information.

The WIA Video Snapshot filter is an addition to WIA that is shipped with Microsoft Windows XP and later operating systems. The WIA Video Snapshot filter enables still frames to be captured from the video stream.

There are two methods of capturing a still image from the device. The first is to insert the WIA Video Snapshot filter downstream from the capture filter and trigger a capture programmatically. The second is to enable still pin support by using the USBCAMD interface to develop a minidriver. The WIA Video Snapshot filter can then be triggered by pushing a button on the device.

The advantages of capturing an image from the still pin as opposed to the video stream are that the still pin can provide a higher resolution image and permit the user to capture an image by pressing a button on the device.

If still pin support isn't explicitly added to the minidriver, the WIA Video Snapshot filter can be triggered by the software, but the resolution will be the same as the video stream.

Some still pin implementations can only be rendered after the capture pin because they are based on the capture pin data formats.

For more information about WIA driver development, see the [still imaging technologies](http://go.microsoft.com/fwlink/p/?linkid=8768) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20USB-Based%20Camera%20with%20a%20Capture%20Button%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


