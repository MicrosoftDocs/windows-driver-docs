---
title: std\_map
description: The std\_map extension displays the entries of a std map tree.
ms.assetid: 7a921226-e7b1-4c3f-9732-c53c66710ccb
keywords: ["std_map Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- std_map
api_type:
- NA
---

# !std\_map


The **!std\_map** extension displays the entries of a std::map tree.

```
!std_map Address [Module!Type [TypeSize]]
!std_map -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the std::map tree to display.

<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the module in which the data structure is defined.

<span id="_______Type______"></span><span id="_______type______"></span><span id="_______TYPE______"></span> *Type*   
Specifies the name of a data structure. This must be expressed in *Module***!std::pair&lt;***Type1***,***Type2***&gt;** form. If the *TypeSize* parameter is used, this parameter must be enclosed in quotation marks.

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

Including the *Module***!***Type* option causes each entry in the table to be interpreted as having the given type.

Use [**dt -ve (Module!std::pair&lt;Type1,Type2&gt;)**](dt--display-type-.md) to display possible sizes.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!std_map%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




