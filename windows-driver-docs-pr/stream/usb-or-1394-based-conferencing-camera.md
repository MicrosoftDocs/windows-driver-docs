---
title: USB or 1394-Based Conferencing Camera
author: windows-driver-content
description: USB or 1394-Based Conferencing Camera
ms.assetid: 06097803-a124-4c9b-bdb4-cfd8648bc81d
keywords: ["filter graph configurations WDK video capture , USB-based video conferencing cameras", "filter graph configurations WDK video capture , 1394-based video conferencing cameras", "USB-based video conferencing cameras WDK video capture", "1394-based video conferencing cameras WDK video capture", "video conferencing cameras WDK video capture", "cameras WDK video capture"]
---

# USB or 1394-Based Conferencing Camera


A simple filter graph consists of a capture filter that exposes a single video stream with no TV/radio tuning capabilities. USB-based and 1394-based video conferencing cameras often use this configuration.

The following diagram demonstrates one of the possible filter graph configurations for a 1394-based video conferencing camera.

![diagram illustrating one of the possible filter graph configurations for a 1394-based video conferencing camera](images/conferencing-camera-1394.gif)

**Note**  : The single capture stream from the camera is replicated by a user-mode DirectShow filter (the Smart Tee filter) to provide separate capture and preview streams. This replication is performed without requiring the minidriver to copy the data.

 

Vendors do not need to write a minidriver for their USB-based camera if it conforms to the UVC specification. Microsoft provides the [USB Video Class Driver](usb-video-class-driver.md) for such cameras. Microsoft recommends that any new USB-based conferencing camera hardware be developed to follow the UVC specification.

Microsoft also provides the [USBCAMD Minidriver Library](usbcamd-minidriver-library.md) for backward compatibility. However, the USBCAMD interface is obsolete, and Microsoft has discontinued its further development.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20USB%20or%201394-Based%20Conferencing%20Camera%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


