---
title: .outmask (Control Output Mask)
description: The .outmask command controls the current output mask.
ms.assetid: a925f948-a746-4fed-9ccd-95513f41e3bf
keywords: ["Control Output Mask (.outmask) command", ".outmask (Control Output Mask) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .outmask (Control Output Mask)
api_type:
- NA
---

# .outmask (Control Output Mask)


The **.outmask** command controls the current output mask.

``` syntax
.outmask[-] [/l] Expression 
.outmask /a 
.outmask /d
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the flags to add to the mask. *Expression* can be any ULONG value that specifies the flag bits that you want. For a list of the possible flags, see the table in the Remarks section.

<span id="_______-______"></span> **-**   
Removes the bits that *Expression* specifies from the mask, instead of adding them to the mask.

<span id="________l______"></span><span id="________L______"></span> **/l**   
Preserves the current value of the log file's output mask. If you do not include **/l**, the log file's output mask is the same as the regular output mask.

<span id="________a______"></span><span id="________A______"></span> **/a**   
Activates all mask flags. This parameter is equivalent to **.outmask 0xFFFFFFFF**.

<span id="________d______"></span><span id="________D______"></span> **/d**   
Restores the output mask to the default value. This parameter is equivalent to **.outmask 0x3F7**.

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

Each output mask flag enables the debugger to display certain output in the [Debugger Command Window](debugger-command-window.md). If all of the mask flags are set, all output is displayed.

You should remove output mask flags with caution, because you might be unable to read debugger output.

The following flag values exist.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Default setting</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Normal output</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Error output</p></td>
</tr>
<tr class="odd">
<td align="left"><p>4</p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Warnings</p></td>
</tr>
<tr class="even">
<td align="left"><p>8</p></td>
<td align="left"><p>Off</p></td>
<td align="left"><p>Additional output</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10</p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Prompt output</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20</p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Register dump before prompt</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x40</p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Warnings that are specific to extension operation</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x80</p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Debug output from the target (for example, <strong>OutputDebugString</strong> or <strong>DbgPrint</strong>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x100</p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Debug input expected by the target (for example, <strong>DbgPrompt</strong>)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x200</p></td>
<td align="left"><p>On</p></td>
<td align="left"><p>Symbol messages (for example, <strong>!sym noisy</strong>)</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.outmask%20%28Control%20Output%20Mask%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




