---
title: Debugging Windows XP and Windows Vista
description: To use WinDbg to debug Windows XP or Windows Vista, get the Windows 7 Debugging Tools for Windows package, which is included in the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0.
ms.assetid: 1E4FC9D9-7F84-4F67-8FBC-4283C69AB0AC
---

# Debugging Windows XP and Windows Vista


To use WinDbg to debug Windows XP or Windows Vista, get the Windows 7 Debugging Tools for Windows package, which is included in the [Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0](http://go.microsoft.com/fwlink/p/?LinkId=320327).

If you want to download only Debugging Tools for Windows, install the SDK, and, during the installation, select the **Debugging Tools for Windows** box and clear all the other boxes.

**Note**  You might have to uninstall Microsoft Visual C++ 2010 Redistributable components before you install the SDK. For more information, see [the Microsoft Support website](http://support.microsoft.com/kb/2717426).

 

## <span id="Debugging_Tools__WinDbg__KD__CDB__NTSD__for_Windows_XP_and_Windows_Vista"></span><span id="debugging_tools__windbg__kd__cdb__ntsd__for_windows_xp_and_windows_vista"></span><span id="DEBUGGING_TOOLS__WINDBG__KD__CDB__NTSD__FOR_WINDOWS_XP_AND_WINDOWS_VISTA"></span>Debugging Tools (WinDbg, KD, CDB, NTSD) for Windows XP and Windows Vista


The Windows 7 Debugging Tools for Windows can run on x86-based or x64-based processors, and they can debug code that's running on x86-based or x64-based processors. Sometimes the debugger and the code being debugged run on the same computer, but other times the debugger and the code being debugged run on separate computers. In either case, the computer that's running the debugger is called the *host computer*, and the computer that is being debugged is called the *target computer*. Use the Windows 7 Debugging Tools for Windows when the target computer is running one of these operating systems.

|               |                     |
|---------------|---------------------|
| Windows XP    | Windows Server 2003 |
| Windows Vista | Windows Server 2008 |

 

If the target computer is running a more recent version of Windows, get the current [Debugging Tools for Windows](introduction6.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Windows%20XP%20and%20Windows%20Vista%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




