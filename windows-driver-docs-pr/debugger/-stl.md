---
title: stl
description: The stl extension displays some of the known Standard Template Library (STL) templates.
ms.assetid: a1f1f923-64bd-44c9-941f-9a648888c7e0
keywords: ["stl Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- stl
api_type:
- NA
ms.localizationpriority: medium
---

# !stl


The **!stl** extension displays some of the known Standard Template Library (STL) templates.

```dbgcmd
!stl [Options] Template 
!stl -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
May include any of the following possibilities:

<span id="-v"></span><span id="-V"></span>**-v**  
Causes detailed output to be displayed.

<span id="-V"></span><span id="-v"></span>**-V**  
Causes more detailed output to be displayed, such as information on the progress of the extension, including when certain functions are called and returned.

<span id="_______Template______"></span><span id="_______template______"></span><span id="_______TEMPLATE______"></span> *Template*   
Specifies the name of the template to be displayed.

<span id="_______-_______"></span> **-?**   
Displays some brief Help text for this extension in the Debugger Command window.

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
<td align="left"><p>Exts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The verbose options will only take effect if the debugger's verbose mode is enabled.

This extension currently supports STL templates of the following types: string, wstring, vector&lt;*string*&gt;, vector&lt;*wstring*&gt;, list&lt;*string*&gt;, list&lt;*wstring*&gt;, and pointers to any of the preceding types.

 

 





