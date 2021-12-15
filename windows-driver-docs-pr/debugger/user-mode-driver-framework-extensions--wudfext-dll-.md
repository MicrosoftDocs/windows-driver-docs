---
title: User-Mode Driver Framework Extensions (Wudfext.dll)
description: User-Mode Driver Framework Extensions (Wudfext.dll)
keywords: ["user-mode driver framework extensions (wudfext.dll)", "user-mode driver framework debugging, extensions (wudfext.dll)", "wudfext.dll (user-mode driver framework extensions)", "extensions, user-mode driver framework"]
ms.date: 05/23/2017
---

# User-Mode Driver Framework Extensions (Wudfext.dll)


Extension commands that are useful for debugging User-Mode Driver Framework drivers are implemented in Wudfext.dll.

Some extensions have additional restrictions on the Windows version or UMDF version that is required; these restrictions are noted on the individual reference pages.

**Note**  When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h. If your driver name exceeds the maximum length, your driver will fail to load.

 

For ways to use these extensions, see [User-Mode Driver Framework Debugging](user-mode-driver-framework-debugging.md).

 

 





