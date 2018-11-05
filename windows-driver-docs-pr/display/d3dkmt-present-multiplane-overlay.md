---
title: D3DKMT\_PRESENT\_MULTIPLANE\_OVERLAY structure
description: Reserved for system use. Do not use in your driver.
ms.assetid: 2526ccce-826a-4e8f-ab15-639510b1d5cf
keywords: ["D3DKMT_PRESENT_MULTIPLANE_OVERLAY structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_PRESENT_MULTIPLANE_OVERLAY
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMT\_PRESENT\_MULTIPLANE\_OVERLAY structure


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct D3DKMT_PRESENT_MULTIPLANE_OVERLAY {
  union {
    D3DKMT_HANDLE hDevice;
    D3DKMT_HANDLE hContext;
  };
  ULONG                          BroadcastContextCount;
  D3DKMT_HANDLE                  BroadcastContext[D3DDDI_MAX_BROADCAST_CONTEXT];
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           PresentCount;
  D3DDDI_FLIPINTERVAL_TYPE       FlipInterval;
  D3DKMT_PRESENTFLAGS            Flags;
  UINT                           PresentPlaneCount;
  D3DKMT_MULTIPLANE_OVERLAY      *pPresentPlanes;
  UINT                           Duration;
} D3DKMT_PRESENT_MULTIPLANE_OVERLAY;
```

Members
-------

**hDevice**

**hContext**

**BroadcastContextCount**

**BroadcastContext**

**VidPnSourceId**

**PresentCount**

**FlipInterval**

**Flags**

**PresentPlaneCount**

**pPresentPlanes**

**Duration**

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
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmthk.h</td>
</tr>
</tbody>
</table>

 

 





