---
title: D3DKMT\_OUTDUPL\_POINTER\_SHAPE\_TYPE enumeration
description: Reserved for system use. Do not use in your driver.
ms.assetid: 50a6cc24-2ac8-435c-8e82-9cd0c02f57e9
keywords: ["D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE enumeration Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# D3DKMT\_OUTDUPL\_POINTER\_SHAPE\_TYPE enumeration


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef enum _D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE {
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME    = 0x00000001,
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_COLOR         = 0x00000002,
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR  = 0x00000004
} D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE;
```

Constants
---------

<span id="D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME"></span><span id="d3dkmt_outdupl_pointer_shape_type_monochrome"></span>**D3DKMT\_OUTDUPL\_POINTER\_SHAPE\_TYPE\_MONOCHROME**

<span id="D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_COLOR"></span><span id="d3dkmt_outdupl_pointer_shape_type_color"></span>**D3DKMT\_OUTDUPL\_POINTER\_SHAPE\_TYPE\_COLOR**

<span id="D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR"></span><span id="d3dkmt_outdupl_pointer_shape_type_masked_color"></span>**D3DKMT\_OUTDUPL\_POINTER\_SHAPE\_TYPE\_MASKED\_COLOR**

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
<td align="left">D3dkmthk.h (include D3dkmthk.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE%20enumeration%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




