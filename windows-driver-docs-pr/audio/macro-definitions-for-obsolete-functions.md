---
title: Macro Definitions for Obsolete Functions
description: Macro Definitions for Obsolete Functions
ms.assetid: 3d69b089-4875-4860-b5eb-3b5edcf3fc89
---

# Macro Definitions for Obsolete Functions


## <span id="ddk_macro_definitions_for_obsolete_functions_ks"></span><span id="DDK_MACRO_DEFINITIONS_FOR_OBSOLETE_FUNCTIONS_KS"></span>


The header file portcls.h defines a number of macros that aid in compiling legacy driver code without requiring edits to source files. These macros conveniently replace calls to obsolete PortCls and kernel-mode driver functions with calls to the new PortCls and kernel-mode driver functions. If you have old source code that contains references to the obsolete functions, you can use the macros in portcls.h to recompile the source files to create executable code that calls the new functions.

The following topics are discussed:

[Obsolete Port Class Functions](obsolete-port-class-functions.md)

[Obsolete Kernel-Mode Driver-Support Functions](obsolete-kernel-mode-driver-support-functions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Macro%20Definitions%20for%20Obsolete%20Functions%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




