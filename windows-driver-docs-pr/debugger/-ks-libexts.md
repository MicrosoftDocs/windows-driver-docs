---
title: ks.libexts
description: The ks.libexts extension provides access to Microsoft-supplied library extensions that are statically linked to the extension module.
ms.assetid: 03328041-9922-4367-b6e9-d822a9c03f32
keywords: ["ks.libexts Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ks.libexts
api_type:
- NA
ms.localizationpriority: medium
---

# !ks.libexts


The **!ks.libexts** extension provides access to Microsoft-supplied library extensions that are statically linked to the extension module.

```dbgcmd
!ks.libexts [Command] [Libext] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>*Command*  
Optional. Specifies one of the following values. If this argument is omitted, **!ks.libexts** returns help information.

<span id="disableall________"></span><span id="DISABLEALL________"></span>**disableall**   
Disable all library extensions. When this is used, omit the *Libext* parameter.

<span id="_________disable"></span><span id="_________DISABLE"></span> **disable**  
Disable a specific library extension by name. When this is used, specify the name in the *Libext* parameter.

<span id="_________enableall"></span><span id="_________ENABLEALL"></span> **enableall**  
Enable all library extensions. Only loaded components with correct symbols are enabled. When this is used, omit the *Libext* parameter.

<span id="enable"></span><span id="ENABLE"></span>**enable**  
Enable a specific library extension by name. When this is used, specify the name in the *Libext* parameter. Only loaded components with correct symbols can be enabled.

<span id="_________details"></span><span id="_________DETAILS"></span> **details**  
Show details about all currently linked library extensions. When this is used, omit the *Libext* parameter.

<span id="_______Libext______"></span><span id="_______libext______"></span><span id="_______LIBEXT______"></span> *Libext*   
Specifies the name of a library extension. Required only for *Command* values of **enable** or **disable**.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel Streaming Debugging](kernel-streaming-debugging.md).

Remarks
-------

The extension module contains an extensibility framework that allows separate components to be built and linked into Ks.dll. These extra components are called library extensions.

The **!ks.libexts** command allows viewing of statistics about those library extensions as well as control over them. For details, issue **!ks.libexts** with no arguments.

 

 





