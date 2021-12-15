---
title: Requirements of an IViewHelper Clone-View COM Object
description: Requirements of an IViewHelper Clone-View COM Object
keywords:
- TMM WDK display , IViewHelper requirements
- monitor configurations WDK display , IViewHelper requirements
ms.date: 04/20/2017
---

# Requirements of an IViewHelper Clone-View COM Object

A hardware vendor's clone-view **IViewHelper** COM interface object must meet the following requirements:

* The COM object must reside within a dynamic-link library (DLL), which is a COM in-process (in-proc) server.

* The implementation of the COM object must be opaque to the operating system.

* The **IViewHelper** interface must provide methods for getting and setting the topology data, which includes clone view.

* The hardware vendor must find a display mode for clone view so that the display is shown on two or more monitors.

* If a call to the COM object's [**IViewHelper::Commit**](/previous-versions/windows/hardware/drivers/ff568167(v=vs.85)) method does not generate a mode change, **Commit** must call the Win32 **BroadcastSystemMessage** function and must always post (using the BSF_POSTMESSAGE broadcast option) a WM_DISPLAYCHANGE message. For more information about **BroadcastSystemMessage**, see the Microsoft Windows SDK documentation.

* The [**IViewHelper::Commit**](/previous-versions/windows/hardware/drivers/ff568167(v=vs.85)) method must not be used in place of a call to the Win32 **ChangeDisplaySettingsEx**(**NULL**, **NULL**, **NULL**, 0, **NULL**) function with the indicated arguments. For more information about **ChangeDisplaySettingsEx**, see the Windows SDK documentation.
