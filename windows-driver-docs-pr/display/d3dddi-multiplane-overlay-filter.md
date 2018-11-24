---
title: D3DDDI\_MULTIPLANE\_OVERLAY\_FILTER structure
description: Reserved for system use. Do not use it in your driver.Note  This structure is available only in the D3dumddi.h header provided with Windows Driver Kit (WDK) Version 8 that shipped with Windows 8. It has been removed from later versions of the header. .
ms.assetid: 56276b78-5550-4d93-8a73-b1183deb54da
keywords: ["D3DDDI_MULTIPLANE_OVERLAY_FILTER structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DDDI_MULTIPLANE_OVERLAY_FILTER
api_location:
- D3dumddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DDDI\_MULTIPLANE\_OVERLAY\_FILTER structure


Reserved for system use. Do not use it in your driver.

&gt; \[!Note\]
&gt;  This structure is available only in the D3dumddi.h header provided with Windows Driver Kit (WDK) Version 8 that shipped with Windows 8. It has been removed from later versions of the header.

 

Syntax
------

```ManagedCPlusPlus
typedef struct _D3DDDI_MULITPLANE_OVERLAY_FILTER {
  D3DDDI_MULTIPLANE_OVERLAY_FILTER_TYPE FilterType;
  BOOL                                  Enabled;
  INT                                   Value;
} D3DDDI_MULTIPLANE_OVERLAY_FILTER;
```

Members
-------

**FilterType**

**Enabled**

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
<td align="left">D3dumddi.h</td>
</tr>
</tbody>
</table>

 

 





