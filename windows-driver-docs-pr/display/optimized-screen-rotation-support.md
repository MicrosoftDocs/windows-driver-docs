---
title: Optimized screen rotation support
description: Windows 8 ensures a flicker-free screen rotation experience by ensuring that the output from the graphics adapter stays enabled during a rotational mode change.
ms.assetid: CFDB4713-EC90-4FAB-B379-742C52888BB3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Optimized screen rotation support


Windows 8 ensures a flicker-free screen rotation experience by ensuring that the output from the graphics adapter stays enabled during a rotational mode change. This feature is required on all Windows Display Driver Model (WDDM) 1.2 drivers that support rotated modes.

**Note**  Starting with Windows 8.1 Update, device driver interfaces (DDIs) are updated to support the highest possible resolution on cloned monitors when the primary display is rotated. See [Supporting Path-Independent Rotation](supporting-path-independent-rotation.md).

 

|                                                      |           |
|------------------------------------------------------|-----------|
| Minimum WDDM version                                 | 1.2       |
| Minimum Windows version                              | 8         |
| Driver implementation—Full graphics and Display only | Mandatory |

 

## <span id="Smooth_rotation_DDI"></span><span id="smooth_rotation_ddi"></span><span id="SMOOTH_ROTATION_DDI"></span>Smooth rotation DDI


The display miniport driver must support updating the path rotation when these driver-implemented functions are called:

-   [*DxgkDdiCommitVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559597)
-   [*DxgkDdiUpdateActiveVidPnPresentPath*](https://msdn.microsoft.com/library/windows/hardware/ff560803)

The driver must indicate support for smooth rotation in a call to [*DxgkDdiUpdateActiveVidPnPresentPath*](https://msdn.microsoft.com/library/windows/hardware/ff560803) by setting the [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062) structure's **SupportSmoothRotation** member, which is available starting with Windows 8.
The driver must always be able to set the path rotation during a call to [*DxgkDdiCommitVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559597).

## <span id="Smooth_rotation_scenarios"></span><span id="smooth_rotation_scenarios"></span><span id="SMOOTH_ROTATION_SCENARIOS"></span>Smooth rotation scenarios


On traditional desktop and laptop systems, screen rotation is not a frequently used scenario. But in mobile devices, screen rotation is often a mainstream scenario. Windows 8 enables optimizations to the display infrastructure to ensure that the monitor synchronization stays enabled during screen rotation. End users can experience a smooth rotation transition when the following are true:

-   The platform is running WDDM 1.2.
-   The desktop composition manager is on and is actively composing.
-   The mode change request is determined to be compatible with smooth rotation mode transition. Two modes are compatible if they have the same dimensions (width and height), topology, refresh rates, pixel formats, and stride, and differ only in screen orientation (that is, are rotated).

 

 





