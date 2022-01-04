---
title: ndiskd.dbgsystems
description: The ndiskd.dbgsystems extension displays and optionally changes the NDIS subsystems that have debug traces enabled.  ndiskd.dbgsystems has been superceded by WPP and Driver Verifier.
keywords: ["ndiskd.dbgsystems Windows Debugging"]
ms.date: 06/15/2020
topic_type:
- apiref
api_name:
- ndiskd.dbgsystems
api_type:
- NA
---

# !ndiskd.dbgsystems

The **!ndiskd.dbgsystems** extension displays and optionally changes the NDIS subsystems that have debug traces enabled.

**Warning**  
**!ndiskd.dbgsystems** has been superceded by WPP (Windows software trace preprocessor) and Driver Verifier. !ndiskd will give you the following warning if your target system does not support **!ndiskd.dbgsystems**.

```console
0: kd> !ndiskd.dbgsystems
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
!ndiskd.dbgsystems [-subsystem <any>]
```

## Parameters

<span id="_______-subsystem______"></span><span id="_______-SUBSYSTEM______"></span> *-subsystem*   
The subsystem to toggle.

If multiple components are selected, separate them with spaces. If a previously-selected component is repeated, its debug monitoring will be toggled off. The following values are possible:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Value</strong></p></td>
<td align="left"><p><strong>Meaning</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>INIT</p></td>
<td align="left"><p>Traces adapter initialization.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CONFIG</p></td>
<td align="left"><p>Traces adapter configuration.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SEND</p></td>
<td align="left"><p>Traces sending data over the network.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RECV</p></td>
<td align="left"><p>Traces receiving data from the network.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PROTOCOL</p></td>
<td align="left"><p>Traces protocol operations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>BIND</p></td>
<td align="left"><p>Traces binding operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>BUS_QUERY</p></td>
<td align="left"><p>Traces bus queries.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>REGISTRY</p></td>
<td align="left"><p>Traces registry operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MEMORY</p></td>
<td align="left"><p>Traces memory management.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILTER</p></td>
<td align="left"><p>Traces filter operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>REQUEST</p></td>
<td align="left"><p>Traces requests.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WORK_ITEM</p></td>
<td align="left"><p>Traces work-item operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PNP</p></td>
<td align="left"><p>Traces Plug and Play operations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PM</p></td>
<td align="left"><p>Traces Power Management operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>OPEN</p></td>
<td align="left"><p>Traces operations that open reference objects.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>LOCKS</p></td>
<td align="left"><p>Traces locking operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>RESET</p></td>
<td align="left"><p>Traces resetting operations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WMI</p></td>
<td align="left"><p>Traces Windows Management Instrumentation operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>NDIS_CO</p></td>
<td align="left"><p>Traces Connection-Oriented NDIS.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>REFERENCE</p></td>
<td align="left"><p>Traces reference operations.</p></td>
</tr>
</tbody>
</table>

### DLL

Ndiskd.dll

### Remarks

This extension applies to checked NDIS.sys only. To check the build info of NDIS.sys, run the [**!ndiskd.ndis**](-ndiskd-ndis.md) extension.

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-175-Debugging-the-Network-Stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**!ndiskd.ndis**](-ndiskd-ndis.md)

[WPP Software Tracing](../devtest/wpp-software-tracing.md)

[Driver Verifier](../devtest/driver-verifier.md)

[WMI Tracing Extensions (Wmitrace.dll)](wmi-tracing-extensions--wmitrace-dll-.md)
