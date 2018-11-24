---
title: DXGK\_INTERFACESPECIFICDATA structure
description: The DXGK\_INTERFACESPECIFICDATA structure is reserved for system use. Do not use it in your driver.
ms.assetid: dc9ad39c-4439-4e01-9825-fc1df3c3adc0
keywords: ["DXGK_INTERFACESPECIFICDATA structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_INTERFACESPECIFICDATA
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGK\_INTERFACESPECIFICDATA structure


The DXGK\_INTERFACESPECIFICDATA structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_INTERFACESPECIFICDATA {
  HANDLE                     hAdapter;
  DXGKCB_GETHANDLEDATA       pfnGetHandleDataCb;
  DXGKCB_GETHANDLEPARENT     pfnGetHandleParentCb;
  DXGKCB_ENUMHANDLECHILDREN  pfnEnumHandleChildrenCb;
  DXGKCB_NOTIFY_INTERRUPT    pfnNotifyInterruptCb;
  DXGKCB_NOTIFY_DPC          pfnNotifyDpcCb;
  DXGKCB_QUERYVIDPNINTERFACE pfnQueryVidPnInterfaceCb;
  DXGKCB_GETCAPTUREADDRESS   pfnGetCaptureAddressCb;
} DXGK_INTERFACESPECIFICDATA;
```

Members
-------

**hAdapter**
Reserved for system use.

**pfnGetHandleDataCb**
Reserved for system use.

**pfnGetHandleParentCb**
Reserved for system use.

**pfnEnumHandleChildrenCb**
Reserved for system use.

**pfnNotifyInterruptCb**
Reserved for system use.

**pfnNotifyDpcCb**
Reserved for system use.

**pfnQueryVidPnInterfaceCb**
Reserved for system use.

**pfnGetCaptureAddressCb**
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
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmddi.h (include D3dkmddi.h)</td>
</tr>
</tbody>
</table>

 

 





