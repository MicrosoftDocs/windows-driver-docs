---
title: Path Priority Order
description: Path Priority Order
keywords:
- connecting displays WDK Windows 7 display , CCD concepts, path priority order
- connecting displays WDK Windows Server 2008 R2 display , CCD concepts, path priority order
- configuring displays WDK Windows 7 display , CCD concepts, path priority order
- configuring displays WDK Windows Server 2008 R2 display , CCD concepts, path priority order
- CCD concepts WDK Windows 7 display , path priority order
- CCD concepts WDK Windows Server 2008 R2 display , path priority order
- path priority order WDK Windows 7 display
- path priority order WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Path Priority Order


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) CCD function determines that the active paths within the path array that is specified by the *pathArray* parameter are ordered such that **SetDisplayConfig** gives higher priority to lower number array path elements. The following items impact the ordering:

-   If [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) does not find an existing display configuration, **SetDisplayConfig** uses the path priority during the best mode logic in the search order. Therefore, **SetDisplayConfig** is more likely to satisfy a higher priority path at native resolution than a lower priority path.

-   In cloned paths, the highest priority path is the path on which flips are scheduled. Therefore, lower priority paths can be subject to minor tearing.

-   The DirectX graphics kernel subsystem uses the path priority (along with the GDI primary view) to derive the path-importance value that the subsystem passes to the **ImportanceOrdinal** member of the [**D3DKMDT\_VIDPN\_PRESENT\_PATH**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path) structure in a call to the display miniport driver. The path-importance value impacts driver decisions, such as, to which path the driver should give priority in resource allocations. For example, the lower-ordinal path might have better access to overlays or to a higher quality controller.

The [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) CCD function always returns the paths in priority order. If the QDC\_ALL\_PATHS flag is set in the *Flags* parameter of **QueryDisplayConfig**, **QueryDisplayConfig** returns all of the inactive path combinations following all the active path combinations in the paths array that the *pPathInfoArray* parameter specifies.

 

