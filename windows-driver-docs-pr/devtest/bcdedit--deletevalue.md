---
title: BCDEdit /deletevalue
description: The BCDEdit /deletevalue command deletes or removes a boot entry option (and its value) from the Windows boot configuration data store (BCD).
ms.assetid: 70833A12-B1F7-4AF6-952F-02A70718E870
ms.date: 05/21/2018
keywords: ["BCDEdit /deletevalue Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /deletevalue
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /deletevalue


The **BCDEdit /deletevalue** command deletes or removes a boot entry option (and its value) from the Windows boot configuration data store (BCD). Use the **BCDEdit /deletevalue** command to remove options that were added using the [**BCDEdit /set**](bcdedit--set.md) command. 
``` syntax
     bcdedit  /deletevalue [{ID}] datatype  

   
```

To delete a boot option value that you have set, use the **BCDEdit /deletevalue** command. A common scenario for using the **BCDEdit /deletevalue** command is to remove boot entry options when you are testing and debugging a driver. 

For example, if you use [**BCDEdit /set**](bcdedit--set.md) to change the **groupsize** processor group option to a new value for testing purposes, you can use **BCDEdit /deletevalue** to delete the new value and revert to the default value by typing the following command. Note that you must then restart the computer for the change to take effect.

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
 

 





