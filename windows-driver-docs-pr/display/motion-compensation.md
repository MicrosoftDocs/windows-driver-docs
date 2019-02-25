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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Motion Compensation


## <span id="ddk_motion_compensation_gg"></span><span id="DDK_MOTION_COMPENSATION_GG"></span>


Motion compensation is the term for an important stage of the decoding process for compressed digital video. Many graphic accelerator devices provide some type of acceleration capability for supporting compressed video decoding. Because the motion compensation process is the most frequently supported part of video decoding, the device driver interface that supports compressed video decoding is called the motion compensation DDI. In addition to motion compensation, some devices can perform IDCT (Inverse Discrete Cosine Transformation) and other hardware functions that a software video decoder can use to accelerate the decoding process. The motion compensation DDI is flexible enough to handle devices that provide these other capabilities as well.

The input data to a software MPEG decoder is well defined. If the decoder is designed for MPEG-2, the input is in MPEG-2 format. The output of the decoder is also well defined. It is an uncompressed frame in a variety of formats. However, the interim formats between the software decoders and the display devices are not well defined, with many devices requiring their own proprietary data formats. Therefore, the motion compensation device driver interface is flexible and the interim formats are described as GUIDs. The display driver reports the GUIDs that represent the capabilities it supports, and the software decoder chooses the GUID that best matches its requirements.

To enable motion compensation functionality, the driver must perform the following steps:

-   Implement a [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) function and set the **GetDriverInfo** member of the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure to point to this function when [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) is called. The driver's *DdGetDriverInfo* function must parse the GUID\_MotionCompCallbacks GUID.

-   Fill in a [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure with the appropriate driver callback pointers and callback type flags set when the *DdGetDriverInfo* function is called with the GUID\_MotionCompCallbacks GUID. The driver must then copy this initialized structure into the Microsoft DirectDraw-allocated buffer to which the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) structure points, and return the number of bytes written into the buffer in **dwActualSize**.

 

 





