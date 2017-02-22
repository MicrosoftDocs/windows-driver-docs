---
title: Windows 2000 Driver Initialization
description: Windows 2000 Driver Initialization
ms.assetid: 82222357-1e5a-4aec-879a-68f19f3faa4f
keywords: ["DirectDraw driver initialization WDK Windows 2000 display , Windows 2000", "Windows 2000 display driver model WDK , DirectDraw"]
---

# Windows 2000 Driver Initialization


## <span id="ddk_windows_2000_driver_initialization_gg"></span><span id="DDK_WINDOWS_2000_DRIVER_INITIALIZATION_GG"></span>


On Windows 2000 and later, driver information is only retrieved when requested by an application. In other words, in response to a Microsoft DirectDraw application's request to create an instance of a DirectDraw object, the graphics engine calls the driver functions to initialize a DirectDraw driver.

Starting with Windows 2000, this sequence is done at boot time and after each mode change. This has a side effect. On Windows 98/Me, drivers typically have two modes of operation--GDI mode and DirectDraw mode. If DirectDraw is running, it will not let GDI cache bitmaps, instead giving all of the memory to DirectDraw (and vice versa when in GDI mode). This behavior caused windowed applications (such as webpages that use DirectX) to suffer. Therefore, on Windows 2000 and later, GDI and DirectDraw are required to cooperate about how memory is used. The Permedia3 sample driver that ships with the Windows Driver Development Kit (DDK) has examples of how to do this. (The DDK preceded the Windows Driver Kit \[WDK\].)

The driver initialization sequence is achieved by calling the following functions:

-   [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) to retrieve information about the hardware's capabilities. GDI calls this function twice:

    -   The first call determines the size of the display memory heap and the number of FOURCCs that the driver supports. GDI passes **NULL** for both *pvmList* and *pdwFourCC* parameters. The driver should initialize and return *pdwNumHeaps* and *pdwNumFourCC* parameters only.
    -   The second call is made after GDI allocates display memory and FOURCC memory based on the values returned from the first call in *pdwNumHeaps* and *pdwNumFourCC* parameters. In the second call, the driver should initialize and return *pdwNumHeaps*, *pvmList*, *pdwNumFourCC*, and *pdwFourCC* parameters.

    GDI allocates and zero-initializes the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure to which *pHalInfo* points. *DrvGetDirectDrawInfo* function should fill in the pertinent members of the DD\_HALINFO structure with driver-specific information:

    -   The driver should initialize the appropriate members of the [**VIDEOMEMORYINFO**](https://msdn.microsoft.com/library/windows/hardware/ff570172) structures to describe the general format of the display's memory. See [Display Memory](display-memory.md).
    -   The driver should initialize the appropriate members of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure to describe the driver's core capabilities to DirectDraw.
    -   If the driver supports any of the DirectX features that are queried by sending a GUID to the driver's [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) callback, the driver must initialize the **GetDriverInfo** member to point to the driver's *DdGetDriverInfo* callback and set the DDHALINFO\_GETDRIVERINFOSET bit in **dwFlags**.
    -   The driver must set **dwSize** to the size, in bytes, of the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure.
-   [**DrvEnableDirectDraw**](https://msdn.microsoft.com/library/windows/hardware/ff556208) is used by the runtime to enable the DirectDraw hardware and determine some of the driver's callback support. GDI allocates and zero-initializes the [**DD\_CALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff550485), [**DD\_SURFACECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551721), and [**DD\_PALETTECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551681) parameter structures. The driver should do the following for each of these callbacks that it implements:

    -   Set the corresponding member of the appropriate structure to point to the callback.
    -   Set the corresponding DDHAL\_*XXX*\_*XXX* bit in the **dwFlags** member of the appropriate structure.

    The driver can implement its *DrvEnableDirectDraw* function to indicate that it supports the callback functions listed in [DirectDraw Callback Support Using DrvEnableDirectDraw](directdraw-callback-support-using-drvenabledirectdraw.md).

    A driver's *DrvEnableDirectDraw* implementation can also dedicate hardware resources such as display memory for use by DirectDraw only.

-   [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) to retrieve the other callback functions and capabilities that the driver supports.

    If it is not **NULL**, the **GetDriverInfo** callback is returned in the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure by the driver's [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229). GDI allocates and initializes the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) structure and calls *DdGetDriverInfo* for each of the GUIDs described in the **DD\_GETDRIVERINFODATA** reference section. All GUIDs are defined in *ddrawint.h*.

    The driver can implement its *DdGetDriverInfo* function to indicate that it supports the callback functions specified in [DirectDraw and Direct3D Callback Support Using DdGetDriverInfo](directdraw-and-direct3d-callback-support-using-ddgetdriverinfo.md).

Locking the surface memory (whether the whole surface or part of a surface) ensures that an application and the hardware cannot obtain access to the surface memory at the same time. This prevents errors from occurring while an application is writing to surface memory. In addition, an application cannot page flip until the surface memory is unlocked.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windows%202000%20Driver%20Initialization%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




