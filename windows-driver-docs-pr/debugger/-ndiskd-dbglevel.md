---
title: ndiskd.dbglevel
description: The ndiskd.dbglevel extension displays and optionally changes the current NDIS debug level. Warning ndiskd.dbglevel has been superceded by WPP and Driver Verifier.
ms.assetid: D134FD03-DABA-4558-A5C3-C365F77BD69A
keywords: ["ndiskd.dbglevel Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.dbglevel
api_type:
- NA
ms.localizationpriority: medium
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

 

For more information about WPP, see [WPP Software Tracing](https://msdn.microsoft.com/windows/hardware/drivers/devtest/wpp-software-tracing).

For more information about Driver Verifier, see [Driver Verifier](https://msdn.microsoft.com/windows/hardware/drivers/devtest/driver-verifier).

For more information about WMI tracing, see [WMI Tracing Extensions (Wmitrace.dll)](https://msdn.microsoft.com/library/windows/hardware/ff561362).

```console
!ndiskd.dbglevel [-level <str>] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-level______"></span><span id="_______-LEVEL______"></span> *-level*   
The level of debugging verbosity. Possible values are:

-   NONE - disables debug tracing
-   FATAL - enables fatal errors to be printed
-   ERROR - enables errors to be printed
-   WARN - enables warnings to be printed
-   INFO - enables informational messages to be printed
-   VERBOSE - enables all debug traces to be printed

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Remarks
-------

This extension applies to checked NDIS.sys only. To check the build info of NDIS.sys, run the [**!ndiskd.ndis**](-ndiskd-ndis.md) extension.

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**!ndiskd.ndis**](-ndiskd-ndis.md)

[WPP Software Tracing](https://msdn.microsoft.com/windows/hardware/drivers/devtest/wpp-software-tracing)

[Driver Verifier](https://msdn.microsoft.com/windows/hardware/drivers/devtest/driver-verifier)

[WMI Tracing Extensions (Wmitrace.dll)](https://msdn.microsoft.com/library/windows/hardware/ff561362)

 

 






