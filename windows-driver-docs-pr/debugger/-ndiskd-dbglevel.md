---
title: ndiskd.dbglevel
description: The ndiskd.dbglevel extension displays and optionally changes the current NDIS debug level. Warning ndiskd.dbglevel has been superceded by WPP and Driver Verifier.
ms.assetid: D134FD03-DABA-4558-A5C3-C365F77BD69A
keywords: ["ndiskd.dbglevel Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.dbglevel
api_type:
- NA
---

# !ndiskd.dbglevel


The **!ndiskd.dbglevel** extension displays and optionally changes the current NDIS debug level.

**Warning**  
**!ndiskd.dbglevel** has been superceded by WPP (Windows software trace preprocessor) and Driver Verifier. !ndiskd will give you the following warning if your target system does not support **!ndiskd.dbglevel**.

```
0: kd> !ndiskd.dbglevel
    This target does not support tracing through !ndiskd.dbglevel or
    !ndiskd.dbgsystems.
    Learn how to collect traces with WPP
```

If you click on the link at the bottom of the warning, !ndiskd will give you more information.

```
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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.dbglevel%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





