---
title: PFND3DKMT\_PINDIRECTFLIPRESOURCES callback function
description: Reserved for system use. Do not use in your driver.
ms.assetid: fc497f21-a9da-4d81-ba39-6e3058942d3e
keywords: ["D3DKMTPinDirectFlipResources callback function Display Devices", "PFND3DKMT_PINDIRECTFLIPRESOURCES"]
topic_type:
- apiref
api_name:
- D3DKMTPinDirectFlipResources
api_location:
- D3dkmthk.h
api_type:
- UserDefined
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PFND3DKMT\_PINDIRECTFLIPRESOURCES callback function


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
PFND3DKMT_PINDIRECTFLIPRESOURCES D3DKMTPinDirectFlipResources;

_Check_return_ NTSTATUS APIENTRY* D3DKMTPinDirectFlipResources(
  _In_ const D3DKMT_PINDIRECTFLIPRESOURCES *pResources
)
{ ... }
```

Parameters
----------

*pResources* \[in\]

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
<td align="left"><p>Target platform</p></td>
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmthk.h (include D3dkmthk.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20PFND3DKMT_PINDIRECTFLIPRESOURCES%20callback%20function%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




