---
title: Requirements of an IViewHelper Clone-View COM Object
description: Requirements of an IViewHelper Clone-View COM Object
ms.assetid: ef599874-64c5-480e-a7bc-666ababd4d08
keywords:
- TMM WDK display , IViewHelper requirements
- monitor configurations WDK display , IViewHelper requirements
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Requirements of an IViewHelper Clone-View COM Object


A hardware vendor's clone-view [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164) COM interface object must meet the following requirements:

-   The COM object must reside within a dynamic-link library (DLL), which is a COM in-process (in-proc) server.

-   The implementation of the COM object must be opaque to the operating system.

-   The [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164) interface must provide methods for getting and setting the topology data, which includes clone view.

-   The hardware vendor must find a display mode for clone view so that the display is shown on two or more monitors.

-   If a call to the COM object's [**IViewHelper::Commit**](https://msdn.microsoft.com/library/windows/hardware/ff568167) method does not generate a mode change, **Commit** must call the Win32 **BroadcastSystemMessage** function and must always post (using the BSF\_POSTMESSAGE broadcast option) a WM\_DISPLAYCHANGE message. For more information about **BroadcastSystemMessage**, see the Microsoft Windows SDK documentation.

-   The [**IViewHelper::Commit**](https://msdn.microsoft.com/library/windows/hardware/ff568167) method must not be used in place of a call to the Win32 **ChangeDisplaySettingsEx**(**NULL**, **NULL**, **NULL**, 0, **NULL**) function with the indicated arguments. For more information about **ChangeDisplaySettingsEx**, see the Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Requirements%20of%20an%20IViewHelper%20Clone-View%20COM%20Object%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




