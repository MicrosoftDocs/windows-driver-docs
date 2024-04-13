---
title: QueryDisplayConfig Summary and Scenarios
description: QueryDisplayConfig Summary and Scenarios
keywords:
- connecting displays WDK Windows 7 display , CCD APIs, QueryDisplayConfig
- connecting displays WDK Windows Server 2008 R2 display , CCD APIs, QueryDisplayConfig
- configuring displays WDK Windows 7 display , CCD APIs, QueryDisplayConfig
- configuring displays WDK Windows Server 2008 R2 display , CCD APIs, QueryDisplayConfig
- CCD concepts WDK Windows 7 display , QueryDisplayConfig
- CCD concepts WDK Windows Server 2008 R2 display , QueryDisplayConfig
- QueryDisplayConfig WDK Windows 7 display
- QueryDisplayConfig WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
---

# QueryDisplayConfig Summary and Scenarios


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following sections summarize how a caller uses the [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) CCD function and provide scenarios for using **QueryDisplayConfig**.

### <span id="querydisplayconfig_summary"></span><span id="QUERYDISPLAYCONFIG_SUMMARY"></span>QueryDisplayConfig Summary

The caller can use [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) to enumerate any of the following information:

-   All of the individual paths that are possible for the current set of connected monitors. The caller can then combine the paths to construct possible topologies.

-   All of the paths that are currently active.

-   The active paths as they are currently defined in the persistence database for the set of connected displays.

-   The source and target mode along with orientation, scaling, layout, and connector type on a per-path basis.

-   The hot-key options that the current topology maps to.

### <span id="querydisplayconfig_scenarios"></span><span id="QUERYDISPLAYCONFIG_SCENARIOS"></span>QueryDisplayConfig Scenarios

[**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) is called in the following scenarios:

-   The display control panel applet calls [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) to populate the Control Panel's user interface with the current applied topology when the Control Panel first starts. The current applied topology includes those displays on which forced projection is enabled.

-   The display control panel applet calls [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) to enumerate all of the possible paths to populate the **multimon** drop-down box.

-   Before the Control Panel user interface starts, the display hot key calls [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) to obtain the display option (that is, clone, internal, external, or extended) that is currently set.

-   A third party application might call [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) to query the current settings that are stored in the database for the set of connected displays.

 

