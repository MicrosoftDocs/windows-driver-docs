---
title: ks.devhdr
description: The ks.devhdr extension displays the kernel streaming device header associated with the given WDM object.
ms.assetid: 1418ccfe-3842-422c-b2ce-124d0019d7b8
keywords: ["ks.devhdr Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ks.devhdr
api_type:
- NA
ms.localizationpriority: medium
---

# !ks.devhdr


The **!ks.devhdr** extension displays the kernel streaming device header associated with the given WDM object.

```dbgcmd
!ks.devhdr DeviceObject 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______DeviceObject______"></span><span id="_______deviceobject______"></span><span id="_______DEVICEOBJECT______"></span> *DeviceObject*   
This parameter specifies a pointer to a WDM device object. If *DeviceObject* is not valid, the command returns an error.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel Streaming Debugging](kernel-streaming-debugging.md).

Remarks
-------

The output from [**!ks.allstreams**](-ks-allstreams.md) can be used as the input for **!ks.devhdr**.

Here is an example of the **!ks.devhdr** display:

```dbgcmd
kd> !devhdr 827aedf0 7
Device Header 824ca1e0
    Child Create Handler List:
        Create Item eb3a7284
            CreateFunction = sysaudio!CFilterInstance::FilterDispatchCreate+0x00 
            ObjectClass = NULL
            Flags = 0
```

 

 





