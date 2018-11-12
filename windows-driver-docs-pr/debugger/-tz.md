---
title: tz
description: The tz extension displays the specified power thermal zone structure.
ms.assetid: f3cc9e54-a0db-4095-b707-380ec1dacf59
keywords: ["thermal zone", "tz Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- tz
api_type:
- NA
ms.localizationpriority: medium
---

# !tz


The **!tz** extension displays the specified power thermal zone structure.

```dbgcmd
!tz [Address]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
The address of a power thermal zone that you want to display. If this parameter is omitted, the display includes all thermal zones on the target computer.

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

To view the system's power capabilities, use the [**!pocaps**](-pocaps.md) extension command. To view the system's power policy, use the [**!popolicy**](-popolicy.md) extension command. For information about power capabilities and power policy, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

To stop execution at any time, press CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 





