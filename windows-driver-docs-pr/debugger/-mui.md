---
title: mui
description: The mui extension displays the Multilingual User Interface (MUI) cache information. The implementation of MUI was improved in Windows Vista. 
ms.assetid: f485450f-0dd2-4f1c-85fe-dbf272c2dbae
keywords: ["multi-language user interface", "mui Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- mui
api_type:
- NA
ms.localizationpriority: medium
---

# !mui


The **!mui** extension displays the Multilingual User Interface (MUI) cache information. 

```dbgcmd
!mui -c
!mui -s
!mui -r ModuleAddress
!mui -i
!mui -f
!mui -t
!mui -u
!mui -d ModuleAddress
!mui -e ModuleAddress
!mui -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-c______"></span><span id="_______-C______"></span> **-c**   
Causes the output to include the language identifier (ID), a pointer to the module, a pointer to the resource configuration data, and a pointer to the associated MUI DLL for each module.

<span id="_______-s______"></span><span id="_______-S______"></span> **-s**   
(Kernel Mode Only) Causes the display to include the full file paths for the module and associated MUI DLL for each module.

<span id="_______-r________ModuleAddress______"></span><span id="_______-r________moduleaddress______"></span><span id="_______-R________MODULEADDRESS______"></span> **-r** **** *ModuleAddress*   
Causes the resource configuration data for the module at *ModuleAddress* to be displayed. This includes the file type, the checksum value, and the resource types.

<span id="_______-i______"></span><span id="_______-I______"></span> **-i**   
Causes the output to include the installed and licensed MUI languages and their associated information.

<span id="_______-f______"></span><span id="_______-F______"></span> **-f**   
Causes the output to include the loader merged language fallback list.

<span id="_______-t______"></span><span id="_______-T______"></span> **-t**   
Causes the output to include the thread preference language.

<span id="_______-u______"></span><span id="_______-U______"></span> **-u**   
Causes the output to include the current thread user UI language setting.

<span id="_______-d_ModuleAddress______"></span><span id="_______-d_moduleaddress______"></span><span id="_______-D_MODULEADDRESS______"></span> **-d** **** *ModuleAddress*   
Causes the output to include contained resources for the module at *ModuleAddress*.

<span id="_______-e_ModuleAddress______"></span><span id="_______-e_moduleaddress______"></span><span id="_______-E_MODULEADDRESS______"></span> **-e** **** *ModuleAddress*   
Causes the output to include contained resource types for the module at *ModuleAddress*.

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
<td align="left"><p><strong>Windows XP</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows Vista and later</strong></p></td>
<td align="left"><p>Exts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about MUI and resource configuration data format, see the Microsoft Windows SDK documentation.

 

 





