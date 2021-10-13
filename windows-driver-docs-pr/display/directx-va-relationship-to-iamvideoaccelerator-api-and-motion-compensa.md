---
title: DXVA in IAMVideoAccelerator API and Motion Compensation DDI
description: DirectX VA Relationship to IAMVideoAccelerator API and Motion Compensation DDI
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
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# DirectX VA Relationship to IAMVideoAccelerator API and Motion Compensation DDI

DirectX VA uses the **IAMVideoAcceleratorNotify** and **IAMVideoAccelerator** interfaces (documented in the Microsoft Windows SDK), and the [motion compensation DDI](motion-compensation.md) to specify the format of the data exchanged between the software decoder, the video mixing renderer (VMR) or the overlay mixer (OVM), and the video display driver. The following figure shows the relationship of these interfaces to the software decoder, VMR, and video display driver.

![diagram illustrating directx va data flow.](images/iamvideo.png)

The **IAMVideoAcceleratorNotify** interface retrieves or sets decompressed buffer information for a given video accelerator GUID.

The **IAMVideoAccelerator** interface enables a video decoder filter to access the functionality of a video accelerator and provides video rendering using the video mixing renderer (VMR) or the overlay mixer (OVM).

The motion compensation DDI establishes a common interface to access hardware acceleration capabilities and allow cross-vendor compatibility between user-mode software applications and acceleration capabilities. The DDI notifies the decoder when a video acceleration object is being used, starts and stops the decoding of frame buffers, indicates the uncompressed picture formats that the hardware supports, and notifies the display driver of the macroblocks that need to be rendered. The motion compensation DDI is accessed through the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure.

For more information about the **IAMVideoAccelerator** and **IAMVideoAcceleratorNotify** interfaces, see the Windows SDK documentation. For more information about the motion compensation DDI, see [Motion Compensation](motion-compensation.md) and [Motion Compensation Callbacks](motion-compensation-callbacks.md).

 

