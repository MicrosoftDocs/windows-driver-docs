---
title: What's New for WDF Drivers in Windows 10
description: This topic summarizes the new features and improvements for Windows Driver Frameworks (WDF) drivers in Windows 10.Windows 10 includes Kernel Mode Driver Framework (KMDF) version 1.15 and User Mode Driver Framework (UMDF) version 2.15.
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 61fd9916-38e7-47d0-aec7-d5a489eb21eb
keywords: ["kernel mode drivers WDK KMDF about KMDF", "KMDF WDK about KMDF", "Kernel Mode Driver Framework WDK about KMDF", "framework based drivers WDK KMDF", "framework based drivers WDK KMDF about framework based drivers", "objects WDK KMDF", "framework objects WDK KMDF"]
---

# What's New for WDF Drivers in Windows 10


**In this article**

-   [WDF source code is now publicly available](#wdf-source-code-is-now-publicly-available)
-   [Automatic Source Level Debugging of Framework Code](#automatic-source-level-debugging-of-framework-code)
-   [Universal Driver Compliance](#universal-driver-compliance)
-   [Debugging and Diagnosability](#debugging-and-diagnosability)
-   [New Performance Tracing tool for WDF drivers](#new-performance-tracing-tool-for-wdf-drivers)
-   [Additional support for HID drivers in UMDF](#additional-support-for-hid-drivers-in-umdf)
-   [Support for interrupts for GPIO-backed devices](#support-for-interrupts-for-gpio-backed-devices)
-   [UMDF no longer requires WinUSB](#umdf-no-longer-requires-winusb)
-   [DDI Updates](#ddi-updates)
-   [Improved Performance](#improved-performance)

This topic summarizes the new features and improvements for Windows Driver Frameworks (WDF) drivers in Windows 10.

Windows 10 includes Kernel-Mode Driver Framework (KMDF) version 1.15 and User-Mode Driver Framework (UMDF) version 2.15.

You can use these framework versions to build drivers for:

-   Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)
-   Windows 10 Mobile
-   Windows 10 IoT Core (IoT Core)
-   Windows Server 2016 Technical Preview

For version history, see [KMDF Version History](kmdf-version-history.md) and [UMDF Version History](umdf-version-history.md). Except where noted, UMDF references on this page describe version 2 functionality that is not available in UMDF version 1.

## WDF source code is now publicly available


-   The WDF source code is now available as open source on GitHub. This is the same source code from which the WDF runtime library that ships in Windows 10 is built. You can debug your driver more effectively when you can follow the interactions between the driver and WDF. Download it from <http://github.com/Microsoft/Windows-Driver-Frameworks>.

-   The private symbol files for WDF on Windows 10 are now available through the Microsoft Symbol Server.

-   The Windows Driver Kit (WDK) 10 samples are also now published to GitHub. Download them from <http://github.com/Microsoft/Windows-Driver-Samples>.

## Automatic Source Level Debugging of Framework Code


When you use WinDbg to debug a WDF driver on Windows 10, WinDbg automatically retrieves the framework source code from Microsoft's public GitHub repository. You can use this feature to step through the WDF source code while debugging, and to learn about framework internals without downloading the source code to a local machine. For more information, see [New support for source-level debugging of WDF code in Windows 10](http://go.microsoft.com/fwlink/?LinkId=618534), [Debugging with WDF Source](http://go.microsoft.com/fwlink/?LinkId=618535), and [Video: Debugging your driver with WDF source code](video--debugging-your-driver-with-wdf-source-code.md).

## Universal Driver Compliance


All WDF driver samples and Visual Studio driver templates are [Universal Windows driver](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers) compliant.

All KMDF and UMDF 2 functionality is Universal Windows driver compliant.

Note that UMDF 1 drivers run only on Windows 10 for desktop editions and earlier versions of desktop Windows. Want to benefit from the universal capabilities of UMDF 2? To learn how to port your old UMDF 1 driver, see [Porting a Driver from UMDF 1 to UMDF 2](porting-a-driver-from-umdf-1-to-umdf-2.md).

## Debugging and Diagnosability


-   All KMDF and UMDF 2 drivers can use the new always on, always available Inflight Trace Recorder (IFR). When a driver provides a custom trace, the driver IFR log contains the trace messages. Note that the new driver IFR log is separate from the framework IFR log that WDF creates for each driver.

    It's easy to turn on the IFR. See [Inflight Trace Recorder (IFR) for logging traces](https://msdn.microsoft.com/library/windows/hardware/dn914610) and [Using Inflight Trace Recorder in KMDF and UMDF Drivers](using-wpp-software-tracing-in-kmdf-and-umdf-2-drivers.md).

-   The IFR maintains a circular buffer of WPP traces in non-pageable memory. If a driver crashes, the logs are frequently included in the crash dump file.

-   If you turn on the IFR in your driver binary, the IFR is present and running during the lifetime of your driver. You don't need to start an explicit trace collection session.

    -   IFR logs are included in minidump files except when the responsible driver is undetermined or if the crash was a host timeout.

    -   You can access both the driver and framework IFR logs by issuing [**!wdfkd.wdflogdump**](https://msdn.microsoft.com/library/windows/hardware/ff565805). (Note that [**!rcdrkd.rcdrlogdump**](https://msdn.microsoft.com/library/windows/hardware/hh920382) is no longer needed for this.)

    -   When debugging a UMDF driver, you can merge framework logs with driver logs by issuing: **!wdfkd.wdflogdump** *&lt;drivername.dll&gt;* **-m**

-   UMDF logs (WudfTrace.etl) and dumps are now located in %ProgramData%\\Microsoft\\WDF instead of %systemDrive%\\LogFiles\\Wudf.

-   New debugger command: [**!wdfkd.wdfumtriage**](https://msdn.microsoft.com/library/windows/hardware/dn961126) provides a kernel-centric view of all UMDF devices on the system.

-   You can run [**!analyze**](https://msdn.microsoft.com/library/windows/hardware/ff562112) to investigate UMDF verifier failures or UMDF unhandled exceptions. This works for live kernel debugging as well as debugging user crash dump files from *%ProgramData%*\\Microsoft\\WDF.

-   In KMDF and UMDF 2, you can monitor power reference usage in the debugger. For info, see [Debugging Power Reference Leaks in WDF](debugging-power-reference-leaks-in-wdf.md).

-   You can use [**!wdfkd.wdfcrashdump**](https://msdn.microsoft.com/library/windows/hardware/ff565682) to display error information about UMDF 2 drivers. For more information, see **!wdfkd.wdfcrashdump**.

## New Performance Tracing tool for WDF drivers


You can use the Windows Performance Toolkit (WPT) to view performance data for a given KMDF or UMDF 2 driver. When tracing is enabled, the framework generates ETW events for I/O, PnP, and Power callback paths. You can then view graphs in the Windows Performance Analyzer (WPA) that show I/O throughput rates, CPU utilization, and callback performance. The WPT is included in the Windows Assessment and Deployment Kit (ADK).

For more information, see [New Performance Tools for WDF Drivers in Windows 10]( http://go.microsoft.com/fwlink/?LinkId=618537) and [Using the Windows Performance Toolkit (WPT) with WDF](using-the-windows-performance-toolkit--wpt--with-wdf.md).

## Additional support for HID drivers in UMDF


-   UMDF now fully supports HID filters (enumerated by HIDClass) and minidrivers. Simply port your existing KMDF driver or write a new UMDF 2 filter; the functionality is automatically enabled.

-   UMDF HID minidrivers that are enumerated by ACPI can perform selective suspend. For more information, see [Creating WDF HID Minidrivers](creating-umdf-hid-minidrivers.md).

-   UMDF drivers can now be installed in the HID stack for low latency input devices such as touch and mouse. A driver for an input device should specify the **UmdfHostPriority** INF directive. For information, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

## Support for interrupts for GPIO-backed devices


-   UMDF 2 supports interrupts for GPIO-backed devices like hardware push-buttons. KMDF supports these devices natively, without the workaround described in [Handling Active-Both Interrupts](handling-active-both-interrupts.md). For more information, see [Creating an Interrupt Object](creating-an-interrupt-object.md).

## UMDF no longer requires WinUSB


New support has been added for USB drivers in UMDF. A UMDF 2 USB driver no longer uses WinUSB. To use the new functionality, the driver sets the **UmdfDispatcher** directive to **NativeUSB**, instead of **WinUSB**. See [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

## DDI Updates


For information about new and updated DDIs, please see [UMDF Version History](umdf-version-history.md) and [KMDF Version History](kmdf-version-history.md).

## Improved Performance


-   UMDF system components consume less disk space.

-   KMDF and UMDF drivers use less non-paged memory.

-   Improved framework version checking reduces header/library mismatches.

-   UMDF provides improved buffer mapping for HID transfers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20What's%20New%20for%20%20WDF%20Drivers%20in%20Windows%C2%A010%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




