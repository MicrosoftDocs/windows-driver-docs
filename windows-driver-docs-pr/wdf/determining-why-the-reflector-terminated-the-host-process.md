---
title: Determining Why the Reflector Terminated the Host Process
description: This topic describes how you can analyze why the reflector terminated the driver host process (WUDFHost.exe).
ms.assetid: c80b117b-597a-494a-bc28-5a918d2a9279
keywords:
- debugging scenarios WDK UMDF , reflector terminates the host process
- UMDF WDK , debugging scenarios, reflector terminates the host process
- UMDF WDK , reflector terminates the host process
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining Why the Reflector Terminated the Host Process


This topic describes how you can analyze why the reflector terminated the driver host process (WUDFHost.exe).

The most common reason for the reflector to terminate the host process is the expiration of UMDF [host process timeouts](how-umdf-enforces-time-outs.md).

## Using Dump Files


For many crashes, dump file details are sufficient to determine why the termination occurred. To review dump file information, follow these steps:

1.  Locate the latest .dmp file in the %windir%\\system32\\LogFiles\\WUDF directory.

    **Note**  Starting in UMDF 2.15, the log directory is *%ProgramData%*\\Microsoft\\WDF.

     

2.  Load the latest .dmp file into the debugger by using the following command:
    ```cpp
    WinDbg -z <path to the .dmp file>
    ```

3.  Look at the state of the threads at the time of termination.

## Using the Debugger


In other cases, you might need to attach to a live kernel-mode target to determine why the reflector terminated the host process. To set up your debugging session, follow the steps described in [How to Enable Debugging of a UMDF Driver](enabling-a-debugger.md#kd).

Once you have established a connection, display the outstanding IRPs by using the [**!wdfkd.wdfumirps**](https://msdn.microsoft.com/library/windows/hardware/dn265384) UMDF debugger extension ([**!wudfext.umirps**](https://msdn.microsoft.com/library/windows/hardware/ff566197) for UMDF version 1).

-   If a PnP IRP or a power IRP is pending, determine why the driver causes the IRP to hang by examining threads in the host process.

    You can use the [**!process**](https://msdn.microsoft.com/library/windows/hardware/ff564717) extension to examine the threads running in the host process. The **0x1f** flags value shows you the stack trace for each thread.

    **!process** *&lt;process addr&gt;* **0x1f**

-   If your driver has not completed a canceled IRP quickly, determine which IRP was canceled and why it has not completed.
-   If a cleanup or close IRP is pending, determine why the IRP is taking a long time to process.

 

 





