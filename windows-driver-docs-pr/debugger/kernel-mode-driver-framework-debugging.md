---
title: Kernel-Mode Driver Framework Debugging
description: Kernel-Mode Driver Framework Debugging
ms.assetid: bec840f8-b500-464f-8e49-53f03f34aa6a
keywords: ["Kernel-Mode Driver Framework debugging", "Windows Driver Foundation"]
---

# Kernel-Mode Driver Framework Debugging


Debugging extensions for Kernel-Mode Driver Framework (KMDF) are contained in the Wdfkd.dll extension library.

You can use the extension commands that the Wdfkd.dll extension library contains to debug drivers that use KMDF.

For a description of the extension commands in Wdfkd.dll, see [Kernel-Mode Driver Framework Extensions (Wdfkd.dll)](kernel-mode-driver-framework-extensions--wdfkd-dll-.md).

These extensions can be used on Microsoft Windows XP and later operating systems. Some extensions have additional restrictions; these restrictions are noted on the individual reference pages.

**Note**  When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h. If your driver name exceeds the maximum length, your driver will fail to load.

 

To use this extension library, you must load the library into your debugger. For information about how to load extension libraries into a debugger, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Kernel-Mode%20Driver%20Framework%20Debugging%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




