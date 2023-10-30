---
title: Build a printer graphics DLL
description: Provides information about how to build a printer graphics DLL.
keywords:
- printer graphics DLL WDK, building
- graphics DLL WDK printer, building
ms.date: 01/26/2023
---

# Build a printer graphics DLL

[!include[Print Support Apps](../includes/print-support-apps.md)]

When building a printer graphics DLL, you must be aware of the following differences between DLLs intended for user-mode execution and those intended for kernel-mode execution.

In Windows Vista, printer graphics DLLs can only execute in user mode. For more information, see [Choosing user mode or kernel mode](choosing-user-mode-or-kernel-mode.md).

## Rules for Building a Printer Graphics DLL

| User-mode graphics DLL | Kernel-mode graphics DLL |
|--|--|
| Set TARGETTYPE=DYNLINK in source file. | Set TARGETTYPE=GDI_DRIVER in source file. |
| Preprocessor macro USERMODE_DRIVER must be defined in source files before winddi.h is included. | Preprocessor macro USERMODE_DRIVER must not be defined. |
| Object modules must be linked with the umpdddi.lib and gdi32.lib import libraries. | Object modules must be linked with the win32k.lib import library. |
| The [**DrvQueryDriverInfo**](/windows/win32/api/winddi/nf-winddi-drvquerydriverinfo) function must return **TRUE** for DRVQUERY_USERMODE. | The [**DrvQueryDriverInfo**](/windows/win32/api/winddi/nf-winddi-drvquerydriverinfo) function must return **FALSE** for DRVQUERY_USERMODE. (Alternatively, the function can be omitted.) |
