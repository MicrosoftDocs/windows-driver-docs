---
title: Windows 2000 Driver Initialization
description: Windows 2000 Driver Initialization
keywords:
- DirectDraw driver initialization WDK Windows 2000 display , Windows 2000
- Windows 2000 display driver model WDK , DirectDraw
ms.date: 04/20/2017
---

# Windows 2000 Driver Initialization


## <span id="ddk_windows_2000_driver_initialization_gg"></span><span id="DDK_WINDOWS_2000_DRIVER_INITIALIZATION_GG"></span>


On Windows 2000 and later, driver information is only retrieved when requested by an application. In other words, in response to a Microsoft DirectDraw application's request to create an instance of a DirectDraw object, the graphics engine calls the driver functions to initialize a DirectDraw driver.

Starting with Windows 2000, this sequence is done at boot time and after each mode change. This has a side effect. On Windows 98/Me, drivers typically have two modes of operation--GDI mode and DirectDraw mode. If DirectDraw is running, it will not let GDI cache bitmaps, instead giving all of the memory to DirectDraw (and vice versa when in GDI mode). This behavior caused windowed applications (such as webpages that use DirectX) to suffer. Therefore, on Windows 2000 and later, GDI and DirectDraw are required to cooperate about how memory is used. The Permedia3 sample driver that ships with the Windows Driver Development Kit (DDK) has examples of how to do this. (The DDK preceded the Windows Driver Kit \[WDK\].)

The driver initialization sequence is achieved by calling the following functions:

-   [**DrvGetDirectDrawInfo**](/windows/win32/api/winddi/nf-winddi-drvgetdirectdrawinfo) to retrieve information about the hardware's capabilities. GDI calls this function twice:

    -   The first call determines the size of the display memory heap and the number of FOURCCs that the driver supports. GDI passes **NULL** for both *pvmList* and *pdwFourCC* parameters. The driver should initialize and return *pdwNumHeaps* and *pdwNumFourCC* parameters only.
    -   The second call is made after GDI allocates display memory and FOURCC memory based on the values returned from the first call in *pdwNumHeaps* and *pdwNumFourCC* parameters. In the second call, the driver should initialize and return *pdwNumHeaps*, *pvmList*, *pdwNumFourCC*, and *pdwFourCC* parameters.

    GDI allocates and zero-initializes the [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo) structure to which *pHalInfo* points. *DrvGetDirectDrawInfo* function should fill in the pertinent members of the DD\_HALINFO structure with driver-specific information:

    -   The driver should initialize the appropriate members of the [**VIDEOMEMORYINFO**](/windows/win32/api/ddrawint/ns-ddrawint-videomemoryinfo) structures to describe the general format of the display's memory. See [Display Memory](display-memory.md).
    -   The driver should initialize the appropriate members of the [**DDCORECAPS**](/windows/win32/api/ddrawi/ns-ddrawi-ddcorecaps) structure to describe the driver's core capabilities to DirectDraw.
    -   If the driver supports any of the DirectX features that are queried by sending a GUID to the driver's [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo) callback, the driver must initialize the **GetDriverInfo** member to point to the driver's *DdGetDriverInfo* callback and set the DDHALINFO\_GETDRIVERINFOSET bit in **dwFlags**.
    -   The driver must set **dwSize** to the size, in bytes, of the [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo) structure.
-   [**DrvEnableDirectDraw**](/windows/win32/api/winddi/nf-winddi-drvenabledirectdraw) is used by the runtime to enable the DirectDraw hardware and determine some of the driver's callback support. GDI allocates and zero-initializes the [**DD\_CALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_callbacks), [**DD\_SURFACECALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surfacecallbacks), and [**DD\_PALETTECALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_palettecallbacks) parameter structures. The driver should do the following for each of these callbacks that it implements:

    -   Set the corresponding member of the appropriate structure to point to the callback.
    -   Set the corresponding DDHAL\_*XXX*\_*XXX* bit in the **dwFlags** member of the appropriate structure.

    The driver can implement its *DrvEnableDirectDraw* function to indicate that it supports the callback functions listed in [DirectDraw Callback Support Using DrvEnableDirectDraw](directdraw-callback-support-using-drvenabledirectdraw.md).

    A driver's *DrvEnableDirectDraw* implementation can also dedicate hardware resources such as display memory for use by DirectDraw only.

-   [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo) to retrieve the other callback functions and capabilities that the driver supports.

    If it is not **NULL**, the **GetDriverInfo** callback is returned in the [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo) structure by the driver's [**DrvGetDirectDrawInfo**](/windows/win32/api/winddi/nf-winddi-drvgetdirectdrawinfo). GDI allocates and initializes the [**DD\_GETDRIVERINFODATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_getdriverinfodata) structure and calls *DdGetDriverInfo* for each of the GUIDs described in the **DD\_GETDRIVERINFODATA** reference section. All GUIDs are defined in *ddrawint.h*.

    The driver can implement its *DdGetDriverInfo* function to indicate that it supports the callback functions specified in [DirectDraw and Direct3D Callback Support Using DdGetDriverInfo](directdraw-and-direct3d-callback-support-using-ddgetdriverinfo.md).

Locking the surface memory (whether the whole surface or part of a surface) ensures that an application and the hardware cannot obtain access to the surface memory at the same time. This prevents errors from occurring while an application is writing to surface memory. In addition, an application cannot page flip until the surface memory is unlocked.

 

