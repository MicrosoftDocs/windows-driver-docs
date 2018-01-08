---
title: D3DKMTSetStereoEnabled function
description: Retrieves a Boolean value that indicates whether the operating system's stereoscopic 3-D display behavior is enabled.
ms.assetid: 03aa74bb-0999-41d3-b67f-a58cfe17043e
keywords: ["D3DKMTSetStereoEnabled function Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMTSetStereoEnabled
api_location:
- GDI32.dll
- API-MS-Win-dx-d3dkmt-l1-1-0.dll
- API-MS-Win-dx-d3dkmt-l1-1-1.dll
- API-MS-Win-DX-D3DKMT-L1-1-2.dll
api_type:
- DllExport
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# D3DKMTSetStereoEnabled function


Retrieves a Boolean value that indicates whether the operating system's stereoscopic 3-D display behavior is enabled.

Syntax
------

```ManagedCPlusPlus
_Check_return_ NTSTATUS APIENTRY D3DKMTSetStereoEnabled(
  _In_ BOOL bStereoEnabled
);
```

Parameters
----------

*bStereoEnabled* \[in\]
**TRUE** if the operating system's stereoscopic 3-D display behavior is enabled; **FALSE** otherwise.

Return value
------------

Returns one of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>STATUS_SUCCESS</strong></td>
<td align="left"><p>The function completed successfully.</p></td>
</tr>
</tbody>
</table>

 

This function might also return other NTSTATUS values.

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
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">GDI32.lib</td>
</tr>
<tr class="even">
<td align="left"><p>DLL</p></td>
<td align="left">GDI32.dll</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3DKMTSetStereoEnabled%20function%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




