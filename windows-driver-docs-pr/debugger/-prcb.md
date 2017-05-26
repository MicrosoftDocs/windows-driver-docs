---
title: prcb
description: The prcb extension displays the processor control block (PRCB).
ms.assetid: 747695a1-8a5d-4d30-9315-91f4bf7f568e
keywords: ["processor control block", "prcb Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- prcb
api_type:
- NA
---

# !prcb


The **!prcb** extension displays the processor control block (PRCB).

``` syntax
!prcb [Processor]
```

## <span id="ddk__prcb_dbg"></span><span id="DDK__PRCB_DBG"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the processor to retrieve the PRCB information from. If *Processor* is omitted, processor zero will be used.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about the PCR and the PRCB, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

The PRCB is an extension of the processor control region (PCR). To display the PCR, use the [**!pcr**](-pcr.md) extension.

Here is an example:

``` syntax
kd> !prcb
PRCB for Processor 0 at e0000000818ba000:
Threads--  Current e0000000818bbe10 Next 0000000000000000 Idle e0000000818bbe10
Number 0 SetMember 00000001
Interrupt Count -- 0000b81f
Times -- Dpc    00000028 Interrupt 000003ff 
         Kernel 00005ef4 User      00000385 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!prcb%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




