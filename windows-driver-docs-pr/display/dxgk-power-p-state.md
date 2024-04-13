---
title: DXGK_POWER_P_STATE Structure
description: Learn about the DXGK\_POWER\_P\_STATE structure, which is reserved for system use. Do not use it in your driver.
keywords: ["DXGK_POWER_P_STATE structure Display Devices", "PDXGK_POWER_P_STATE structure pointer Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DXGK_POWER_P_STATE
api_location:
- D3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# DXGK\_POWER\_P\_STATE structure


Reserved for system use. Do not use it in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _DXGK_POWER_P_STATE {
  ULONG     NominalPower;
  ULONG     OperatingFrequency;
  ULONGLONG TransitionLatencies[DXGK_MAX_P_STATES];
  ULONGLONG ResidencyRequirement;
} DXGK_POWER_P_STATE, *PDXGK_POWER_P_STATE;
```

## Members

**NominalPower**

**OperatingFrequency**

**TransitionLatencies**

**ResidencyRequirement**

## Requirements

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

 

 





