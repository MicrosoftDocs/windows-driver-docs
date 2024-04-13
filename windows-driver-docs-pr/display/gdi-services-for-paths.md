---
title: GDI Services for Paths
description: GDI Services for Paths
keywords:
- GDI WDK Windows 2000 display , paths
- graphics drivers WDK Windows 2000 display , paths
- drawing WDK GDI , paths
- paths WDK GDI
- filling paths WDK GDI
ms.date: 04/20/2017
---

# GDI Services for Paths

To assist vector devices in filling complex areas, their drivers can call the engine functions, listed in the following table, that create, modify, and enumerate a path. The driver has access to paths through the [**PATHOBJ**](/windows/win32/api/winddi/ns-winddi-pathobj) structure.

| GDI Path Service Function | Description |
| ------------------------- | ----------- |
| [**EngCreatePath**](/windows/win32/api/winddi/nf-winddi-engcreatepath) | Allocates a path for the driver's temporary use. The driver should delete this path before returning to GDI from its current drawing call. |
| [**EngDeletePath**](/windows/win32/api/winddi/nf-winddi-engdeletepath) | Deletes a path allocated by the **EngCreatePath** function. |
| [**PATHOBJ_bCloseFigure**](/windows/win32/api/winddi/nf-winddi-pathobj_bclosefigure) | Closes a path (for filling) by drawing a line back to the starting point. |
| [**PATHOBJ_bEnum**](/windows/win32/api/winddi/nf-winddi-pathobj_benum) | Retrieves the next [**PATHDATA**](/windows/win32/api/winddi/ns-winddi-pathdata) record from a path. Each record describes all or part of a subpath. |
| [**PATHOBJ_bEnumClipLines**](/windows/win32/api/winddi/nf-winddi-pathobj_benumcliplines) | Enumerates clipped line segments from a path. |
| [**PATHOBJ_bMoveTo**](/windows/win32/api/winddi/nf-winddi-pathobj_bmoveto) | Changes the current position in a [**PATHOBJ**](/windows/win32/api/winddi/ns-winddi-pathobj)-defined path. |
| [**PATHOBJ_bPolyBezierTo**](/windows/win32/api/winddi/nf-winddi-pathobj_bpolybezierto) | Draws Bezier curves (cubic splines) in a PATHOBJ-defined path. |
| [**PATHOBJ_bPolyLineTo**](/windows/win32/api/winddi/nf-winddi-pathobj_bpolylineto) | Draws lines in a PATHOBJ-defined path. |
| [**PATHOBJ_vEnumStart**](/windows/win32/api/winddi/nf-winddi-pathobj_venumstart) | Notifies a [**PATHOBJ**](/windows/win32/api/winddi/ns-winddi-pathobj) that the driver will begin calling **PATHOBJ_bEnum** to enumerate the curves in the specified path. This function must be called in case of an enumeration restart. |
| [**PATHOBJ_vEnumStartClipLines**](/windows/win32/api/winddi/nf-winddi-pathobj_venumstartcliplines) | Allows the driver to ask for lines to be clipped against a [**CLIPOBJ**](/windows/win32/api/winddi/ns-winddi-clipobj) clip region is more complex than a single rectangle. |
| [**PATHOBJ_vGetBounds**](/windows/win32/api/winddi/nf-winddi-pathobj_vgetbounds) | Returns a bounding rectangle for the path. |
