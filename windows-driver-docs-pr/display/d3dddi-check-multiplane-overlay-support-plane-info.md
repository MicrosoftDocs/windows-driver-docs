---
title: D3DDDI\_CHECK\_MULTIPLANE\_OVERLAY\_SUPPORT\_PLANE\_INFO structure
description: Specifies the support attributes that the hardware provides for multiplane overlays.
ms.assetid: dda53c24-bd3d-4476-bbb4-b00b0d8aeb3d
keywords: ["D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO
api_location:
- D3dumddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DDDI\_CHECK\_MULTIPLANE\_OVERLAY\_SUPPORT\_PLANE\_INFO structure


Specifies the support attributes that the hardware provides for multiplane overlays.

Syntax
------

```ManagedCPlusPlus
typedef struct D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO {
  HANDLE                               hResource;
  UINT                                 SubResourceIndex;
  D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES PlaneAttributes;
} D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO;
```

Members
-------

**hResource**
A handle to the resource. The display miniport driver must set this member to a value that it can use to refer to its private tracking structure for the resource.

**SubResourceIndex**
The zero-based index into the resource, which is specified by the handle in the **hResource** member. This index indicates the subresource, or surface, on which an overlay plane is to be displayed.

**PlaneAttributes**
A [**D3DDDI\_MULTIPLANE\_OVERLAY\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/hh780234) structure that specifies overlay plane attributes.

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
<td align="left">D3dumddi.h (include D3d10umddi.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**D3DDDI\_MULTIPLANE\_OVERLAY\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/hh780234)

 

 






