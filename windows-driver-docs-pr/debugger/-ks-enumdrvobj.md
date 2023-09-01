---
title: ks.enumdrvobj
description: The ks.enumdrvobj extension displays all KSDEVICE structures associated with a given WDM driver object, and lists the filter types and filters currently instantiated on these devices.
keywords: ["ks.enumdrvobj Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ks.enumdrvobj
api_type:
- NA
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

 

### Additional Information

For more information, see [Kernel Streaming Debugging](kernel-streaming-debugging.md).

## Remarks

Since **!ks.enumdrvobj** enumerates every device chained off a WDM driver object, it is equivalent to invoking [**!ks.enumdevobj**](-ks-enumdevobj.md) on every device chained off a given driver.

 

 





