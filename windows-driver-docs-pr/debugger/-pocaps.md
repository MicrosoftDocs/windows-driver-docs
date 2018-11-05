---
title: pocaps
description: The pocaps extension displays the power capabilities of the target computer.
ms.assetid: 011d923a-a5c4-4d3b-ba06-fe5dc884adaa
keywords: ["pocaps Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pocaps
api_type:
- NA
ms.localizationpriority: medium
---

# !pocaps


The **!pocaps** extension displays the power capabilities of the target computer.

```dbgcmd
!pocaps
```

## <span id="ddk__pocaps_dbg"></span><span id="DDK__POCAPS_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

To view the system's power policy, use the [**!popolicy**](-popolicy.md) extension command. For information about power capabilities and power policy, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

Here is an example of this command's output:

```dbgcmd
kd> !pocaps
PopCapabilities @ 0x8016b100
  Misc Supported Features:  S4 FullWake
  Processor Features:      
  Disk Features:            SpinDown
  Battery Features:        
  Wake Caps
    Ac OnLine Wake:         Sx
    Soft Lid Wake:          Sx
    RTC Wake:               Sx
    Min Device Wake:        Sx
    Default Wake:           Sx
```

 

 





