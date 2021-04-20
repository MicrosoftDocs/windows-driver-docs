---
title: Returning Display Modes DrvGetModes
description: Returning Display Modes DrvGetModes
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

The display driver must also support [**DrvGetModes**](/windows/win32/api/winddi/nf-winddi-drvgetmodes). This function gives GDI a pointer to an array of [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structures. The structures define the attributes of the display for the various modes that it supports, including the dimension (in both pixels and millimeters), number of planes, bits per plane, color information, and so on.

The order in which a driver writes the available display modes to memory when the [**DrvGetModes**](/windows/win32/api/winddi/nf-winddi-drvgetmodes) function is called can affect the final display mode that Windows chooses. In general, if an application does not specify a default mode, the system will select the first matching mode in the list supplied by the driver.

For example, suppose that the current display mode is

800x600x32bpp@60Hz DMDO_DEFAULT DMDFO_CENTER

and the driver specifies the list of available display modes as follows:

| Mode | Mode details |
| ---- | ------------ |
| **A** | 600x800x32bpp@60Hz DMDO_270 DMDFO_STRETCH |
| **B** | 600x800x32bpp@60Hz DMDO_90 DMDFO_STRETCH |
| **C** | 600x800x32bpp@60Hz DMDO_90 DMDFO_CENTER |
| **D** | 600x800x32bpp@60Hz DMDO_270 DMDFO_CENTER |

* **Case 1**

  If an application attempts to set the monitor to 600x800x32bpp@60Hz, but the DM_DISPLAYORIENTATION and DM_DISPLAYFIXEDOUTPUT flags are not set in the **dmFields** member of [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew), the system must choose the orientation and fixed output modes. In this case the system will choose display mode **C** because it is the first listed mode that matches the current DMDFO_CENTER setting.

* **Case 2**

  If the application attempts to set the monitor to 600x800x32bpp@60Hz DMDFO_STRETCH, the system will choose display mode **A**.

* **Case 3**

  If the application attempts to set the monitor to 600x800x32bpp@60Hz DMDO_270, the system will choose display mode **D**.

* **Case 4**

  If the application attempts to set the monitor to 600x800x32bpp@60Hz DMDO_DEFAULT, the system will fail to find an acceptable match.

One exception applies to these rules: when the system seeks a match for the display orientation, and the orientation is not specified and the current mode cannot be matched, the system will give DMDO_DEFAULT priority over other display orientations.

For example, suppose that the current display mode is

600x800x32bpp@60Hz DMDO_90 DMDFO_STRETCH

and the driver specifies the list of available display modes as follows:

| Mode | Mode details |
| ---- | ------------ |
| **A** | 800x600x32bpp@60Hz DMDO_180 DMDFO_CENTER |
| **B** | 800x600x32bpp@60Hz DMDO_180 DMDFO_STRETCH |
| **C** | 800x600x32bpp@60Hz DMDO_DEFAULT DMDFO_CENTER |
| **D** | 800x600x32bpp@60Hz DMDO_DEFAULT DMDFO_STRETCH |

In this situation, if the application attempts to set the monitor to 800x600x32bpp@60Hz, the system will choose display mode **D**.
