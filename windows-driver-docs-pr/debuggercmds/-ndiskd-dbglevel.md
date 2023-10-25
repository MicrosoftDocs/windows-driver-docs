---
title: ndiskd.dbglevel
description: The ndiskd.dbglevel extension displays and optionally changes the current NDIS debug level. Warning ndiskd.dbglevel has been superceded by WPP and Driver Verifier.
keywords: ["ndiskd.dbglevel Windows Debugging"]
ms.date: 06/15/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.dbglevel
api_type:
- NA
---

# !ndiskd.dbglevel

The **!ndiskd.dbglevel** extension displays and optionally changes the current NDIS debug level.

**Warning**  
**!ndiskd.dbglevel** has been superceded by WPP (Windows software trace preprocessor) and Driver Verifier. !ndiskd will give you the following warning if your target system does not support **!ndiskd.dbglevel**.

```console
0: kd> !ndiskd.dbglevel
    This target does not support tracing through !ndiskd.dbglevel or
    !ndiskd.dbgsystems.
    Learn how to collect traces with WPP
```

If you click on the link at the bottom of the warning, !ndiskd will give you more information.

```console
0: kd> !ndiskd.help wpptracing
    WPP traces are fast, flexible, and detailed.  Plus, starting with Windows 8
    and Windows Server 2012, you can automatically decode NDIS traces using the
    symbol file.  Just point TraceView (or tracepdb.exe) at NDIS.PDB, and it
    will be able to get all the TMFs it needs to trace NDIS activity.
    
    If you would like traces to be printed in the debugger window, you use the
    !wmitrace extension.  For example, you might enable traces with this:

    !wmitrace.searchpath c:\path\to\TMF\files
    !wmitrace.start ndis -kd
    !wmitrace.enable ndis {DD7A21E6-A651-46D4-B7C2-66543067B869} -level 4 -flag 0x31f3
```

For more information about WPP, see [WPP Software Tracing](../devtest/wpp-software-tracing.md).

For more information about Driver Verifier, see [Driver Verifier](../devtest/driver-verifier.md).

For more information about WMI tracing, see [WMI Tracing Extensions (Wmitrace.dll)](wmi-tracing-extensions--wmitrace-dll-.md).

```console
!ndiskd.dbglevel [-level <str>]
```

## Parameters

<span id="_______-level______"></span><span id="_______-LEVEL______"></span> *-level*   
The level of debugging verbosity. Possible values are:

- NONE - disables debug tracing
- FATAL - enables fatal errors to be printed
- ERROR - enables errors to be printed
- WARN - enables warnings to be printed
- INFO - enables informational messages to be printed
- VERBOSE - enables all debug traces to be printed

### DLL

Ndiskd.dll

### Remarks

This extension applies to checked NDIS.sys only. To check the build info of NDIS.sys, run the [**!ndiskd.ndis**](-ndiskd-ndis.md) extension.

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**!ndiskd.ndis**](-ndiskd-ndis.md)

[WPP Software Tracing](../devtest/wpp-software-tracing.md)

[Driver Verifier](../devtest/driver-verifier.md)

[WMI Tracing Extensions (Wmitrace.dll)](wmi-tracing-extensions--wmitrace-dll-.md)
