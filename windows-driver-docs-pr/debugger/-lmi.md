---
title: lmi
description: The lmi extension displays detailed information about a module.
ms.assetid: 00438edf-618a-401e-818f-24add7861487
keywords: ["lmi Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- lmi
api_type:
- NA
---

# !lmi


The **!lmi** extension displays detailed information about a module.

``` syntax
!lmi Module
```

## <span id="ddk__lmi_dbg"></span><span id="DDK__LMI_DBG"></span>Parameters


<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies a loaded module, either by name or by base address.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Module addresses can be determined by using the [**lm (List Loaded Modules)**](lm--list-loaded-modules-.md) command.

The **!lmi** extension analyzes the module headers and displays a formatted summary of the information therein. If the module headers are paged out, an error message is displayed. To see a more extensive display of header information, use the [**!dh**](-dh.md) extension command.

This command shows a number of fields, each with a different title. Some of these titles have specific meanings:

-   The **Image Name** field shows the name of the executable file, including the extension. Typically, the full path is included in user mode but not in kernel mode.

-   The **Module** field shows the *module name*. This is usually just the file name without the extension. In a few cases, the module name differs significantly from the file name.

-   The **Symbol Type** field shows information about the debugger's attempts to load this module's symbols. For an explanation of the various status values, see [Symbol Status Abbreviations](symbol-status-abbreviations.md). If symbols have been loaded, the symbol file name follows this.

-   The first address in the module is shown as **Base Address**. The size of the module is shown as **Size**. Thus, if **Base Address** is "faab4000" and **Size** is "2000", the module extends from 0xFAAB4000 to 0xFAAB5FFF, inclusive.

Here is an example:

``` syntax
0:000> lm 
start    end        module name
00400000 0042d000   Prymes     C (pdb symbols)              Prymes.pdb
77e80000 77f35000   KERNEL32     (export symbols)           C:\WINNT\system32\KERNEL32.dll
77f80000 77ffb000   ntdll        (export symbols)           ntdll.dll

0:000> !lmi 00400000
Loaded Module Info: [00400000] 
         Module: Prymes
   Base Address: 00400000
     Image Name: Prymes.exe
   Machine Type: 332 (I386)
     Time Stamp: 3c76c346 Fri Feb 22 14:16:38 2002
           Size: 2d000
       CheckSum: 0
Characteristics: 230e stripped 
Debug Data Dirs: Type Size     VA  Pointer
                 MISC  110,     0,   77a00 [Data not mapped]
    Symbol Type: EXPORT   - PDB not found
    Load Report: export symbols
```

For an explanation of the abbreviations shown on the **Characteristics** line of this example, see [Symbol Status Abbreviations](symbol-status-abbreviations.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!lmi%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




