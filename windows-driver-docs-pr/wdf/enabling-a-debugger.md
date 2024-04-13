---
title: How to Enable Debugging of a UMDF Driver
description: How to Enable Debugging of a UMDF Driver
keywords:
- debuggers WDK UMDF
- debuggers WDK UMDF , enabling
- User-Mode Driver Framework WDK , enabling a debugger
- UMDF WDK , enabling a debugger
- user-mode drivers WDK UMDF , enabling a debugger
- debugging drivers WDK UMDF , enabling a debugger
- driver debugging WDK UMDF , enabling a debugger
ms.date: 04/20/2017
---

# How to Enable Debugging of a UMDF Driver


You can use the following configurations to debug a User-Mode Driver Framework (UMDF) driver during development. All configurations involve two machines, a host and a target. 

-   Manually copy the driver to the target. Perform user-mode debugging on the target. In this scenario, you attach manually to an instance of the driver host process running on the target.
-   Manually copy the driver to the target and then perform kernel-mode debugging from the host.

We recommend doing all UMDF driver testing and development with a kernel debugger attached.

## <a href="" id="bp"></a>Best Practices

We recommend doing all UMDF driver testing with a kernel debugger attached.

The following are recommended settings. You can set these manually, or use the [WDF Verifier Control Application](../devtest/wdf-verifier-control-application.md) (WDFVerifier.exe) tool in the WDK to view or change these settings.

-   Enable Application Verifier on WUDFHost.exe:

    ```cpp
    AppVerif –enable Heaps Exceptions Handles Locks Memory TLS Leak –for WudfHost.exe
    ```

    If exceptions occur, Application Verifier sends diagnostic messages to the debugger and breaks in.

-   If you are using a kernel-mode debugging session, set **HostFailKdDebugBreak** so that the reflector breaks into the kernel-mode debugger before terminating the driver host process. This setting is enabled by default starting in Windows 8.

-   Disable pooling by setting **UmdfHostProcessSharing** to **ProcessSharingDisabled**. For info, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).
-   By default, when a UMDF device fails, the framework attempts to restart it up to five times. You can turn off automatic restart by setting **DebugModeFlags** to 0x01. For more info, see [Registry Values for Debugging WDF Drivers](registry-values-for-debugging-kmdf-drivers.md).
-   Reboot your computer.

-   For debugging UMDF driver problems review [Determining Why the Reflector Terminated the Host Process](determining-why-the-reflector-terminated-the-host-process.md) and [Debugging UMDF driver crashes](debugging-umdf-2-0-drivers.md) 

## Using WinDbg to attach manually (user-mode debugging)


On the target machine, you can manually attach WinDbg to the instance of WUDFHost that hosts the driver. When you attach, you break into the debugger and you can set breakpoints in your driver.

Because driver initialization occurs shortly after WUDFHost loads, it is not feasible to attach manually in time to debug initialization code. Instead, you can set a registry value to cause the host process to wait some number of seconds at host initialization or driver load time. This delay gives you time to attach WinDbg to the correct instance of the WUDFHost process.

Follow these steps:

1.  In the registry on the target computer, set **HostProcessDbgBreakOnStart** or **HostProcessDbgBreakOnDriverLoad** to some number of seconds and reboot.
2.  On the target computer, open WinDbg as Administrator.
3.  On the **File** menu, choose **Attach to Process**. Select **By Executable**, and locate all processes that are named WUDFHost.exe (there might not be any). If there are any processes named WUDFHost.exe, write down their process identifiers for future reference.
4.  In Device Manager, enable the driver.
5.  Repeat step 2 and locate a new instance of WUDFHost.exe. If you don't see a new instance of WUDFHost.exe, click **Cancel**, and choose **Attach to Process** again. When you find the new instance of WUDFHost.exe, select it, and click **OK**.

If [device pooling](using-device-pooling-in-umdf-drivers.md) is in use and you set the **HostProcessDbgBreakOnDriverLoad** registry value, you may see debugger breaks due to other drivers loading. You can turn off device pooling by using UMDF debug mode.

To use debug mode, either use the F5 option in Visual Studio, or set the **DebugModeFlags** and **DebugModeBinaries** values in the registry.

For detailed information about UMDF registry values, see [Registry Values for Debugging WDF Drivers (KMDF and UMDF)](registry-values-for-debugging-kmdf-drivers.md).

## <a href="" id="kd"></a>Using WinDbg to remotely debug from a host machine (kernel-mode debugging)


From a remote host, establish a kernel-mode debugging session and then set current process to the instance of Wudfhost that is hosting your driver. If you are debugging from a remote kernel debugger, you can set **HostProcessDbgBreakOnDriverStart** or **HostProcessDbgBreakOnDriverLoad** to 0x80000000 to specify no timeout, but break into the kernel debugger.

Use these steps:

1. Disable pooling. turn on **DebugModeFlags** and list your driver in **DebugModeBinaries**
2. If your driver uses UMDF 1.11 or later, **HostFailKdDebugBreak** is enabled by default. Skip this step.

   If your driver uses UMDF 1.9 or earlier, set **HostFailKdDebugBreak** to 1.

3. If you are debugging problems related to timeouts, turn off **HostProcessDbgBreakOnDriverStart** and **HostProcessDbgBreakOnDriverLoad**. (When **HostProcessDbgBreakOnDriverStart** or **HostProcessDbgBreakOnDriverLoad** is non-zero, the framework disables timeouts so that the reflector does not terminate the host while a user-mode debugger is attached to the host process.) If you need to debug driver initialization code, instead of using these two values, try issuing the following command in WinDbg before your driver loads: **sxe ld:**<em>MyDriver.dll</em> (break on module load)
4. Reboot if you made any registry changes.
5. Depending on the selections you made above, your remote kernel debugger should break in when the driver loads or unloads on the target.

 

