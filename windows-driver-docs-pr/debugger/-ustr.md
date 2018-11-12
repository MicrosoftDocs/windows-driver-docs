---
title: ustr
description: The ustr extension displays a UNICODE_STRING structure.
ms.assetid: 17b84bf0-5a5b-47a5-893b-fdc58ca2afc3
keywords: ["strings", "UNICODE_STRING structure", "ustr Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ustr
api_type:
- NA
ms.localizationpriority: medium
---

# !ustr


The **!ustr** extension displays a UNICODE\_STRING structure.

```dbgcmd
!ustr Address
```

## <span id="ddk__ustr_dbg"></span><span id="DDK__USTR_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the UNICODE\_STRING structure.

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

For more information about UNICODE\_STRING structures, see the Microsoft Windows SDK documentation.

Remarks
-------

Unicode strings are counted 16-bit character strings, as defined in the following structure:

```cpp
typedef struct _UNICODE_STRING {
    USHORT Length;
    USHORT MaximumLength;
    PWSTR  Buffer;
} UNICODE_STRING;
```

If the string is null-terminated, **Length** does not include the trailing null.

Most Win32 character string arguments are converted to Unicode strings before any real work is done.

 

 





