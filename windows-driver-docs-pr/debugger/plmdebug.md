---
title: PLMDebug
description: PLMDebug.exe is a tool that enables you to use the Windows debugger to debug Windows app, which run under Process Lifecycle Management (PLM). 
ms.assetid: 68BE8F5D-6425-43E2-B5BC-C1D35614AB32
keywords: ["PLMDebug Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PLMDebug
api_type:
- NA
ms.localizationpriority: medium
---

# PLMDebug


PLMDebug.exe is a tool that enables you to use the Windows debugger to debug Windows app, which run under Process Lifecycle Management (PLM). With PLMDebug, you can take manual control of suspending, resuming, and terminating a Windows app.

**Tip**  With Windows 10, version 1607 or later, you can use the UWP commands, such as .createpackageapp to debug UWP apps. For more information see [Debugging a UWP app using WinDbg](debugging-a-uwp-app-using-windbg.md).

 

**Where to get PLMDebug**

PLMDebug.exe is included in [Debugging Tools for Windows](index.md).

```console
plmdebug /query [Package]
plmdebug /enableDebug Package [DebuggerCommandLine]
plmdebug /terminate Package
plmdebug /forceterminate Package
plmdebug /cleanterminate Package
plmdebug /suspend Package
plmdebug /resume Package
plmdebug /disableDebug Package
plmdebug /enumerateBgTasks Package
plmdebug /activateBgTaskTaskId
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Package"></span><span id="_______package"></span><span id="_______PACKAGE"></span> *Package*  
The full name of a package or the ID of a running process.

<span id="_______DebuggerCommandLine"></span><span id="_______debuggercommandline"></span><span id="_______DEBUGGERCOMMANDLINE"></span> *DebuggerCommandLine*  
A command line to open a debugger. The command line must include the full path to the debugger. If the path has blank spaces, it must be enclosed in quotes. The command line can also include arguments. Here are some examples:

`"C:\Program Files (x86)\Windows Kits\8.0\Debuggers\x64\WinDbg.exe"`

`"\"C:\Program Files\Debugging Tools for Windows (x64)\WinDbg.exe\" -server npipe:pipe=test"`

<span id="________query_Package"></span><span id="________query_package"></span><span id="________QUERY_PACKAGE"></span> **/query** \[*Package*\]  
Displays the running state for an installed package. If *Package* is not specified, this command displays the running states for all installed packages.

<span id="________enableDebug_Package_DebuggerCommandLine"></span><span id="________enabledebug_package_debuggercommandline"></span><span id="________ENABLEDEBUG_PACKAGE_DEBUGGERCOMMANDLINE"></span> **/enableDebug** *Package* \[*DebuggerCommandLine*\]  
Increments the debug reference count for a package. The package is exempt from PLM policy if it has a non-zero debug reference count. Each call to **/enableDebug** must be paired with a call to /**disableDebug**. If you specify *DebuggerCommandLine*, the debugger will attach when any app from the package is launched.

<span id="________terminate_Package"></span><span id="________terminate_package"></span><span id="________TERMINATE_PACKAGE"></span> **/terminate** *Package*  
Terminates a package.

<span id="________forceTerminate_Package"></span><span id="________forceterminate_package"></span><span id="________FORCETERMINATE_PACKAGE"></span> **/forceTerminate** *Package*  
Forces termination of a package.

<span id="________cleanTerminate_Package"></span><span id="________cleanterminate_package"></span><span id="________CLEANTERMINATE_PACKAGE"></span> **/cleanTerminate** *Package*  
Suspends and then terminates a package.

<span id="________suspend_Package"></span><span id="________suspend_package"></span><span id="________SUSPEND_PACKAGE"></span> **/suspend** *Package*  
Suspends a package.

<span id="________resume_Package"></span><span id="________resume_package"></span><span id="________RESUME_PACKAGE"></span> **/resume** *Package*  
Resumes a package.

<span id="________disableDebug_Package"></span><span id="________disabledebug_package"></span><span id="________DISABLEDEBUG_PACKAGE"></span> **/disableDebug** *Package*  
Decrements the debug reference count for a package.

<span id="________enumerateBgTasksPackage"></span><span id="________enumeratebgtaskspackage"></span><span id="________ENUMERATEBGTASKSPACKAGE"></span> **/enumerateBgTasks***Package*  
Enumerate background task ids for a package.

<span id="________activateBgTaskTaskId"></span><span id="________activatebgtasktaskid"></span><span id="________ACTIVATEBGTASKTASKID"></span> **/activateBgTask***TaskId*  
Activates a background task. Note that not all background tasks can be activated using PLMDebug.

Remarks
-------

You must call **plmdebug /enableDebug** before you call any of the suspend, resume, or terminate functions.

The PLMDebug tool calls the methods of the [IPackageDebugSettings interface](https://go.microsoft.com/fwlink/p/?LinkID=267918). This interface enables you to take manual control of the process lifecycle management for your apps. Through this interface (and as a result, through this tool), you can suspend, resume, and terminate your Windows app. Note that the methods of the [IPackageDebugSettings interface](https://go.microsoft.com/fwlink/p/?LinkID=267918) apply to an entire package. Suspend, resume, and terminate affect all currently running apps in the package.

Examples
--------

**Example 1**

**Attach a debugger when your app is launched**

Suppose you have an app named MyApp that is in a package named MyApp\_1.0.0.0\_x64\_\_tnq5r49etfg3c. Verify that your package is installed by displaying the full names and running states all installed packages. In a Command Prompt window, enter the following command.

**plmdebug /query**

```console
Package full name: 1daa103b-74e1-426d-8193-b6bc7ed66fed_1.0.0.0_x86__tnq5r49etfg3c
Package state: Terminated

Package full name: 41fb5f27-7b60-4f5e-8459-803673131dd9_1.0.0.0_x86__tnq5r49etfg3c
Package state: Suspended
...
Package full name: MyApp_1.0.0.0_x64__tnq5r49etfg3c
Package state: Terminated
...
```

Increment the debug reference count for your package, and specify that you want WinDbg to attach when your app is launched.

**plmdebug /enableDebug MyApp\_1.0.0.0\_x64\_\_tnq5r49etfg3c "C:\\Program Files (x86)\\Windows Kits\\8.0\\Debuggers\\x64\\WinDbg.exe"**

When you launch your app, WinDbg will attach and break in.

When you have finished debugging, detach the debugger. Then decrement the debug reference count for your package.

**plmdebug /disableDebug MyApp\_1.0.0.0\_x64\_\_tnq5r49etfg3c**

**Example 2**

**Attach a debugger to an app that is already running**

Suppose you want to attach WinDbg to MyApp, which is already running. In WinDbg, on the **File** menu, choose **Attach to a Process**. Note the process ID for MyApp. Let's say the process ID is 4816.

Increment the debug reference count for the package that contains MyApp.

**plmdebug /enableDebug 4816**

In WinDbg, in the **Attach to Process** dialog box, select process 4816, and click **OK**. WinDbg will attach to MyApp.

When you have finished debugging MyApp, detach the debugger. Then decrement the debug reference count for the package.

**plmdebug /disableDebug 4816**

**Example 3**

**Manually suspend and resume your app**

Suppose you want to manually suspend and resume your app. First, increment the debug reference count for the package that contains your app.

**plmdebug /enableDebug MyApp\_1.0.0.0\_x64\_\_tnq5r49etfg3c**

Suspend the package. Your app's suspend handler is called, which can be helpful for debugging.

**plmdebug /suspend MyApp\_1.0.0.0\_x64\_\_tnq5r49etfg3c**

When you have finished debugging, resume the package.

**plmdebug /resume MyApp\_1.0.0.0\_x64\_\_tnq5r49etfg3c**

Finally, decrement the debug reference count for the package.

**plmdebug /disableDebug MyApp\_1.0.0.0\_x64\_\_tnq5r49etfg3c**

## <span id="see_also"></span>See also


[How to trigger suspend, resume, and background events in Windows Apps](https://go.microsoft.com/fwlink/p/?LinkID=267916)

[Tools Included in Debugging Tools for Windows](extra-tools.md)

 

 






