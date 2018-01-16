---
title: sym
description: The sym extension controls noisy symbol loading and symbol prompts.
ms.assetid: 84551b24-740c-4289-acc4-8a0053f80b41
keywords: ["symbols, noisy symbol loading", "symbols, prompts", "sym Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- sym
api_type:
- NA
---

# !sym


The **!sym** extension controls noisy symbol loading and symbol prompts.

```
!sym 
!sym noisy 
!sym quiet 
!sym prompts 
!sym prompts off
```

## <span id="ddk__sym_dbg"></span><span id="DDK__SYM_DBG"></span>Parameters


<span id="_______noisy______"></span><span id="_______NOISY______"></span> **noisy**   
Activates noisy symbol loading.

<span id="_______quiet______"></span><span id="_______QUIET______"></span> **quiet**   
Deactivates noisy symbol loading.

<span id="_______prompts______"></span><span id="_______PROMPTS______"></span> **prompts**   
Allows authentication dialog boxes to appear when SymSrv receives an authentication request.

<span id="_______prompts_off______"></span><span id="_______PROMPTS_OFF______"></span> **prompts off**   
Suppresses all authentication dialog boxes when SymSrv receives an authentication request. This may result in SymSrv being unable to access symbols over the internet.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If the **!sym** extension is used with no arguments, the current state of noisy symbol loading and symbol prompting is displayed.

The **!sym noisy** and **!sym quiet** extensions control noisy symbol loading. For details and for other methods of displaying and changing this option, see [SYMOPT\_DEBUG](symbol-options.md#symopt-debug).

The **!sym prompts** and **!sym prompts off** extensions control whether authentication dialogs are displayed when SymSrv encounters an authentication request. These commands must be followed by [**.reload (Reload Module)**](-reload--reload-module-.md) for them to take effect. Authentication requests may be sent by proxy servers, internet firewalls, smart card readers, and secure websites. For details and for other methods of changing this option, see [Firewalls and Proxy Servers](firewalls-and-proxy-servers.md).

**Note**   Noisy symbol loading should not be confused with noisy source loading -- that is controlled by the [**.srcnoisy (Noisy Source Loading)**](-srcnoisy--noisy-source-loading-.md) command.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!sym%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




