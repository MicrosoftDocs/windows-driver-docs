---
title: minipkd.help
description: The minipkd.help extension displays help text for the Minipkd.dll extension commands.
ms.assetid: 5629aec8-8c9d-4ed0-91fb-c8d020f78405
keywords: ["minipkd.help Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- minipkd.help
api_type:
- NA
ms.localizationpriority: medium
---

# !minipkd.help


The **!minipkd.help** extension displays help text for the Minipkd.dll extension commands.

```dbgcmd
!minipkd.help 
```

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Minipkd.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [SCSI Miniport Debugging](scsi-miniport-debugging.md).

Remarks
-------

If an error message similar to the following appears, it indicates that the symbol path is incorrect and does not point to the correct version of the Scsiport.sys symbols.

```dbgcmd
minipkd error (0) <path> ... \minipkd\minipkd.c @ line 435
```

Use the [**.sympath (Set Symbol Path)**](-sympath--set-symbol-path-.md) command to display the current path and change the path. Use the [**.reload (Reload Module)**](-reload--reload-module-.md) command to reload symbols from the current path.

 

 





