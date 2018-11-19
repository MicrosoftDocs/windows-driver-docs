---
title: Diagnosing problems running WDTF-based tests
description: To help you troubleshoot problems running WDTF-based test, you can use a debugger.
ms.assetid: 24257B50-ED9C-4D45-A245-1EC855463D33
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Diagnosing problems running WDTF-based tests


To help you troubleshoot problems running WDTF-based test, you can use a debugger.

## Diagnose problems with unresponsive WDTF-based tests (run from Visual Studio)


1.  Configure and connect a kernel debugger to the computer that is running the WDTF-based test. See [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909) or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/dn745909).
2.  Search for Te.exe process and switch context to that process. For information about Te.exe, see [Test Authoring and Execution Framework (TAEF)](https://msdn.microsoft.com/library/windows/hardware/hh439725).

    ``` syntax
    !process 0 0 Te.exe 

    PROCESS fffffa80093c6340

    SessionId: 1 Cid: 1320 Peb: 7f6595b3000 ParentCid: 12a0

    DirBase: 21eee000 ObjectTable: fffff8a0035b0a00 HandleCount: 327.

    Image: TE.exe

    ·         .process /p /r fffffa80093c6340

    ·         
    ```

3.  Run the [**!process**](https://msdn.microsoft.com/library/windows/hardware/ff564717) command to identify the threads running under Te.exe.

    ``` syntax
    !process fffffa80093c6340
    ```

    Look for threads with **WDTF**\* on the stack.

4.  Repeat step 3 for Te.ProcessHost.exe (if it exists).

## Diagnose problems with PnP and power management tests


You can diagnose problems with these commands.

[**!powertriage**](https://msdn.microsoft.com/library/windows/hardware/mt431710) (provides information about system and device power related components)
[**!devnode**](https://msdn.microsoft.com/library/windows/hardware/ff562345) (to display information about the PnP tree)
[**!process**](https://msdn.microsoft.com/library/windows/hardware/ff564717) (to examine processes to locate associated threads)
[**!thread**](https://msdn.microsoft.com/library/windows/hardware/ff565440) (to view information about threads)
[**!wdfkd.wdfdevice**](https://msdn.microsoft.com/library/windows/hardware/ff565703) (for WDF driver information)
After confirming that there are active PnP or power management threads that are stuck (examine TickCount for this), follow up with the right component owners. (You can locate the component owners from looking at the stacks of the stuck threads).

 

 




