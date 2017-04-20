---
title: Supporting Transient Multi-Monitor Manager
description: Supporting Transient Multi-Monitor Manager
ms.assetid: 5091fe00-76d9-4585-9ef0-4b5b7ab8bc06
keywords:
- Transient Multi-Monitor Manager WDK display
- TMM WDK display
- clone view WDK display
- mobile devices WDK , TMM support
- monitor configurations WDK display , TMM support
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Transient Multi-Monitor Manager


Transient Multi-Monitor Manager is a Windows Vista feature that simplifies the setup of display configurations on mobile computers. TMM can place a mobile computer display (for example, a laptop computer display) into clone view when a new monitor is detected. TMM is disabled on desktop computers. For Windows Vista, there is no GDI function that an application can call to enter clone view. Hardware vendors must continue to use their own proprietary methods to enter clone view on desktop computers. However, hardware vendors should implement and provide an [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164) COM interface object that will allow TMM to set clone-view mode on mobile computers.

This section includes:

[TMM Terminology](tmm-terminology.md)

[Requirements of an IViewHelper Clone-View COM Object](requirements-of-an-iviewhelper-clone-view-com-object.md)

[Using an IViewHelper Clone-View COM Object](using-an-iviewhelper-clone-view-com-object.md)

[Handling Monitor Configurations](handling-monitor-configurations.md)

[Determining Whether a Platform is Mobile or Desktop](determining-whether-a-platform-is-mobile-or-desktop.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Transient%20Multi-Monitor%20Manager%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




