---
title: Using AMLI Debugger Extensions
description: Using AMLI Debugger Extensions
ms.assetid: 98b9cd6e-b2e1-44bd-aff6-376b9cf2daa2
keywords: ["AMLI Debugger, AMLI Debugger extensions", "amli extension", "acpikd.amli extension"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using AMLI Debugger Extensions


## <span id="ddk_using_amli_debugger_extensions_dbg"></span><span id="DDK_USING_AMLI_DEBUGGER_EXTENSIONS_DBG"></span>


In Windows XP and later versions of Windows, AMLI Debugger extension commands are contained in the extension module Kdexts.dll and use the following syntax:

```
kd> !amli command [parameters] 
```

In Windows 2000, these extension commands are contained in Acpikd.dll and use the following syntax:

```
kd> !acpikd.amli command [parameters] 
```

As with any extension module, after it has been loaded you can omit the **acpikd** prefix.

If you are at the AMLI Debugger prompt, you can execute any of these extension commands by simply entering the *command* name without the **!amli** prefix:

```
AMLI(? for help)-> command [parameters] 
```

When you are at this prompt, the **!amli debugger** command is not available (because it would be meaningless). Also, the help command ( **?** ) at this prompt shows all AMLI Debugger extensions and commands, while the **!amli ?** extension only displays help on actual extensions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Action</th>
<th align="left">Extension Command</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Display Help</p></td>
<td align="left"><p>[<strong>!amli ?</strong>](-amli--.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Set AML Breakpoint</p></td>
<td align="left"><p>[<strong>!amli bp</strong>](-amli-bp.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>List AML Breakpoints</p></td>
<td align="left"><p>[<strong>!amli bl</strong>](-amli-bl.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Disable AML Breakpoint</p></td>
<td align="left"><p>[<strong>!amli bd</strong>](-amli-bd.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Enable AML Breakpoint</p></td>
<td align="left"><p>[<strong>!amli be</strong>](-amli-be.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Clear AML Breakpoint</p></td>
<td align="left"><p>[<strong>!amli bc</strong>](-amli-bc.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Enter AMLI Debugger</p></td>
<td align="left"><p>[<strong>!amli debugger</strong>](-amli-debugger.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Display Event Log</p></td>
<td align="left"><p>[<strong>!amli dl</strong>](-amli-dl.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Clear Event Log</p></td>
<td align="left"><p>[<strong>!amli cl</strong>](-amli-cl.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Display Heap</p></td>
<td align="left"><p>[<strong>!amli dh</strong>](-amli-dh.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Data Object</p></td>
<td align="left"><p>[<strong>!amli do</strong>](-amli-do.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Display Stack</p></td>
<td align="left"><p>[<strong>!amli ds</strong>](-amli-ds.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Namespace Object</p></td>
<td align="left"><p>[<strong>!amli dns</strong>](-amli-dns.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Find Namespace Object</p></td>
<td align="left"><p>[<strong>!amli find</strong>](-amli-find.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Nearest Method</p></td>
<td align="left"><p>[<strong>!amli ln</strong>](-amli-ln.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>List All Contexts</p></td>
<td align="left"><p>[<strong>!amli lc</strong>](-amli-lc.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Context Information</p></td>
<td align="left"><p>[<strong>!amli r</strong>](-amli-r.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Unassemble AML Code</p></td>
<td align="left"><p>[<strong>!amli u</strong>](-amli-u.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Set AMLI Debugger Options</p></td>
<td align="left"><p>[<strong>!amli set</strong>](-amli-set.md)</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20AMLI%20Debugger%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




