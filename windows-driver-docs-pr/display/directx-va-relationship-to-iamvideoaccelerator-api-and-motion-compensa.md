---
title: DirectX VA Relationship to IAMVideoAccelerator API and Motion Compensation DDI
description: DirectX VA Relationship to IAMVideoAccelerator API and Motion Compensation DDI
ms.assetid: 8bfa198f-b29f-491f-8133-a1f3b41e0cbe
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , IAMVideoAccelerator
- Video Acceleration WDK DirectX , IAMVideoAccelerator
- VA WDK DirectX , IAMVideoAccelerator
- IAMVideoAcceleratorNotify
- IAMVideoAccelerator
- video mixing renderer WDK DirectX VA
- VMR WDK DirectX VA
- overlay mixer WDK DirectX VA
- OVM WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectX VA Relationship to IAMVideoAccelerator API and Motion Compensation DDI


## <span id="ddk_directx_va_relationship_to_iamvideoaccelerator_api_and_motion_comp"></span><span id="DDK_DIRECTX_VA_RELATIONSHIP_TO_IAMVIDEOACCELERATOR_API_AND_MOTION_COMP"></span>


DirectX VA uses the **IAMVideoAcceleratorNotify** and **IAMVideoAccelerator** interfaces (documented in the Microsoft Windows SDK), and the [motion compensation DDI](motion-compensation.md) to specify the format of the data exchanged between the software decoder, the video mixing renderer (VMR) or the overlay mixer (OVM), and the video display driver. The following figure shows the relationship of these interfaces to the software decoder, VMR, and video display driver.

![diagram illustrating directx va data flow](images/iamvideo.png)

The **IAMVideoAcceleratorNotify** interface retrieves or sets decompressed buffer information for a given video accelerator GUID.

The **IAMVideoAccelerator** interface enables a video decoder filter to access the functionality of a video accelerator and provides video rendering using the video mixing renderer (VMR) or the overlay mixer (OVM).

The motion compensation DDI establishes a common interface to access hardware acceleration capabilities and allow cross-vendor compatibility between user-mode software applications and acceleration capabilities. The DDI notifies the decoder when a video acceleration object is being used, starts and stops the decoding of frame buffers, indicates the uncompressed picture formats that the hardware supports, and notifies the display driver of the macroblocks that need to be rendered. The motion compensation DDI is accessed through the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure.

For more information about the **IAMVideoAccelerator** and **IAMVideoAcceleratorNotify** interfaces, see the Windows SDK documentation. For more information about the motion compensation DDI, see [Motion Compensation](motion-compensation.md) and [Motion Compensation Callbacks](motion-compensation-callbacks.md).

 

 





