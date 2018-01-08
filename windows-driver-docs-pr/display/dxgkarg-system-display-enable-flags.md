---
title: DXGKARG\_SYSTEM\_DISPLAY\_ENABLE\_FLAGS structure
description: Reserved for system use. Do not use it in your driver.
ms.assetid: f23d6692-4c9d-48eb-8d7f-ef70334494b1
keywords: ["DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS structure Display Devices", "PDXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS structure pointer Display Devices"]
topic_type:
- apiref
api_name:
- DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS
api_location:
- Dispmprt.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DXGKARG\_SYSTEM\_DISPLAY\_ENABLE\_FLAGS structure


Reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS {
  union {
    struct {
      UINT Reserved  :32;
    };
    UINT   Value;
  };
} DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS, *PDXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS;
```

Members
-------

**Reserved**
Reserved for system use.

**Value**
Reserved for system use.

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
<td align="left">Dispmprt.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS%20structure%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




