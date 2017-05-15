---
title: tls
description: The tls extension displays a thread local storage (TLS) slot.
ms.assetid: 43325322-8e6e-47fc-b1ec-8b1c304bb1e9
keywords: ["TLS (thread local storage)", "thread local storage (TLS)", "tls Windows Debugging"]
topic_type:
- apiref
api_name:
- tls
api_type:
- NA
---

# !tls


The **!tls** extension displays a thread local storage (TLS) slot.

``` syntax
!tls Slot [TEB]
```

## <span id="ddk__tls_dbg"></span><span id="DDK__TLS_DBG"></span>Parameters


<span id="_______Slot______"></span><span id="_______slot______"></span><span id="_______SLOT______"></span> *Slot*   
Specifies the TLS slot. This can be any value between 0 and 1088 (decimal). If *Slot* is -1, all slots are displayed.

<span id="_______TEB______"></span><span id="_______teb______"></span> *TEB*   
Specifies the thread environment block (TEB). If this is 0 or omitted, the current thread is used.

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

Here is an example:

``` syntax
0:000> !tls -1
TLS slots on thread: c08.f54
0x0000 : 00000000
0x0001 : 003967b8
0:000> !tls 0
c08.f54: 00000000
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!tls%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




