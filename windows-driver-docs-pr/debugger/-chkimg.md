---
title: chkimg
description: The chkimg extension detects corruption in the images of executable files by comparing them to the copy on a symbol store or other file repository.
ms.assetid: 8079676c-1138-4c60-95df-62fd270fee62
keywords: ["executable files and paths, corruption", "chkimg Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- chkimg
api_type:
- NA
ms.localizationpriority: medium
---

# !chkimg


The **!chkimg** extension detects corruption in the images of executable files by comparing them to the copy on a symbol store or other file repository.

```dbgsyntax
!chkimg [Options] [-mmw LogFile LogOptions] [Module]
```

## <span id="ddk__chkimg_dbg"></span><span id="DDK__CHKIMG_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Any combination of the following options:

<span id="-p_SearchPath_"></span><span id="-p_searchpath_"></span><span id="-P_SEARCHPATH_"></span>**-p** **** *SearchPath*   
Recursively searches *SearchPath* for the file before accessing the symbol server.

<span id="-f"></span><span id="-F"></span>**-f**  
Fixes errors in the image. Whenever the scan detects differences between the file on the symbol store and the image in memory, the contents of the file on the symbol store are copied over the image. If you are performing live debugging, you can create a dump file before you execute the **!chkimg -f** extension.

<span id="-nar"></span><span id="-NAR"></span>**-nar**  
Prevents the mapped image of the file on the symbol server from being moved. By default, when the copy of the file is located on the symbol server and mapped into memory, **!chkimg** moves the image of the file on the symbol server. However, if you use the **-nar** option, the image of the file from the server is not moved.

The executable image that is already in memory (that is, the one that is being scanned) is moved, because the debugger always relocates images that it loads.

This switch is useful only if the operating system already moved the original image. If the image has not been moved, **!chkimg** and the debugger will move the image. Use of this switch is rare.

<span id="-ss_SectionName_"></span><span id="-ss_sectionname_"></span><span id="-SS_SECTIONNAME_"></span>**-ss** **** *SectionName*   
Limits the scan to those sections whose names contain the string *SectionName*. The scan will include any non-discardable section whose name contains this string. *SectionName* is case sensitive and cannot exceed 8 characters.

<span id="-as"></span><span id="-AS"></span>**-as**  
Causes the scan to include all sections of the image except discardable sections. By default, (if you do not use **-as** or **-ss**), the scan skips sections that are writeable, sections that are not executable, sections that have "PAGE" in their name, and discardable sections.

<span id="-r_StartAddress_EndAddress__"></span><span id="-r_startaddress_endaddress__"></span><span id="-R_STARTADDRESS_ENDADDRESS__"></span>**-r** **** *StartAddress* **** *EndAddress*   
Limits the scan to the memory range that begins with *StartAddress* and ends with *EndAddress*. Within this range, any sections that would typically be scanned are scanned. If a section partially overlaps with this range, only that part of the section that overlaps with this range is scanned. The scan is limited to this range even if you also use the **-as** or **-ss** switch.

<span id="-nospec"></span><span id="-NOSPEC"></span>**-nospec**  
Causes the scan to include the reserved sections of Hal.dll and Ntoskrnl.exe. By default, **!chkimg** does not check certain parts of these files.

<span id="-noplock"></span><span id="-NOPLOCK"></span>**-noplock**  
Displays areas that mismatch by having a byte value of 0x90 (a **nop** instruction) and a byte value of 0xF0 (a **lock** instruction). By default, these mismatches are not displayed.

<span id="-np"></span><span id="-NP"></span>**-np**  
Causes patched instructions to be recognized.

<span id="-d"></span><span id="-D"></span>**-d**  
Displays a summary of all mismatched areas while the scan is occurring. For more information about this summary text, see the Remarks section.

<span id="-db"></span><span id="-DB"></span>**-db**  
Displays mismatched areas in a format that is similar to the [**db debugger command**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md). Therefore, each display line shows the address of the first byte in the line, followed by up to 16 hexadecimal byte values. The byte values are immediately followed by the corresponding ASCII values. All nonprintable characters, such as carriage returns and line feeds, are displayed as periods (.). The mismatched bytes are marked by an asterisk (\*).

<span id="-lo_lines"></span><span id="-LO_LINES"></span>**-lo** **** *lines*  
Limits the number of output lines that **-d** or **-db** display to the lines number of lines.

<span id="-v"></span><span id="-V"></span>**-v**  
Displays verbose information.

<span id="_______-mmw______"></span><span id="_______-MMW______"></span> **-mmw**   
Creates a log file and records the activity of **!chkimg** in this file. Each line of the log file represents a single mismatch.

<span id="_______LogFile______"></span><span id="_______logfile______"></span><span id="_______LOGFILE______"></span> *LogFile*   
Specifies the full path of the log file. If you specify a relative path, the path is relative to the current path.

<span id="_______LogOptions______"></span><span id="_______logoptions______"></span><span id="_______LOGOPTIONS______"></span> *LogOptions*   
Specifies the contents of the log file. *LogOptions* is a string that consists of a concatenation of various letters. Each line in the log file contains several columns that are separated by commas. These columns include the items that the following option letters specify, in the order that the letters appear in the *LogOptions* string. You can include the following options multiple times. You must include at least one option.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Log option</th>
<th align="left">Information included in the log file</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>v</p></td>
<td align="left"><p>The virtual address of the mismatch</p></td>
</tr>
<tr class="even">
<td align="left"><p>r</p></td>
<td align="left"><p>The offset (relative address) of the mismatch within the module</p></td>
</tr>
<tr class="odd">
<td align="left"><p>s</p></td>
<td align="left"><p>The symbol that corresponds to the address of the mismatch</p></td>
</tr>
<tr class="even">
<td align="left"><p>S</p></td>
<td align="left"><p>The name of the section that contains the mismatch</p></td>
</tr>
<tr class="odd">
<td align="left"><p>e</p></td>
<td align="left"><p>The correct value that was expected at the mismatch location</p></td>
</tr>
<tr class="even">
<td align="left"><p>w</p></td>
<td align="left"><p>The incorrect value that was at the mismatch location</p></td>
</tr>
</tbody>
</table>

 

*LogOptions* can also include some, or none, of the following additional options.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Log option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>o</p></td>
<td align="left"><p>If a file that has the name <em>LogFile</em> already exists, the existing file is overwritten. By default, the debugger appends new information to the end of any existing file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>t<em>String</em></p></td>
<td align="left"><p>Adds an extra column to the log file. Each entry in this column contains <em>String</em>. The <strong>t</strong><em>String</em> option is useful if you are appending new information to an existing log file and you have to distinguish the new records from the old. You cannot add space between <strong>t</strong> and <em>String</em>. If you use the <strong>t</strong>I<em>String</em> option, it must be the final option in <em>LogOptions</em>, because <em>String</em> is taken to include all of the characters that are present before the next space.</p></td>
</tr>
</tbody>
</table>

 

For example, if *LogOptions* is **rSewo**, each line of the log file contains the relative address and section name of the mismatch location and the expected and actual values at that location. This option also causes any previous file to be overwritten. You can use the **-mmw** switch multiple times if you want to create several log files that have different options. You can create up to 10 log files at the same time.

<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the module to check. *Module* can be the name of the module, the starting address of the module, or any address that is contained in the module. If you omit *Module*, the debugger uses the module that contains the current instruction pointer.

<span></span>  

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When you use **!chkimg**, it compares the image of an executable file in memory to the copy of the file that resides on a symbol store.

All sections of the file are compared, except for sections that are discardable, that are writeable, that are not executable, that have "PAGE" in their name, or that are from INITKDBG. You can change this behavior can by using the **-ss**, **-as**, or **-r** switches.

**!chkimg** displays any mismatch between the image and the file as an image error, with the following exceptions:

-   Addresses that are occupied by the Import Address Table (IAT) are not checked.

-   Certain specific addresses in Hal.dll and Ntoskrnl.exe are not checked, because certain changes occur when these sections are loaded. To check these addresses, include the **-nospec** option.

-   If the byte value 0x90 is present in the file, and if the value 0xF0 is present in the corresponding byte of the image (or vice versa), this situation is considered a match. Typically, the symbol server holds one version of a binary that exists in both uniprocessor and multiprocessor versions. On an x86-based processor, the **lock** instruction is 0xF0, and this instruction corresponds to a **nop** (0x90) instruction in the uniprocessor version. If you want **!chkimg** to display this pair as a mismatch, set the **-noplock** option.

**Note**   If you use the **-f** option to fix image mismatches, **!chkimg** fixes only those mismatches that it considers to be errors. For example, **!chkimg** does not change an 0x90 byte to an 0xF0 byte unless you include **-noplock**.

 

When you include the **-d** option, **!chkimg** displays a summary of all mismatched areas while the scan is occurring. Each mismatch is displayed on two lines. The first line includes the start of the range, the end of the range, the size of the range, the symbol name and offset that corresponds to the start of the range, and the number of bytes since the last error (in parentheses). The second line is enclosed in brackets and includes the hexadecimal byte values that were expected, a colon, and then the hexadecimal byte values that were actually encountered in the image. If the range is longer than 8 bytes, only the first 8 bytes are shown before the colon and after the colon. The following example shows this situation.

```dbgcmd
be000015-be000016  2 bytes - win32k!VeryUsefulFunction+15 (0x8)
     [ 85 dd:95 23 ]
```

Occasionally, a driver alters part of the Microsoft Windows kernel by using hooks, redirection, or other methods. Even a driver that is no longer on the stack might have altered part of the kernel. You can use the **!chkimg** extension as a file comparison tool to determine which parts of the Windows kernel (or any other image) are being altered by drivers and exactly how the parts are being changed. This comparison is most effective on full dump files.

You can also use **!chkimg** together with the [**!for\_each\_module**](-for-each-module.md) extension to check the image of each loaded module. The following example shows this situation.

```dbgcmd
!for_each_module !chkimg @#ModuleName 
```

Suppose that you encounter a bug check, for example, and begin by using [**!analyze**](-analyze.md).

```dbgcmd
kd> !analyze 
....
BugCheck 1000008E, {c0000005, bf920e48, baf75b38, 0}
Probably caused by : memory_corruption
CHKIMG_EXTENSION: !chkimg !win32k
....
```

In this example, the [**!analyze**](-analyze.md) output suggests that memory corruption has occurred and includes a CHKIMG\_EXTENSION line that suggests that Win32k.sys could be the corrupted module. (Even if this line is not present, you might consider possible corruption in the module on top of the stack.) Start by using **!chkimg** without any switches, as the following example shows.

```dbgcmd
kd> !chkimg win32k
Number of different bytes for win32k: 31
```

The following example shows that there are indeed memory corruptions. Use **!chkimg -d** to display all of the errors for the Win32k module.

```dbgcmd
kd> !chkimg win32k -d
    bf920e40-bf920e46  7 bytes - win32k!HFDBASIS32::vSteadyState+1f
        [ 78 08 d3 78 0c c2 04:00 00 00 00 00 01 00 ]
    bf920e48-bf920e5f  24 bytes - win32k!HFDBASIS32::vHalveStepSize (+0x08)
        [ 8b 51 0c 8b 41 08 56 8b:00 00 00 00 00 00 00 00 ]
Number of different bytes for win32k: 31
```

When you try to disassemble the corrupted image of the second section that is listed, the following output might occur.

```dbgcmd
kd> u  win32k!HFDBASIS32::vHalveStepSize
win32k!HFDBASIS32::vHalveStepSize:
bf920e48 0000             add     [eax],al
bf920e4a 0000             add     [eax],al
bf920e4c 0000             add     [eax],al
bf920e4e 0000             add     [eax],al
bf920e50 7808            js win32k!HFDBASIS32::vHalveStepSize+0x12 (bf920e5a)
bf920e52 d3780c           sar     dword ptr [eax+0xc],cl
bf920e55 c20400           ret     0x4
bf920e58 8b510c           mov     edx,[ecx+0xc]
```

Then, use **!chkimg -f**to fix the memory corruption.

```dbgcmd
kd> !chkimg win32k -f
Warning: Any detected errors will be fixed to what we expect!
Number of different bytes for win32k: 31 (fixed)
```

Now you can disassemble the corrected view and see the changes that you have made.

```dbgcmd
kd> u  win32k!HFDBASIS32::vHalveStepSize
win32k!HFDBASIS32::vHalveStepSize:
bf920e48 8b510c           mov     edx,[ecx+0xc]
bf920e4b 8b4108           mov     eax,[ecx+0x8]
bf920e4e 56               push    esi
bf920e4f 8b7104           mov     esi,[ecx+0x4]
bf920e52 03c2             add     eax,edx
bf920e54 c1f803           sar     eax,0x3
bf920e57 2bf0             sub     esi,eax
bf920e59 d1fe             sar     esi,1
```

 

 





