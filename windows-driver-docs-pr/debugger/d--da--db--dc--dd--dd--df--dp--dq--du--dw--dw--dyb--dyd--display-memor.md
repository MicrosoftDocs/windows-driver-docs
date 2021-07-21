---
title: d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)
description: The d* commands display the contents of memory in the given range.
keywords: ["d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)
api_type:
- NA
ms.localizationpriority: medium
---

# d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)


The **d\*** commands display the contents of memory in the given range.

```dbgcmd
d{a|b|c|d|D|f|p|q|u|w|W} [Options] [Range] 
dy{b|d} [Options] [Range] 
d [Options] [Range] 
```

## <span id="ddk_cmd_display_memory_dbg"></span><span id="DDK_CMD_DISPLAY_MEMORY_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies one or more display options. Any of the following options can be included, except that no more than one **/p**\* option can be indicated:

<span id="_cWidth"></span><span id="_cwidth"></span><span id="_CWIDTH"></span>**/c**_Width_  
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

**Modes**: user mode, kernel mode

**Targets**: live, crash dump

**Platforms**: all

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

## Remarks

Each line displayed will include the address of the first byte in the line followed by the contents of memory at that and following locations.

If you omit *Range*, the command will display memory starting at the ending location of the last display command. This allows you to continuously scan through memory.

This command exists in the following forms. The second characters of the **dd**, **dD**, **dw**, and **dW** commands are case-sensitive, as are the third characters of the **dyb** and **dyd** commands.

|Command|Display|
|--- |--- |
|d|This displays data in the same format as the most recent d command. If no previous d command has been issued, d has the same effect as db. Notice that d repeats the most recent command that began with d. This includes dda, ddp, ddu, dpa, dpp, dpu, dqa, dqp, dqu, dds, dps, dqs, ds, dS, dg, dl, dt, and dv, as well as the display commands on this page. If the parameters given after d are not appropriate, errors may result.|
|da|ASCII characters. Each line displays up to 48 characters. The display continues until the first null byte or until all characters in range have been displayed. All nonprintable characters, such as carriage returns and line feeds, are displayed as periods (.).|
|db|Byte values and ASCII characters. Each display line shows the address of the first byte in the line, followed by up to 16 hexadecimal byte values. The byte values are immediately followed by the corresponding ASCII values. The eighth and ninth hexadecimal values are separated by a hyphen (-). All nonprintable characters, such as carriage returns and line feeds, are displayed as periods (.). The default count is 128 bytes.|
|dc|Double-word values (4 bytes) and ASCII characters. Each display line shows the address of the first word in the line and up to eight hexadecimal word values, as well as their ASCII equivalent. The default count is 32 DWORDs (128 bytes).| 
|dd|Double-word values (4 bytes).The default count is 32 DWORDs (128 bytes).|
|dD|Double-precision floating-point numbers (8 bytes). The default count is 15 numbers (120 bytes).|
|df|Single-precision floating-point numbers (4 bytes). The default count is 16 numbers (64 bytes).|
|dp|Pointer-sized values. This command is equivalent to dd or dq, depending on whether the target computer's processor architecture is 32-bit or 64-bit, respectively. The default count is 32 DWORDs or 16 quad-words (128 bytes).|
|dq|Quad-word values (8 bytes). The default count is 16 quad-words (128 bytes).|
|du|Unicode characters. Each line displays up to 48 characters. The display continues until the first null byte or until all characters in range have been displayed. All nonprintable characters, such as carriage returns and line feeds, are displayed as periods (.).|
|dw|Word values (2 bytes). Each display line shows the address of the first word in the line and up to eight hexadecimal word values. The default count is 64 words (128 bytes).|
|dW|Word values (2 bytes) and ASCII characters. Each display line shows the address of the first word in the line and up to eight hexadecimal word values. The default count is 64 words (128 bytes).|
|dyb|Binary values and byte values. The default count is 32 bytes.|
|dyd|Binary values and double-word values (4 bytes). The default count is 8 DWORDs (32 bytes).|

 

If you attempt to display an invalid address, its contents are shown as question marks (**?**).

 

 





