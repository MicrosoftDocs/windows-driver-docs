---
title: Writing WdbgExts Extensions
description: Writing WdbgExts Extensions
keywords: ["WdbgExts extensions, writing"]
ms.date: 01/05/2026
ms.topic: concept-article
---

# Writing WdbgExts extensions

WdbgExts extensions are the original type of debugger extensions. They're less powerful than DbgEng extensions, but they still offer a wide range of functionality when performing user-mode or kernel-mode debugging on Microsoft Windows.

If you perform a full install of Debugging Tools for Windows, you can find a sample WdbgExts extension called **simplext** in the `sdk\samples\simplext` subdirectory of the installation directory.

For more information, see these articles in the WdbgExts Extension Design Guide:

- [WdbgExts Extension API Overview](wdbgexts-extension-api-overview.md)
- [32-Bit Pointers and 64-Bit Pointers](32-bit-pointers-and-64-bit-pointers.md)
- [Using WdbgExts Extension Callbacks](using-wdbgexts-extension-callbacks.md)
- [Using the DECLARE_API Macro](using-the-declare-api-macro.md)
- [Writing WdbgExts Extension Code](writing-wdbgexts-extension-code.md)
- [Building WdbgExts Extensions](building-wdbgexts-extensions.md)

For the complete `wdbgexts.h` reference, see [WdbgExts Extension Reference](/windows-hardware/drivers/ddi/wdbgexts/).
