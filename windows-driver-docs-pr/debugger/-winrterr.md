---
title: winrterr
description: The winrterr sets the debugger reporting mode for Windows Runtime errors.
ms.assetid: 72E3EF7A-6055-405F-9E24-C9B81C07B8A7
keywords: ["winrterr Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- winrterr
api_type:
- NA
---

# !winrterr


The **!winrterr** sets the debugger reporting mode for Windows Runtime errors.

``` syntax
!winrterr Mode
!winrterr
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="Mode"></span><span id="mode"></span><span id="MODE"></span>*Mode*  
The following table describes the possible values for *Mode*.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="report"></span><span id="REPORT"></span>report</p></td>
<td align="left"><p>When a Windows Runtime error occurs, the error and related text are displayed in the debugger, but execution contunues. This is the default mode.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="break"></span><span id="BREAK"></span>break</p></td>
<td align="left"><p>When a Windows Runtime error occurs, the error and related text are displayed in the debugger, and execution stops.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="quiet"></span><span id="QUIET"></span>quiet</p></td>
<td align="left"><p>When a Windows Runtime error occurs, nothing is displayed in the debugger, and execution continues.</p></td>
</tr>
</tbody>
</table>

 

If *Mode* is omitted, **!winrterr** displays the current reporting mode. If the debugger has broken in as a result of a Windows Runtime error, the error and related text are also displayed.

## <span id="see_also"></span>See also


[Windows Runtime Debugger Commands](windows-runtime-debugger-commands.md)

[**!hstring**](-hstring.md)

[**!hstring2**](-hstring2.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!winrterr%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





