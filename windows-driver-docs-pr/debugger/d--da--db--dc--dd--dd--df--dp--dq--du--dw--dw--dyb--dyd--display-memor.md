---
title: d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)
description: The d* commands display the contents of memory in the given range.
ms.assetid: deb58b77-6648-466d-be00-e2e0a92895b5
keywords: ["d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)
api_type:
- NA
---

# d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)


The **d\*** commands display the contents of memory in the given range.

```
d{a|b|c|d|D|f|p|q|u|w|W} [Options] [Range] 
dy{b|d} [Options] [Range] 
d [Options] [Range] 
```

## <span id="ddk_cmd_display_memory_dbg"></span><span id="DDK_CMD_DISPLAY_MEMORY_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies one or more display options. Any of the following options can be included, except that no more than one **/p**\* option can be indicated:

<span id="_cWidth"></span><span id="_cwidth"></span><span id="_CWIDTH"></span>**/c***Width*  
Specifies the number of columns to use in the display. If this is omitted, the default number of columns depends on the display type.

<span id="_p"></span><span id="_P"></span>**/p**  
(Kernel-mode only) Uses physical memory addresses for the display. The range specified by *Range* will be taken from physical memory rather than virtual memory.

<span id="_p_c_"></span><span id="_P_C_"></span>**/p\[c\]**  
(Kernel-mode only) Same as **/p**, except that cached memory will be read. The brackets around **c** must be included.

<span id="_p_uc_"></span><span id="_P_UC_"></span>**/p\[uc\]**  
(Kernel-mode only) Same as **/p**, except that uncached memory will be read. The brackets around **uc** must be included.

<span id="_p_wc_"></span><span id="_P_WC_"></span>**/p\[wc\]**  
(Kernel-mode only) Same as **/p**, except that write-combined memory will be read. The brackets around **wc** must be included.

<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory area to display. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md). If you omit *Range*, the command will display memory starting at the ending location of the last display command. If *Range* is omitted and no previous display command has been used, the display begins at the current instruction pointer.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

Each line displayed will include the address of the first byte in the line followed by the contents of memory at that and following locations.

If you omit *Range*, the command will display memory starting at the ending location of the last display command. This allows you to continuously scan through memory.

This command exists in the following forms. The second characters of the **dd**, **dD**, **dw**, and **dW** commands are case-sensitive, as are the third characters of the **dyb** and **dyd** commands.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Display</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>d</strong></p></td>
<td align="left"><p>This displays data in the same format as the most recent <strong>d*</strong> command. If no previous <strong>d*</strong> command has been issued, <strong>d</strong> has the same effect as <strong>db</strong>.</p>
<p>Notice that <strong>d</strong> repeats the most recent command that began with <strong>d</strong>. This includes <strong>dda</strong>, <strong>ddp</strong>, <strong>ddu</strong>, <strong>dpa</strong>, <strong>dpp</strong>, <strong>dpu</strong>, <strong>dqa</strong>, <strong>dqp</strong>, <strong>dqu</strong>, <strong>dds</strong>, <strong>dps</strong>, <strong>dqs</strong>, <strong>ds</strong>, <strong>dS</strong>, <strong>dg</strong>, <strong>dl</strong>, <strong>dt</strong>, and <strong>dv</strong>, as well as the display commands on this page. If the parameters given after <strong>d</strong> are not appropriate, errors may result.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>da</strong></p></td>
<td align="left"><p>ASCII characters.</p>
<p>Each line displays up to 48 characters. The display continues until the first null byte or until all characters in <em>range</em> have been displayed. All nonprintable characters, such as carriage returns and line feeds, are displayed as periods (<strong>.</strong>).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>db</strong></p></td>
<td align="left"><p>Byte values and ASCII characters.</p>
<p>Each display line shows the address of the first byte in the line, followed by up to 16 hexadecimal byte values. The byte values are immediately followed by the corresponding ASCII values. The eighth and ninth hexadecimal values are separated by a hyphen (<strong>-</strong>). All nonprintable characters, such as carriage returns and line feeds, are displayed as periods (<strong>.</strong>).</p>
<p>The default count is 128 bytes.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>dc</strong></p></td>
<td align="left"><p>Double-word values (4 bytes) and ASCII characters.</p>
<p>Each display line shows the address of the first word in the line and up to eight hexadecimal word values, as well as their ASCII equivalent.</p>
<p>The default count is 32 DWORDs (128 bytes).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dd</strong></p></td>
<td align="left"><p>Double-word values (4 bytes).</p>
<p>The default count is 32 DWORDs (128 bytes).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>dD</strong></p></td>
<td align="left"><p>Double-precision floating-point numbers (8 bytes).</p>
<p>The default count is 15 numbers (120 bytes).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>df</strong></p></td>
<td align="left"><p>Single-precision floating-point numbers (4 bytes).</p>
<p>The default count is 16 numbers (64 bytes).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>dp</strong></p></td>
<td align="left"><p>Pointer-sized values. This command is equivalent to <strong>dd</strong> or <strong>dq</strong>, depending on whether the target computer's processor architecture is 32-bit or 64-bit, respectively.</p>
<p>The default count is 32 DWORDs or 16 quad-words (128 bytes).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dq</strong></p></td>
<td align="left"><p>Quad-word values (8 bytes).</p>
<p>The default count is 16 quad-words (128 bytes).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>du</strong></p></td>
<td align="left"><p>Unicode characters.</p>
<p>Each line displays up to 48 characters. The display continues until the first null byte or until all characters in <em>range</em> have been displayed. All nonprintable characters, such as carriage returns and line feeds, are displayed as periods (<strong>.</strong>).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dw</strong></p></td>
<td align="left"><p>Word values (2 bytes).</p>
<p>Each display line shows the address of the first word in the line and up to eight hexadecimal word values.</p>
<p>The default count is 64 words (128 bytes).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>dW</strong></p></td>
<td align="left"><p>Word values (2 bytes) and ASCII characters.</p>
<p>Each display line shows the address of the first word in the line and up to eight hexadecimal word values.</p>
<p>The default count is 64 words (128 bytes).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dyb</strong></p></td>
<td align="left"><p>Binary values and byte values.</p>
<p>The default count is 32 bytes.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>dyd</strong></p></td>
<td align="left"><p>Binary values and double-word values (4 bytes).</p>
<p>The default count is 8 DWORDs (32 bytes).</p></td>
</tr>
</tbody>
</table>

 

If you attempt to display an invalid address, its contents are shown as question marks (**?**).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20d,%20da,%20db,%20dc,%20dd,%20dD,%20df,%20dp,%20dq,%20du,%20dw%20%28Display%20Memory%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




