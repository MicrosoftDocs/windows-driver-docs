---
title: Choosing User Mode or Kernel Mode
description: Choosing User Mode or Kernel Mode
ms.assetid: 1e63d01e-8cf2-488a-89e8-d4a3ff5cfe19
keywords:
- printer graphics DLL WDK , user-mode vs. kernel-mode
- graphics DLL WDK printer , user-mode vs. kernel-mode
- user-mode execution WDK printer graphics
- kernel-mode execution WDK printer graphics
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Choosing User Mode or Kernel Mode





User-mode execution of printer graphics DLLs provides the following advantages over kernel-mode execution:

-   Unlimited stack space.

-   Access to Win32 APIs.

-   Less potential for causing system crashes.

-   Easier debugging, with user-mode debuggers.

-   Better floating-point capabilities, since use of graphics DDI floating-point functions is not required.

-   Ability to call any customized, vendor-supplied user-mode DLLs that are not part of the described Microsoft Windows 2000 and later printer driver architecture

In Windows Vista, it is not possible to install a kernel-mode printer driver. If an application attempts to do so, the AddPrinterDriver and AddprinterDriverEx functions (described in the Windows SDK documentation) will fail with the error code ERROR\_KM\_DRIVER\_BLOCKED.

The following table shows allowed printer driver execution modes:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Operating system version</th>
<th>Allowed execution mode of printer graphics DLL</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Windows NT 4.0</p></td>
<td><p>kernel</p></td>
</tr>
<tr class="even">
<td><p>Windows 2000</p></td>
<td><p>user or kernel</p></td>
</tr>
<tr class="odd">
<td><p>Windows XP and Server 2003</p></td>
<td><p>kernel mode available for existing printers; user mode required for new printer installations</p></td>
</tr>
<tr class="even">
<td>Windows Vista</td>
<td><p>user</p></td>
</tr>
</tbody>
</table>

 

### Using the Graphics DDI in User Mode

