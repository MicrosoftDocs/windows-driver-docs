---
title: D3DKMT_WDDM_2_0_CAPS Structure
description: Learn about the D3DKMT\_WDDM\_2\_0\_CAPS structure, which is reserved for system use. Do not use in your driver.
keywords: ["D3DKMT_WDDM_2_0_CAPS structure Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- D3DKMT_WDDM_2_0_CAPS
api_location:
- D3dkmdt.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# D3DKMT\_WDDM\_2\_0\_CAPS structure


Reserved for system use. Do not use in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _D3DKMT_WDDM_2_0_CAPS {
  union {
    struct {
      UINT Support64BitAtomics  :1;
      UINT GpuMmuSupported  :1;
      UINT IoMmuSupported  :1;
      UINT Reserved  :29;
    };
    UINT   Value;
  };
} D3DKMT_WDDM_2_0_CAPS;
```

## Members

**Support64BitAtomics**

**GpuMmuSupported**

**IoMmuSupported**

**Reserved**

**Value**

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmdt.h (include D3dkmddi.h)</td>
</tr>
</tbody>
</table>

 

 





