---
title: errpkt
description: The errpkt extension displays the contents of a Windows Hardware Error Architecture (WHEA) hardware error packet.
ms.assetid: cf4b1dfa-3b15-45d4-b5e2-1da7cdbca350
keywords: ["errpkt Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- errpkt
api_type:
- NA
ms.localizationpriority: medium
---

# !errpkt


The **!errpkt** extension displays the contents of a Windows Hardware Error Architecture (WHEA) hardware error packet.

```dbgcmd
!errpkt Address 
```

## <span id="ddk__ubp_dbg"></span><span id="DDK__UBP_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the hardware error packet.

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
<td align="left"><p><strong>Windows XP</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Windows Server 2003</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows Vista and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

This extension can be used only in Windows Vista and later versions of Windows.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

The [**!whea**](-whea.md) and [**!errrec**](-errrec.md) extensions can be used to display additional WHEA information. For general information about WHEA, see [Windows Hardware Error Architecture (WHEA)](https://go.microsoft.com/fwlink/p/?linkid=153571) in the Windows Driver Kit (WDK) documentation.

Remarks
-------

The following example shows the output of the **!errpkt** extension:

```dbgcmd
3: kd> !errpkt fffffa8007cf44da 
   WHEA Error Packet Info Section (@ fffffa8007cf44da)
   Flags            : 0x00000000
   Size             : 0x218
   RawDataLength    : 0x392
   Context          : 0x0000000000000000
   ErrorType        : 0x0 - Processor
   ErrorSeverity    : 0x1 - Fatal
   ErrorSourceId    : 0x0
   ErrorSourceType  : 0x0 - MCE
   Version          : 00000002
   Cpu              : 0000000000000002
   RawDataFormat    : 0x2 - Intel64 MCA

   Raw Data         : Located @ FFFFFA8007CF45F2

Processor Error: (Internal processor error)
This error means either the processor is damaged or perhaps
voltage and/or temperature thresholds have been exceeded.
If the problem continues to occur, replace the processor.
Processor Number : 2
Bank Number      : 0
   Status  :                0
   Address : 0000000000000000 (I)
   Misc    : 0000000000000000 (I)
```

 

 





