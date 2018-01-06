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
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO%20structure%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





