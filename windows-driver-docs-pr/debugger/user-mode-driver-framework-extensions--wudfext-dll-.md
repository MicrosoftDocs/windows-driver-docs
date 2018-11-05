---
title: User-Mode Driver Framework Extensions (Wudfext.dll)
description: User-Mode Driver Framework Extensions (Wudfext.dll)
ms.assetid: 56b1c794-5740-44fd-9e5b-691fbfefe5a9
keywords: ["user-mode driver framework extensions (wudfext.dll)", "user-mode driver framework debugging, extensions (wudfext.dll)", "wudfext.dll (user-mode driver framework extensions)", "extensions, user-mode driver framework"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# User-Mode Driver Framework Extensions (Wudfext.dll)


Extension commands that are useful for debugging User-Mode Driver Framework drivers are implemented in Wudfext.dll.

You can use the Wudfext.dll extension commands in Microsoft Windows XP and later operating systems. Some extensions have additional restrictions on the Windows version or UMDF version that is required; these restrictions are noted on the individual reference pages.

**Note**  When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h. If your driver name exceeds the maximum length, your driver will fail to load.

 

For ways to use these extensions, see [User-Mode Driver Framework Debugging](user-mode-driver-framework-debugging.md).

 

 





