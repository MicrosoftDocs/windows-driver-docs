---
title: D3DKMT_WDDM_1_3_CAPS Structure
description: Learn about the D3DKMT\_WDDM\_1\_3\_CAPS structure, which is reserved for system use. Do not use in your driver.
keywords: ["D3DKMT_WDDM_1_3_CAPS structure Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- D3DKMT_WDDM_1_3_CAPS
api_location:
- D3dkmdt.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# D3DKMT\_WDDM\_1\_3\_CAPS structure


Reserved for system use. Do not use in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _D3DKMT_WDDM_1_3_CAPS {
  union {
    struct {
      UINT SupportMiracast  :1;
      UINT IsHybridIntegratedGPU  :1;
      UINT IsHybridDiscreteGPU  :1;
      UINT SupportPowerManagementPStates  :1;
      UINT Reserved  :28;
    };
  };
} D3DKMT_WDDM_1_3_CAPS;
```

## Members

**SupportMiracast**

**IsHybridIntegratedGPU**

**IsHybridDiscreteGPU**

**SupportPowerManagementPStates**

**Reserved**

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
<td align="left">D3dkmdt.h (include D3dkmdt.h)</td>
</tr>
</tbody>
</table>

 

 





