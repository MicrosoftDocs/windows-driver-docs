---
title: Windows Driver Framework Extensions (Wdfkd.dll)
description: Windows Driver Framework Extensions (Wdfkd.dll)
ms.assetid: 2fa2b131-f6fd-459b-a4e3-799246076338
keywords: ["Kernel-Mode Driver Framework debugging, extensions (wdfkd.dll)", "Kernel-Mode Driver Framework extensions (wdfkd.dll)", "wdfkd.dll (Kernel-Mode Driver Framework extensions)", "extensions, Kernel-Mode Driver Framework"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Windows Driver Framework Extensions (Wdfkd.dll)


Extension commands that are useful for debugging drivers built with the Kernel-Mode Driver Framework (KMDF) or version 2 of the User-Mode Driver Framework (UMDF 2) are implemented in Wdfkd.dll.

These extensions can be used on Microsoft Windows XP and later operating systems. Some extensions have additional restrictions; these restrictions are noted on the individual reference pages.

**Note**  When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h. If your driver name exceeds the maximum length, your driver will fail to load.

 

For more information about how to use these extensions, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

 

 





