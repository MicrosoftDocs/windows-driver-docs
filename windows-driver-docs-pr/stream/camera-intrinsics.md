---
title: Camera intrinsics
description: Provides information about camera intrinsics.
ms.author: windowsdriverdev
ms.date: 06/11/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Camera intrinsics

A camera driver (or through DMFT) can attach camera intrinsics attribute to either stream attribute store using GUID [MFStreamExtension_PinholeCameraIntrinsics](https://msdn.microsoft.com/en-us/library/windows/desktop/mt740401), or attach to each media frame attribute store using GUID [MFSampleExtension_PinholeCameraIntrinsics](https://msdn.microsoft.com/en-us/library/windows/desktop/mt740399).    If it is attached to the stream attribute store, the values of camera intrinsics does not change during camera streaming. If it is attached to the media frame attribute store, then the intrinsics value might change for every frame. 

For above two attributes, the value must be a structure of type [MFPinholeCameraIntrinsics](https://msdn.microsoft.com/en-us/library/windows/desktop/mt740396), which reports a list of camera intrinsic models. Each entry in this list is with type [MFPinholeCameraIntrinsic_IntrinsicModel](https://msdn.microsoft.com/en-us/library/windows/desktop/mt740397), containing a resolution (width/height), pinhole model, and [MFCameraIntrinsic_DistortionModel](https://msdn.microsoft.com/en-us/library/windows/desktop/mt740394) distortion model. 

When using **MFPinholeCameraIntrinsics** with Stream attribute store, this list must contains at least one, and possibly many intrinsic models. The system will pick the intrinsics model based on the actively streaming frame format by matching the width/height of the frames. If an exact match is found, the intrinsics will be used.  Otherwise, the first intrinsics with same aspect ratio will be used instead. For example, when the list contains two entries, with 640x480 and 1920x1080 respectively. If streaming with 1280x720 media format, the 1080p intrinsics will be used with proper scaling. 

When using **MFPinholeCameraIntrinsics** with media frame attribute store, this list must contain exactly one intrinsics model with exact resolution as the frame resolution.
