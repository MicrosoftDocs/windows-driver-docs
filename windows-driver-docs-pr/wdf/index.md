---
title: What's New for WDF Drivers
description: Summarizes new features and improvements for WDF drivers.
keywords:
- kernel-mode drivers WDK KMDF , about KMDF
- KMDF WDK , about KMDF
- Kernel-Mode Driver Framework WDK , about KMDF
- framework-based drivers WDK KMDF
- framework-based drivers WDK KMDF , about framework-based drivers
- objects WDK KMDF
- framework objects WDK KMDF
ms.date: 02/03/2023
ms.topic: article
---

# What's New for WDF Drivers

Windows Driver Frameworks (WDF) drivers include both Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF).

This topic summarizes new features and improvements that affect drivers using either framework.

To learn about changes that are specific to only one framework, see [KMDF Version History](kmdf-version-history.md) and [UMDF Version History](umdf-version-history.md). 

Windows 11 and Windows Server 2022 include KMDF version 1.33 and UMDF version 2.33.

You can use these framework versions to build drivers for:

- Windows 10 and 11 (all SKUs)
- Windows Server 2022



## Windows 10, version 1703 (KMDF 1.21, UMDF 2.21)

- New WDF Verifier settings to detect excessive object creation
 
    In some cases, framework objects are incorrectly parented and not deleted after use.  With this feature, you can specify a maximum number of objects and what should happen when this threshold is exceeded.
    
    To start monitoring, add the following registry values under:
    `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\<driver service>\Parameters\wdf`
    
  1. Add a DWORD value named **ObjectLeakDetectionLimit** with the threshold value. This is the maximum number of objects of the types described in the **ObjectsForLeakDetection** key.
    
  2. Add a new REG_MULTI_SZ value named **ObjectsForLeakDetection** that lists each type name to verify. For example, you could specify `WDFDMATRANSACTION WDFDEVICE`. To specify all handle types, use `*` as the string.

  3. To control whether exceeding this threshold should cause a debug break or a bugcheck, set the [DbgBreakOnError](using-kmdf-verifier.md) key.

     By default, if the ObjectsForLeakDetection key is not specified, the framework monitors WDFREQUEST, WDFWORKITEM, WDFKEY, WDFSTRING, WDFOBJECT, and WDFDEVICE.
    
     The limit scales with the number of devices installed, so if the driver creates three WDFDEVICE objects, the WDF Verifier limit is three times the value specified in **ObjectLeakDetectionLimit**.
    
     If you specify WDFREQUEST, the verifier only counts WDFREQUEST objects that the driver creates.
    
     This feature does not currently support tracking the WDFMEMORY object type. 



## Windows 10, version 1507 (KMDF 1.15, UMDF 2.15)

### WDF source code is publicly available


-   The WDF source code is now available as open source on GitHub. This is the same source code from which the WDF runtime library that ships in Windows 10 is built. You can debug your driver more effectively when you can follow the interactions between the driver and WDF. Download it from <https://github.com/Microsoft/Windows-Driver-Frameworks>.

-   The private symbol files for WDF on Windows 10 are now available through the Microsoft Symbol Server.

-   The Windows Driver Kit (WDK) 10 samples are also now published to GitHub. Download them from <https://github.com/Microsoft/Windows-Driver-Samples>.

### Automatic Source Level Debugging of Framework Code


When you use WinDbg to debug a WDF driver on Windows 10, WinDbg automatically retrieves the framework source code from Microsoft's public GitHub repository. You can use this feature to step through the WDF source code while debugging, and to learn about framework internals without downloading the source code to a local machine. For more information, see [Debugging with WDF Source](https://go.microsoft.com/fwlink/p/?LinkId=618535) and [Video: Debugging your driver with WDF source code](video--debugging-your-driver-with-wdf-source-code.md).

### Universal Driver Compliance


All WDF driver samples and Visual Studio driver templates are [Universal Windows driver](/windows-hardware/drivers) compliant.

All KMDF and UMDF 2 functionality is Universal Windows driver compliant.

Note that UMDF 1 drivers run only on Windows 10 for desktop editions and earlier versions of desktop Windows. Want to benefit from the universal capabilities of UMDF 2? To learn how to port your old UMDF 1 driver, see [Porting a Driver from UMDF 1 to UMDF 2](porting-a-driver-from-umdf-1-to-umdf-2.md).

### Debugging and Diagnosability


