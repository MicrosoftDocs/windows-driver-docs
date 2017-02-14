---
title: Bitmaps in Display Drivers
description: Bitmaps in Display Drivers
ms.assetid: 3f0ed208-1cfb-4583-beaf-894cd210b459
keywords: ["display drivers WDK Windows 2000 , bitmaps", "bitmaps WDK Windows 2000 display", "bit-block transfers WDK Windows 2000 display", "off-screen memory WDK Windows 2000 display"]
---

# Bitmaps in Display Drivers


## <span id="ddk_bitmaps_in_display_drivers_gg"></span><span id="DDK_BITMAPS_IN_DISPLAY_DRIVERS_GG"></span>


Certain devices, such as the 16-color VGA display, can more rapidly perform bit-block transfers from nonstandard bitmaps. To support this, a driver can hook [**DrvCreateDeviceBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff556185) which allows the driver to create a bitmap that a driver manages completely. When a driver creates such a bitmap, the driver can store it in any format. The driver examines the passed parameters and provides a bitmap with at least as many bits-per-pixel as requested. The contents of the bitmap are undefined after creation. If the application requests a device-managed bitmap, GDI calls the driver for [drawing functions](optional-display-driver-functions.md) after **DrvCreateDeviceBitmap** returns control. If the driver returns **FALSE**, the driver-managed bitmap is not created, so GDI can handle drawing operations on an [*engine-managed surface*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-engine-managed-surface).

The [**DrvSaveScreenBits**](https://msdn.microsoft.com/library/windows/hardware/ff556278) function is also related to bit-block transfers in display drivers. Some display drivers can move data to or from off-screen device memory more rapidly than an area can be redrawn or copied from a [*DIB*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-). These drivers can hook **DrvSaveScreenBits**, which lets the driver be called to save or restore a specified rectangle of a displayed image more quickly when a menu or dialog box appears.

**Note**   For bit-block transfer calls, GDI (not the driver) handles [*pointer exclusion*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pointer-exclusion) and [*clip region locking*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-clip-region-locking).

 

Drivers that implement device bitmaps in [*off-screen memory*](https://msdn.microsoft.com/library/windows/hardware/ff556318#wdkgloss-off-screen-memory) can significantly improve system performance. Off-screen device bitmaps improve system performance by:

-   Using accelerator hardware in place of GDI to draw.

-   Improving the speed of bitmap-to-screen bit-block transfers.

-   Reducing demands on main memory (a bitmap stored in off-screen memory isn't taking up space in main memory).

-   Leveraging hardware to perform operations that support OpenGL, such as mask bit-block transfers and double-buffering.

Drivers should implement device bitmaps in off-screen memory through [**DrvCreateDeviceBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff556185).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Bitmaps%20in%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




