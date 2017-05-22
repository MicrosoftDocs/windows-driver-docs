---
title: mui
description: The mui extension displays the Multilingual User Interface (MUI) cache information. The implementation of MUI was improved in Windows Vista. 
ms.assetid: f485450f-0dd2-4f1c-85fe-dbf272c2dbae
keywords: ["multi-language user interface", "mui Windows Debugging"]
topic_type:
- apiref
api_name:
- mui
api_type:
- NA
---

# !mui


The **!mui** extension displays the Multilingual User Interface (MUI) cache information. The implementation of MUI was improved in Windows Vista. As a result, the behavior of this extension on earlier implementations is undefined.

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!mui%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




