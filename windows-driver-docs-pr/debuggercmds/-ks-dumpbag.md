---
title: ks.dumpbag
description: The ks.dumpbag extension displays the contents of the object bag for the specified object.
keywords: ["ks.dumpbag Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ks.dumpbag
api_type:
- NA
---

# !ks.dumpbag


The **!ks.dumpbag** extension displays the contents of the object bag for the specified object.

```dbgcmd
!ks.dumpbag Object [Level]  
```

## Parameters


<span id="_______Object______"></span><span id="_______object______"></span><span id="_______OBJECT______"></span> *Object*   
Specifies a pointer to a valid client viewable object structure, or to the private class object.

<span id="_______Level______"></span><span id="_______level______"></span><span id="_______LEVEL______"></span> *Level*   
Optional. Specifies the level of detail to display on a 0-7 scale with progressively more information displayed for higher values. To display all available details, supply a value of 7.

## DLL

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

 

### Additional Information

For more information, see [Kernel Streaming Debugging](../debugger/kernel-streaming-debugging.md).

## Remarks

Here is an example of the **!ks.dumpbag** display for a filter:

```dbgcmd
kd> !dumpbag 829493c4
Filter 829493c4 [CKsFilter = 82949350]:
    Object Bag 829493d0:
        Object Bag Item 829dce28:
            Reference Count        : 1
            Item Cleanup Handler   : f7a21730
```

 

 





