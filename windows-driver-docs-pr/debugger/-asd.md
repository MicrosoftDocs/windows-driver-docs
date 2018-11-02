---
title: asd
description: The asd extension displays a specified number of failure analysis entries from the data cache, starting at the specified address.
ms.assetid: fb0eeedd-d50b-4385-b35f-4ac46fb97ce0
keywords: ["failure analysis entries, display from data cache", "asd Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- asd
api_type:
- NA
ms.localizationpriority: medium
---

# !asd


The **!asd** extension displays a specified number of failure analysis entries from the data cache, starting at the specified address.

```dbgcmd
    !asd Address DataUsed
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the first failure analysis entry to display.

<span id="_______DataUsed______"></span><span id="_______dataused______"></span><span id="_______DATAUSED______"></span> *DataUsed*   
Determines the number of tokens to display.

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

You can use the [**!dumpfa**](-dumpfa.md) extension to debug the [**!analyze**](-analyze.md) extension.

Remarks
-------

The **!asd** extension is useful only when you are debugging the [**!analyze**](-analyze.md) extension.

 

 





