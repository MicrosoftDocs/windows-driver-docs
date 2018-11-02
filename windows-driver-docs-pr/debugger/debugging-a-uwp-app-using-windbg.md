---
title: Debugging a UWP app using WinDbg
description: You can debug Universal Windows Platform (UWP) app using WinDbg.
ms.assetid: 1CE337AC-54C0-4EF5-A374-3ECF1D72BA60
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Debugging a UWP app using WinDbg


You can debug Universal Windows Platform (UWP) app using WinDbg. This approach would typically be used for advanced scenarios, where it is not possible to complete the debugging task using the built in Visual Studio debugger. For more information about debugging in Visual Studio, see [Debugging in Visual Studio](https://msdn.microsoft.com/library/sc65sadd.aspx).

## <span id="Attaching_to_a_UWP_app"></span><span id="attaching_to_a_uwp_app"></span><span id="ATTACHING_TO_A_UWP_APP"></span>Attaching to a UWP app


Attaching to UWP process is the same as attaching to a user mode process. For example, in WinDbg you can attach to a running process by choosing **Attach to a Process from the File** menu or by pressing F6. For more information, see [Debugging a User-Mode Process Using WinDbg](debugging-a-user-mode-process-using-windbg.md).

A UWP app will not be suspended in the same ways that it does when not being debugged. To explicitly suspend/resume a UWP app, you can use the .suspendpackage and .resumepackage commands (details below). For general information on Process Lifecycle Management (PLM) used by UWP apps, see [App lifecycle](https://msdn.microsoft.com/library/windows/apps/mt243287) and [Launching, resuming, and background tasks](https://msdn.microsoft.com/library/windows/apps/mt227652).

## <span id="Launching_and_debugging__a_UWP_app"></span><span id="launching_and_debugging__a_uwp_app"></span><span id="LAUNCHING_AND_DEBUGGING__A_UWP_APP"></span>Launching and debugging a UWP app


The -plmPackage and -plmApp command line parameters instruct the debugger to launch an app under the debugger.

```console
windbg.exe -plmPackage <PLMPackageName> -plmApp <ApplicationId> [<parameters>]
```

Since multiple apps can be contained within a single package, both &lt;PLMPackage&gt; and &lt;ApplicationId&gt; parameters are required. This is a summary of the parameters.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><strong>Parameter</strong></td>
<td align="left"><strong>Description</strong></td>
</tr>
<tr class="even">
<td align="left">&lt;PLMPackageName&gt;</td>
<td align="left">The name of the application package. Use the .querypackages command to lists all UWP applications. Do not provide a path to the location of the package, provide just the package name.</td>
</tr>
<tr class="odd">
<td align="left">&lt;ApplicationId&gt;</td>
<td align="left"><p>The ApplicationId is located in the application manifest file and can be viewed using the .querypackage or .querypackages command as discussed in this topic.</p>
<p>For more information about the application manifest file, see <a href="https://msdn.microsoft.com/library/windows/apps/br211474" data-raw-source="[App package manifest](https://msdn.microsoft.com/library/windows/apps/br211474)">App package manifest</a>.</p></td>
</tr>
<tr class="even">
<td align="left">[&lt;parameters&gt;]</td>
<td align="left"><p>Optional parameters passed to the App. Not all apps use or require parameters.</p></td>
</tr>
</tbody>
</table>

 

**HelloWorld Sample**

To demonstrate UWP debugging, this topic uses the HelloWorld example described in [Create a "Hello, world" app (XAML)](https://msdn.microsoft.com/windows/uwp/get-started/create-a-hello-world-app-xaml-universal).

To create a workable test app, it is only necessary to complete up to step three of the lab.

**Locating the Full Package Name and AppId**

Use the .querypackages command to locate the full package name and the AppId. Type .querypackages and then user CRTL+F to search up in the output for the application name, such as HelloWorld. When the entry is located using CTRL+F, it will show the package full name, for example *e24caf14-8483-4743-b80c-ca46c28c75df\_1.0.0.0\_x86\_\_97ghe447vaan8* and the AppId of *App*.

Example:

```dbgcmd
0:000>  .querypackages 
...
Package Full Name: e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
Package Display Name: HelloWorld
Version: 1.0.0.0
Processor Architecture: x86
Publisher: CN=domars
Publisher Display Name: domars
Install Folder: c:\users\domars\documents\visual studio 2015\Projects\HelloWorld\HelloWorld\bin\x86\Release\AppX
Package State: Unknown
AppId: App
...
```

**Viewing the Base Package Name in the in the Manifest**

For troubleshooting, you may want to view the base package name in Visual Studio.

To locate the base package name in Visual Studio, click on the ApplicationManifest.xml file in project explorer. The base package name will be displayed under the packaging tab as "Package name". By default, the package name will be a GUID, for example *e24caf14-8483-4743-b80c-ca46c28c75df*.

To use notepad to locate the base package name, open the ApplicationManifest.xml file and locate the **Identity Name** tag.

```xml
  <Identity
    Name="e24caf14-8483-4743-b80c-ca46c28c75df"
    Publisher="CN= User1"
    Version="1.0.0.0" />
```

**Locating the Application Id in the Manifest**

To locate the Application Id in the manifest file for an installed UWP app, look for the *Application Id* entry.

For example, for the hello world app the Application ID is *App*.

```xml
<Application Id="App"
      Executable="$targetnametoken$.exe"
      EntryPoint="HelloWorld.App">
```

**Example WinDbg Command Line**

This is an example command line loading the HelloWorld app under the debugger using the full package name and AppId.

```console
windbg.exe -plmPackage e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8 -plmApp App
```

## <span id="Launching_a_background_task_under_the_debugger"></span><span id="launching_a_background_task_under_the_debugger"></span><span id="LAUNCHING_A_BACKGROUND_TASK_UNDER_THE_DEBUGGER"></span>Launching a background task under the debugger


A background task can be explicitly launched under the debugger from the command line using the TaskId. To do this, use the -plmPackage and -plmBgTaskId command line parameters:

```console
windbg.exe -plmPackage <PLMPackageName> -plmBgTaskId <BackgroundTaskId>
```

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><strong>Parameter</strong></td>
<td align="left"><strong>Description</strong></td>
</tr>
<tr class="even">
<td align="left">&lt;PLMPackageName&gt;</td>
<td align="left"><p>The name of the application package. Use the .querypackages command to lists all UWP applications. Do not provide a path to the location of the package, provide just the package name.</p></td>
</tr>
<tr class="odd">
<td align="left">&lt;BackgroundTaskId&gt;</td>
<td align="left"><p>The BackgroundTaskId can be located using the .querypackages command as described below.</p>
<p>For more information about the application manifest file, see <a href="https://msdn.microsoft.com/library/windows/apps/br211474" data-raw-source="[App package manifest](https://msdn.microsoft.com/library/windows/apps/br211474)">App package manifest</a>.</p></td>
</tr>
</tbody>
</table>

 

This is an example of loading the SDKSamples.BackgroundTask code under the debugger.

```console
windbg.exe -plmPackage Microsoft.SDKSamples.BackgroundTask.CPP_1.0.0.0_x64__8wekyb3d8bbwe -plmBgTaskId {ee4438ee-22db-4cdd-85e4-8ad8a1063523}
```

You can experiment with the Background task sample code to become familiar with UWP debugging. It can be downloaded at [Background task sample](https://code.msdn.microsoft.com/windowsapps/Background-Task-Sample-9209ade9).

Use the .querypackages command to locate the BackgroundTaskId. Use CTRL-F to locate the app and then locate the *Background Task Id* field. The background task must be running to display the associated background task name and task Id.

```dbgcmd
0:000> .querypackages
...
Package Full Name: Microsoft.SDKSamples.BackgroundTask.CPP_1.0.0.0_x86__8wekyb3d8bbwe
Package Display Name: BackgroundTask C++ sample
Version: 1.0.0.0
Processor Architecture: x86
Publisher: CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
Publisher Display Name: Microsoft Corporation
Install Folder: C:\Users\DOMARS\Documents\Visual Studio 2015\Projects\Background_task_sample\C++\Debug\BackgroundTask.Windows\AppX
Package State: Running
AppId: BackgroundTask.App
Background Task Name: SampleBackgroundTask
Background Task Id: {ee4438ee-22db-4cdd-85e4-8ad8a1063523}
...
```

If you know the full package name you can use .querypackage to display the *Background Task Id* field.

You can also locate the BackgroundTaskId by using the enumerateBgTasks option of the PLMDebug. For more information about the PMLDebug utiltity, see [**PLMDebug**](plmdebug.md).

```console
C:\Program Files\Debugging Tools for Windows (x64)>PLMDebug /enumerateBgTasks Microsoft.SDKSamples.BackgroundTask.CPP_1.0.0.0_x64__8wekyb3d8bbwe
Package full name is Microsoft.SDKSamples.BackgroundTask.CPP_1.0.0.0_x64__8wekyb3d8bbwe.
Background Tasks:
SampleBackgroundTask : {C05806B1-9647-4765-9A0F-97182CEA5AAD}

SUCCEEDED
```

## <span id="Debugging_a_UWP_process_remotely_using_a_Process_Server__DbgSrv_"></span><span id="debugging_a_uwp_process_remotely_using_a_process_server__dbgsrv_"></span><span id="DEBUGGING_A_UWP_PROCESS_REMOTELY_USING_A_PROCESS_SERVER__DBGSRV_"></span>Debugging a UWP process remotely using a Process Server (DbgSrv)


All of the -plm\* commands work correctly with dbgsrv. To debug using dbgsrv, use the -premote switch with the connection string for dbgsrv:

```console
windbg.exe -premote npipe:pipe=fdsa,server=localhost -plmPackage e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8 -plmApp App
```

For more information about the -premote options, see [Process Servers (User Mode)](process-servers--user-mode-.md) and [Process Server Examples](process-server-examples.md).

## <span id="Summary_of_UWP_app_commands"></span><span id="summary_of_uwp_app_commands"></span><span id="SUMMARY_OF_UWP_APP_COMMANDS"></span>Summary of UWP app commands


This section provides a summary of UWP app debugger commands

**Gathering Package Information**

**.querypackage**

The .querypackage displays the state of a UWP application. For example, if the app is running, it can be in the *Active* state.

```dbgcmd
.querypackage <PLMPackageName>
```

Example:

```dbgcmd
0:000> .querypackage e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
Package Full Name: e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
Package Display Name: HelloWorld
Version: 1.0.0.0
Processor Architecture: x86
Publisher: CN=domars
Publisher Display Name: domars
Install Folder: c:\users\domars\documents\visual studio 2015\Projects\HelloWorld\HelloWorld\bin\x86\Release\AppX
Package State: Running
AppId: App
Executable: HelloWorld.exe
```

**.querypackages**

The .querypackages command lists all the installed UWP applications and their current state.

```dbgcmd
.querypackages
```

Example:

```dbgcmd
0:000> .querypackages
...
Package Full Name: Microsoft.MicrosoftSolitaireCollection_3.9.5250.0_x64__8wekyb3d8bbwe
Package Display Name: Microsoft Solitaire Collection
Version: 3.9.5250.0
Processor Architecture: x64
Publisher: CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
Publisher Display Name: Microsoft Studios
Install Folder: C:\Program Files\WindowsApps\Microsoft.MicrosoftSolitaireCollection_3.9.5250.0_x64__8wekyb3d8bbwe
Package State: Unknown
AppId: App

Package Full Name: e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
Package Display Name: HelloWorld
Version: 1.0.0.0
Processor Architecture: x86
Publisher: CN=domars
Publisher Display Name: domars
Install Folder: c:\users\domars\documents\visual studio 2015\Projects\HelloWorld\HelloWorld\bin\x86\Release\AppX
Package State: Running
AppId: App
Executable: HelloWorld.exe

Package Full Name: Microsoft.SDKSamples.BackgroundTask.CPP_1.0.0.0_x86__8wekyb3d8bbwe
Package Display Name: BackgroundTask C++ sample
Version: 1.0.0.0
Processor Architecture: x86
Publisher: CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
Publisher Display Name: Microsoft Corporation
Install Folder: C:\Users\DOMARS\Documents\Visual Studio 2015\Projects\Background_task_sample\C++\Debug\BackgroundTask.Windows\AppX
Package State: Unknown
AppId: BackgroundTask.App

...
```

**Launching an app for Debugging**

**.createpackageapp**

The .createpackageapp command enables debugging and launches a UWP application.

```dbgcmd
.createpackageapp <PLMPackageName> <ApplicationId> [<parameters>] 
```

This table lists the parameters for .createpackageapp.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><strong>Parameter</strong></td>
<td align="left"><strong>Description</strong></td>
</tr>
<tr class="even">
<td align="left">&lt;PLMPackageName&gt;</td>
<td align="left">The name of the application package. Use the .querypackages command to lists all UWP applications. Do not provide a path to the location of the package, provide just the package name.</td>
</tr>
<tr class="odd">
<td align="left">&lt;ApplicationId&gt;</td>
<td align="left"><p>The ApplicationId can be located using .querypackage or .querypackages as discussed earlier in this topic.</p>
<p>For more information about the application manifest file, see <a href="https://msdn.microsoft.com/library/windows/apps/br211474" data-raw-source="[App package manifest](https://msdn.microsoft.com/library/windows/apps/br211474)">App package manifest</a>.</p></td>
</tr>
<tr class="even">
<td align="left">[&lt;parameters&gt;]</td>
<td align="left">Optional parameters that are passed to the application. Not all applications require or use these optional parameters.</td>
</tr>
</tbody>
</table>

 

Example:

```dbgcmd
.createpackageapp e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8 App
```

**Enabling and Disabling Use of Debug Commands**

**.enablepackagedebug**

The .enablepackagedebug command enables debugging for UWP application. You must use .enablepackagedebug before you call any of the suspend, resume, or terminate functions.

Note that the .createpackageapp command also enables debugging of the app.

```dbgcmd
.enablepackagedebug <PLMPackageName>
```

Example:

```dbgcmd
.enablepackagedebug e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

**.disablepackagedebug**

The .disablepackagedebug command disables debugging for UWP application.

```dbgcmd
.disablepackagedebug <PLMPackageName>
```

Example:

```dbgcmd
.disablepackagedebug e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

**Starting and Stopping apps**

Note that suspend, resume, and terminate affect all currently running apps in the package.

**.suspendpackage**

The .suspendpackage command, suspends a UWP application.

```dbgcmd
.suspendpackage <PLMPackageName> 
```

Example:

```dbgcmd
0:024> .suspendpackage e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

**.resumepackage**

The .resumepackage command resumes a UWP application.

```dbgcmd
.resumepackage <PLMPackageName> 
```

Example:

```dbgcmd
.resumepackage e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

**.terminatepackageapp**

The .terminatepackageapp command terminates the all of the UWP applications in the package.

```dbgcmd
.terminatepackageapp <PLMPackageName> 
```

Example:

```dbgcmd
.terminatepackageapp e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

**Background Tasks**

**.activatepackagebgtask**

The .activatepackagebgtask command enables debugging and launches a UWP background task.

```dbgcmd
 .activatepackagebgtask <PLMPackageName> <bgTaskId>
```

Example:

```dbgcmd
.activatepackagebgtask Microsoft.SDKSamples.BackgroundTask.CPP_1.0.0.0_x64__8wekyb3d8bbwe {C05806B1-9647-4765-9A0F-97182CEA5AAD}
```

## <span id="Usage_Examples"></span><span id="usage_examples"></span><span id="USAGE_EXAMPLES"></span>Usage Examples


**Attach a debugger when your app is launched**

Suppose you have an app named HelloWorld that is in a package named e24caf14-8483-4743-b80c-ca46c28c75df\_1.0.0.0\_x86\_\_97ghe447vaan8. Verify that your package is installed by displaying the full names and running states all installed packages. In a Command Prompt window, enter the following command. You can use CTRL+F to search the command output for the app name of HelloWorld.

```dbgcmd
.querypackages 
...

Package Full Name: e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
Package Display Name: HelloWorld
Version: 1.0.0.0
Processor Architecture: x86
Publisher: CN=domars
Publisher Display Name: user1
Install Folder: c:\users\user1\documents\visual studio 2015\Projects\HelloWorld\HelloWorld\bin\x86\Release\AppX
Package State: Unknown
AppId: App

...
```

Use .createpackageapp to launch and attach to the app. The .createpackageapp command also enables debugging of the app.

```dbgcmd
.createpackageapp e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8 App
```

When you have finished debugging, decrement the debug reference count for the package using the .disablepackagedebug command.

```dbgcmd
.disablepackagedebug e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

**Attach a debugger to an app that is already running**

Suppose you want to attach WinDbg to MyApp, which is already running. In WinDbg, on the **File** menu, choose **Attach to a Process**. Note the process ID for MyApp. Let's say the process ID is 4816. Increment the debug reference count for the package that contains MyApp.

```dbgcmd
.enablepackagedebug e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

In WinDbg, in the **Attach to Process** dialog box, select process 4816, and click OK. WinDbg will attach to MyApp.

When you have finished debugging, decrement the debug reference count for the package using the .disablepackagedebug command.

```dbgcmd
.disablepackagedebug e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

**Manually suspend and resume your app**

Follow these steps to manually suspend and resume your app. First, increment the debug reference count for the package that contains your app.

```dbgcmd
.enablepackagedebug  e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

Suspend the package. Your app's suspend handler is called, which can be helpful for debugging.

```dbgcmd
.suspendpackage e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

When you have finished debugging, resume the package.

```dbgcmd
.resumepackage e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

Finally, decrement the debug reference count for the package.

```dbgcmd
.disablepackagedebug e24caf14-8483-4743-b80c-ca46c28c75df_1.0.0.0_x86__97ghe447vaan8
```

## <span id="related_topics"></span>Related topics


[Debugging Using WinDbg](debugging-using-windbg.md)

 

 






