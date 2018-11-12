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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Transient Multi-Monitor Manager


Transient Multi-Monitor Manager is a Windows Vista feature that simplifies the setup of display configurations on mobile computers. TMM can place a mobile computer display (for example, a laptop computer display) into clone view when a new monitor is detected. TMM is disabled on desktop computers. For Windows Vista, there is no GDI function that an application can call to enter clone view. Hardware vendors must continue to use their own proprietary methods to enter clone view on desktop computers. However, hardware vendors should implement and provide an [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164) COM interface object that will allow TMM to set clone-view mode on mobile computers.

This section includes:

[TMM Terminology](tmm-terminology.md)

[Requirements of an IViewHelper Clone-View COM Object](requirements-of-an-iviewhelper-clone-view-com-object.md)

[Using an IViewHelper Clone-View COM Object](using-an-iviewhelper-clone-view-com-object.md)

[Handling Monitor Configurations](handling-monitor-configurations.md)

[Determining Whether a Platform is Mobile or Desktop](determining-whether-a-platform-is-mobile-or-desktop.md)

 

 





