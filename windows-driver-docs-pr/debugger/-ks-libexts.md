---
title: ks.libexts
description: The ks.libexts extension provides access to Microsoft-supplied library extensions that are statically linked to the extension module.
ms.assetid: 03328041-9922-4367-b6e9-d822a9c03f32
keywords: ["ks.libexts Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ks.libexts
api_type:
- NA
---

# !ks.libexts


The **!ks.libexts** extension provides access to Microsoft-supplied library extensions that are statically linked to the extension module.

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ks.libexts%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




