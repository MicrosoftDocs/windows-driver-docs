---
title: Optimized screen rotation support
description: Windows 8 ensures a flicker-free screen rotation experience by ensuring that the output from the graphics adapter stays enabled during a rotational mode change.
ms.assetid: CFDB4713-EC90-4FAB-B379-742C52888BB3
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Optimized%20screen%20rotation%20support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




