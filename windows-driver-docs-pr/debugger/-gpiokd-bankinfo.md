---
title: gpiokd.bankinfo
description: The gpiokd.bankinfo command displays information about a GPIO bank.
ms.assetid: C4AFF469-0624-4D59-AE78-9D7FC407AC3A
keywords: ["gpiokd.bankinfo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- gpiokd.bankinfo
api_type:
- NA
---

# !gpiokd.bankinfo


The **!gpiokd.bankinfo** command displays information about a GPIO bank.

```
!gpiokd.bankinfo BankAddress [Flags]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______BankAddress______"></span><span id="_______bankaddress______"></span><span id="_______BANKADDRESS______"></span> *BankAddress*   
Address of a [\_GPIO\_BANK\_ENTRY](gpio-extensions.md#data-structures-used-by-the-gpio-commands) structure that represents a bank of a GPIO controller.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Flags that specify which information is displayed. This parameter is a bitwise OR of one or more of the following flags.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="0x1"></span><span id="0X1"></span>0x1</p></td>
<td align="left"><p>Displays the pin table.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="0x2"></span><span id="0X2"></span>0x2</p></td>
<td align="left"><p>Displays the Enable and Mask registers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="0x4"></span><span id="0X4"></span>0x4</p></td>
<td align="left"><p>If bit 0 (0x1) is set and this flag (0x4) is set, the display includes unconfigured pins.</p></td>
</tr>
</tbody>
</table>

 

## <span id="DLL"></span><span id="dll"></span>DLL


Gpiokd.dll

## <span id="see_also"></span>See also


[GPIO Extensions](gpio-extensions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!gpiokd.bankinfo%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





