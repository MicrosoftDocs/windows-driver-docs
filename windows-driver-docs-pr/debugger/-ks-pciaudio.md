---
title: ks.pciaudio
description: The ks.pciaudio extension displays a list of FDOs currently attached to PortCls.
ms.assetid: 30d74f14-1cff-4b18-996a-8c91c20edebe
keywords: ["ks.pciaudio Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ks.pciaudio
api_type:
- NA
ms.localizationpriority: medium
---

# !ks.pciaudio


The **!ks.pciaudio** extension displays a list of FDOs currently attached to PortCls.

```dbgcmd
!ks.pciaudio [Options] [Level]  
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Optional. Specifies the kind of information to be displayed. *Options* can be any combination of the following bits.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Display a list of running streams.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Display a list all streams.

<span id="Bit_3__0x4_"></span><span id="bit_3__0x4_"></span><span id="BIT_3__0X4_"></span>Bit 3 (0x4)  
Output displayed streams. *Level* has meaning only when this bit is set.

<span id="_______Level______"></span><span id="_______level______"></span><span id="_______LEVEL______"></span> *Level*   
Optional, and applicable only if Bit 3 is set in *Options*. Levels are the same as those for [**!ks.dump**](-ks-dump.md).

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel Streaming Debugging](kernel-streaming-debugging.md).

Remarks
-------

Here is an example of the output from **!ks.pciaudio**:

```dbgcmd
kd> !ks.pciaudio
1 Audio FDOs found:
 Functional Device 8299be18 [\Driver\smwdm]
```

 

 





