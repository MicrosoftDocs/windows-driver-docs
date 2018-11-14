---
title: Preparing to Use UMDH
description: Preparing to Use UMDH
ms.assetid: 9adebe43-3167-4e1a-ac98-db19ace944be
keywords: ["UMDH, preparing to use UMDH", "UMDH, disabling BSTR caching", "SetNoOaCache function", "OANOCACHE environment variable", "stack trace database"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Preparing to Use UMDH


## <span id="ddk_preparing_to_use_umdh_dtools"></span><span id="DDK_PREPARING_TO_USE_UMDH_DTOOLS"></span>


You must complete the configuration tasks described in this section before using User-Mode Dump Heap (UMDH) to capture the heap allocations for a process. If the computer is not configured correctly, UMDH will not generate any results or the results will be incomplete or incorrect.

### <span id="create_the_user_mode_stack_trace_database"></span><span id="CREATE_THE_USER_MODE_STACK_TRACE_DATABASE"></span>Create the user-mode stack trace database

Before using UMDH to capture the heap allocations for a process, you must configure Windows to capture stack traces.

To enable stack trace capturing for a process, use [GFlags](gflags.md) to set the **Create user mode stack trace database** flag for the process. This can be done by either of the following methods:

-   In the GFlags graphical interface, choose the **Image File** tab. Type the process name, including the file name extension (for example, Notepad.exe). Press the **TAB** key, select **Create user mode stack trace database**, and then click **Apply**.

-   Or, equivalently, use the following GFlags command line, where *ImageName* is the process name (including the file name extension):

    **gflags /i** *ImageName* **+ust**

By default, the amount of stack trace data that Windows gathers is limited to 32 MB on an x86 processor, and 64 MB on an x64 processor. If you must increase the size of this database, choose the **Image File** tab in the GFlags graphical interface, type the process name, press the **TAB** key, check the **Stack Backtrace (Megs)** check box, type a value (in MB) in the associated text box, and then click **Apply**.

**Note**   Increase this database only when necessary, because it may deplete limited Windows resources. When you no longer need the larger size, return this setting to its original value.

 

These settings affects all new instances of the program. It does not affect currently running instances of the program.

### <span id="access_the_necessary_symbols"></span><span id="ACCESS_THE_NECESSARY_SYMBOLS"></span>Access the Necessary Symbols

Before using UMDH, you must have access to the proper symbols for your application. UMDH uses the symbol path specified by the environment variable \_NT\_SYMBOL\_PATH. Set this variable equal to a path containing the symbols for your application.

If you also include a path to Windows symbols, the analysis may be more complete. The syntax for this symbol path is the same as that used by the debugger; for details, see [Symbol Path](symbol-path.md).

For example, if the symbols for your application are located at C:\\MyApp\\Symbols, and you have installed the Windows symbol files to \\\\myshare\\winsymbols, you would use the following command to set your symbol path:

```console
set _NT_SYMBOL_PATH=c:\myapp\symbols;\\myshare\winsymbols
```

As another example, if the symbols for your application are located at C:\\MyApp\\Symbols, and you want to use the public Microsoft symbol store for your Windows symbols, using C:\\MyCache as your downstream store, you would use the following command to set your symbol path:

```console
set _NT_SYMBOL_PATH=c:\myapp\symbols;srv*c:\mycache*https://msdl.microsoft.com/download/symbols
```

**Important**  Suppose you have two computers: a *logging computer* where you create a UMDH log and an *analysis computer* where you analyze the UMDH log. The symbol path on your analysis computer must point to the symbols for the version of Windows that was loaded on the logging computer at the time the log was made. Do not point the symbol path on the analysis computer to a symbol server. If you do, UMDH will retrieve symbols for the version of Windows that is running on the analysis computer, and UMDH will not display meaningful results.

 

### <span id="disable_bstr_caching"></span><span id="DISABLE_BSTR_CACHING"></span>Disable BSTR Caching

Automation (formerly known as OLE Automation) caches the memory used by BSTR strings. This can prevent UMDH from correctly determining the owner of a memory allocation. To avoid this problem, you must disable BSTR caching.

To disable BSTR caching, set the OANOCACHE environment variable equal to one (1). This setting must be made before launching the application whose allocations are to be traced.

Alternatively, you can disable BSTR caching from within the application itself by calling the .NET Framework **SetNoOaCache** function. If you choose this method, you should call this function early, because any BSTR allocations that have already been cached when **SetNoOaCache** is called will remain cached.

If you need to trace the allocations made by a service, you must set OANOCACHE as a system environment variable and then restart Windows for this setting to take effect.

On Windows 2000, in addition to setting OANOCACHE equal to 1, you must also install the hotfix available with [Microsoft Support Article 139071](https://go.microsoft.com/fwlink/p/?LinkId=241583). This hotfix is not needed on Windows XP and later versions of Windows.

### <span id="find_the_process_id"></span><span id="FIND_THE_PROCESS_ID"></span>Find the Process ID

UMDH identifies the process by its process identifier (PID). You can find the PID of any running process by using Task Manager, Tasklist (Windows XP and later operating systems), or [TList](tlist.md).

 

 





