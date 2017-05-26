---
title: minipkd.srb
description: The minipkd.srb extension displays the specified SCSI request block (SRB) data structure.
ms.assetid: d742a900-f8a8-43a8-b00a-12bb82ca1460
keywords: ["minipkd.srb Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- minipkd.srb
api_type:
- NA
---

# !minipkd.srb


The **!minipkd.srb** extension displays the specified SCSI request block (SRB) data structure.

``` syntax
    !minipkd.srb SRB 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______SRB______"></span><span id="_______srb______"></span> *SRB*   
Specifies the address of an SRB.

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
<td align="left"><p>Minipkd.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [SCSI Miniport Debugging](scsi-miniport-debugging.md).

Remarks
-------

The addresses of all currently active requests can be found in the *SRB* fields of the output from the [**!minipkd.req**](-minipkd-req.md) command.

This extension displays the status of the SRB, the driver it is addressed to, the SCSI that issued the SRB and its address, and a hexadecimal flag value. If 0x10000 is set in the flag value, this request is currently in the miniport.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!minipkd.srb%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




