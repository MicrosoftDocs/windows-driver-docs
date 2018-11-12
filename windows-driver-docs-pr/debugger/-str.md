---
title: str
description: The str extension displays an ANSI_STRING or OEM_STRING structure.
ms.assetid: 5ebb29d4-5d77-475b-ace5-8bc8a4299320
keywords: ["strings", "ANSI_STRING structure", "str Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- str
api_type:
- NA
ms.localizationpriority: medium
---

# !str


The **!str** extension displays an ANSI\_STRING or OEM\_STRING structure.

```dbgcmd
!str Address
```

## <span id="ddk__str_dbg"></span><span id="DDK__STR_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the ANSI\_STRING or OEM\_STRING structure.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about ANSI\_STRING structures, see the Microsoft Windows SDK documentation.

Remarks
-------

ANSI strings are counted 8-bit character strings, as defined in the following structure:

```cpp
typedef struct _STRING {
    USHORT Length;
    USHORT MaximumLength;
    PCHAR Buffer;
} STRING;
typedef STRING ANSI_STRING;
typedef STRING OEM_STRING;
```

If the string is null-terminated, **Length** does not include the trailing null.

 

 





