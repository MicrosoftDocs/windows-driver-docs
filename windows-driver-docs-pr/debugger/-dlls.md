---
title: dlls
description: The dlls extension displays the table entries of all loaded modules or all modules that a specified thread or process are using.
ms.assetid: a47ec828-ba5a-4f0d-be85-18633c4e4185
keywords: ["DLL table entry", "dlls Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dlls
api_type:
- NA
ms.localizationpriority: medium
---

# !dlls


The **!dlls** extension displays the table entries of all loaded modules or all modules that a specified thread or process are using.

```dbgcmd
!dlls [Options] [LoaderEntryAddress] 
!dlls -h
```

## <span id="ddk__dlls_dbg"></span><span id="DDK__DLLS_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies the level of output. This parameter can be any combination of the following values:

<span id="-f"></span><span id="-F"></span>**-f**  
Displays file headers.

<span id="-s"></span><span id="-S"></span>**-s**  
Displays section headers.

<span id="-a"></span><span id="-A"></span>**-a**  
Displays complete module information. (This option is equivalent to -f -s.)

<span id="-c_ModuleAddress"></span><span id="-c_moduleaddress"></span><span id="-C_MODULEADDRESS"></span>**-c** **** *ModuleAddress*  
Displays the module that contains *ModuleAddress*.

<span id="-i"></span><span id="-I"></span>**-i**  
Sorts the display by initialization order.

<span id="-l"></span><span id="-L"></span>**-l**  
Sorts the display by load order. This situation is the default.

<span id="-m"></span><span id="-M"></span>**-m**  
Sorts the display by memory order.

<span id="-v"></span><span id="-V"></span>**-v**  
(Windows XP and later) Displays version information. This information is taken from the resource section of each module.

<span id="_______LoaderEntryAddress______"></span><span id="_______loaderentryaddress______"></span><span id="_______LOADERENTRYADDRESS______"></span> *LoaderEntryAddress*   
Specifies the address of the loader entry for a module. If you include this parameter, the debugger displays only this specific module.

<span id="_______-h______"></span><span id="_______-H______"></span> **-h**   
Displays some Help text for this extension in the [Debugger Command window](debugger-command-window.md).

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Kdextx86.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Exts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The module listing includes all entry points into each module.

The **.dlls** extension works only in live debugging (not with crash dump analysis).

In kernel mode, this extension displays the modules for the current [process context](changing-contexts.md#process-context). You cannot use **!dlls** together with a system process or the idle process.

The following examples shows you how to use the **!dlls** extension.

```dbgcmd
kd> !dlls -c 77f60000
Dump dll containing 0x77f60000:

0x00091f38: E:\WINDOWS\System32\ntdll.dll
      Base   0x77f60000  EntryPoint  0x00000000  Size        0x00097000
      Flags  0x00004004  LoadCount   0x0000ffff  TlsIndex    0x00000000
             LDRP_IMAGE_DLL
             LDRP_ENTRY_PROCESSED

kd> !dlls -a 91ec0

0x00091ec0: E:\WINDOWS\system32\winmine.exe
      Base   0x01000000  EntryPoint  0x01003e2e  Size        0x00020000
      Flags  0x00005000  LoadCount   0x0000ffff  TlsIndex    0x00000000
             LDRP_LOAD_IN_PROGRESS
             LDRP_ENTRY_PROCESSED

File Type: EXECUTABLE IMAGE
FILE HEADER VALUES
     14C machine (i386)
       3 number of sections
3A98E856 time date stamp Sun Feb 25 03:11:18 2001

       0 file pointer to symbol table
       0 number of symbols
      E0 size of optional header
     10F characteristics
            Relocations stripped
            Executable
            Line numbers stripped
            Symbols stripped
            32 bit word machine

OPTIONAL HEADER VALUES
     10B magic #
    7.00 linker version
    3A00 size of code
   19E00 size of initialized data
       0 size of uninitialized data
    3E2E address of entry point
    1000 base of code
         ----- new -----
01000000 image base
    1000 section alignment
     200 file alignment
       2 subsystem (Windows GUI)
    5.01 operating system version
    5.01 image version
    4.00 subsystem version
   20000 size of image
     400 size of headers
   21970 checksum
00040000 size of stack reserve
00001000 size of stack commit
00100000 size of heap reserve
00001000 size of heap commit
01000100 Opt Hdr
       0 [       0] address [size] of Export Directory
    40B4 [      B4] address [size] of Import Directory
    6000 [   19170] address [size] of Resource Directory
       0 [       0] address [size] of Exception Directory
       0 [       0] address [size] of Security Directory
       0 [       0] address [size] of Base Relocation Directory
    11B0 [      1C] address [size] of Debug Directory
       0 [       0] address [size] of Description Directory
       0 [       0] address [size] of Special Directory
       0 [       0] address [size] of Thread Storage Directory
       0 [       0] address [size] of Load Configuration Directory
     258 [      A8] address [size] of Bound Import Directory
    1000 [     1B0] address [size] of Import Address Table Directory
       0 [       0] address [size] of Reserved Directory
       0 [       0] address [size] of Reserved Directory
       0 [       0] address [size] of Reserved Directory


SECTION HEADER #1
   .text name
    3992 virtual size
    1000 virtual address
    3A00 size of raw data
     400 file pointer to raw data
       0 file pointer to relocation table
       0 file pointer to line numbers
       0 number of relocations
       0 number of line numbers
60000020 flags
         Code
         (no align specified)
         Execute Read


Debug Directories(1)
        Type       Size     Address  Pointer

        cv           1c        13d0      7d0    Format: NB10, 3a98e856, 1, winmi
ne.pdb

SECTION HEADER #2
   .data name
     BB8 virtual size
    5000 virtual address
     200 size of raw data
    3E00 file pointer to raw data
       0 file pointer to relocation table
       0 file pointer to line numbers
       0 number of relocations
       0 number of line numbers
C0000040 flags
         Initialized Data
         (no align specified)
         Read Write

SECTION HEADER #3
   .rsrc name
   19170 virtual size
    6000 virtual address
   19200 size of raw data
    4000 file pointer to raw data
       0 file pointer to relocation table
       0 file pointer to line numbers
       0 number of relocations
       0 number of line numbers
40000040 flags
         Initialized Data
         (no align specified)
         Read Only
```

 

 





