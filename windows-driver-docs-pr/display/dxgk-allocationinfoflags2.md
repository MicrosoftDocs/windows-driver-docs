---
title: \_DXGK\_ALLOCATIONINFOFLAGS2 structure
description: The DXGK\_ALLOCATIONINFOFLAGS2 structure is reserved for system use. Do not use in your driver.
ms.assetid: 67c27f53-29f0-4639-a360-0dbf7f3b3849
keywords: ["_DXGK_ALLOCATIONINFOFLAGS2 structure Display Devices", "DXGK_ALLOCATIONINFOFLAGS2 structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGK_ALLOCATIONINFOFLAGS2
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# \_DXGK\_ALLOCATIONINFOFLAGS2 structure


The DXGK\_ALLOCATIONINFOFLAGS2 structure is reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGK_ALLOCATIONINFOFLAGS2 {
  union {
    struct {
      UINT CpuVisible;
      UINT ReadOnly;
      UINT PermanentSysMem;
      UINT Cached;
      UINT ExistingSysMem;
      UINT ExistingKernelSysMem;
      UINT Swizzled;
      UINT Overlay;
      UINT Capture;
      UINT SynchronousPaging;
      UINT LinkMirrored;
      UINT LinkInstanced;
      UINT HistoryBuffer  :1;
      UINT Reserved  :2;
      UINT DXGK_ALLOC_RESERVED16  :1;
      UINT DXGK_ALLOC_RESERVED15  :1;
      UINT DXGK_ALLOC_RESERVED14  :1;
      UINT DXGK_ALLOC_RESERVED13  :1;
      UINT DXGK_ALLOC_RESERVED12  :1;
      UINT DXGK_ALLOC_RESERVED11  :1;
      UINT DXGK_ALLOC_RESERVED9  :1;
      UINT DXGK_ALLOC_RESERVED8  :1;
      UINT DXGK_ALLOC_RESERVED7  :1;
      UINT DXGK_ALLOC_RESERVED6  :1;
      UINT DXGK_ALLOC_RESERVED5  :1;
      UINT DXGK_ALLOC_RESERVED4  :1;
      UINT DXGK_ALLOC_RESERVED3  :1;
      UINT DXGK_ALLOC_RESERVED2  :1;
      UINT DXGK_ALLOC_RESERVED1  :1;
      UINT DXGK_ALLOC_RESERVED0  :1;
    };
    UINT Value;
  };
} DXGK_ALLOCATIONINFOFLAGS2;
```

Members
-------

**CpuVisible**

**ReadOnly**

**PermanentSysMem**

**Cached**

**ExistingSysMem**

**ExistingKernelSysMem**

**Swizzled**

**Overlay**

**Capture**

**SynchronousPaging**

**LinkMirrored**

**LinkInstanced**

**HistoryBuffer**

**Reserved**

**DXGK\_ALLOC\_RESERVED16**

**DXGK\_ALLOC\_RESERVED15**

**DXGK\_ALLOC\_RESERVED14**

**DXGK\_ALLOC\_RESERVED13**

**DXGK\_ALLOC\_RESERVED12**

**DXGK\_ALLOC\_RESERVED11**

**DXGK\_ALLOC\_RESERVED9**

**DXGK\_ALLOC\_RESERVED8**

**DXGK\_ALLOC\_RESERVED7**

**DXGK\_ALLOC\_RESERVED6**

**DXGK\_ALLOC\_RESERVED5**

**DXGK\_ALLOC\_RESERVED4**

**DXGK\_ALLOC\_RESERVED3**

**DXGK\_ALLOC\_RESERVED2**

**DXGK\_ALLOC\_RESERVED1**

**DXGK\_ALLOC\_RESERVED0**

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
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems. Updated in Windows 8.1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmddi.h (include D3dkmddi.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20_DXGK_ALLOCATIONINFOFLAGS2%20structure%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




