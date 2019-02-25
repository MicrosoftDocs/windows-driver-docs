---
title: Requirements of an IViewHelper Clone-View COM Object
description: Requirements of an IViewHelper Clone-View COM Object
ms.assetid: ef599874-64c5-480e-a7bc-666ababd4d08
keywords:
- TMM WDK display , IViewHelper requirements
- monitor configurations WDK display , IViewHelper requirements
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requirements of an IViewHelper Clone-View COM Object


A hardware vendor's clone-view [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164) COM interface object must meet the following requirements:

-   The COM object must reside within a dynamic-link library (DLL), which is a COM in-process (in-proc) server.

-   The implementation of the COM object must be opaque to the operating system.

-   The [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164) interface must provide methods for getting and setting the topology data, which includes clone view.

-   The hardware vendor must find a display mode for clone view so that the display is shown on two or more monitors.

-   If a call to the COM object's [**IViewHelper::Commit**](https://msdn.microsoft.com/library/windows/hardware/ff568167) method does not generate a mode change, **Commit** must call the Win32 **BroadcastSystemMessage** function and must always post (using the BSF\_POSTMESSAGE broadcast option) a WM\_DISPLAYCHANGE message. For more information about **BroadcastSystemMessage**, see the Microsoft Windows SDK documentation.

-   The [**IViewHelper::Commit**](https://msdn.microsoft.com/library/windows/hardware/ff568167) method must not be used in place of a call to the Win32 **ChangeDisplaySettingsEx**(**NULL**, **NULL**, **NULL**, 0, **NULL**) function with the indicated arguments. For more information about **ChangeDisplaySettingsEx**, see the Windows SDK documentation.

 

 





