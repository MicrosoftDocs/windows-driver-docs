---
title: ".allow_image_mapping (Allow Image Mapping)"
description: "The .allow_image_mapping command controls whether image files will be mapped."
keywords: [".allow_image_mapping (Allow Image Mapping) Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- .allow_image_mapping (Allow Image Mapping)
api_type:
- NA
---

# .allow\_image\_mapping (Allow Image Mapping)

The **.allow\_image\_mapping** command controls whether image files will be mapped.

```dbgcmd
    .allow_image_mapping [/r] 0 
    .allow_image_mapping [/r] 1 
    .allow_image_mapping 
```

## Parameters

<span id="________r______"></span><span id="________R______"></span> **/r**   
Reloads all modules in the debugger's module list. This is equivalent to [**.reload /d**](-reload--reload-module-.md).

<span id="_______0______"></span> **0**   
Prevents image files from being mapped.

<span id="_______1______"></span> **1**   
Allows image files to be mapped.

## Environment

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

## Remarks

With no parameters, **.allow\_image\_mapping** will display whether image file mapping is currently allowed. By default, this mapping is allowed.

Image mapping is most common when a minidump is being debugged. Image mapping can also occur if DbgHelp is unable to access debug records (for example, during kernel debugging when memory has been paged out).
