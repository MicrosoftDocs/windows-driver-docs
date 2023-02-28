---
title: GUID_DISPLAY_DEVICE_ARRIVAL
description: GUID_DISPLAY_DEVICE_ARRIVAL
keywords: ["GUID_DISPLAY_DEVICE_ARRIVAL Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DISPLAY_DEVICE_ARRIVAL
api_location:
- Ntddvdeo.h
api_type:
- HeaderDef
ms.date: 02/24/2023
ms.topic: reference
---

# GUID_DISPLAY_DEVICE_ARRIVAL

The GUID_DISPLAY_DEVICE_ARRIVAL [device interface class](./overview-of-device-interface-classes.md) is defined for [display adapters](../display/index.md).

| Attribute | Setting |
| --------- | ------- |
| Identifier | GUID_DISPLAY_DEVICE_ARRIVAL |
| Class GUID | {1CA05180-A699-450A-9A0C-DE4FBE3DDD89} |

## Remarks

The system-supplied components of the [Windows Display Driver Model](../display/windows-vista-display-driver-model-design-guide.md) register instances of this device interface class to notify the operating system and applications of the presence of display adapters.

A device that registers this interface can be of any type supported by the Windows graphics stack. That is, it can be Display Only, Render Only, Display + Render, Compute Only (MCDM), and so forth. After a device is enumerated, applications need to check the device capabilities before using it for some purpose. For example, an application can call [**D3DKMTOpenAdapterFromDeviceName**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtopenadapterfromdevicename) to get a handle to the adapter object and call [**D3DKMTQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtqueryadapterinfo) to get various device capabilities.

The better way for applications to enumerate WDDM adapters is to use [DXGI](/windows/win32/direct3ddxgi/d3d10-graphics-programming-guide-dxgi#enumerating-adapters) or [DXCore](/windows/win32/dxcore/dxcore-enum-adapters) APIs.

For information about the device interface class for display views that are supported by display adapters, see [**GUID_DEVINTERFACE_DISPLAY_ADAPTER**](guid-devinterface-display-adapter.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddvdeo.h (include Ntddvdeo.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_DISPLAY_ADAPTER**](guid-devinterface-display-adapter.md)

 

