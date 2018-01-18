---
title: Debugging a Service Application
description: Debugging a Service Application
ms.assetid: 1d1e24d5-8b6b-4ed5-84ad-b73356168b10
keywords: ["service application debugging", "postmortem debugging, debugging service applications", "services"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging a Service Application


A *service*, also known as a *Windows service*, is a user-mode process designed to be started by Windows without human interaction. It is started automatically at system boot, or by an application that uses the service functions included in the Win32 API. A service can also be started by a human user through the Services control panel utility. Every service must conform to the interface rules of the service control manager (SCM).

Each service is composed of three elements: a *service application*, a *service control program*, and the service control manager itself. Although a service application is sometimes (incorrectly) referred to as a "service," it is actually one of the three components that make up a service. The service application can contain almost any kind of user-mode code. The service control program controls when the service application starts and stops. The service control manager is part of Windows.

The following sections describe how to debug a service application:

[Choosing the Best Method](choosing-the-best-method.md)

[Preparing to Debug the Service Application](preparing-to-debug-the-service-application.md)

[Debugging the Service Application Automatically](debugging-the-service-application-automatically.md)

[Debugging the Service Application Manually](debugging-the-service-application-manually.md)

For an overview of services, service applications, and the service control manager, see *Microsoft Windows Internals: Microsoft Windows Server 2003, Windows XP, and Windows 2000* by David A. Solomon and Mark E. Russinovich (4th edition, Microsoft Press, 2005).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20a%20Service%20Application%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




