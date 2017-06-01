---
title: .force\_radix\_output (Use Radix for Integers)
description: The .force\_radix\_output command specifies whether integers are displayed in decimal format or in the default radix.
ms.assetid: 9ce79919-69fd-426f-8de1-34d0721c35a5
keywords: ["Use Radix for Integers (.force_radix_output) command", ".force_radix_output (Use Radix for Integers) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .force_radix_output (Use Radix for Integers)
api_type:
- NA
---

# .force\_radix\_output (Use Radix for Integers)


The **.force\_radix\_output** command specifies whether integers are displayed in decimal format or in the default radix.

```
.force_radix_output 0 
.force_radix_output 1 
```

## <span id="ddk_meta_use_radix_for_integers_dbg"></span><span id="DDK_META_USE_RADIX_FOR_INTEGERS_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Displays all integers (except for long integers) in decimal format. This is the default behavior for the Debugger.

<span id="_______1______"></span> **1**   
Displays all integers (except for long integers) in the default radix.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **.force\_radix\_output** command affects the output of the [**dt (Display Type)**](dt--display-type-.md) command.

In WinDbg, **.force\_radix\_output** also affects the display in the [Locals window](locals-window.md) and the Watch window. You can select or clear **Always display numbers in default radix** on the shortcut menu of the Locals or Watch window to have the same effect as **.force\_radix\_output**. These windows are automatically updated after you issue this command.

The **.force\_radix\_output** command affects only the display of standard integers. To specify whether long integers are displayed in decimal format or the default radix, use the [**.enable\_long\_status (Enable Long Integer Display)**](-enable-long-status--enable-long-integer-display-.md) command.

To change the default radix, use the [**n (Set Number Base)**](n--set-number-base-.md) command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.force_radix_output%20%28Use%20Radix%20for%20Integers%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




