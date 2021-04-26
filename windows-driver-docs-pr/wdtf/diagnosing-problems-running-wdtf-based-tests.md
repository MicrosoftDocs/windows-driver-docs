---
title: Diagnosing problems running WDTF-based tests
description: To help you troubleshoot problems running WDTF-based test, you can use a debugger.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Diagnosing problems running WDTF-based tests


To help you troubleshoot problems running WDTF-based test, you can use a debugger.

## Diagnose problems with unresponsive WDTF-based tests (run from Visual Studio)


1.  Configure and connect a kernel debugger to the computer that is running the WDTF-based test. See [Provision a computer for driver deployment and testing (WDK 8.1)](../gettingstarted/provision-a-target-computer-wdk-8-1.md) or [Provision a computer for driver deployment and testing (WDK 8)](../gettingstarted/provision-a-target-computer-wdk-8-1.md).
2.  Search for Te.exe process and switch context to that process. For information about Te.exe, see [Test Authoring and Execution Framework (TAEF)](../taef/index.md).

    ``` syntax
    !process 0 0 Te.exe 

    PROCESS fffffa80093c6340

    SessionId: 1 Cid: 1320 Peb: 7f6595b3000 ParentCid: 12a0

    DirBase: 21eee000 ObjectTable: fffff8a0035b0a00 HandleCount: 327.

    Image: TE.exe

    ·         .process /p /r fffffa80093c6340

    ·         
    ```

3.  Run the [**!process**](../debugger/-process.md) command to identify the threads running under Te.exe.

    ``` syntax
    !process fffffa80093c6340
    ```

    Look for threads with **WDTF**\* on the stack.

4.  Repeat step 3 for Te.ProcessHost.exe (if it exists).

## Diagnose problems with PnP and power management tests


You can diagnose problems with these commands.

[**!powertriage**](../debugger/-powertriage.md) (provides information about system and device power related components)
[**!devnode**](../debugger/-devnode.md) (to display information about the PnP tree)
[**!process**](../debugger/-process.md) (to examine processes to locate associated threads)
[**!thread**](../debugger/-thread.md) (to view information about threads)
[**!wdfkd.wdfdevice**](../debugger/-wdfkd-wdfdevice.md) (for WDF driver information)
After confirming that there are active PnP or power management threads that are stuck (examine TickCount for this), follow up with the right component owners. (You can locate the component owners from looking at the stacks of the stuck threads).

 

