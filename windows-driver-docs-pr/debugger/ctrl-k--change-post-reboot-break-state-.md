---
title: CTRL+K (Change Post-Reboot Break State)
description: The CTRL+K key changes the conditions on which the debugger will automatically break into the target computer.
ms.assetid: 74f57775-63ad-4a96-9ba5-bfedd4c8c826
keywords: ["CTRL+K (Change Post-Reboot Break State) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- CTRL+K (Change Post-Reboot Break State)
api_type:
- NA
---

# CTRL+K (Change Post-Reboot Break State)


The CTRL+K key changes the conditions on which the debugger will automatically break into the target computer.

KD Syntax

``` syntax
CTRL+K  ENTER 
```

WinDbg Syntax

``` syntax
CTRL+ALT+K 
```

## <span id="ddk_meta_ctrl_k_dbg"></span><span id="DDK_META_CTRL_K_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Debuggers</strong></p></td>
<td align="left"><p>KD and WinDbg only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an overview of related commands and an explanation of how the reboot process affects the debugger, see [Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md).

Remarks
-------

This control key causes the kernel debugger to cycle through the following three states:

<span id="No_break"></span><span id="no_break"></span><span id="NO_BREAK"></span>**No break**  
In this state, the debugger will not break into the target computer unless you press [**CTRL+C**](ctrl-c--break-.md).

<span id="Break_on_reboot"></span><span id="break_on_reboot"></span><span id="BREAK_ON_REBOOT"></span>**Break on reboot**  
In this state, the debugger will break into a rebooted target computer after the kernel initializes. This is equivalent to starting KD or WinDbg with the **-b**[command-line option](command-line-options.md).

<span id="Break_on_first_module_load"></span><span id="break_on_first_module_load"></span><span id="BREAK_ON_FIRST_MODULE_LOAD"></span>**Break on first module load**  
In this state, the debugger will break into a rebooted target computer after the first kernel module is loaded. (This will cause the break to occur earlier than in the **Break on reboot** option.) This is equivalent to starting KD or WinDbg with the **-d**[command-line option](command-line-options.md).

When CTRL+K is used, the new break state is displayed.

In WinDbg, this can also be accomplished by selecting [Debug | Kernel Connection | Cycle Initial Break](debug---kernel-connection---cycle-initial-break.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20CTRL+K%20%28Change%20Post-Reboot%20Break%20State%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




