---
title: OUTPUTDUPL_CONTEXT_DEBUG_INFO Structure
description: Learn about the OUTPUTDUPL\_CONTEXT\_DEBUG\_INFO structure, which is reserved for system use. Do not use in your driver.
keywords: ["OUTPUTDUPL_CONTEXT_DEBUG_INFO structure Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- OUTPUTDUPL_CONTEXT_DEBUG_INFO
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.date: 01/05/2018
---

# OUTPUTDUPL\_CONTEXT\_DEBUG\_INFO structure


Reserved for system use. Do not use in your driver.

## Syntax

```ManagedCPlusPlus
typedef struct _OUTPUTDUPL_CONTEXT_DEBUG_INFO {
  OUTPUTDUPL_CONTEXT_DEBUG_STATUS Status;
  HANDLE                          ProcessID;
  UINT32                          AccumulatedPresents;
  LARGE_INTEGER                   LastPresentTime;
  LARGE_INTEGER                   LastMouseTime;
  CHAR                            ProcessName[DXGK_DIAG_PROCESS_NAME_LENGTH];
} OUTPUTDUPL_CONTEXT_DEBUG_INFO;
```

## Members

**Status**

**ProcessID**

**AccumulatedPresents**

**LastPresentTime**

**LastMouseTime**

**ProcessName**

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmthk.h (include D3dkmthk.h)</td>
</tr>
</tbody>
</table>

 

 





