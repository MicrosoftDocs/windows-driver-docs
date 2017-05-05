---
title: Motion Compensation
description: Motion Compensation
ms.assetid: 3b5c91f9-6c22-4110-943a-5b833f32c014
keywords:
- drawing WDK DirectDraw , motion compensation
- DirectDraw WDK Windows 2000 display , motion compensation
- motion compensation WDK
- compressed video decoding WDK DirectDraw
- video decoding WDK DirectDraw
- decoding WDK DirectDraw
- digital video decoding WDK DirectDraw
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Motion Compensation


## <span id="ddk_motion_compensation_gg"></span><span id="DDK_MOTION_COMPENSATION_GG"></span>


Motion compensation is the term for an important stage of the decoding process for compressed digital video. Many graphic accelerator devices provide some type of acceleration capability for supporting compressed video decoding. Because the motion compensation process is the most frequently supported part of video decoding, the device driver interface that supports compressed video decoding is called the motion compensation DDI. In addition to motion compensation, some devices can perform IDCT (Inverse Discrete Cosine Transformation) and other hardware functions that a software video decoder can use to accelerate the decoding process. The motion compensation DDI is flexible enough to handle devices that provide these other capabilities as well.

The input data to a software MPEG decoder is well defined. If the decoder is designed for MPEG-2, the input is in MPEG-2 format. The output of the decoder is also well defined. It is an uncompressed frame in a variety of formats. However, the interim formats between the software decoders and the display devices are not well defined, with many devices requiring their own proprietary data formats. Therefore, the motion compensation device driver interface is flexible and the interim formats are described as GUIDs. The display driver reports the GUIDs that represent the capabilities it supports, and the software decoder chooses the GUID that best matches its requirements.

To enable motion compensation functionality, the driver must perform the following steps:

-   Implement a [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) function and set the **GetDriverInfo** member of the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure to point to this function when [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) is called. The driver's *DdGetDriverInfo* function must parse the GUID\_MotionCompCallbacks GUID.

-   Fill in a [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure with the appropriate driver callback pointers and callback type flags set when the *DdGetDriverInfo* function is called with the GUID\_MotionCompCallbacks GUID. The driver must then copy this initialized structure into the Microsoft DirectDraw-allocated buffer to which the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) structure points, and return the number of bytes written into the buffer in **dwActualSize**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Motion%20Compensation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




