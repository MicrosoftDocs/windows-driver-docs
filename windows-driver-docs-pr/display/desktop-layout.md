---
title: Desktop Layout
description: Desktop Layout
keywords:
- connecting displays WDK Windows 7 display , CCD concepts, desktop layout
- connecting displays WDK Windows Server 2008 R2 display , CCD concepts, desktop layout
- configuring displays WDK Windows 7 display , CCD concepts, desktop layout
- configuring displays WDK Windows Server 2008 R2 display , CCD concepts, desktop layout
- CCD concepts WDK Windows 7 display , desktop layout
- CCD concepts WDK Windows Server 2008 R2 display , desktop layout
ms.date: 04/20/2017
---

# Desktop Layout


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The caller uses the **position** member of the [**DISPLAYCONFIG\_SOURCE\_MODE**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_source_mode) structure in a call to the [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) CCD function to control the arrangement of source surfaces on the desktop. The **position** member specifies the position in desktop coordinates of the upper-left corner of the source surface. The source surface that is positioned at (0, 0) is consider the primary surface. GDI has strict rules about how the source surfaces can be arranged in the desktop space. For example, GDI does not allow any gaps between source surfaces and no overlaps in source surfaces.

Although [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) attempts to rearrange sources surfaces to enforce these GDI layout rules, the caller should specify the layout of the sources surfaces. It is undefined how GDI will rearrange the sources surfaces to enforce its layout rules, and the resultant layout of sources surfaces might not be what the caller wanted to achieve.

 

