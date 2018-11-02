---
title: .imgscan (Find Image Headers)
description: The .imgscan command scans virtual memory for image headers.
ms.assetid: 8b524665-0471-4634-aa31-1c82d6cc8569
keywords: ["Find Image Headers (.imgscan) command", ".imgscan (Find Image Headers) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .imgscan (Find Image Headers)
api_type:
- NA
ms.localizationpriority: medium
---

# .imgscan (Find Image Headers)


The **.imgscan** command scans virtual memory for image headers.

```dbgcmd
.imgscan [Options] 
```

## <span id="ddk_meta_find_image_headers_dbg"></span><span id="DDK_META_FIND_IMAGE_HEADERS_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Any of the following options:

<span id="_r_Range"></span><span id="_r_range"></span><span id="_R_RANGE"></span>**/r** **** *Range*  
Specifies the range to search. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md). If you specify only one address, the debugger searches a range that begins at that address and extends 0x10000 bytes.

<span id="_l"></span><span id="_L"></span>**/l**  
Loads module information for any image header that is found.

<span id="_v"></span><span id="_V"></span>**/v**  
Displays verbose information.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If you do not use the **/r** parameter, the debugger searches all virtual memory regions.

The **.imgscan** command displays any image headers that it finds and the header type. Header types include Portable Executable (PE) headers and Microsoft MS-DOS MZ headers.

The following example shows the **.imgscan** command.

```dbgcmd
0:000> .imgscan
MZ at 00400000, prot 00000002, type 01000000 - size 2d000
MZ at 77f80000, prot 00000002, type 01000000 - size 7d000
  Name: ntdll.dll
MZ at 7c570000, prot 00000002, type 01000000 - size b8000
  Name: KERNEL32.dll
```

 

 





