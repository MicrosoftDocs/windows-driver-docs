---
title: ih
description: The ih extension displays the interrupt history record for the specified processor.
ms.assetid: 4c81bde4-da8b-4c44-8013-6c586c08e22b
keywords: ["interrupt history record", "ih Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ih
api_type:
- NA
ms.localizationpriority: medium
---

# !ih


The **!ih** extension displays the interrupt history record for the specified processor.

```dbgcmd
!ih Processor
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies a processor. If *Processor* is omitted, the current processor is used.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

This extension command can only be used with an Itanium-based target computer.

Remarks
-------

This extension displays the interrupt history record without referencing the program counter symbols. To display the interrupt history record using the program counter symbols, use the [**!ihs**](-ihs.md) extension. To enable the interrupt history record, add **/configflag=32** to the boot entry options.

Here is an example of the output from this extension:

```dbgcmd
kd> !ih
Total # of interruptions = 2093185
Vector              IIP                   IPSR          ExtraField 
 VHPT FAULT  e0000000830d3190      1010092a6018  IFA=      6fc00a0200c 
        VHPT FAULT  e0000000830d33d0      1010092a6018  IFA= 1ffffe00001de2d0 
 VHPT FAULT  e0000000830d33d0      1010092a6018  IFA= 1ffffe01befff338 
        VHPT FAULT  e0000000830d3190      1010092a6018  IFA=      6fc00a0200c 
        VHPT FAULT  e0000000830d33d0      1010092a6018  IFA= 1ffffe00001d9188 
        VHPT FAULT  e0000000830d3880      1010092a6018  IFA= 1ffffe01befff250 
        VHPT FAULT  e0000000830d3fb0      1010092a6018  IFA= e0000165f82dc1c0 
 VHPT FAULT  e000000083063390      1010092a6018  IFA= e0000000fffe0018 
     THREAD SWITCH  e000000085896040  e00000008588c040  OSP= e0000165f82dbd40 
        VHPT FAULT  e00000008329b130      1210092a6018  IFA= e0000165f7edaf30 
        VHPT FAULT  e0000165f7eda640      1210092a6018  IFA= e0000165fff968a9 
    PROCESS SWITCH  e0000000818bbe10  e000000085896040  OSP= e0000165f8281de0 
        VHPT FAULT  e00000008307cfc0      1010092a2018  IFA= e00000008189fe50 
EXTERNAL INTERRUPT  e0000000830623b0      1010092a6018  IVR=               d0 
        VHPT FAULT  e00000008314e310      1010092a2018  IFA= e0000165f88203f0 
        VHPT FAULT  e000000083580760      1010092a2018  IFA= e0000000f00ff3fd 
    PROCESS SWITCH  e00000008558c990  e0000000818bbe10  OSP= e00000008189fe20 
        VHPT FAULT  e00000008307cfc0      1010092a2018  IFA= e0000165f02433f0 
        VHPT FAULT          77cfbda0      1013082a6018  IFA=         77cfbda0 
 VHPT FAULT          77cfbdb0      1213082a6018  IFA=      6fbfee0ff98 
   DATA ACCESS BIT          77b8e150      1213082a6018  IFA=         77c16ab8 
        VHPT FAULT          77ed5d60      1013082a6018  IFA=      6fbfffa6048 
   DATA ACCESS BIT          77ed5d60      1213082a6018  IFA=         77c229c0 
 DATA ACCESS BIT          77b8e1b0      1013082a6018  IFA=         77c1c320 
      USER SYSCALL          77cafa40        10082a6018  Num=               42 
 VHPT FAULT  e00000008344dc20      1010092a6018  IFA= e000010600703784 
...
```

 

 





