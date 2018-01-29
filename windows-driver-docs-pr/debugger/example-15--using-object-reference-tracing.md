---
title: Example 15 Using Object Reference Tracing
description: Example 15 Using Object Reference Tracing
ms.assetid: 3c6102e6-4dac-4d90-ab8f-162dd6d8adf9
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Example 15: Using Object Reference Tracing


Object Reference Tracing is a Windows feature that records a sequential stack trace when an object is referenced or dereferenced. It is designed to detect errors in object handling that can lead to crashes or memory leaks. Some of these errors are difficult to detect because they do not appear consistently. For detailed information, see [Object Reference Tracing](object-reference-tracing.md).

You can configure Object Reference Tracing by using the **Global Flags** dialog box or at a command prompt. The following examples use the command prompt. For information about using the **Global Flags** dialog box to configure Object Reference Tracing, see [Configuring Object Reference Tracing](configuring-object-reference-tracing.md).

You can use Gflags to enable, disable, and configure Object Reference Tracing. The process is as follows:

-   **Use Gflags to enable Object Reference Tracing** in the registry or as a kernel flag (run time) setting. If you add the setting to the registry, you must restart the computer to start tracing. If you enable the run time version of the settings, the trace starts immediately, but the trace settings revert to those in the registry key when you shut down or restart the computer.

-   **Start the process that creates the suspect object**. The trace includes only objects created by processes that are started after the trace begins. If the process starts during or soon after restarting, add the trace settings to the registry, and then restart the system.

-   **Use the** [**!obtrace**](-obtrace.md) **debugger extension** to view the trace. By default, the trace is maintained until the object is destroyed, but you can use the **/p** parameter to maintain the trace until tracing is disabled.

-   **Use Gflags to disable Object Reference Tracing**.in the registry or as a kernel flag (run time) setting. If you delete the setting from the registry, you must restart the computer to end tracing. If you disable the run time version of the settings, the trace ends immediately, but the trace settings revert to those in the registry when you shut down or restart the computer.

These examples show how to use Gflags to enable and disable object reference tracing. \\

### <span id="enable_run_time_tracing"></span><span id="ENABLE_RUN_TIME_TRACING"></span>Enable Run-time Tracing

The following command enables Object Reference Tracing at the command prompt. The command uses the **/ko** parameter to enable Object Reference Tracing as a kernel flag (run time) setting. The command uses the **/t** parameter to specify the pool tags **Tag1** and **Fred**. As a result, all objects that are created with **Tag1** or **Fred** are traced.

```
gflags /ko /t Tag1;Fred
```

Because the command changes the kernel flag (run-time) settings, object reference tracing starts immediately. The trace will include all objects with the pool tags **Tag1** or **Fred** that are created by processes that start after the command is submitted.

Gflags responds by printing the following message:

```
Running Kernel Settings :
Object Ref Tracing Enabled
        Temporary Traces
        Pool Tags: Tag1;Fred
        Process Name: All Processes
```

This message indicates that Object Reference Tracing is enabled. "Temporary Traces" indicates that all records of the trace are deleted when the object is destroyed. To make the trace "permanent," use the **/p** parameter, which directs Windows to retain the trace data until Object Reference Tracing is disabled, or the computer is shut down or restarted.

### <span id="enable_tracing_in_the_registry"></span><span id="ENABLE_TRACING_IN_THE_REGISTRY"></span>Enable Tracing in the Registry

The following command adds an Object Reference Tracing configuration to the registry. The trace that you configure begins when you restart the computer.

The command uses the **/ro** parameter to enable Object Reference Tracing as a registry setting. The command uses the **/i** to specify the process for notepad.exe and the **/t** parameter to specify the pool tags **Tag1** and **Fred**. As a result, all objects that are created by the Notepad process with the **Tag1** or **Fred** pool tags are traced. The command also uses the **/p** parameter, which retains the trace data until the tracing is disabled.

```
gflags /ro /t Tag1;Fred /i Notepad.exe /p
```

When you submit the command, Gflags stores the information in the registry. However, because registry settings are not effective until you restart the computer, this object reference tracing is configured, but is not yet started.

Gflags responds by printing the following message:

```
Boot Registry Settings :
Object Ref Tracing Enabled
        Permanent Traces
        Pool Tags: Tag1;Fred
        Process Name: Notepad.exe
```

The message indicates that Object Reference Tracing is enabled in the registry. "Permanent Traces" indicates that the trace data will be retained until you shut down or restart the computer. The message also lists the pool tags and image file names that will be traced.

### <span id="display_the_object_reference_tracing_configuration"></span><span id="DISPLAY_THE_OBJECT_REFERENCE_TRACING_CONFIGURATION"></span>Display the Object Reference Tracing Configuration

You can display the Object Reference Tracing configuration that is currently effective or is stored in the registry to be used when the computer is restarted.

In this example, there is one Object Reference Tracing configuration stored in the registry and a different one configured for run time. The run-time trace begins immediately (and overrides any registry settings). However, if you restart the system, the run-time settings are lost, and the Object Reference Tracing session registry settings become effective.

The following command displays the run time Object Reference Tracing configuration. It uses the **/ko** parameter with no other parameters.

```
gflags /ko
```

```
Running Kernel Settings :
Object Ref Tracing Enabled
        Temporary Traces
        Pool Tags: Tag1;Fred
        Process Name: All Processes
```

If Object Reference Tracing is enabled, as it is in this example, the settings that are displayed describe a trace that is in progress.

The following command displays the Object Reference Tracing configuration data stored in the registry. It uses the **/ro** parameter with no other parameters.

```
gflags /ro
```

In response, Gflags displays the data stored in the registry:

```
Boot Registry Settings :
Object Ref Tracing Enabled
        Permanent Traces
        Pool Tags: Tag1;Fred
        Process Name: Notepad.exe
```

If you have restarted the computer since you added the Object Reference Tracing configuration to the registry, the settings that are displayed in response to a gflags /ro command describe the trace that is in progress. However, if you have not yet restarted, or you have restarted, but then started a run-time object reference trace (**/ko**), the settings that are stored in the registry are not currently effective, but they will become effective again when you reboot the system.

### <span id="disable_object_reference_tracing"></span><span id="DISABLE_OBJECT_REFERENCE_TRACING"></span>Disable Object Reference Tracing

When you disable run-time (kernel flag) Object Reference Tracing settings, the trace stops immediately. When you disable Object Reference Tracing settings in the registry, the trace stops when you restart the computer.

The following command disables run-time Object Reference Tracing. It uses the **/d** parameter to disable all settings. You cannot disable settings selectively.

```
gflags /ko -d
```

When the command succeeds, Gflags responds with the following message:

```
Running Kernel Settings :
Object Ref Tracing Disabled
```

The following command disables run-time Object Reference Tracing.

The following command disables Object Reference Tracing settings in the registry. It uses the **/d** parameter to disable all settings. You cannot disable settings selectively. This command is effective when you restart the computer.

```
gflags /ro -d
```

When the command succeeds, Gflags responds with the following message:

```
Boot Registry Settings :
Object Ref Tracing Disabled
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%2015:%20Using%20Object%20Reference%20Tracing%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