A user-mode printer graphics DLL is not limited to calling the [GDI Support Services](https://msdn.microsoft.com/library/windows/hardware/ff566714) and other Eng-prefixed graphics DDI callback functions. However, there are some rules that must be followed:

-   Like kernel-mode graphics DLLs, user-mode graphics DLLs must call the graphics DDIs that create or modify a drawing surface. These callback functions are the GDI Support Services, and calling Win32 equivalents of these drawing functions is not allowed.

    For user-mode DLLs, calls to these drawing callback functions are intercepted by the user-mode GDI client, which then passes the calls to GDI's kernel-mode graphics rendering engine (GRE).

-   The following list of Eng-prefixed graphics DDI functions cannot be called by user-mode DLLs:

    [**EngCreatePath**](https://msdn.microsoft.com/library/windows/hardware/ff564755)

    [**EngGetType1FontList**](https://msdn.microsoft.com/library/windows/hardware/ff564956)

    [**EngMapModule**](https://msdn.microsoft.com/library/windows/hardware/ff564974)

    [**EngDebugBreak**](https://msdn.microsoft.com/library/windows/hardware/ff564773)

-   User-mode printer graphics DLLs can continue to use graphics DDI functions for [GDI floating-point services](https://msdn.microsoft.com/library/windows/hardware/ff566535).

### Converting an Existing Printer Graphics DLL to User Mode

If you have previously developed a printer graphics DLL that executes in kernel mode, you can convert the DLL to user-mode execution. To convert, simply add a [**DrvQueryDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556261) function to the DLL, and then follow the rules for [building a printer graphics DLL](building-a-printer-graphics-dll.md).

### Creating a New Printer Graphics DLL in User Mode

To develop a new printer graphics DLL that executes in user mode, you can continue to use all the graphics DDI functions used by kernel-mode DLLs. However, you also have the following options:

-   For Eng-prefixed functions that have exact Win32 equivalents, it is strongly recommended that you call the Win32 functions. The following table lists these Eng-prefixed functions, along with their Win32 equivalents.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Eng-prefixed Function</th>
    <th>Win32 Equivalent</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>EngAllocMem</p></td>
    <td><p>HeapAlloc</p></td>
    </tr>
    <tr class="even">
    <td><p>EngAllocUserMem</p></td>
    <td><p>HeapAlloc</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngEnumForms</p></td>
    <td><p>EnumForms</p></td>
    </tr>
    <tr class="even">
    <td><p>EngFreeMem</p></td>
    <td><p>HeapFree</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngFreeUserMem</p></td>
    <td><p>HeapFree</p></td>
    </tr>
    <tr class="even">
    <td><p>EngFindImageProcAddress</p></td>
    <td><p>GetProcAddress</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngGetForm</p></td>
    <td><p>GetForm</p></td>
    </tr>
    <tr class="even">
    <td><p>EngGetLastError</p></td>
    <td><p>GetLastError</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngGetPrinter</p></td>
    <td><p>GetPrinter</p></td>
    </tr>
    <tr class="even">
    <td><p>EngGetPrinterData</p></td>
    <td><p>GetPrinterData</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngGetPrinterDriver</p></td>
    <td><p>GetPrinterDriver</p></td>
    </tr>
    <tr class="even">
    <td><p>EngLoadImage</p></td>
    <td><p>LoadLibrary</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngMulDiv</p></td>
    <td><p>MulDiv</p></td>
    </tr>
    <tr class="even">
    <td><p>EngSetLastError</p></td>
    <td><p>SetLastError</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngSetPrinterData</p></td>
    <td><p>SetPrinterData</p></td>
    </tr>
    <tr class="even">
    <td><p>EngUnloadImage</p></td>
    <td><p>FreeLibrary</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngWritePrinter</p></td>
    <td><p>WritePrinter</p></td>
    </tr>
    </tbody>
    </table>

     

<!-- -->

-   For Eng-prefixed functions that correspond to Win32 functions with similar functionality, it is also strongly recommended that you call the Win32 functions. The following table lists several of these Eng-prefixed functions, together with their Win32 counterparts.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Eng-prefixed Function</th>
    <th>Win32 Equivalent</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>EngAcquireSemaphore</p></td>
    <td><p>EnterCriticalSection</p></td>
    </tr>
    <tr class="even">
    <td><p>EngCreateSemaphore</p></td>
    <td><p>Allocate a CRITICAL_SECTION object, and initialize it using a call to the Win32 InitializeCriticalSection function.</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngDeleteSemaphore</p></td>
    <td><p>DeleteCriticalSection</p></td>
    </tr>
    <tr class="even">
    <td><p>EngFindResource</p></td>
    <td><p>FindResource</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngFreeModule</p></td>
    <td><p>FreeLibrary</p></td>
    </tr>
    <tr class="even">
    <td><p>EngLoadModule</p></td>
    <td><p>LoadLibrary</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngMultiByteToWideChar</p></td>
    <td><p>MultiByteToWideChar</p></td>
    </tr>
    <tr class="even">
    <td><p>EngQueryLocalTime</p></td>
    <td><p>GetLocalTime</p></td>
    </tr>
    <tr class="odd">
    <td><p>EngReleaseSemaphore</p></td>
    <td><p>ReleaseSemaphore</p></td>
    </tr>
    <tr class="even">
    <td><p>EngWideCharToMultiByte</p></td>
    <td><p>WideCharToMultiByte</p></td>
    </tr>
    </tbody>
    </table>

     

<!-- -->

-   For functions that create or modify a drawing service, new drivers must continue to call [GDI support services](https://msdn.microsoft.com/library/windows/hardware/ff566714) and not their Win32 equivalents.

-   Instead of using graphics DDI functions for [GDI Floating-Point Services](https://msdn.microsoft.com/library/windows/hardware/ff566535), you can use the FLOAT data type.

 

 




