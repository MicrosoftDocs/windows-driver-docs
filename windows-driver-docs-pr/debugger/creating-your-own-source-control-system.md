---
title: Creating Your Own Source Control System
description: Creating Your Own Source Control System
ms.assetid: 86492545-fc94-40ee-b22d-26fa2b0fbcc8
keywords: ["source servers, HTTP sites", "source servers, UNC shares", "SrcSrv, HTTP sites", "SrcSrv, UNC shares"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating Your Own Source Control System


This section enables you to understand how to prepare instrumentation scripts so that SrcSrv can be integrated into your build or version control system. The implementation is dependent on the language specification version that ships with SrcSrv.

Many of the specifics of how Srcsrv.dll is called by symbol handler code are discussed. However, this information is not static and will not become so in the future. No one should attempt to write code that calls Srcsrv.dll directly. This is reserved for DbgHelp or the Visual Studio products. Third-party vendors wanting to integrate such functionality into their products should use the **SymGetSourceFile** function. This function, along with others in the DbgHelp API, is described in the DbgHelp documentation, which can be found in the sdk/help subdirectory of the Debugging Tools for Windows installation directory.

This section includes:

[Language Specification 1](language-specification-1.md)

[Language Specification 2](language-specification-2.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Creating%20Your%20Own%20Source%20Control%20System%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




