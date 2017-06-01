---
title: CTRL+A (Toggle Baud Rate)
description: The CTRL+A key toggles the baud rate used in the kernel debugging connection.
ms.assetid: 77a95ca1-073c-480a-abda-f484adbc1d23
keywords: ["CTRL+A (Toggle Baud Rate) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- CTRL+A (Toggle Baud Rate)
api_type:
- NA
---

# CTRL+A (Toggle Baud Rate)


The CTRL+A key toggles the baud rate used in the kernel debugging connection.

KD Syntax

```
CTRL+A  ENTER 
```

WinDbg Syntax

```
CTRL+ALT+A 
```

## <span id="ddk_meta_ctrl_a_dbg"></span><span id="DDK_META_CTRL_A_DBG"></span>


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

 

Remarks
-------

This will cycle through all available baud rates for the kernel debugging connection.

Supported baud rates are 19200, 38400, 57600, and 115200. Each time this control key is used, the next baud rate will be selected. If the baud rate is already at 115200, it will be reduced to 19200.

In WinDbg, this can also be accomplished by selecting [Debug | Kernel Connection | Cycle Baud Rate](debug---kernel-connection---cycle-baud-rate.md).

You cannot actually use this control key to change the baud rate at which you are debugging. The baud rate of the host computer and the target computer must match, and the baud rate of the target computer cannot be changed without rebooting. Therefore, you only need to toggle through the baud rates if the two computers are attempting to communicate at different rates. In this case, you must change the host computer's baud rate to match that of the target computer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20CTRL+A%20%28Toggle%20Baud%20Rate%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




