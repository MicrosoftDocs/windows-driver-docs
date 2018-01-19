---
title: User-Mode Driver Framework Extensions (Wudfext.dll)
description: User-Mode Driver Framework Extensions (Wudfext.dll)
ms.assetid: 56b1c794-5740-44fd-9e5b-691fbfefe5a9
keywords: ["user-mode driver framework extensions (wudfext.dll)", "user-mode driver framework debugging, extensions (wudfext.dll)", "wudfext.dll (user-mode driver framework extensions)", "extensions, user-mode driver framework"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# User-Mode Driver Framework Extensions (Wudfext.dll)


Extension commands that are useful for debugging User-Mode Driver Framework drivers are implemented in Wudfext.dll.

You can use the Wudfext.dll extension commands in Microsoft Windows XP and later operating systems. Some extensions have additional restrictions on the Windows version or UMDF version that is required; these restrictions are noted on the individual reference pages.

**Note**  When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h. If your driver name exceeds the maximum length, your driver will fail to load.

 

For ways to use these extensions, see [User-Mode Driver Framework Debugging](user-mode-driver-framework-debugging.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20User-Mode%20Driver%20Framework%20Extensions%20%28Wudfext.dll%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




