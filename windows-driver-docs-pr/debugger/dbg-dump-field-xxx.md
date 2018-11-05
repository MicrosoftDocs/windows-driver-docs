---
title: DBG\_DUMP\_FIELD\_XXX
description: DBG\_DUMP\_FIELD\_XXX
ms.assetid: c168c1b7-c4ef-4a70-9060-611b86120635
ms.author: domars
ms.date: 12/07/2017
keywords: ["DBG_DUMP_FIELD_XXX Windows Debugging"]
topic_type:
- apiref
api_name:
- DBG_DUMP_FIELD_XXX
api_location:
- wdbgexts.h
api_type:
- HeaderDef
ms.localizationpriority: medium
---

# DBG\_DUMP\_FIELD\_XXX


## <span id="ddk_dbg_dump_xxx_dbx"></span><span id="DDK_DBG_DUMP_XXX_DBX"></span>


The DBG\_DUMP\_FIELD\_*XXX* bit flags are used by the **fOptions** member of the [**FIELD\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff545316) structure to control the behavior of the [**IG\_DUMP\_SYMBOL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff550906)[**Ioctl**](https://msdn.microsoft.com/library/windows/hardware/ff551084) operation.

The following flags can be present.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DBG_DUMP_FIELD_CALL_BEFORE_PRINT</p></td>
<td align="left"><p>The callback function is called before printing the member.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_DUMP_FIELD_NO_CALLBACK_REQ</p></td>
<td align="left"><p>No callback function is called.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_DUMP_FIELD_RECUR_ON_THIS</p></td>
<td align="left"><p>Submembers of the member are processed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_DUMP_FIELD_FULL_NAME</p></td>
<td align="left"><p><strong>fName</strong> must match completely, as opposed to just having a matching prefix, for the member to be processed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_DUMP_FIELD_ARRAY</p></td>
<td align="left"><p>Print array elements of an array member.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_DUMP_FIELD_COPY_FIELD_DATA</p></td>
<td align="left"><p>The value of the member is copied into <strong>pBuffer</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_DUMP_FIELD_RETURN_ADDRESS</p></td>
<td align="left"><p>During a callback or when <strong>Ioctl</strong> returns, the FIELD_INFO.<strong>address</strong> member contains the address of the symbol&#39;s member.</p>
<p>If no address is supplied for the type, FIELD_INFO.<strong>address</strong> contains total offset of the member from the beginning of the type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_DUMP_FIELD_SIZE_IN_BITS</p></td>
<td align="left"><p>For a bit field, return the offset and size in bits instead of bytes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_DUMP_FIELD_NO_PRINT</p></td>
<td align="left"><p>Do not print this member (only callback function are called and data copies are performed).</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_DUMP_FIELD_DEFAULT_STRING DBG_DUMP_FIELD_WCHAR_STRING DBG_DUMP_FIELD_MULTI_STRING DBG_DUMP_FIELD_GUID_STRING</p></td>
<td align="left"><p>If the member is a pointer, it is printed as a string, ANSI string , WCHAR string, MULTI string, or GUID.</p></td>
</tr>
</tbody>
</table>

 

In addition, the result of the macro DBG\_DUMP\_RECUR\_LEVEL(*Level*) can be added to the bit-set to specify how deep into structures to recurse. *Level* can be a number between 0 and 15.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Wdbgexts.h (include Wdbgexts.h, Wdbgexts.h, or Dbgeng.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**IG\_DUMP\_SYMBOL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff550906)

[**Ioctl**](https://msdn.microsoft.com/library/windows/hardware/ff551084)

[**FIELD\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff545316)

 

 






