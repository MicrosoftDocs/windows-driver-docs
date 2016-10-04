---
title: Diagnosing problems running WDTF-based tests
author: windows-driver-content
description: To help you troubleshoot problems running WDTF-based test, you can use a debugger.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 24257B50-ED9C-4D45-A245-1EC855463D33
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
After confirming that there are active PnP or power management threads that are stuck (examine TickCount for this), follow up with the right component owners. (You can locate the the component owners from looking at the stacks of the stuck threads).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdtf\dtf%5D:%20Diagnosing%20problems%20running%20WDTF-based%20tests%20%20RELEASE:%20%289/13/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


