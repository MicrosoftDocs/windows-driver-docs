---
title: Determining Why the Reflector Terminated the Host Process
description: This topic describes how you can analyze why the reflector terminated the driver host process (WUDFHost.exe).
keywords:
- debugging scenarios WDK UMDF , reflector terminates the host process
- UMDF WDK , debugging scenarios, reflector terminates the host process
- UMDF WDK , reflector terminates the host process
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining Why the Reflector Terminated the Host Process


This topic describes how you can analyze why the reflector terminated the driver host process (WUDFHost.exe) or why the driver host process crashed.

The most common reason for the reflector to terminate the host process is the expiration of UMDF [host process timeouts](how-umdf-enforces-time-outs.md).

We strongly recommend doing all development and testing of your UMDF driver with a kernel debugger attached to the test system and enabling [Application Verifier (AppVerif.exe)](../debugger/debugger-download-tools.md) on WUDFHost.exe. Use the following command, attach a kernel debugger and then reboot.

```cpp
AppVerif –enable Heaps Exceptions Handles Locks Memory TLS Leak –for WudfHost.exe
```

## Using Dump Files


When your UMDF driver crashes or encounters a problem, a break will be reported in the kernel debugger. These problems should be debugged when user-mode exceptions are reported in the kernel debugger. Kernel debugger breaks are also reported by WudfRd.sys before it terminates a driver host process because of a problematic (non-responsive) UMDF driver. You will also find logs and heap dumps reported at the following location. To review dump files captured by UMDF, follow these steps:

1.  Locate the latest .dmp file in the *%ProgramData%*\\Microsoft\\WDF directory.
    Before UMDF 2.15 that shipped with Windows 10 1507, the log directory is under %windir%\\system32\\LogFiles\\WUDF.

2.  Load the latest .dmp file into the debugger by using the following command:
    ```cpp
    WinDbg -z <path to the .dmp file>
    ```

3.  Look at the state of the threads at the time of termination.

If you need heap dumps captured, at the time of testing set the following registry values and re-boot your test system before running tests. You can also examine Windows Error Reporting history from the system's application event log at %SystemRoot%\System32\Winevt\Logs\Application.evtx 

```cpp
reg add "HKLM\Software\Microsoft\windows NT\CurrentVersion\Wudf" /v LogMinidumpType /t REG_DWORD /d 0x1122
reg add "HKLM\Software\Microsoft\windows NT\CurrentVersion\Wudf" /v LogEnable /t REG_DWORD /d 1 
```

## Using the Debugger

In other cases, you might need to attach to a live kernel-mode target to determine why the reflector terminated the host process. To set up your debugging session, follow the steps described in [How to Enable Debugging of a UMDF Driver](enabling-a-debugger.md#kd).

Once you have established a connection, use !wdfkd.wdfumtriage to examine the UMDF drivers, display the outstanding IRPs by using the [**!wdfkd.wdfumirps**](../debugger/-wdfkd-wdfumirps.md) UMDF debugger extension ([**!wudfext.umirps**](../debugger/-wudfext-umirps.md) for UMDF version 1).

-   If a PnP IRP or a power IRP is pending, determine why the driver causes the IRP to hang by examining threads in the host process.

    You can use the [**!process**](../debugger/-process.md) extension to examine the threads running in the host process. The **0x1f** flags value shows you the stack trace for each thread.

    **!process** *&lt;process addr&gt;* **0x1f**

-   If your driver has not completed a canceled IRP quickly, determine which IRP was canceled and why it has not completed.
-   If a cleanup or close IRP is pending, determine why the IRP is taking a long time to process.

 

