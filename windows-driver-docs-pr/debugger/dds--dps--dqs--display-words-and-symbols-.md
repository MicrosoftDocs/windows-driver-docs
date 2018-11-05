---
title: dds, dps, dqs (Display Words and Symbols)
description: The dds, dps, and dqs commands display the contents of memory in the given range. This memory is assumed to be a series of addresses in the symbol table. 
ms.assetid: 5a3ed1c4-723a-4902-bfbf-d4a44d2cd0b5
keywords: ["dds, dps, dqs (Display Words and Symbols) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dds, dps, dqs (Display Words and Symbols)
api_type:
- NA
ms.localizationpriority: medium
---

# dds, dps, dqs (Display Words and Symbols)


The **dds**, **dps**, and **dqs** commands display the contents of memory in the given range. This memory is assumed to be a series of addresses in the symbol table. The corresponding symbols are displayed as well.

```dbgcmd
dds [Options] [Range] 
dqs [Options] [Range] 
dps [Options] [Range] 
```

## <span id="ddk_cmd_display_words_and_symbols_dbg"></span><span id="DDK_CMD_DISPLAY_WORDS_AND_SYMBOLS_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies one or more display options. Any of the following options can be included, except that no more than one **/p**\* option can be indicated:

<span id="_c_Width"></span><span id="_c_width"></span><span id="_C_WIDTH"></span>**/c** *Width*  
Specifies the number of columns to use in the display. If this is omitted, the default number of columns depends on the display type. Because of the way symbols are displayed by these commands, it is usually best to use the default of only one data column.

<span id="_p"></span><span id="_P"></span>**/p**  
(Kernel-mode only) Uses physical memory addresses for the display. The range specified by *Range* will be taken from physical memory rather than virtual memory.

<span id="_p_c_"></span><span id="_P_C_"></span>**/p\[c\]**  
(Kernel-mode only) Same as **/p**, except that cached memory will be read. The brackets around **c** must be included.

<span id="_p_uc_"></span><span id="_P_UC_"></span>**/p\[uc\]**  
(Kernel-mode only) Same as **/p**, except that uncached memory will be read. The brackets around **uc** must be included.

<span id="_p_wc_"></span><span id="_P_WC_"></span>**/p\[wc\]**  
(Kernel-mode only) Same as **/p**, except that write-combined memory will be read. The brackets around **wc** must be included.

<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory area to display. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md). If you omit *Range*, the command will display memory starting at the ending location of the last display command. If *Range* is omitted and no previous display command has been used, the display begins at the current instruction pointer. If a simple address is given, the default range length is 128 bytes.

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

The second character of **dds** is case-sensitive. The third character of all these commands is case-sensitive.

The **dds** command displays double-word (4 byte) values like the [**dd**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command. The **dqs** command displays quad-word (8 byte) values like the **dq** command. The **dps** command displays pointer-sized values (4 byte or 8 byte, depending on the target computer's architecture) like the **dp** command.

Each of these words is treated as an address in the symbol table. The corresponding symbol information is displayed for each word.

If line number information has been enabled, source file names and line numbers will be displayed when available.

 

 