-   All KMDF and UMDF 2 drivers can use an always on, always available Inflight Trace Recorder (IFR). When a driver provides a custom trace, the driver IFR log contains the trace messages. Note that the new driver IFR log is separate from the framework IFR log that WDF creates for each driver.

    It's easy to turn on the IFR. See [Inflight Trace Recorder (IFR) for logging traces](../devtest/using-wpp-recorder.md) and [Using Inflight Trace Recorder in KMDF and UMDF Drivers](using-wpp-software-tracing-in-kmdf-and-umdf-2-drivers.md).

-   The IFR maintains a circular buffer of WPP traces in non-pageable memory. If a driver crashes, the logs are frequently included in the crash dump file.

-   If you turn on the IFR in your driver binary, the IFR is present and running during the lifetime of your driver. You don't need to start an explicit trace collection session.

    -   IFR logs are included in minidump files except when the responsible driver is undetermined or if the crash was a host timeout.

    -   If you have a debugger connected, you can access both the driver and framework IFR logs by issuing [**!wdfkd.wdflogdump**](../debugger/-wdfkd-wdflogdump.md).

    -   If you do not have a debugger connected, you can still access both logs.  To learn how, see [Video: Accessing driver IFR logs without a debugger](video--accessing-driver-ifr-logs-without-a-debugger.md).

    -   When debugging a UMDF driver, you can merge framework logs with driver logs by issuing: **!wdfkd.wdflogdump** *&lt;drivername.dll&gt;* **-m**

-   UMDF logs (WudfTrace.etl) and dumps are now located in %ProgramData%\\Microsoft\\WDF instead of %systemDrive%\\LogFiles\\Wudf.

-   New debugger command: [**!wdfkd.wdfumtriage**](../debugger/-wdfkd-wdfumtriage.md) provides a kernel-centric view of all UMDF devices on the system.

-   You can run [**!analyze**](../debugger/-analyze.md) to investigate UMDF verifier failures or UMDF unhandled exceptions. This works for live kernel debugging as well as debugging user crash dump files from *%ProgramData%*\\Microsoft\\WDF.

-   In KMDF and UMDF 2, you can monitor power reference usage in the debugger. For info, see [Debugging Power Reference Leaks in WDF](debugging-power-reference-leaks-in-wdf.md).

-   You can use [**!wdfkd.wdfcrashdump**](../debugger/-wdfkd-wdfcrashdump.md) to display error information about UMDF 2 drivers. For more information, see **!wdfkd.wdfcrashdump**.

### Performance Tracing tool for WDF drivers


You can use the Windows Performance Toolkit (WPT) to view performance data for a given KMDF or UMDF 2 driver. When tracing is enabled, the framework generates ETW events for I/O, PnP, and Power callback paths. You can then view graphs in the Windows Performance Analyzer (WPA) that show I/O throughput rates, CPU utilization, and callback performance. The WPT is included in the Windows Assessment and Deployment Kit (ADK).

For more information, see [Using the Windows Performance Toolkit (WPT) with WDF](using-the-windows-performance-toolkit--wpt--with-wdf.md).

### Additional support for HID drivers in UMDF


-   UMDF now fully supports HID filters (enumerated by HIDClass) and minidrivers. Simply port your existing KMDF driver or write a new UMDF 2 filter; the functionality is automatically enabled.

-   UMDF HID minidrivers that are enumerated by ACPI can perform selective suspend. For more information, see [Creating WDF HID Minidrivers](creating-umdf-hid-minidrivers.md).

-   UMDF drivers can now be installed in the HID stack for low latency input devices such as touch and mouse. A driver for an input device should specify the **UmdfHostPriority** INF directive. For information, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

### Support for interrupts for GPIO-backed devices


-   UMDF 2 supports interrupts for GPIO-backed devices like hardware push-buttons. KMDF supports these devices natively, without the workaround described in [Handling Active-Both Interrupts](handling-active-both-interrupts.md). For more information, see [Creating an Interrupt Object](creating-an-interrupt-object.md).

### UMDF no longer requires WinUSB


New support has been added for USB drivers in UMDF. A UMDF 2 USB driver no longer uses WinUSB. To use the new functionality, the driver sets the **UmdfDispatcher** directive to **NativeUSB**, instead of **WinUSB**. See [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).


### Improved Performance


-   UMDF system components consume less disk space.

-   KMDF and UMDF drivers use less non-paged memory.

-   Improved framework version checking reduces header/library mismatches.

-   UMDF provides improved buffer mapping for HID transfers.

 

