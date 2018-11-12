---
title: ks.enumdrvobj
description: The ks.enumdrvobj extension displays all KSDEVICE structures associated with a given WDM driver object, and lists the filter types and filters currently instantiated on these devices.
ms.assetid: 8fcb8c83-48b6-402a-8374-6b1f0314837e
keywords: ["ks.enumdrvobj Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ks.enumdrvobj
api_type:
- NA
ms.localizationpriority: medium
---

# !ks.enumdrvobj


The **!ks.enumdrvobj** extension displays all KSDEVICE structures associated with a given WDM driver object, and lists the filter types and filters currently instantiated on these devices.

```dbgcmd
!ks.enumdrvobj DriverObject
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______DriverObject______"></span><span id="_______driverobject______"></span><span id="_______DRIVEROBJECT______"></span> *DriverObject*   
Specifies a pointer to a WDM driver object.

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

Since **!ks.enumdrvobj** enumerates every device chained off a WDM driver object, it is equivalent to invoking [**!ks.enumdevobj**](-ks-enumdevobj.md) on every device chained off a given driver.

 

 





