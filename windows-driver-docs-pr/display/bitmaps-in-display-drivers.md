---
title: Bitmaps in Display Drivers
description: Bitmaps in Display Drivers
keywords:
- display drivers WDK Windows 2000 , bitmaps
- bitmaps WDK Windows 2000 display
- bit-block transfers WDK Windows 2000 display
- off-screen memory WDK Windows 2000 display
ms.date: 04/20/2017
---

# Bitmaps in Display Drivers


## <span id="ddk_bitmaps_in_display_drivers_gg"></span><span id="DDK_BITMAPS_IN_DISPLAY_DRIVERS_GG"></span>


Certain devices, such as the 16-color VGA display, can more rapidly perform bit-block transfers from nonstandard bitmaps. To support this, a driver can hook [**DrvCreateDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-drvcreatedevicebitmap) which allows the driver to create a bitmap that a driver manages completely. When a driver creates such a bitmap, the driver can store it in any format. The driver examines the passed parameters and provides a bitmap with at least as many bits-per-pixel as requested. The contents of the bitmap are undefined after creation. If the application requests a device-managed bitmap, GDI calls the driver for [drawing functions](optional-display-driver-functions.md) after **DrvCreateDeviceBitmap** returns control. If the driver returns **FALSE**, the driver-managed bitmap is not created, so GDI can handle drawing operations on an *engine-managed surface*.

The [**DrvSaveScreenBits**](/windows/win32/api/winddi/nf-winddi-drvsavescreenbits) function is also related to bit-block transfers in display drivers. Some display drivers can move data to or from off-screen device memory more rapidly than an area can be redrawn or copied from a *DIB*. These drivers can hook **DrvSaveScreenBits**, which lets the driver be called to save or restore a specified rectangle of a displayed image more quickly when a menu or dialog box appears.

**Note**   For bit-block transfer calls, GDI (not the driver) handles *pointer exclusion* and *clip region locking*.

 


Drivers that implement device bitmaps in [*off-screen memory*](video-present-network-terminology.md#off_screen_memory) can significantly improve system performance. Off-screen device bitmaps improve system performance by:

-   Using accelerator hardware in place of GDI to draw.

-   Improving the speed of bitmap-to-screen bit-block transfers.

-   Reducing demands on main memory (a bitmap stored in off-screen memory isn't taking up space in main memory).

-   Leveraging hardware to perform operations that support OpenGL, such as mask bit-block transfers and double-buffering.


Drivers should implement device bitmaps in off-screen memory through [**DrvCreateDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-drvcreatedevicebitmap).

