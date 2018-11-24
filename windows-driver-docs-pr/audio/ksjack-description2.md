---
title: KSJACK\_DESCRIPTION2 structure
description: The KSJACK\_DESCRIPTION2 structure specifies the capabilities and the current state of a jack that supports jack presence detection.
ms.assetid: 0db29870-20d0-459b-a531-3dea5d073183
keywords: ["KSJACK_DESCRIPTION2 structure Audio Devices", "PKSJACK_DESCRIPTION2 structure pointer Audio Devices"]
topic_type:
- apiref
api_name:
- KSJACK_DESCRIPTION2
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSJACK\_DESCRIPTION2 structure


The `KSJACK_DESCRIPTION2` structure specifies the capabilities and the current state of a jack that supports jack presence detection.

Syntax
------

```ManagedCPlusPlus
typedef struct _tagKSJACK_DESCRIPTION2 {
  DWORD DeviceStateInfo;
  DWORD JackCapabilities;
} KSJACK_DESCRIPTION2, *PKSJACK_DESCRIPTION2;
```

Members
-------

**DeviceStateInfo**  
Specifies the lower 16 bits of the DWORD parameter. This parameter indicates whether the jack is currently active, streaming, idle, or hardware not ready.

**JackCapabilities**  
Specifies the lower 16 bits of the DWORD parameter. This parameter is a flag and it indicates the capabilities of the jack. This flag can be set to one of the values in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Flag</strong></p></td>
<td align="left"><p><strong>Meaning</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>JACKDESC2_PRESENCE_DETECT_CAPABILITY (0x00000001)</p></td>
<td align="left"><p>Jack supports jack presence detection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>JACKDESC2_DYNAMIC_FORMAT_CHANGE_CAPABILITY (0x00000002)</p></td>
<td align="left"><p>Jack supports dynamic format change.</p></td>
</tr>
</tbody>
</table>

 

For more information about dynamic format change, see [Dynamic Format Change](https://msdn.microsoft.com/library/windows/hardware/ff536371).

Remarks
-------

If an audio device lacks jack presence detection, the **IsConnected** member of the [**KSJACK\_DESCRIPTION**](ksjack-description.md) structure must always be set to **TRUE**. To remove the ambiguity that results from this dual meaning of the **TRUE** value for **IsConnected**, a client application can call [IKsJackDescription2::GetJackDescription2](https://go.microsoft.com/fwlink/p/?linkid=143698) to read the **JackCapabilities** flag of the `KSJACK_DESCRIPTION2` structure. If this flag has the JACKDESC2\_PRESENCE\_DETECT\_CAPABILITY bit set, it indicates that the endpoint does in fact support jack presence detection. In that case, the return value of the **IsConnected** member can be interpreted to accurately reflect the insertion status of the jack.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSJACK\_DESCRIPTION**](ksjack-description.md)

[IKsJackDescription2::GetJackDescription2](https://go.microsoft.com/fwlink/p/?linkid=143698)

 

 






