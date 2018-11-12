---
title: Kernel-Mode Driver Framework Debugging
description: Kernel-Mode Driver Framework Debugging
ms.assetid: bec840f8-b500-464f-8e49-53f03f34aa6a
keywords: ["Kernel-Mode Driver Framework debugging", "Windows Driver Foundation"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Kernel-Mode Driver Framework Debugging


Debugging extensions for Kernel-Mode Driver Framework (KMDF) are contained in the Wdfkd.dll extension library.

You can use the extension commands that the Wdfkd.dll extension library contains to debug drivers that use KMDF.

For a description of the extension commands in Wdfkd.dll, see [Kernel-Mode Driver Framework Extensions (Wdfkd.dll)](kernel-mode-driver-framework-extensions--wdfkd-dll-.md).

These extensions can be used on Microsoft Windows XP and later operating systems. Some extensions have additional restrictions; these restrictions are noted on the individual reference pages.

**Note**  When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h. If your driver name exceeds the maximum length, your driver will fail to load.

 

To use this extension library, you must load the library into your debugger. For information about how to load extension libraries into a debugger, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

 

 





