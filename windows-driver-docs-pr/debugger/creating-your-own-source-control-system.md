---
title: Creating Your Own Source Control System
description: Creating Your Own Source Control System
ms.assetid: 86492545-fc94-40ee-b22d-26fa2b0fbcc8
keywords: ["source servers, HTTP sites", "source servers, UNC shares", "SrcSrv, HTTP sites", "SrcSrv, UNC shares"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Creating Your Own Source Control System


This section enables you to understand how to prepare instrumentation scripts so that SrcSrv can be integrated into your build or version control system. The implementation is dependent on the language specification version that ships with SrcSrv.

Many of the specifics of how Srcsrv.dll is called by symbol handler code are discussed. However, this information is not static and will not become so in the future. No one should attempt to write code that calls Srcsrv.dll directly. This is reserved for DbgHelp or the Visual Studio products. Third-party vendors wanting to integrate such functionality into their products should use the **SymGetSourceFile** function. This function, along with others in the DbgHelp API, is described in the DbgHelp documentation, which can be found in the sdk/help subdirectory of the Debugging Tools for Windows installation directory.

This section includes:

[Language Specification 1](language-specification-1.md)

[Language Specification 2](language-specification-2.md)

 

 





