---
title: zombies
description: The zombies extension displays all dead ( \ 0034;zombie \ 0034;) processes or threads.
ms.assetid: f7fbce79-456a-4643-ad31-8cb2e6449ecf
keywords: ["zombies Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- zombies
api_type:
- NA
---

# !zombies


The **!zombies** extension displays all dead ("zombie") processes or threads.

```
!zombies [Flags [RestartAddress]]
```

## <span id="ddk__zombies_dbg"></span><span id="DDK__ZOMBIES_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies what will be displayed. Possible values include:

<span id="1"></span>1  
Displays all zombie processes. (This is the default.)

<span id="2"></span>2  
Displays all zombie threads.

<span id="_______RestartAddress______"></span><span id="_______restartaddress______"></span><span id="_______RESTARTADDRESS______"></span> *RestartAddress*   
Specifies the hexadecimal address at which to begin the search. This is useful if the previous search was terminated prematurely. The default is zero.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

To see a list of all processes and threads, use the [**!process**](-process.md) extension.

For general information about processes and threads in kernel mode, see [Changing Contexts](changing-contexts.md). For more information about analyzing processes and threads, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

Zombie processes are dead processes that have not yet been removed from the process list. Zombie threads are analogous.

This extension is available only for Windows 2000.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!zombies%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




