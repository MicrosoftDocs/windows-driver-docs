---
title: ks.enumdevobj
description: The ks.enumdevobj extension displays the KSDEVICE associated with a given WDM device object, and lists the filter types and filters currently instantiated on this device.
ms.assetid: 3730fe3e-df7a-47fd-825b-ef31be6f7620
keywords: ["ks.enumdevobj Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ks.enumdevobj
api_type:
- NA
ms.localizationpriority: medium
---

# !ks.enumdevobj


The **!ks.enumdevobj** extension displays the KSDEVICE associated with a given WDM device object, and lists the filter types and filters currently instantiated on this device.

```dbgcmd
!ks.enumdevobj DeviceObject 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______DeviceObject______"></span><span id="_______deviceobject______"></span><span id="_______DEVICEOBJECT______"></span> *DeviceObject*   
Specifies a pointer to a WDM device object.

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

The output from [**!ks.allstreams**](-ks-allstreams.md) can be used as the input for **!ks.enumdevobj**.

Here is an example of the **!ks.enumdevobj** display:

```dbgcmd
kd> !enumdevobj 8241c020
WDM device object 8241c020:
    Corresponding KSDEVICE        823b8430
    Factory 829782dc [Descriptor f7a233c8] instances:
        829493c4 
```

 

 





