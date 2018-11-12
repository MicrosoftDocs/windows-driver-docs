---
title: std_map
description: The std_map extension displays the entries of a std map tree.
ms.assetid: 7a921226-e7b1-4c3f-9732-c53c66710ccb
keywords: ["std_map Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- std_map
api_type:
- NA
ms.localizationpriority: medium
---

# !std\_map


The **!std\_map** extension displays the entries of a std::map tree.

```dbgcmd
!std_map Address [Module!Type [TypeSize]]
!std_map -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the std::map tree to display.

<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the module in which the data structure is defined.

<span id="_______Type______"></span><span id="_______type______"></span><span id="_______TYPE______"></span> *Type*   
Specifies the name of a data structure. This must be expressed in <em>Module</em>**!std::pair&lt;**<em>Type1</em>**,**<em>Type2</em>**&gt;** form. If the *TypeSize* parameter is used, this parameter must be enclosed in quotation marks.

<span id="_______TypeSize______"></span><span id="_______typesize______"></span><span id="_______TYPESIZE______"></span> *TypeSize*   
Specifies the size of the data structure to make the symbols unambiguous.

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
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

To display other Standard Template Library (STL) defined templates, see [**!stl**](-stl.md).

Remarks
-------

Including the <em>Module</em>**!**<em>Type</em> option causes each entry in the table to be interpreted as having the given type.

Use [**dt -ve (Module!std::pair&lt;Type1,Type2&gt;)**](dt--display-type-.md) to display possible sizes.

 

 





