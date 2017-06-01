---
title: stl
description: The stl extension displays some of the known Standard Template Library (STL) templates.
ms.assetid: a1f1f923-64bd-44c9-941f-9a648888c7e0
keywords: ["stl Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- stl
api_type:
- NA
---

# !stl


The **!stl** extension displays some of the known Standard Template Library (STL) templates.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!stl%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




