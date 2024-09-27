---
title: Debugging Managed Code Using the Windows Debugger
description: You can use the windows debuggers (WinDbg, CDB, and NTSD) to debug target applications that contain managed code.
keywords: debugging, debug, Windbg, managed code debugging, .NET common language runtime, common language runtime, CLR , JIT compiler, JITted code
ms.date: 09/27/2024
---

# Debugging Managed Code Using the Windows Debugger

You can use the Windows debuggers (WinDbg, CDB, and NTSD) to debug target applications that contain managed code. To debug managed code, use the !SOS debugging extension (sos.dll) and a data access component (mscordacwks.dll) in combination with the CLR runtime.

The Windows debuggers, such as WinDbg are separate from the Visual Studio debugger. For information about the distinction between the Windows debuggers and the Visual Studio debugger, see [Debugging Tools for Windows](debugger-download-tools.md).

This article provides instructions on using Windows debuggers (WinDbg, CDB, NTSD) to debug managed code, including .NET Framework, .NET Core, and .NET 5+ applications.

> [!NOTE]
> When debugging .NET Framework, .NET Core, and .NET 5+ applications, ensure that you are using the latest version of the Windows Debugger tools. Additionally, consider using Visual Studio or Visual Studio Code for a more integrated debugging experience. WinDbg is more complex, takes more work to set up, and is typically used when additional low level information is required. 

## Introduction to Managed Code

Managed code is executed together with the Microsoft .NET Common Language Runtime (CLR). In a managed-code application, the binary code that the compiler produces is in Microsoft Intermediate Language (MSIL), which is platform-independent.

When managed code is run, the runtime produces native code that is platform-specific. The process of generating native code from MSIL is called *just-in-time (JIT) compiling*. After the JIT compiler has compiled the MSIL for a specific method, the method's native code remains in memory. Whenever this method is later called, the native code executes and the JIT compiler does not have to be involved.

You can build managed code by using several compilers that are manufactured by a variety of software producers. In particular, Microsoft Visual Studio can build managed code from several different languages including C#, Visual Basic, JScript, and C++ with managed extensions.

The CLR is not updated every time the .NET Framework is updated. For example, versions 2.0, 3.0, and 3.5 of the .NET Framework all use version 2.0 of the CLR. For additional information on .NET versions, see [.NET Framework versions and dependencies](/dotnet/framework/migration-guide/versions-and-dependencies). For information on determing the version of .NET on your PC, see [Determine which .NET Framework versions are installed](/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed).

## Debugging Managed Code

To debug managed code using the !SOS debugging extension, the debugger must load various components. The !SOS debugging extension and the required components that are used for different for .NET Core and the original .NET Framework. For either, the Data Access Component (DAC) (mscordacwks.dll) is used.

The .NET SDK provides tools that may be helpful in working with debugging .NET apps. For more information, see [What is the .NET SDK?](/dotnet/core/sdk).

### .NET Core 

- For .NET Core or .NET 5+ and later versions, the runtime is `coreclr.dll`. For more information, see [Common Language Runtime (CLR) overview](/dotnet/standard/clr).
- [.NET Core SOS debugging extension](/dotnet/core/diagnostics/sos-debugging-extension)

For .NET Core there is a dotnet CLI tool available to install !sos.dll. For more information, see [SOS installer (dotnet-sos)](/dotnet/core/diagnostics/dotnet-sos). 

### The Original .NET Framework.

- For the original .NET Framework, `clr.dll` is the runtime. 
- [SOS debugging extension (sos.dll)](/dotnet/framework/tools/sos-dll-sos-debugging-extension)


### Getting the SOS Debugging Extension (sos.dll)

