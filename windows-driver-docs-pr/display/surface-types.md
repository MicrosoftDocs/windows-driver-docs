---
title: Surface Types
description: Surface Types
keywords:
- DIB WDK GDI
- device-managed surfaces WDK GDI
- engine-managed surfaces WDK GDI
- surface negotiation WDK GDI , surface types
- surface types WDK GDI
- device-dependent bitmaps WDK GDI
- DDB WDK GDI
- device-independent bitmaps WDK GDI
ms.date: 04/20/2017
---

# Surface Types


## <span id="ddk_surface_types_gg"></span><span id="DDK_SURFACE_TYPES_GG"></span>


Surface types can be viewed in the context of how they are handled. The following types exist:

-   Engine-managed surfaces

-   Device-managed surfaces (standard-format bitmaps)

-   Device-managed surfaces (nonstandard-format bitmaps)

### <span id="Engine-Managed_Surfaces"></span><span id="engine-managed_surfaces"></span><span id="ENGINE-MANAGED_SURFACES"></span>Engine-Managed Surfaces

An engine-managed surface:

-   Is created and managed by GDI.

-   Is created as a device-independent bitmap (DIB) in one of the standard DIB formats: top-down, in which the origin is at the upper-left corner, or bottom-up, in which the origin is at the lower-left corner.

-   Is of type STYPE\_BITMAP.

-   Does not have a corresponding device handle to a surface.

A standard-format bitmap is a single-plane, packed-pixel (where the data for each pixel is stored in a contiguous manner) format bitmap. Each scan line of the bitmap is aligned on a four-byte boundary.

Bitmaps created in the [**EngCreateBitmap**](/windows/win32/api/winddi/nf-winddi-engcreatebitmap) function are in DIB format. A bitmap must be in DIB format for the engine to manage it.

### <span id="Device-Managed_Surfaces__Standard-Format_Bitmaps_"></span><span id="device-managed_surfaces__standard-format_bitmaps_"></span><span id="DEVICE-MANAGED_SURFACES__STANDARD-FORMAT_BITMAPS_"></span>Device-Managed Surfaces (Standard-Format Bitmaps)

A device-managed surface:

-   Is created by a call to the device driver's [**DrvCreateDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-drvcreatedevicebitmap) function.

-   Has an associated device handle to a surface (DHSURF; for more information, see [**SURFOBJ**](/windows/win32/api/winddi/ns-winddi-surfobj)).

-   Can be either *opaque* or *nonopaque*.

An opaque device-managed surface is one for which GDI has neither any information about the bitmap format nor a reference to the bits in the bitmap. For these reasons, the driver must support, at minimum, the [**DrvBitBlt**](/windows/win32/api/winddi/nf-winddi-drvbitblt), [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout), and [**DrvStrokePath**](/windows/win32/api/winddi/nf-winddi-drvstrokepath) functions. The type of such a surface is STYPE\_DEVBITMAP.

A nonopaque device-managed surface is one for which GDI has information about the bitmap format and knows the location of the bits within the bitmap. Because of this, the driver does not need to implement any drawing operations, deferring all of them to GDI. The type of such a surface is SYTPE\_BITMAP.

For a driver to convert a device-managed opaque bitmap to one that is nonopaque, it must call the [**EngModifySurface**](/windows/win32/api/winddi/nf-winddi-engmodifysurface) function. With this call, the driver is informing GDI of the bitmap format and location of the bitmap in memory.

When a driver has a device-managed DIB surface, the driver can call back to GDI to have GDI draw on the surface. A driver that is managing its own surfaces, but is using a DIB, can still refer calls back to GDI by wrapping a DIB (which is created with the [**EngCreateBitmap**](/windows/win32/api/winddi/nf-winddi-engcreatebitmap) function) around its surface. The following steps describe how the driver can have GDI draw on a device-managed DIB surface:

1.  The driver calls [**EngCreateBitmap**](/windows/win32/api/winddi/nf-winddi-engcreatebitmap) to create a DIB engine-managed surface.

2.  The driver calls the [**EngCreateDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-engcreatedevicebitmap) function to create a device-dependent bitmap (DDB) surface, which is a device-managed DIB surface.

3.  The driver internally saves the engine-managed DIB data in the device-managed DDB data.

4.  GDI always calls the driver to interact with the surface through the device-managed DDB data.

5.  When the driver receives a call from GDI and cannot handle the call (for example, the driver cannot handle complex clipping), the driver retrieves the DIB data that is stored in the DDB data and passes the DIB data to GDI to render.

### <span id="Device-Managed_Surfaces__Nonstandard-Format_Bitmaps_"></span><span id="device-managed_surfaces__nonstandard-format_bitmaps_"></span><span id="DEVICE-MANAGED_SURFACES__NONSTANDARD-FORMAT_BITMAPS_"></span>Device-Managed Surfaces (Nonstandard-Format Bitmaps)

A driver can enable a device-managed non-DIB surface by calling the [**EngCreateDeviceSurface**](/windows/win32/api/winddi/nf-winddi-engcreatedevicesurface) function to have GDI create the surface and return a handle to it. GDI relies on the driver to access, to control drawing to, and to read from a device-managed surface.

A device-dependent bitmap (DDB), which is sometimes called a device-format bitmap, is another type of non-DIB, device-managed surface. The DDB is supported to allow certain drivers, such as the VGA driver, to implement faster bitmap-to-screen block transfers. The DDB also allows drivers to draw to banked or non-DIB bitmaps in offscreen display memory. If a DDB is required, the driver can support the [**DrvCreateDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-drvcreatedevicebitmap) function and call the [**EngCreateDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-engcreatedevicebitmap) function to have the engine return a handle to the bitmap.

 

