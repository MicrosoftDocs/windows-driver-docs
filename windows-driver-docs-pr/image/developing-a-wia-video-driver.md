---
title: Developing a WIA Video Driver
description: Developing a WIA Video Driver
ms.assetid: 3cf14fd3-1dfa-480e-a69c-c4d2c196a504
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Developing a WIA Video Driver





WIA supports video and video cameras. A video camera that is going to work with WIA should use the video drivers that ship with Windows Me, Windows XP and later operating system versions, or develop DirectShow video drivers. WIA relies on DirectShow to get still images from a video stream.

Only a few modifications to the INF file of a DirectShow driver are necessary for WIA to recognize it as a supported camera. The necessary changes are:

```INF
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

 

 




