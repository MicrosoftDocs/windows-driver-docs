---
title: BCDEdit /deletevalue
description: The BCDEdit /deletevalue command deletes or removes a boot entry option (and its value) from the Windows boot configuration data store (BCD).
ms.assetid: 70833A12-B1F7-4AF6-952F-02A70718E870
keywords: ["BCDEdit /deletevalue Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /deletevalue
api_type:
- NA
---

# BCDEdit /deletevalue


The **BCDEdit /deletevalue** command deletes or removes a boot entry option (and its value) from the Windows boot configuration data store (BCD). Use the **BCDEdit /deletevalue** command to remove options that were added using [**BCDEdit /set**](bcdedit--set.md) command. You might need to remove boot entry options when you are testing and debugging your driver for Windows 7, Windows 8, Windows 8.1, Windows 10 and later versions of Windows.

``` syntax
     bcdedit  /deletevalue [{ID}] datatype  

   
```

To delete a boot option value that you have set, use the **BCDEdit /deletevalue** command.

For example, if you change the processor group option, **groupsize**, to a new value for testing purposes, you can revert to the default value of 64 by typing the following command and then restarting the computer.

``` syntax
bcdedit /deletevalue groupsize
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows Vista</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2008</p></td>
</tr>
</tbody>
</table>

See also
--------

[**BCDEdit /set**](bcdedit--set.md)
 

 





