---
title: Choose user mode or kernel mode
description: Provides information about how to choose user mode or kernel mode.
keywords:
- printer graphics DLL WDK , user-mode vs. kernel-mode
- graphics DLL WDK printer , user-mode vs. kernel-mode
- user-mode execution WDK printer graphics
- kernel-mode execution WDK printer graphics
ms.date: 09/09/2022
---

# Choose user mode or kernel mode

User-mode execution of printer graphics DLLs provides the following advantages over kernel-mode execution:

- Unlimited stack space.

- Access to Win32 APIs.

- Less potential for causing system crashes.

- Easier debugging, with user-mode debuggers.

- Better floating-point capabilities, since use of graphics DDI floating-point functions is not required.

- Ability to call any customized, vendor-supplied user-mode DLLs that are not part of the described Microsoft Windows 2000 and later printer driver architecture

In Windows Vista, it is not possible to install a kernel-mode printer driver. If an application attempts to do so, the AddPrinterDriver and AddprinterDriverEx functions (described in the Windows SDK documentation) will fail with the error code ERROR_KM_DRIVER_BLOCKED.

The following table shows allowed printer driver execution modes:

| Operating system version | Allowed execution mode of printer graphics DLL |
|--|--|
| Windows NT 4.0 | kernel |
| Windows 2000 | user or kernel |
| Windows XP and Server 2003 | kernel mode available for existing printers; user mode required for new printer installations |
| Windows Vista | user |

## Using the graphics DDI in user mode

A user-mode printer graphics DLL is not limited to calling the [GDI Support Services](../display/gdi-support-services.md) and other Eng-prefixed graphics DDI callback functions. However, there are some rules that must be followed:

- Like kernel-mode graphics DLLs, user-mode graphics DLLs must call the graphics DDIs that create or modify a drawing surface. These callback functions are the GDI Support Services, and calling Win32 equivalents of these drawing functions is not allowed.

    For user-mode DLLs, calls to these drawing callback functions are intercepted by the user-mode GDI client, which then passes the calls to GDI's kernel-mode graphics rendering engine (GRE).

- The following list of Eng-prefixed graphics DDI functions cannot be called by user-mode DLLs:

    [**EngCreatePath**](/windows/win32/api/winddi/nf-winddi-engcreatepath)

    [**EngGetType1FontList**](/windows/win32/api/winddi/nf-winddi-enggettype1fontlist)

    [**EngMapModule**](/windows/win32/api/winddi/nf-winddi-engmapmodule)

    [**EngDebugBreak**](/windows/win32/api/winddi/nf-winddi-engdebugbreak)

- User-mode printer graphics DLLs can continue to use graphics DDI functions for [GDI floating-point services](../display/gdi-floating-point-services.md).

## Converting an existing printer graphics DLL to user mode

If you have previously developed a printer graphics DLL that executes in kernel mode, you can convert the DLL to user-mode execution. To convert, simply add a [**DrvQueryDriverInfo**](/windows/win32/api/winddi/nf-winddi-drvquerydriverinfo) function to the DLL, and then follow the rules for [building a printer graphics DLL](building-a-printer-graphics-dll.md).

## Creating a new printer graphics DLL in user mode

To develop a new printer graphics DLL that executes in user mode, you can continue to use all the graphics DDI functions used by kernel-mode DLLs. However, you also have the following options:

- For Eng-prefixed functions that have exact Win32 equivalents, it is strongly recommended that you call the Win32 functions. The following table lists these Eng-prefixed functions, along with their Win32 equivalents.

    | Eng-prefixed function | Win32 equivalent |
    |--|--|
    | EngAllocMem | HeapAlloc |
    | EngAllocUserMem | HeapAlloc |
    | EngEnumForms | EnumForms |
    | EngFreeMem | HeapFree |
    | EngFreeUserMem | HeapFree |
    | EngFindImageProcAddress | GetProcAddress |
    | EngGetForm | GetForm |
    | EngGetLastError | GetLastError |
    | EngGetPrinter | GetPrinter |
    | EngGetPrinterData | GetPrinterData |
    | EngGetPrinterDriver | GetPrinterDriver |
    | EngLoadImage | LoadLibrary |
    | EngMulDiv | MulDiv |
    | EngSetLastError | SetLastError |
    | EngSetPrinterData | SetPrinterData |
    | EngUnloadImage | FreeLibrary |
    | EngWritePrinter | WritePrinter |

- For Eng-prefixed functions that correspond to Win32 functions with similar functionality, it is also strongly recommended that you call the Win32 functions. The following table lists several of these Eng-prefixed functions, together with their Win32 counterparts.

    | Eng-prefixed function | Win32 equivalent |
    |--|--|
    | EngAcquireSemaphore | EnterCriticalSection |
    | EngCreateSemaphore | Allocate a CRITICAL_SECTION object, and initialize it using a call to the Win32 InitializeCriticalSection function. |
    | EngDeleteSemaphore | DeleteCriticalSection |
    | EngFindResource | FindResource |
    | EngFreeModule | FreeLibrary |
    | EngLoadModule | LoadLibrary |
    | EngMultiByteToWideChar | MultiByteToWideChar |
    | EngQueryLocalTime | GetLocalTime |
    | EngReleaseSemaphore | ReleaseSemaphore |
    | EngWideCharToMultiByte | WideCharToMultiByte |

- For functions that create or modify a drawing service, new drivers must continue to call [GDI support services](../display/gdi-support-services.md) and not their Win32 equivalents.

- Instead of using graphics DDI functions for [GDI Floating-Point Services](../display/gdi-floating-point-services.md), you can use the FLOAT data type.
