---
title: gdikdx.verifier
description: The gdikdx.verifier extension displays the status of Driver Verifier during the verification of a graphics driver.
ms.assetid: a7e189bb-ed63-4da3-ab7a-bf502ec131ed
keywords: ["gdikdx.verifier Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- gdikdx.verifier
api_type:
- NA
ms.localizationpriority: medium
---

# !gdikdx.verifier


The **!gdikdx.verifier** extension displays the status of Driver Verifier during the verification of a graphics driver.

```dbgcmd
!gdikdx.verifier [-Flags] 
```

## <span id="ddk__gdikdx_verifier_dbg"></span><span id="DDK__GDIKDX_VERIFIER_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies what information will be displayed in the output from this command. Any combination of the following (preceded by a hyphen) is allowed:

<span id="d"></span><span id="D"></span>**d**  
Causes the display to include statistics on **Memory Pool Tracking**. This includes the address, size, and tag of each pool.

<span id="h__or___"></span><span id="H__OR___"></span>**h** (or **?**)  
Displays some brief Help text for this command in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Gdikdx.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about Driver Verifier, see the Windows Driver Kit (WDK) documentation.

Remarks
-------

When verifying drivers that are not graphics drivers, the standard kernel-mode extension [**!verifier**](-verifier.md) should be used instead of **!gdikdx.verifier**.

Regardless of which flags are selected, this extension will display the Driver Verifier options that are active. It will also display statistics on the frequency of random failure.

 

 





