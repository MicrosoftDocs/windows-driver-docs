---
title: "!wdfkd.wdflogdump"
description: "The !wdfkd.wdflogdump extension displays the WDF In-flight Recorder log records, if available, for a KMDF driver or a UMDF 2 driver. "
keywords: ["!wdfkd.wdflogdump Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdflogdump
api_type:
- NA
---

# !wdfkd.wdflogdump

The **!wdfkd.wdflogdump** extension displays the WDF In-flight Recorder log records, if available, for a KMDF driver or a UMDF 2 driver. You can use this command with a [complete memory dump](../debugger/complete-memory-dump.md), a [kernel memory dump](../debugger/kernel-memory-dump.md), or a [live kernel-mode target](../debugger/live-kernel-mode-targets.md).

KMDF

```dbgcmd
!wdfkd.wdflogdump [DriverName][WdfDriverGlobals][-d | -f | -a LogAddress]
```

UMDF

```dbgcmd
!wdfkd.wdflogdump  [DriverName.dll][HostProcessId][-d | -f | -m]
```

## Parameters


<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
-   KMDF: The name of a KMDF driver. The name must not include the .sys filename extension.
-   UMDF: The name of a UMDF 2 driver. The name must include the .dll filename extension.

<span id="_______Parameter2______"></span><span id="_______parameter2______"></span><span id="_______PARAMETER2______"></span> *Parameter2*   
-   KMDF: *WdfDriverGlobals* - The address of the *WdfDriverGlobals* structure. You can determine this address by running [**!wdfkd.wdfldr**](-wdfkd-wdfldr.md) and looking for the field labeled "WdfGlobals". Or, you can supply @@(Driver!WdfDriverGlobals) as the address value, where *Driver* is the name of the driver. If any *WdfDriverGlobals* address is supplied, *DriverName* is ignored (although it must nevertheless be supplied).
-   UMDF: *HostProcessId* - The process ID of an instance of wudfhost.exe. If you supply the process ID, this command displays the log records for that process. If you do not supply the process ID, this command displays a list of commands in this form:

    **!wdflogdump** *DriverName* **** *ProcessID*

    If a single process can be determined it will automatically be chosen.

*Options*
KMDF:

**-d** Displays only the driver logs.

**-f** Displays only the framework logs.

**-a** *LogAddress*Displays a specific driver log. If this option is used, the LogAddress must be provided.

UMDF:

**-d** Displays only the driver logs.

**-f** Displays only the framework logs.

**-m** Merges framework and driver logs in their recorded order.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1, UMDF 2

## Remarks

If you omit the *DriverName* parameter, the default driver name is used. Use the [**!wdfkd.wdfgetdriver**](-wdfkd-wdfgetdriver.md) extension to display the default driver name, and use the [**!wdfkd.wdfsetdriver**](-wdfkd-wdfsetdriver.md) extension to set the default driver name.

To display the framework's error log records from a [small memory dump](../debugger/small-memory-dump.md), use the [**!wdfkd.wdfcrashdump**](-wdfkd-wdfcrashdump.md) extension.

For information about setting information that the debugger needs to format WPP tracing messages, see [**!wdfkd.wdftmffile**](-wdfkd-wdftmffile.md) and [**!wdfkd.wdfsettraceprefix**](-wdfkd-wdfsettraceprefix.md).

**Additional Information**

For information about enabling the inflight trace recorder for your driver, see [Using Inflight Trace Recorder (IFR) in KMDF and UMDF 2 Drivers](../wdf/using-wpp-software-tracing-in-kmdf-and-umdf-2-drivers.md). For more information about debugging WDF drivers, see [Debugging WDF Drivers](../debugger/debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md). For information about KMDF debugging, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## See also

[**!wdfkd.wdfcrashdump**](-wdfkd-wdfcrashdump.md)

[**!wdfkd.wdfsettraceprefix**](-wdfkd-wdfsettraceprefix.md)
