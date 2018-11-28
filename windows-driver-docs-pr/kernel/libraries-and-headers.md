---
title: Libraries and Headers
description: Libraries and Headers
ms.assetid: 0d4d0273-775f-4cbb-8b7f-63b22f3ccdae
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Libraries and Headers


Kernel-mode drivers use the native system services routines by calling the **Nt** and **Zw** entry points in the Ntoskrnl.exe dynamic link library (DLL). This DLL contains the actual implementations of these routines. To access these entry points, a driver statically links to the Ntoskrnl.lib library, which is available in the Windows Driver Kit (WDK). The routines that are implemented in Ntoskrnl.lib are stubs that dynamically link to the entry points in Ntoskrnl.exe at run time.

The WDK documentation describes some, but not all, of the **Zw** entry points in Ntoskrnl.exe. For descriptions of the **Zw** routines that can be called by drivers, see [ZwXxx Routines](https://msdn.microsoft.com/library/windows/hardware/ff567122).

Most of the documented **Zw** routines are defined in the Wdm.h header file in the WDK, but a few are defined in other header files, such as Ntddk.h and Ntifs.h.

Typically, user-mode applications do not call the **Nt** and **Zw** routines. Instead, an application might call a Win32 routine, such as [CreateFile](http://go.microsoft.com/fwlink/p/?linkid=152795), which then calls a native system services routine, such as [NtCreateFile](http://go.microsoft.com/fwlink/p/?linkid=157250) or [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), to perform the requested operation. However, a user-mode application might directly call an **Nt** or **Zw** routine to perform an operation that is not supported by the Win32 routines.

User-mode applications use the native system services routines by calling the entry points in the Ntdll.dll dynamic link library. These entry points convert calls to **Nt** and **Zw** routines into system calls that are trapped to kernel mode. To access these entry points, a user-mode application statically links to the Ntdll.lib library, which is available in the WDK. The routines that are implemented in Ntdll.lib are stubs that dynamically link to the entry points in Ntdll.dll at run time.

The Windows SDK documentation describes some, but not all, of the **Nt** entry points in Ntdll.lib. Most of the documented **Nt** routines are defined in the Winternl.h header file in the Windows SDK. This documentation makes little mention of the **Zw** entry points, and no header files in the Windows SDK contain definitions of **Zw** routines.

With a couple of minor exceptions, each entry point in Ntdll.dll for an **Nt** routine has a matching entry point for a **Zw** routine. The documentation for the WDK and Windows SDK recommends that application developers avoid calling undocumented **Nt** entry points, and warns that the **Zw** entry points might disappear from Ntdll.dll in a future version of Windows. Application developers who call the **Zw** routines from user mode should be prepared for this occurrence.

For descriptions of the **Nt** routines that can be called by applications, see [Winternl](http://go.microsoft.com/fwlink/p/?linkid=157253), [Files](http://go.microsoft.com/fwlink/p/?linkid=157254), and [Miscellaneous Low-Level Client Support](http://go.microsoft.com/fwlink/p/?linkid=157255). Some reference pages for **Nt** routines in the Windows SDK documentation label the routines as "deprecated" and advise readers to use the equivalent Win32 routines instead of the deprecated **Nt** routines.

A user-mode application cannot call the entry points in Ntoskrnl.exe, and a kernel-mode driver cannot call the entry points in Ntdll.dll.

 

 




