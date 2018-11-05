---
title: dpa
description: The dpa extension displays pool allocation information.
ms.assetid: 1eb31741-bc50-4188-823d-b6324d2dfdf1
keywords: ["pool allocation", "dpa Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dpa
api_type:
- NA
ms.localizationpriority: medium
---

# !dpa


The **!dpa** extension displays pool allocation information.

```dbgcmd
!dpa Options 
!dpa -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Must be exactly one of the following options:

<span id="-c"></span><span id="-C"></span>**-c**  
Displays current pool allocation statistics.

<span id="-v"></span><span id="-V"></span>**-v**  
Displays all current pool allocations.

<span id="-vs"></span><span id="-VS"></span>**-vs**  
Causes the display to include stack traces.

<span id="-f"></span><span id="-F"></span>**-f**  
Displays failed pool allocations.

<span id="-r"></span><span id="-R"></span>**-r**  
Displays free pool allocations.

<span id="-p_Ptr"></span><span id="-p_ptr"></span><span id="-P_PTR"></span>**-p** **** *Ptr*  
Displays all pool allocations that contain the pointer *Ptr*.

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
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Pool instrumentation must be enabled in Win32k.sys in order for this extension to work.

 

 





