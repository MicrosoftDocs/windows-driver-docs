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
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3DDDI_MULTIPLANE_OVERLAY_FILTER%20structure%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




