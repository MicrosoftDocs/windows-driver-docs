---
title: .allow\_image\_mapping (Allow Image Mapping)
description: The .allow\_image\_mapping command controls whether image files will be mapped.
ms.assetid: 3d216d17-f2af-48f7-9d91-e12c3c305a67
keywords: [".allow_image_mapping (Allow Image Mapping) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .allow_image_mapping (Allow Image Mapping)
api_type:
- NA
---

# .allow\_image\_mapping (Allow Image Mapping)


The **.allow\_image\_mapping** command controls whether image files will be mapped.

``` syntax
    .allow_image_mapping [/r] 0 
.allow_image_mapping [/r] 1 
.allow_image_mapping 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________r______"></span><span id="________R______"></span> **/r**   
Reloads all modules in the debugger's module list. This is equivalent to [**.reload /d**](-reload--reload-module-.md).

<span id="_______0______"></span> **0**   
Prevents image files from being mapped.

<span id="_______1______"></span> **1**   
Allows image files to be mapped.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode and kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

With no parameters, **.allow\_image\_mapping** will display whether image file mapping is currently allowed. By default, this mapping is allowed.

Image mapping is most common when a minidump is being debugged. Image mapping can also occur if DbgHelp is unable to access debug records (for example, during kernel debugging when memory has been paged out).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.allow_image_mapping%20%28Allow%20Image%20Mapping%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




