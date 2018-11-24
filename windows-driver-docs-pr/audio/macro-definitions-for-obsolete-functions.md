---
title: Macro Definitions for Obsolete Functions
description: Macro Definitions for Obsolete Functions
ms.assetid: 3d69b089-4875-4860-b5eb-3b5edcf3fc89
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Macro Definitions for Obsolete Functions


## <span id="ddk_macro_definitions_for_obsolete_functions_ks"></span><span id="DDK_MACRO_DEFINITIONS_FOR_OBSOLETE_FUNCTIONS_KS"></span>


The header file portcls.h defines a number of macros that aid in compiling legacy driver code without requiring edits to source files. These macros conveniently replace calls to obsolete PortCls and kernel-mode driver functions with calls to the new PortCls and kernel-mode driver functions. If you have old source code that contains references to the obsolete functions, you can use the macros in portcls.h to recompile the source files to create executable code that calls the new functions.

The following topics are discussed:

[Obsolete Port Class Functions](obsolete-port-class-functions.md)

[Obsolete Kernel-Mode Driver-Support Functions](obsolete-kernel-mode-driver-support-functions.md)

 

 





