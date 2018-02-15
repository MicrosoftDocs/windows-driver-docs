---
title: OUTPUTDUPL\_CONTEXT\_DEBUG\_STATUS enumeration
description: Reserved for system use. Do not use in your driver.
ms.assetid: 3720b101-cac4-4f81-ae71-088ab03f8756
keywords: ["OUTPUTDUPL_CONTEXT_DEBUG_STATUS enumeration Display Devices"]
topic_type:
- apiref
api_name:
- OUTPUTDUPL_CONTEXT_DEBUG_STATUS
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

# OUTPUTDUPL\_CONTEXT\_DEBUG\_STATUS enumeration


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef enum _OUTPUTDUPL_CONTEXT_DEBUG_STATUS {
  OUTPUTDUPL_CONTEXT_DEBUG_STATUS_INACTIVE         = 0,
  OUTPUTDUPL_CONTEXT_DEBUG_STATUS_ACTIVE           = 1,
  OUTPUTDUPL_CONTEXT_DEBUG_STATUS_PENDING_DESTROY  = 2,
  OUTPUTDUPL_CONTEXT_DEBUG_STATUS_FORCE_UINT32     = 0xffffffff
} OUTPUTDUPL_CONTEXT_DEBUG_STATUS;
```

Constants
---------

<span id="OUTPUTDUPL_CONTEXT_DEBUG_STATUS_INACTIVE"></span><span id="outputdupl_context_debug_status_inactive"></span>**OUTPUTDUPL\_CONTEXT\_DEBUG\_STATUS\_INACTIVE**

<span id="OUTPUTDUPL_CONTEXT_DEBUG_STATUS_ACTIVE"></span><span id="outputdupl_context_debug_status_active"></span>**OUTPUTDUPL\_CONTEXT\_DEBUG\_STATUS\_ACTIVE**

<span id="OUTPUTDUPL_CONTEXT_DEBUG_STATUS_PENDING_DESTROY"></span><span id="outputdupl_context_debug_status_pending_destroy"></span>**OUTPUTDUPL\_CONTEXT\_DEBUG\_STATUS\_PENDING\_DESTROY**

<span id="OUTPUTDUPL_CONTEXT_DEBUG_STATUS_FORCE_UINT32"></span><span id="outputdupl_context_debug_status_force_uint32"></span>**OUTPUTDUPL\_CONTEXT\_DEBUG\_STATUS\_FORCE\_UINT32**

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20OUTPUTDUPL_CONTEXT_DEBUG_STATUS%20enumeration%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




