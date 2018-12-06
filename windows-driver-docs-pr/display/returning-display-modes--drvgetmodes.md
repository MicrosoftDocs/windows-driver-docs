---
title: Returning Display Modes DrvGetModes
description: Returning Display Modes DrvGetModes
ms.assetid: 1010235a-0609-4380-8b83-7d8c649c2404
keywords:
- display drivers WDK Windows 2000 , desktop management
- desktop management WDK Windows 2000 display
- returning display modes WDK Windows 2000 display
- DrvGetModes
- display modes WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning Display Modes: DrvGetModes


## <span id="ddk_returning_display_modes_drvgetmodes_gg"></span><span id="DDK_RETURNING_DISPLAY_MODES_DRVGETMODES_GG"></span>


The display driver must also support [**DrvGetModes**](https://msdn.microsoft.com/library/windows/hardware/ff556233). This function gives GDI a pointer to an array of [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structures. The structures define the attributes of the display for the various modes that it supports, including the dimension (in both pixels and millimeters), number of planes, bits per plane, color information, and so on.

The order in which a driver writes the available display modes to memory when the [**DrvGetModes**](https://msdn.microsoft.com/library/windows/hardware/ff556233) function is called can affect the final display mode that Windows chooses. In general, if an application does not specify a default mode, the system will select the first matching mode in the list supplied by the driver.

For example, suppose that the current display mode is

800x600x32bpp@60Hz DMDO\_DEFAULT DMDFO\_CENTER

and the driver specifies the list of available display modes as follows:

**A.** 600x800x32bpp@60Hz DMDO\_270 DMDFO\_STRETCH

**B.** 600x800x32bpp@60Hz DMDO\_90 DMDFO\_STRETCH

**C.** 600x800x32bpp@60Hz DMDO\_90 DMDFO\_CENTER

**D.** 600x800x32bpp@60Hz DMDO\_270 DMDFO\_CENTER

**Case 1**

If an application attempts to set the monitor to 600x800x32bpp@60Hz, but the DM\_DISPLAYORIENTATION and DM\_DISPLAYFIXEDOUTPUT flags are not set in the **dmFields** member of [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837), the system must choose the orientation and fixed output modes. In this case the system will choose display mode C because it is the first listed mode that matches the current DMDFO\_CENTER setting.

**Case 2**

If the application attempts to set the monitor to 600x800x32bpp@60Hz DMDFO\_STRETCH, the system will choose display mode A.

**Case 3**

If the application attempts to set the monitor to 600x800x32bpp@60Hz DMDO\_270, the system will choose display mode D.

**Case 4**

If the application attempts to set the monitor to 600x800x32bpp@60Hz DMDO\_DEFAULT, the system will fail to find an acceptable match.

One exception applies to these rules: when the system seeks a match for the display orientation, and the orientation is not specified and the current mode cannot be matched, the system will give DMDO\_DEFAULT priority over other display orientations.

For example, suppose that the current display mode is

600x800x32bpp@60Hz DMDO\_90 DMDFO\_STRETCH

and the driver specifies the list of available display modes as follows:

**A.** 800x600x32bpp@60Hz DMDO\_180 DMDFO\_CENTER

**B.** 800x600x32bpp@60Hz DMDO\_180 DMDFO\_STRETCH

**C.** 800x600x32bpp@60Hz DMDO\_DEFAULT DMDFO\_CENTER

**D.** 800x600x32bpp@60Hz DMDO\_DEFAULT DMDFO\_STRETCH

In this situation, if the application attempts to set the monitor to 800x600x32bpp@60Hz, the system will choose display mode D.

 

 





