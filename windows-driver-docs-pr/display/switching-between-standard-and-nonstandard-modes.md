---
title: Switching Between Standard and Nonstandard Modes
description: Switching Between Standard and Nonstandard Modes
ms.assetid: 15939910-b325-47ff-b4ed-bbaeec4149bd
keywords:
- nonstandard display modes WDK DirectX 9.0 , switching between standard and nonstandard modes
- switching between standard and nonstandard modes WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Switching Between Standard and Nonstandard Modes


## <span id="ddk_switching_between_standard_and_nonstandard_modes_gg"></span><span id="DDK_SWITCHING_BETWEEN_STANDARD_AND_NONSTANDARD_MODES_GG"></span>


A DirectX 9.0 driver creates the standard primary surface for a standard display mode and a dummy primary surface for the nonstandard mode so that the runtime can switch between modes when necessary. Both surfaces represent the same video memory, except displayed in different formats. The driver switches between standard and nonstandard modes when a page flip is requested as shown in the following sequence:

1.  The application requests a mode switch.

    An application calls the **ChangeDisplaySettings** function to change video mode to a matching bit depth. For the 10:10:10:2 mode, the bit depth is 32 bits per pixel. For more information about **ChangeDisplaySettings**, see documentation for the Microsoft Windows SDK.

2.  The driver creates the standard primary surface.

    The runtime calls the driver's [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) function to request the creation of the primary surface. This primary surface uses the standard display format (for example, D3DFMT\_A8B8G8R8) and has no back buffers.

3.  The driver creates the dummy primary surface chain.

    The runtime calls the driver's *DdCreateSurface* function to request the creation of the dummy primary surface. The runtime specifies the DDSCAPS2\_EXTENDEDFORMATPRIMARY (0x40000000) capability bit in the **dwCaps2** member of the [**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292) structure for this surface to indicate that the surface uses a nonstandard display mode (for example, D3DFMT\_A2R10G10B10). The runtime also specifies the DDSCAPS\_OFFSCREENPLAIN capability bit in the **dwCaps** member of DDSCAPS2 to indicate that the surface has an explicit pixel format.

    Because this surface is intended to be just another name for the existing primary surface, the driver should not allocate further video memory to the surface.

    For this surface, the runtime also specifies the DDSCAPS\_FLIP and DDSCAPS\_COMPLEX capability bits in **dwCaps** and an attached set of back buffers similarly to the way the runtime sets up a standard primary surface flipping chain. The driver should allocate video memory for these back buffers because no further calls to the driver's *DdCreateSurface* function are made for these back buffers; that is, the runtime creates more than one surface object only for the standard primary.

4.  The driver flips the surface to the nonstandard format.

    While the display device outputs the standard format, the application composes a nonstandard image in one of these back buffers. Once this image is ready for display, the runtime specifies one of the nonstandard surfaces as the target in a call to the driver's [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) function. The driver then reprograms the display device to output the nonstandard format.

5.  The application runs.

    The application generates further calls to the driver's *DdFlip* function between the nonstandard buffers, and the driver continues to display the nonstandard format. The application can also generate calls to the driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function using the D3DDP2OP\_BLT operation code to copy the back buffer to the front buffer, but these calls are always made between two nonstandard surface objects. Unless the driver supports the nonstandard format in windowed mode, the driver does not process blts between nonstandard and standard surface formats. For more information about the windowed-mode case, see [Supporting Two-Dimensional Operations](supporting-two-dimensional-operations.md).

6.  The driver flips the surface back to standard format.

    When the application is closed or minimized, the runtime specifies the standard-format primary surface as the destination in a call to the driver's *DdFlip* function. The driver then reprograms the display device to output the standard format.

7.  The driver destroys the dummy surface.

    When the driver destroys the dummy surface, it should ensure that the standard format is reprogrammed in the display device.

 

 





