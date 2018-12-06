---
title: Setting the NDIS 6.0 Miniport Adapter Attributes
description: Setting the NDIS 6.0 Miniport Adapter Attributes
ms.assetid: 76d4bda0-c3e3-4abe-b16b-d2b5392c3db4
keywords:
- miniport adapters WDK networking , attributes
- adapters WDK networking , attributes
- porting miniport drivers WDK networking , adapters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the NDIS 6.0 Miniport Adapter Attributes





The [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function replaces the [**NdisMSetAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff553619) and [**NdisMSetAttributesEx**](https://msdn.microsoft.com/library/windows/hardware/ff553623) functions. The driver passes miniport adapter configuration attributes to **NdisMSetMiniportAttributes**, including the medium type, flags, check-for-hang time, and interface type.

The [**NDIS\_MINIPORT\_ADAPTER\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565920) structure passed to **NdisMSetMiniportAttributes** is actually a pointer to one of the following structures:

[**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934)

[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[**NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565930)

The registration attributes flags of the miniport adapter are updated for NDIS 6.0.

All NDIS 6.0 and later miniport drivers are deserialized. Therefore, the NDIS\_ATTRIBUTE\_DESERIALIZE attribute flag is removed.

The following code sample shows initialization of a registration attributes structure:

```C++
MiniportAttributes.Header.Type = NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES;
MiniportAttributes.Header.Revision = NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES_REVISION_1;
MiniportAttributes.Header.Size = sizeof(MiniportAttributes);
MiniportAttributes.AttributeFlags = NDIS_MINIPORT_ATTRIBUTES_HARDWARE_DEVICE | NDIS_ATTRIBUTE_BUS_MASTER;
MiniportAttributes.CheckForHangTimeInSeconds = 2;
MiniportAttributes.InterfaceType = NdisInterfacePci;
```

For more information about setting miniport driver attributes, see [Initializing an Adapter](initializing-a-miniport-adapter.md).

 

 





