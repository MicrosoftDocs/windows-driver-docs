---
title: apicerr
description: The apicerr extension displays the local Advanced Programmable Interrupt Controller (APIC) error log.
ms.assetid: b058412b-a4df-42cc-8550-b5db4e0bbccc
keywords: ["APIC (Advanced Programmable Interrupt Controller)", "apicerr Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- apicerr
api_type:
- NA
ms.localizationpriority: medium
---

# !apicerr


The **!apicerr** extension displays the local Advanced Programmable Interrupt Controller (APIC) error log.

```dbgcmd
     !apicerr [Format] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Format______"></span><span id="_______format______"></span><span id="_______FORMAT______"></span> *Format*   
Specifies the order in which to display the error log contents. This can be any one of the following values:

<span id="0x0"></span><span id="0X0"></span>0x0  
Displays the error log according to order of occurrence.

<span id="0x1"></span><span id="0X1"></span>0x1  
Displays the error log according to processor.

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

 

This extension command can only be used with an x86-based or an x64-based target computer.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about APICs, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

 

 





