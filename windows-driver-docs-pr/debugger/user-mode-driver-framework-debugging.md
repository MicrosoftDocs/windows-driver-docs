---
title: User-Mode Driver Framework Debugging
description: User-Mode Driver Framework Debugging
ms.assetid: f59a420e-57d3-4ae0-84e3-58ec6e088b63
keywords: ["User-Mode Driver Framework debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# User-Mode Driver Framework Debugging


For an overview of how to debug User-Mode Driver Framework (UMDF) drivers, including information on how to start this kind of debugging session, see the [Debugging UMDF Drivers](https://go.microsoft.com/fwlink/p/?linkid=153578) section of the Windows Driver Kit (WDK) documentation.

### <span id="umdf_debugging_extensions"></span><span id="UMDF_DEBUGGING_EXTENSIONS"></span>UMDF Debugging Extensions

User-Mode Driver Framework (UMDF) debugging extensions are implemented in the extension module Wudfext.dll. You can use these extensions to debug drivers that use UMDF.

For a complete description of the extension commands in Wudfext.dll, see [User-Mode Driver Framework Extensions (Wudfext.dll)](user-mode-driver-framework-extensions--wudfext-dll-.md).

These extensions can be used on Microsoft Windows XP and later operating systems. Some extensions have additional restrictions on the Windows version or UMDF version that is required; these restrictions are noted on the individual reference pages.

**Note**  When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h. If your driver name exceeds the maximum length, your driver will fail to load.

 

To use this extension library, you must load the library into your debugger. For information about how to load extension libraries into a debugger, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

 

 





