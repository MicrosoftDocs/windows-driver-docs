---
title: D3DKMT\_WDDM\_1\_2\_CAPS structure
description: Reserved for system use. Do not use in your driver.
ms.assetid: 0cd26fad-4772-4631-81fc-da2ddb7dc9a1
keywords: ["D3DKMT_WDDM_1_2_CAPS structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_WDDM_1_2_CAPS
api_location:
- D3dkmdt.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMT\_WDDM\_1\_2\_CAPS structure


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _D3DKMT_WDDM_1_2_CAPS {
  D3DKMDT_PREEMPTION_CAPS PreemptionCaps;
  union {
    struct {
      UINT SupportNonVGA  :1;
      UINT SupportSmoothRotation  :1;
      UINT SupportPerEngineTDR  :1;
      UINT SupportKernelModeCommandBuffer  :1;
      UINT SupportCCD  :1;
      UINT SupportSoftwareDeviceBitmaps  :1;
      UINT SupportGammaRamp  :1;
      UINT SupportHWCursor  :1;
      UINT SupportHWVSync  :1;
      UINT SupportSurpriseRemovalInHibernation  :1;
      UINT Reserved  :22;
    };
    UINT   Value;
  };
} D3DKMT_WDDM_1_2_CAPS;
```

Members
-------

**PreemptionCaps**

**SupportNonVGA**

**SupportSmoothRotation**

**SupportPerEngineTDR**

**SupportKernelModeCommandBuffer**

**SupportCCD**

**SupportSoftwareDeviceBitmaps**

**SupportGammaRamp**

**SupportHWCursor**

**SupportHWVSync**

**SupportSurpriseRemovalInHibernation**

**Reserved**

**Value**

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
<td align="left">D3dkmdt.h (include D3dkmdt.h)</td>
</tr>
</tbody>
</table>

 

 





