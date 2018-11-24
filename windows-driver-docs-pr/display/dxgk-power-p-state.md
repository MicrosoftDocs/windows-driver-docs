---
title: DXGK\_POWER\_P\_STATE structure
description: Reserved for system use. Do not use it in your driver.
ms.assetid: F4612284-36C8-49C4-914D-43C32489EABD
keywords: ["DXGK_POWER_P_STATE structure Display Devices", "PDXGK_POWER_P_STATE structure pointer Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_POWER_P_STATE
api_location:
- D3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGK\_POWER\_P\_STATE structure


Reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_POWER_P_STATE {
  ULONG     NominalPower;
  ULONG     OperatingFrequency;
  ULONGLONG TransitionLatencies[DXGK_MAX_P_STATES];
  ULONGLONG ResidencyRequirement;
} DXGK_POWER_P_STATE, *PDXGK_POWER_P_STATE;
```

Members
-------

**NominalPower**

**OperatingFrequency**

**TransitionLatencies**

**ResidencyRequirement**

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012 R2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmddi.h (include D3dkmddi.h)</td>
</tr>
</tbody>
</table>

 

 





