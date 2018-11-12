---
title: vad
description: The vad extension displays details of a virtual address descriptor (VAD) or a tree of VADs.
ms.assetid: 96bd5a38-016d-4ce9-b128-cc730577be45
keywords: ["virtual address descriptor (VAD)", "VAD (virtual address descriptor)", "addresses, virtual address descriptor (VAD)", "vad Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- vad
api_type:
- NA
ms.localizationpriority: medium
---

# !vad


The **!vad** extension displays details of a virtual address descriptor (VAD) or a tree of VADs.

-   Displays details of one virtual addres descriptor (VAD)
-   Displays details of a tree of VADs.
-   Displays information about the VADs for a particular user-mode module and provides a string that you can use to load the symbols for that module.

```dbgcmd
!vad VAD-Root [Flag]
!vad Address 1
```

## <span id="ddk__vad_dbg"></span><span id="DDK__VAD_DBG"></span>Parameters


<span id="_______VAD-Root______"></span><span id="_______vad-root______"></span><span id="_______VAD-ROOT______"></span> *VAD-Root*   
Address of the root of the VAD tree to be displayed.

<span id="_______Flag______"></span><span id="_______flag______"></span><span id="_______FLAG______"></span> *Flag*   
Specifies the form the display will take. Possible values include:

<span id="0"></span>0  
The entire VAD tree based at *VAD-Root* is displayed. (This is the default.)

<span id="1"></span>1  
Only the VAD specified by *VAD-Root* is displayed. The display will include a more detailed analysis.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Address in the virtual address range of a user-mode module.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 2000</p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about virtual address descriptors, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

The address of the root of the VAD for any process can be found by using the [**!process**](-process.md) command.

The **!vad** command can be helpful when you need to load symbols for a user-mode module that has been paged out of memory. For details, see [Mapping Symbols When the PEB is Paged Out](mapping-symbols-when-the-peb-is-paged-out.md).

Here is an example of the **!vad** extension:

```dbgcmd
kd> !vad 824bc2f8
VAD     level      start      end    commit
82741bf8 ( 1)      78000    78045         8 Mapped  Exe  EXECUTE_WRITECOPY
824ef368 ( 2)      7f6f0    7f7ef         0 Mapped       EXECUTE_READ
824bc2f8 ( 0)      7ffb0    7ffd3         0 Mapped       READONLY
8273e508 ( 2)      7ffde    7ffde         1 Private      EXECUTE_READWRITE
82643fc8 ( 1)      7ffdf    7ffdf         1 Private      EXECUTE_READWRITE

Total VADs:     5  average level:    2  maximum depth: 2

kd> !vad 824bc2f8 1

VAD @ 824bc2f8
  Start VPN:         7ffb0  End VPN:    7ffd3  Control Area:  827f1208
  First ProtoPte: e1008500  Last PTE e100858c  Commit Charge         0 (0.)
  Secured.Flink          0  Blink           0  Banked/Extend:        0 Offset 0
   ViewShare NoChange READONLY

SecNoChange 
```

 

 





