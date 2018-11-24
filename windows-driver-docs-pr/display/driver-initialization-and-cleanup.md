---
title: Driver Initialization and Cleanup
description: Driver Initialization and Cleanup
ms.assetid: 57f22818-a298-4f9a-87a6-5ca4d97bf32b
keywords:
- drawing WDK GDI , initialization, description
- initializing graphics drivers WDK Windows 2000 display , description
- GDI WDK Windows 2000 display , initialization, description
- graphics drivers WDK Windows 2000 display , initialization, description
- DrvEnableDriver
- drawing WDK GDI , cleanup
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Initialization and Cleanup


## <span id="ddk_driver_initialization_and_cleanup_gg"></span><span id="DDK_DRIVER_INITIALIZATION_AND_CLEANUP_GG"></span>


While the device driver may implement several or many functions, it exports only [**DrvEnableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff556210) to GDI. The driver exposes its other supported functions through a function table. The first call GDI makes to a device driver is to the **DrvEnableDriver** function. Within this function, the driver fills in the passed-in [**DRVENABLEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff556206) structure so that GDI can determine which other *DrvXxx* functions are supported and where they are located. The driver supplies the following information in DRVENABLEDATA:

-   The **iDriverVersion** member contains the graphics DDI version number for a particular Windows operating system version. The *winddi.h* header defines the following constants:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Constant</th>
    <th align="left">Operating System Version</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>DDI_DRIVER_VERSION_NT4</p></td>
    <td align="left"><p>Windows NT 4.0</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>DDI_DRIVER_VERSION_NT5</p></td>
    <td align="left"><p>Windows 2000</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>DDI_DRIVER_VERSION_NT5_01</p></td>
    <td align="left"><p>Windows XP</p></td>
    </tr>
    </tbody>
    </table>

     

For more information about how these constants are used, see [**DRVENABLEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff556206).

-   The **c** member contains the number of DRVFN structures in the array.

-   The **pdrvfn** member points to an array of [**DRVFN**](https://msdn.microsoft.com/library/windows/hardware/ff556221) structures that lists the supported functions and their indexes.

For GDI to call a function other than the driver's enable and disable functions, the driver must make the function's name and location available to GDI.

While [**DrvEnableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff556210) can also perform one-time initializations, such as the allocation of semaphores, a driver should not actually enable the hardware during **DrvEnableDriver**. Hardware initialization should occur in a driver's [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) function. Likewise, a driver should enable the surface in the [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214) function.

GDI calls the [**DrvDisableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff556196) function to notify the driver that it is about to be unloaded. In response to this call, the driver should free all resources and memory still allocated by the driver at this point.

If the hardware needs to be reset, GDI calls the driver's [**DrvAssertMode**](https://msdn.microsoft.com/library/windows/hardware/ff556178) function.

 

 