The SOS debugging extension (sos.dll) files are not included in all versions of the Debugging Tools for Windows. If sos.dll is not available, see, [Installing SOS on Windows](https://github.com/dotnet/diagnostics/blob/main/documentation/installing-sos-windows-instructions.md). 

### Loading the SOS Debugging Extension (sos.dll)

To debug .NET Core and .NET 5+ applications, you need to load the appropriate version of the SOS debugging extension. 

For example, to a version of !SOS that is included with the debugger and is included in the current extension search path, the [**.load**](../debuggercmds/-load---loadby--load-extension-dll-.md) command would be used. 

`0:000> .load sos.dll`

To verify that the SOS debugging extension loaded correctly, use the [**.chain**](../debuggercmds/-chain--list-debugger-extensions-.md) command and exmaine the *Extension DLL chain*.

```dbgcmd
...
Extension DLL chain:
    C:\Windows\Microsoft.NET\Framework\v4.0.30319\SOS.dll: image 4.8.9275.0, API 1.0.0, built Wed Aug 28 14:43:27 2024
        [path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\SOS.dll]
    C:\Program Files (x86)\dotnet\shared\Microsoft.NETCore.App\8.0.8\coreclr.dll: image 8,0,824,36612 @Commit: 08338fcaa5c9b9a8190abb99222fed12aaba956c, built Tue Jul 16 11:10:19 2024
        [path: C:\Program Files (x86)\dotnet\shared\Microsoft.NETCore.App\8.0.8\coreclr.dll]
```

If the version of the debugger does not include the sos.dll, you might need to specify the complete path to the SOS.dll file. You can typically find the SOS.dll file in the runtime directory of your .NET Core or .NET Framework installation.

`0:000> .load C:\Windows\Microsoft.NET\Framework64\v4.0.30319\sos.dll`

### Loading a specific version of sos.dll

Loading the sos.dll can be complex, as there is a dependency on the additional DLLs, that are used by the sos.dll to communicate with .NET. In addition, the DLL version required is dependent on the .NET version of the app being debugged, and multiple versions of .NET may be  present on the machine. 

One strategy to load the correct version of the dependent DLL, is to ask the debugger to break in when the first .NET clr notification (CLRN) occurs using the sx, sxd, sxe, sxi, sxn, sxr, sx- (Set Exceptions)[../debuggercmds/sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md] command. Once you have attached to the target .NET application, this command would be used after the first break in.

`0:000> sxe CLRN`

Next resume execution and wait for the break to occur.

`0:000> g`

When the break occurs, disable the clr notification break, as we know clr.dll (or coreclr.dll) was loaded.

`0:000> sxd CLRN`

With the debugger in this context, use the [**.loadby**](../debuggercmds/-load---loadby--load-extension-dll-.md) to load the !sos from the same "nearby" directory location. 

`0:000> .loadby sos clr`

Another option is to use the [.cordll (Control CLR Debugging)](../debuggercmds/-cordll--control-clr-debugging-.md) to load the CLR debugging DLLs by providing a path to the target framework location.

```dbgcmd
0:000> .cordll -ve -u -lp C:\Windows\Microsoft.NET\Framework\v4.0.30319\
CLRDLL: Loaded DLL C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscordacwks.dll
Automatically loaded SOS Extension
CLR DLL status: Loaded DLL C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscordacwks.dll
```

### Using the SOS Debugging Extension

To verify that the SOS debugging extension loaded correctly, enter the [**.chain**](../debuggercmds/-chain--list-debugger-extensions-.md) command.

```dbgcmd
0:000> .chain
Extension DLL search Path:
    C:\Program Files\Debugging Tools for Windows (x64);...
Extension DLL chain:
    C:\Windows\Microsoft.NET\Framework\v4.0.30319\SOS.dll: image 4.8.9275.0, API 1.0.0, built Wed Aug 28 14:43:27 2024
        [path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\SOS.dll]
...
```

### .NET symbol files

Symbol files are essential for debugging. For .NET Framework, .NET Core, and .NET 5+ applications, you can retrieve the necessary symbol files from Microsoft's public symbol server. Use the following command to set the symbol path and echo symbol loading.

`.symfix` 

`!sym noisy`

`.reload`

### Testing the .NET Core !sos extension

To test the SOS debugging extension, enter **!sos.help**. 

```dbgcmd
0:000> !sos.help
-------------------------------------------------------------------------------
SOS is a debugger extension DLL designed to aid in the debugging of managed
programs. Functions are listed by category, then roughly in order of
importance. Shortcut names for popular functions are listed in parenthesis.
Type "!help <functionname>" for detailed info on that function. 

Object Inspection                  Examining code and stacks
-----------------------------      -----------------------------
DumpObj (do)                       Threads
DumpArray (da)                     ThreadState
DumpStackObjects (dso)             IP2MD
DumpHeap                           U
DumpVC                             DumpStack
GCRoot                             EEStack
ObjSize                            CLRStack
FinalizeQueue                      GCInfo
PrintException (pe)                EHInfo
TraverseHeap                       BPMD 
                                   COMState
```

Then try one of the command provided by the SOS debugging extension. For example, you could try **!sos.DumpDomain** or the **!sos.Threads** command provided by the [.NET Core SOS debugging extension](/dotnet/core/diagnostics/sos-debugging-extension).

```dbgcmd
0:000> !sos.DumpDomain
--------------------------------------
System Domain:      7565d980
LowFrequencyHeap:   7565dca4
HighFrequencyHeap:  7565dcf0
StubHeap:           7565dd3c
Stage:              OPEN
Name:               None
--------------------------------------
Shared Domain:      7565d620
LowFrequencyHeap:   7565dca4
HighFrequencyHeap:  7565dcf0
StubHeap:           7565dd3c
Stage:              OPEN
Name:               None
Assembly:           00fa5e78 [C:\WINDOWS\Microsoft.Net\assembly\GAC_32\mscorlib\v4.0_4.0.0.0__b77a5c561934e089\mscorlib.dll]
ClassLoader:        00fa5f40
  Module Name
73571000    C:\WINDOWS\Microsoft.Net\assembly\GAC_32\mscorlib\v4.0_4.0.0.0__b77a5c561934e089\mscorlib.dll

0:000> !sos.Threads
ThreadCount:      2
UnstartedThread:  0
BackgroundThread: 2
PendingThread:    0
DeadThread:       0
Hosted Runtime:   no
                                                                         Lock  
       ID OSID ThreadOBJ    State GC Mode     GC Alloc Context  Domain   Count Apt Exception
   0    1 4538 00f91110     20220 Preemptive  02FE1238:00000000 00f58be0 1     Ukn 
   7    2 250c 00f9da88     21220 Cooperative 00000000:00000000 00f58be0 1     Ukn (Finalizer) 
```

### Testing the .NET Framework !sos extension

To test the SOS debugging extension, enter **!sos.help**. Then try one of the command provided by the SOS debugging extension. For example, you could try **!sos.sostatus** or the **!sos.threads** command.

```dbgcmd
0:030> !soshelp
crashinfo                                 Displays the crash details that created the dump.
help, soshelp <command>                   Displays help for a command.
loadsymbols <url>                         Loads symbols for all modules.
logclose <path>                           Disables console file logging.
logging <path>                            Enables/disables internal diagnostic logging.
logopen <path>                            Enables console file logging.
maddress                                  Displays a breakdown of the virtual address space.
modules, lm                               Displays the native modules in the process.
registers, r                              Displays the thread's registers.
runtimes <id>                             Lists the runtimes in the target or changes the default runtime.
setclrpath <path>                         Sets the path to load coreclr DAC/DBI files.
setsymbolserver, SetSymbolServer <url>    Enables and sets symbol server support for symbols and module download.
sosflush                                  Resets the internal cached state.
sosstatus                                 Displays internal status.
threads, setthread <thread>               Lists the threads in the target or sets the current thread.
```

### Notes

Sometimes a managed-code application loads more than one version of the CLR. In that case, you must specify which version of the DAC to load. For more information, see [**.cordll**](../debuggercmds/-cordll--control-clr-debugging-.md) and [Clrver.exe (CLR Version Tool)](/dotnet/framework/tools/clrver-exe-clr-version-tool).
