---
title: d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)
description: Learn about the d* commands, which display the contents of memory in the given range. You can specify several options.
keywords: ["d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory) Windows Debugging"]
ms.date: 1/06/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)
api_type:
- NA
---

# d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)

The **d\*** commands display the contents of memory in the given range.

```dbgcmd
d{a|b|c|d|D|f|p|q|u|w|W} [Options] [Range] 
dy{b|d} [Options] [Range] 
d [Options] [Range] 
```

## Parameters

*Options* 

Specifies one or more display options. You can include any of the following options, but no more than one **/p**\* option.

**/c**_Width_

  Specifies the number of columns to use in the display. If you don't specify this option, the default number of columns depends on the display type.

**/p**

  (Kernel mode only) Uses physical memory addresses for the display. The range specified by **Range** is taken from physical memory rather than virtual memory.

**/p\[c\]**  

  (Kernel mode only) Same as **/p**, except that cached memory is read. Include the brackets around **c**.

**/p\[uc\]**  

  (Kernel mode only) Same as **/p**, except that uncached memory is read. Include the brackets around **uc**.

**/p\[wc\]**  

  (Kernel mode only) Same as **/p**, except that write-combined memory is read. Include the brackets around **wc**.

*Range* 

Specifies the memory area to display. For more syntax details, see [Address and address range syntax](address-and-address-range-syntax.md). If you omit **Range**, the command displays memory starting at the ending location of the last display command. If you omit **Range** and there's no previous display command, the display begins at the current instruction pointer.

### Environment

**Modes**: user mode, kernel mode

**Targets**: live, crash dump

**Platforms**: all

### Additional information

For an overview of memory manipulation and a description of other memory-related commands, see [Reading and writing memory](reading-and-writing-memory.md).

## Remarks

Each line displayed includes the address of the first byte in the line followed by the contents of memory at that and following locations.

If you omit **Range**, the command displays memory starting at the ending location of the last display command. This approach allows you to continuously scan through memory.

This command exists in the following forms. The second characters of the **dd**, **dD**, **dw**, and **dW** commands are case-sensitive, as are the third characters of the **dyb** and **dyd** commands.

| Command | Display |
|:------- |:------- |
| d | This command displays data in the same format as the most recent **d\*** command. If no previous **d\*** command has been issued, **d\*** has the same effect as **db**. Notice that **d** repeats the most recent command that began with *d*. These commands include **dda**, **ddp**, **ddu**, **dpa**, **dpp**, **dpu**, **dqa**, **dqp**, **dqu**, **dds**, **dps**, **dqs**, **ds**, **dS**, **dg**, **dl**, **dt**, **dv**, and the display commands in this article. If the parameters given after *d* aren't appropriate, errors might result. |
| da | ASCII characters. Each line displays up to 48 characters. The display continues until the first null byte or until all characters in range have been displayed. All nonprintable characters, such as carriage returns and line feeds, are displayed as periods (.). |
| db | Byte values and ASCII characters. Each display line shows the address of the first byte in the line, followed by up to 16 hexadecimal byte values. The byte values are immediately followed by the corresponding ASCII values. The eighth and ninth hexadecimal values are separated by a hyphen (-). All nonprintable characters, such as carriage returns and line feeds, are displayed as periods (.). The default count is 128 bytes. |
| dc | Double-word values (4 bytes) and ASCII characters. Each display line shows the address of the first word in the line and up to eight hexadecimal word values and their ASCII equivalent. The default count is 32 DWORDs (128 bytes). |
| dd | Double-word values (4 bytes). The default count is 32 DWORDs (128 bytes). |
| dD | Double-precision floating-point numbers (8 bytes). The default count is 15 numbers (120 bytes). |
| df | Single-precision floating-point numbers (4 bytes). The default count is 16 numbers (64 bytes). |
| dp | Pointer-sized values. This command is equivalent to **dd** or **dq**, depending on whether the target computer processor architecture is 32-bit or 64-bit, respectively. The default count is 32 DWORDs or 16 quad-words (128 bytes). |
| dq | Quad-word values (8 bytes). The default count is 16 quad-words (128 bytes). |
| du | Unicode characters. Each line displays up to 48 characters. The display continues until the first null byte or until all characters in range have been displayed. All nonprintable characters, such as carriage returns and line feeds, are displayed as periods (.). |
| dw | Word values (2 bytes). Each display line shows the address of the first word in the line and up to eight hexadecimal word values. The default count is 64 words (128 bytes). |
| dW | Word values (2 bytes) and ASCII characters. Each display line shows the address of the first word in the line and up to eight hexadecimal word values. The default count is 64 words (128 bytes). |
| dyb | Binary values and byte values. The default count is 32 bytes. |
| dyd | Binary values and double-word values (4 bytes). The default count is 8 DWORDs (32 bytes). |

If you attempt to display an invalid address, its contents are shown as question marks (**?**).
