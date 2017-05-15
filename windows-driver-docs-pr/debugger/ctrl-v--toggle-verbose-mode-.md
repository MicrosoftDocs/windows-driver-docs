---
title: CTRL+V (Toggle Verbose Mode)
description: The CTRL+V key toggles verbose mode on and off.
ms.assetid: 1aca1452-86dd-4573-8ad0-e46aa474a324
keywords: ["CTRL+V (Toggle Verbose Mode) Windows Debugging"]
topic_type:
- apiref
api_name:
- CTRL+V (Toggle Verbose Mode)
api_type:
- NA
---

# CTRL+V (Toggle Verbose Mode)


The CTRL+V key toggles verbose mode on and off.

CDB / KD Syntax

``` syntax
CTRL+V  ENTER 
```

WinDbg Syntax

``` syntax
CTRL+ALT+V 
```

## <span id="ddk_meta_ctrl_v_dbg"></span><span id="DDK_META_CTRL_V_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Debuggers</strong></p></td>
<td align="left"><p>CDB, KD, WinDbg</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When verbose mode is turned on, some display commands (such as register dumping) produce more detailed output. Every MODULE LOAD operation that is sent to the debugger will be displayed. And every time a driver or DLL is loaded by the operating system, the debugger will be notified.

In WinDbg, this can also be accomplished by selecting [View | Verbose Output](view---verbose-output.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20CTRL+V%20%28Toggle%20Verbose%20Mode%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




