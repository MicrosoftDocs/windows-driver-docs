---
title: dda, ddp, ddu, dpa, dpp, dpu, dqa, dqp, dqu (Display Referenced Memory)
description: The dda, ddp, ddu, dpa, dpp, dpu, dqa, dqp, and dqu commands display the pointer at the specified location, dereference that pointer, and display the associated memory.
keywords: ["dda, ddp, ddu, dpa, dpp, dpu, dqa, dqp, dqu (Display Referenced Memory) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dda, ddp, ddu, dpa, dpp, dpu, dqa, dqp, dqu (Display Referenced Memory)
api_type:
- NA
ms.localizationpriority: medium
---

# dda, ddp, ddu, dpa, dpp, dpu, dqa, dqp, dqu (Display Referenced Memory)


The **dda**, **ddp**, **ddu**, **dpa**, **dpp**, **dpu**, **dqa**, **dqp**, and **dqu** commands display the pointer at the specified location, dereference that pointer, and then display the memory at the resulting location in a variety of formats.

```dbgcmd
ddp [Options] [Range] 
dqp [Options] [Range] 
dpp [Options] [Range] 
dda [Options] [Range] 
dqa [Options] [Range] 
dpa [Options] [Range] 
ddu [Options] [Range] 
dqu [Options] [Range] 
dpu [Options] [Range]
```

## <span id="ddk_cmd_display_referenced_memory_dbg"></span><span id="DDK_CMD_DISPLAY_REFERENCED_MEMORY_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies one or more display options. Any of the following options can be included, except that no more than one **/p**\* option can be indicated:

<span id="_cWidth"></span><span id="_cwidth"></span><span id="_CWIDTH"></span>**/c**_Width_  
Specifies the number of columns to use in the display. If this is omitted, the default number of columns depends on the display type. Because of the way pointers are displayed by these commands, it is usually best to use the default of only one data column.

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

**Modes**: user mode, kernel mode

**Targets**: live, crash dump

**Platforms**: all

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

## Remarks

The second and third characters of this command are case-sensitive.

The second character of this command determines the pointer size used:

|Command|Display|
|--- |--- |
|dd|32-bit pointers used|
|dq|64-bit pointers used|
|dp*|Standard pointer sizes used: 32-bit or 64-bit, depending on the target's processor architecture|

 

The third character of this command determines how the dereferenced memory is displayed:

|Command|Display|
|--- |--- |
|dp|Displays the contents of the memory referenced by the pointer in DWORD or QWORD format, depending on the pointer size of the target's processor architecture. If this value matches any known symbol, this symbol is displayed as well.|
|da|Displays the contents of the memory referenced by the pointer in ASCII character format.|
|d*u|Displays the contents of the memory referenced by the pointer in Unicode character format.|

 

If line number information has been enabled, source file names and line numbers will be displayed when available.

 

 





