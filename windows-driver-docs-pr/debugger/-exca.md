---
title: exca
description: The exca extension displays PC-Card Interrupt Controller (PCIC) Exchangable Card Architecture (ExCA) registers.
ms.assetid: a395f7f3-0e1d-4f4c-80a1-018ca52a20fd
keywords: ["PCIC (PC Card Interrupt Controller)", "ExCA registers", "exca Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- exca
api_type:
- NA
---

# !exca


The **!exca** extension displays PC-Card Interrupt Controller (PCIC) Exchangable Card Architecture (ExCA) registers.

``` syntax
!exca BasePort.SocketNumber
```

## <span id="ddk__exca_dbg"></span><span id="DDK__EXCA_DBG"></span>Parameters


<span id="_______BasePort______"></span><span id="_______baseport______"></span><span id="_______BASEPORT______"></span> *BasePort*   
Specifies the base port of the PCIC.

<span id="_______SocketNumber______"></span><span id="_______socketnumber______"></span><span id="_______SOCKETNUMBER______"></span> *SocketNumber*   
Specifies the socket number of the ExCA register on the PCIC.

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
Kext.dll
Kdextx86.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kext.dll</p></td>
</tr>
</tbody>
</table>

 

The **!exca** extension is only available for an x86-based target computer.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

The [**!cbreg**](-cbreg.md) extension can be used to display CardBus Socket registers and CardBus ExCA registers by address.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!exca%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




