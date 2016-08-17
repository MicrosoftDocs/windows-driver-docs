---
title: Developing a WIA Video Driver
description: Developing a WIA Video Driver
MS-HAID:
- 'WIA\_drv\_cus\_1c8438e5-89dd-4625-ae56-2470ce939c02.xml'
- 'image.developing\_a\_wia\_video\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3cf14fd3-1dfa-480e-a69c-c4d2c196a504
---

# Developing a WIA Video Driver


## <a href="" id="ddk-developing-a-wia-video-driver-si"></a>


WIA supports video and video cameras. A video camera that is going to work with WIA should use the video drivers that ship with Windows Me, Windows XP and later operating system versions, or develop DirectShow video drivers. WIA relies on DirectShow to get still images from a video stream.

Only a few modifications to the INF file of a DirectShow driver are necessary for WIA to recognize it as a supported camera. The necessary changes are:

```
[Device]
Include= sti.inf
Needs= STI.WIAVideo.Registration
SubClass=StillImage
DeviceType=3
DeviceSubType=0x1
Capabilities=0x00000031
ICMProfiles="sRGB Color Space Profile.icm"
```

If you do not make these additions WIA will not recognize the device. Be sure to *add* these changes to your INF file. Do not replace your INF file with only these lines.

For an example of how to support WIA from a video camera using USBCAMD model with a still pin from your driver see [USB-Based Camera with a Capture Button](https://msdn.microsoft.com/library/windows/hardware/ff568643).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Developing%20a%20WIA%20Video%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




