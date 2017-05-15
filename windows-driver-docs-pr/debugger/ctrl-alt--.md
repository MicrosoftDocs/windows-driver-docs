---
title: CTRL+ALT+\\ (Debug Current Debugger)
description: The CTRL+ALT+\\ key launches a new instance of CDB; this new debugger takes the current debugger as its target.
ms.assetid: 0a36baa4-fe40-4498-9cf8-ae81497f1dda
keywords: ["CTRL+ALT+\ (Debug Current Debugger) Windows Debugging"]
topic_type:
- apiref
api_name:
- CTRL+ALT+\ (Debug Current Debugger)
api_type:
- NA
---

# CTRL+ALT+\\ (Debug Current Debugger)


The **CTRL+ALT+\\** key launches a new instance of CDB; this new debugger takes the current debugger as its target.

``` syntax
CTRL+ALT+\ 
```

## <span id="ddk_meta_ctrl_p_dbg"></span><span id="DDK_META_CTRL_P_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><strong>Debuggers</strong></td>
<td align="left"><p>WinDbg</p></td>
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

This is equivalent to launching a new CDB through the [**remote.exe**](the-remote-exe-utility.md) utility, and using it to debug the debugger that you are already running.

**CTRL+ALT+\\** is similar to the [**.dbgdbg (Debug Current Debugger)**](-dbgdbg--debug-current-debugger-.md) command, however **CTRL+ALT+\\** has the advantage that it can be used when no debugger command line is available.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20CTRL+ALT+\%20%28Debug%20Current%20Debugger%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




