---
title: poolval
description: The poolval extension analyzes the headers for a pool page and diagnoses any possible corruption. This extension is only available in Windows XP and later versions.
ms.assetid: b67ab2d4-c765-4721-81ed-c6b7c9a0ba6d
keywords: ["poolval Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- poolval
api_type:
- NA
ms.localizationpriority: medium
---

# !poolval


The **!poolval** extension analyzes the headers for a pool page and diagnoses any possible corruption. This extension is only available in Windows XP and later versions.

```dbgcmd
!poolval Address [DisplayLevel]
```

## <span id="ddk__poolval_dbg"></span><span id="DDK__POOLVAL_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the pool whose header is to be analyzed.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Specifies the information to include in the display. This can be any of the following values (the default is zero):

<span id="0"></span>0  
Causes basic information to be displayed.

<span id="1"></span>1  
Causes basic information and linked header lists to be displayed.

<span id="2"></span>2  
Causes basic information, linked header lists, and basic header information to be displayed.

<span id="3"></span>3  
Causes basic information, linked header lists, and full header information to be displayed.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about memory pools, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

 

 





