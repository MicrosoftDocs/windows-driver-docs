---
title: devhandles
description: The devhandles extension displays the open handles for the specified device.
ms.assetid: a473dd58-1571-4969-b8b7-f7a71128d824
keywords: ["devhandles Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- devhandles
api_type:
- NA
ms.localizationpriority: medium
---

# !devhandles


The **!devhandles** extension displays the open handles for the specified device.

```dbgcmd
!devhandles Address 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the device for which to display the open handles.

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
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

To display complete handle information, this extension requires private symbols.

The address of a device object can be obtained using the [**!drvobj**](-drvobj.md) or [**!devnode**](-devnode.md) extensions.

Here is a truncated example:

```dbgcmd
lkd> !devhandles 0x841153d8

Checking handle table for process 0x840d3940
Handle table at 95fea000 with 578 Entries in use

Checking handle table for process 0x86951d90
Handle table at 8a8ef000 with 28 Entries in use

...

Checking handle table for process 0x87e63650
Handle table at 947bc000 with 308 Entries in use

Checking handle table for process 0x87e6f4f0
00000000: Unable to read handle table
```

 

 





