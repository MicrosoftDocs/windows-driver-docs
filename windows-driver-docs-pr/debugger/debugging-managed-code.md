---
title: Debugging Managed Code Using the Windows Debugger
description: You can use the windows debuggers (WinDbg, CDB, and NTSD) to debug target applications that contain managed code.
ms.assetid: eb4cc883-71ac-4a57-8654-07c3120310c0
keywords: debugging, debug, Windbg, managed code debugging, .NET common language runtime, common language runtime, CLR , JIT compiler, JITted code
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging Managed Code Using the Windows Debugger


You can use the Windows debuggers (WinDbg, CDB, and NTSD) to debug target applications that contain managed code. To debug managed code, you must load the [SOS debugging extension (sos.dll)](https://go.microsoft.com/fwlink/p/?linkid=223345) and a data access component (mscordacwks.dll).

The Windows debuggers are separate from the Visual Studio debugger. For information about the distinction between the Windows debuggers and the Visual Studio debugger, see [Windows Debugging](index.md).

## <span id="introduction-to-managed-code"></span><span id="INTRODUCTION_TO_MANAGED_CODE"></span>Introduction to Managed Code


Managed code is executed together with the Microsoft .NET Common Language Runtime (CLR). In a managed-code application, the binary code that the compiler produces is in Microsoft Intermediate Language (MSIL), which is platform-independent.

When managed code is run, the runtime produces native code that is platform-specific. The process of generating native code from MSIL is called *just-in-time (JIT) compiling*. After the JIT compiler has compiled the MSIL for a specific method, the method's native code remains in memory. Whenever this method is later called, the native code executes and the JIT compiler does not have to be involved.

You can build managed code by using several compilers that are manufactured by a variety of software producers. In particular, Microsoft Visual Studio can build managed code from several different languages including C#, Visual Basic, JScript, and C++ with managed extensions.

The CLR is not updated every time the .NET Framework is updated. For example, versions 2.0, 3.0, and 3.5 of the .NET Framework all use version 2.0 of the CLR. The following table shows the version and filename of the CLR used by each version of the .NET Framework.

| .NET Framework version | CLR version | CLR filename |
|------------------------|-------------|--------------|
| 1.1                    | 1.1         | mscorwks.dll |
| 2.0                    | 2.0         | mscorwks.dll |
| 3.0                    | 2.0         | mscorwks.dll |
| 3.5                    | 2.0         | mscorwks.dll |
| 4.0                    | 4.0         | clr.dll      |
| 4.5                    | 4.0         | clr.dll      |

 

## <span id="debugging-managed_code"></span><span id="DEBUGGING_MANAGED_CODE"></span>Debugging Managed Code


To debug managed code, the debugger must load these two components.

-   Data access component (DAC) (mscordacwks.dll)
-   [SOS debugging extension (sos.dll)](https://go.microsoft.com/fwlink/p/?linkid=223345)

**Note**  For all versions of the .NET Framework, the filename of the DAC is mscordacwks.dll, and the filename of the SOS debugging extension is sos.dll.

 

### <span id="getting-the-sos-debugging-extension"></span><span id="GETTING_THE_SOS_DEBUGGING_EXTENSION"></span>Getting the SOS Debugging Extension (sos.dll)

The SOS debugging extension (sos.dll) files are not included in the current version of Debugging Tools for Windows.

For .NET Framework versions 2.0 and later, sos.dll is included in the .NET Framework installation.

For version 1.*x* of the .NET Framework, sos.dll is not included in the .NET Framework installation. To get sos.dll for .NET Framework 1.*x*, download the 32-bit version of Windows 7 Debugging Tools for Windows.

Windows 7 Debugging Tools for Windows is included in the Windows SDK for Windows 7, which is available at these two places:

-   [Windows SDK for Windows 7 and .NET Framework 4.0](https://go.microsoft.com/fwlink/p?LinkId=320327)
-   [Windows SDK for Windows 7 and .NET Framework 4.0 (ISO)](https://go.microsoft.com/fwlink/p?LinkId=320328)

If you are running an x64 version of Windows, use the [ISO](https://go.microsoft.com/fwlink/p?LinkID=320328) site, so that you can specify that you want the 32-bit version of the SDK. Sos.dll is included only in the 32-bit version of Windows 7 Debugging Tools for Windows.

### <span id="Loading_mscordacwks.dll_and_sos.dll__live_debugging_"></span><span id="loading_mscordacwks.dll_and_sos.dll__live_debugging_"></span><span id="LOADING_MSCORDACWKS.DLL_AND_SOS.DLL__LIVE_DEBUGGING_"></span>Loading mscordacwks.dll and sos.dll (live debugging)

Assume that the debugger and the application being debugged are running on the same computer. Then the .NET Framework being used by the application is installed on the computer and is available to the debugger.

The debugger must load a version of the DAC that is the same as the version of the CLR that the managed-code application is using. The bitness (32-bit or 64-bit) must also match. The DAC (mscordacwks.dll) comes with the .NET Framework. To load the correct version of the DAC, attach the debugger to the managed-code application, and enter this command.

**.cordll -ve -u -l**

The output should be similar to this.

```dbgcmd
CLRDLL: Loaded DLL C:\Windows\Microsoft.NET\Framework64\v4.0.30319\mscordacwks.dll
CLR DLL status: Loaded DLL C:\Windows\Microsoft.NET\Framework64\v4.0.30319\mscordacwks.dll
```

To verify that the version of mscordacwks.dll matches the version of the CLR that the application is using, enter one of the following commands to display information about the loaded CLR module.

**lmv mclr** (for version 4.0 of the CLR)

**lmv mscorwks** (for version 1.0 or 2.0 of the CLR)

The output should be similar to this.

```dbgcmd
start             end                 module name
000007ff`26710000 000007ff`2706e000   clr        (deferred)             
    Image path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll
...
```

In the preceding example, notice that the version of the CLR (clr.dll) matches the version of the DAC (mscordacwks.dll): v4.0.30319. Also notice that both components are 64-bit.

When you use [**.cordll**](-cordll--control-clr-debugging-.md) to load the DAC, the SOS debugging extension (sos.dll) might get loaded automatically. If sos.dll doesn't get loaded automatically, you can use one of these commands to load it.

**.loadby sos clr** (for version 4.0 of the CLR)

**.loadby sos mscorwks** (for version 1.0 or 2.0 of the CLR)

As an alternative to using [**.loadby**](-load---loadby--load-extension-dll-.md), you can use **.load**. For example, to load version 4.0 of the 64-bit CLR, you could enter a command similar to this.

**.load C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\sos.dll**

In the preceding output, notice that the version of the SOS debugging extension (sos.dll) matches the version of the CLR and the DAC: v4.0.30319. Also notice that all three components are 64-bit.

### <span id="Loading_mscordacwks.dll_and_sos.dll__dump_file_"></span><span id="loading_mscordacwks.dll_and_sos.dll__dump_file_"></span><span id="LOADING_MSCORDACWKS.DLL_AND_SOS.DLL__DUMP_FILE_"></span>Loading mscordacwks.dll and sos.dll (dump file)

Suppose you use the debugger to open a dump file (of a managed-code application) that was created on another computer.

The debugger must load a version of the DAC that is the same as the version of the CLR that the managed-code application was using on the other computer. The bitness (32-bit or 64-bit) must also match.

The DAC (mscordacwks.dll) comes with the .NET Framework, but let's assume that you do not have the correct version of the .NET Framework installed on the computer that is running the debugger. You have three options.

-   Load the DAC from a symbol server. For example, you could include Microsoft's public symbol server in your symbol path.
-   Install the correct version of the .NET Framework on the computer that is running the debugger.
-   Get the correct version of mscordacwks.dll from the person who created the dump file (on another computer) and manually copy it to the computer that is running the debugger.

Here we illustrate using Microsoft's public symbol server.

Enter these commands.

**.sympath+ srv\\*** (Add symbol server to symbol path.)

**!sym noisy**

**.cordll -ve -u -l**

The output will be similar to this.

```dbgcmd
CLRDLL: Unable to get version info for 'C:\Windows\Microsoft.NET
   \Framework64\v4.0.30319\mscordacwks.dll', Win32 error 0n87

SYMSRV:  C:\ProgramData\dbg\sym\mscordacwks_AMD64_AMD64_4.0.30319.18010.dll
   \5038768C95e000\mscordacwks_AMD64_AMD64_4.0.30319.18010.dll not found

SYMSRV:  mscordacwks_AMD64_AMD64_4.0.30319.18010.dll from 
   https://msdl.microsoft.com/download/symbols: 570542 bytes - copied         
...
SYMSRV:  C:\ProgramData\dbg\sym\SOS_AMD64_AMD64_4.0.30319.18010.dll
   \5038768C95e000\SOS_AMD64_AMD64_4.0.30319.18010.dll not found

SYMSRV:  SOS_AMD64_AMD64_4.0.30319.18010.dll from 
   https://msdl.microsoft.com/download/symbols: 297048 bytes - copied         
...
Automatically loaded SOS Extension
...
```

In the preceding output, you can see that the debugger first looked for mscordacwks.dll and sos.dll on the local computer in C:\\Windows\\Microsoft.NET and in the symbol cache (C:\\ProgramData\\dbg\\sym). When the debugger did not find the correct versions of the files on the local computer, it retrieved them from the public symbol server.

To verify that the version of mscordacwks.dll matches the version of the CLR that the application was using, enter one of the following commands to display information about the loaded CLR module.

**lmv -mclr** (for version 4.0 of the CLR)

**lmv -mscorwks** (for version 1.0 or 2.0 of the CLR)

The output should be similar to this.

```dbgcmd
start             end                 module name
000007ff`26710000 000007ff`2706e000   clr        (deferred)             
    Image path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll
...
```

In the preceding example, notice that the version of the CLR (clr.dll) matches the version of the DAC (mscordacwks.dll): v4.0.30319. Also notice that both components are 64-bit.

### <span id="Using_the_SOS_Debugging_Extension_"></span><span id="using_the_sos_debugging_extension_"></span><span id="USING_THE_SOS_DEBUGGING_EXTENSION_"></span>Using the SOS Debugging Extension

To verify that the SOS debugging extension loaded correctly, enter the [**.chain**](-chain--list-debugger-extensions-.md) command.

```dbgcmd
0:000> .chain
Extension DLL search Path:
...
Extension DLL chain:
    C:\ProgramData\dbg\sym\SOS_AMD64_AMD64_4.0.30319.18010.dll\...
        ...
    dbghelp: image 6.13.0014.1665, API 6.2.6, built Wed Dec 12 03:02:43 2012
...
```

To test the SOS debugging extension, enter **!sos.help**. Then try one of the command provided by the SOS debugging extension. For example, you could try **!sos.DumpDomain** or the **!sos.Threads** command.

### <span id="Notes"></span><span id="notes"></span><span id="NOTES"></span>Notes

Sometimes a managed-code application loads more than one version of the CLR. In that case, you must specify which version of the DAC to load. For more information, see [**.cordll**](-cordll--control-clr-debugging-.md).

 

 





