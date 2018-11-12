---
title: Tracking Window Changes
description: Tracking Window Changes
ms.assetid: 76539ee8-439a-4c6a-b16a-3998e341f954
keywords:
- display drivers WDK Windows 2000 , window changes
- window change tracking WDK Windows 2000 display
- WNDOBJ
- client region changes WDK Windows 2000 display
- visible client regions WDK Windows 2000 display
- size WDK Windows 2000 display
- positions WDK Windows 2000 display
- tracking window changes WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tracking Window Changes


## <span id="ddk_tracking_window_changes_gg"></span><span id="DDK_TRACKING_WINDOW_CHANGES_GG"></span>


Changes to a window, including one in a [multiple-monitor system](multiple-monitor-support-in-the-display-driver.md), can be tracked by a device driver through a [**WNDOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570599). A WNDOBJ is a driver-level window object that contains information about the position, size, and the visible client region of a window. That is, by creating a WNDOBJ that corresponds to an application window, the driver can track the size, position, and client region changes in that window.

An application uses the Win32 API to access the **WNDOBJ\_SETUP** functionality implemented by the device driver. Access is gained through the Win32 **ExtEscape** function. GDI passes this escape call to the device driver with [**DrvEscape**](https://msdn.microsoft.com/library/windows/hardware/ff556217), implemented by the device driver with **WNDOBJ\_SETUP** for the value of *iEsc*.

An application calls <strong>ExtEscape(</strong>hdc, WNDOBJ\_SETUP,...**)** and passes a handle to the application-created window (created by **CreateWindow** or some equivalent Win32 function) through the input buffer to the driver. If the driver is to keep track of the window, it calls [**EngCreateWnd**](https://msdn.microsoft.com/library/windows/hardware/ff564769), within the context of the **ExtEscape** call, to create a WNDOBJ structure for the given window. From that point on, any changes to that window will pass down to the driver.

The driver should handle the **ExtEscape** call in a manner similar to the following:

```cpp
ULONG DrvEscape(
  SURFOBJ *pso,
  ULONG    iEsc,
  ULONG    cjIn,
  PVOID    pvIn,
  ULONG    cjOut,
  PVOID    pvOut)
{
    WNDOBJ *pwo;
    WNDDATA *pwd;

    if (iEsc == WNDOBJ_SETUP)
    {
        pwo = EngCreateWnd(pso,*((HWND *)pvIn),&DrvVideo,
                           WO_RGN_CLIENT, 0);

    // Allocate space for caching client rects. Remember the pointer
    // in the pvConsumer field.

        pwd = EngAllocMem(0, sizeof(WNDDATA), DRIVER_TAG);
        WNDOBJ_vSetConsumer(pwo,pwd);

    // Update the rectangle list for this wndobj.

        vUpdateRects(pwo);
        return(1);
    }

}
```

Creating a window object involves locking special window resources, therefore [**EngCreateWnd**](https://msdn.microsoft.com/library/windows/hardware/ff564769) should be called only in the context of the **WNDOBJ\_SETUP** escape in [**DrvEscape**](https://msdn.microsoft.com/library/windows/hardware/ff556217) or [**DrvSetPixelFormat**](https://msdn.microsoft.com/library/windows/hardware/ff556285).

The **EngCreateWnd** function supports window tracking by multiple drivers. Through **EngCreateWnd**, each driver identifies its own callback routine that GDI is to call for changes to the corresponding window. This feature allows, for example, a live video driver to track changes to live video windows while an OpenGL driver is tracking changes to OpenGL windows.

GDI will call back to the driver with the most recent window states if a new [**WNDOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570599) is created in *DrvSetPixelFormat* or **ExtEscape**. GDI will also call back to the driver when a window referenced by a WNDOBJ is destroyed.

As an accelerator, the driver may access public members of the [**WNDOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570599) structure.

Tracking window changes involves the use of three callback functions provided to support the WNDOBJ structure. The visible client region may be enumerated by calling the [**WNDOBJ\_cEnumStart**](https://msdn.microsoft.com/library/windows/hardware/ff570603) and [**WNDOBJ\_bEnum**](https://msdn.microsoft.com/library/windows/hardware/ff570602) callback functions. A driver may associate its own data with a WNDOBJ by calling the [**WNDOBJ\_vSetConsumer**](https://msdn.microsoft.com/library/windows/hardware/ff570606) callback function.









