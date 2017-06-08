---
title: dh
description: The dh extension displays the headers for the specified image.
ms.assetid: 1b4f94ae-42cc-4381-a2d1-c2f248e4d5a6
keywords: ["NTFS file object", "dh Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- dh
api_type:
- NA
---

# !dh


The **!dh** extension displays the headers for the specified image.

``` syntax
!dh [Options] Address 
!dh -h
```

## <span id="ddk__dh_dbg"></span><span id="DDK__DH_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Any one of the following options:

<span id="-f"></span><span id="-F"></span>**-f**  
Displays file headers.

<span id="-s"></span><span id="-S"></span>**-s**  
Displays section headers.

<span id="-a"></span><span id="-A"></span>**-a**  
Displays all header information.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the image.

<span id="_______-h______"></span><span id="_______-H______"></span> **-h**   
Displays some Help text for this extension in the [Debugger Command window](debugger-command-window.md).

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Dbghelp.dll
Kdextx86.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The [**!lmi**](-lmi.md) extension extracts the most important information from the image header and displays it in a concise summary format. That extension is frequently more useful than **!dh**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!dh%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




