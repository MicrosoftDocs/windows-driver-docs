---
title: OID_GEN_CO_SUPPORTED_GUIDS
author: windows-driver-content
description: This topic describes the OID_GEN_CO_SUPPORTED_GUIDS object identifier (OID).
ms.assetid: d82d6ecb-f70b-4fc2-97eb-331aafe1fe57
keywords:
- OID_GEN_CO_SUPPORTED_GUIDS
ms.author: windowsdriverdev
ms.date: 11/02/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_GEN_CO_SUPPORTED_GUIDS

The OID_GEN_CO_SUPPORTED_GUIDS OID requests the miniport driver to return an array of structures of the type NDIS_GUID. Each structure in the array specifies the mapping of a custom GUID (globally unique identifier) to either a custom OID or to an NDIS_STATUS that the miniport driver sends through [NdisMCoIndicateStatusEx](https://msdn.microsoft.com/library/windows/hardware/ff563562).

The NDIS_GUID structure is defined as follows:

```c++
typedef struct _NDIS_GUID {
    GUID    Guid;
    union {
        NDIS_OID    Oid;
        NDIS_STATUS Status;
    };
    ULONG   Size;
    ULONG   Flags;
} NDIS_GUID, *PNDIS_GUID;
```

The members of this structure contain the following information:

**Guid**  
The custom GUID defined for the miniport driver.

**Oid**  
The custom OID to which **Guid** maps.

**Status**  
The NDIS_STATUS to which **Guid** maps.

**Size**  
When the fNDIS_GUID_ARRAY flag is set, **Size** specifies the size in bytes of each data item in the array returned by the miniport driver. If the fNDIS_GUID_ANSI_STRING or fNDIS_GUID_NDIS_STRING flag is set, **Size** is set to -1. Otherwise, **Size** specifies the size in bytes of the data item that the GUID represents.

**Flags**  
The following flags can be ORed together to indicate whether the GUID maps to an OID or to an NDIS_STATUS string and to indicate the type of data supplied for the GUID: 

fNDIS_GUID_TO_OID  
When set, indicates that the NDIS_GUID structure maps a GUID to an OID.

fNDIS_GUID_TO_STATUS  
When set, indicates that the NDIS_GUID structure maps a GUID to an NDIS_STATUS string.

fNDIS_GUID_ANSI_STRING  
When set, indicates that a null-terminated ANSI string is supplied for the GUID.

fNDIS_GUID_UNICODE_STRING  
When set, indicates that a Unicode string is supplied for the GUID.

fNDIS_GUID_ARRAY  
When set, indicates that an array of data items is supplied for the GUID. The specified Size indicates the length of each data item in the array.

fNDIS_GUID_ALLOW_READ  
When set, indicates that all users are allowed to query this GUID.

fNDIS_GUID_ALLOW_WRITE  
When set, indicates that all users are allowed to set this GUID.

## Remarks

> [!NOTE]
> By default, custom WMI GUIDs supplied by a miniport driver are only accessible to users with administrator privileges. A user with administrator privileges can always read or write to a custom GUID if the miniport driver supports the read or write operation for that GUID. Set the fNDIS_GUID_ALLOW_READ and fNDIS_GUID_ALLOW_WRITE flags to allow all users to access a custom GUID.

Note that all custom GUIDs registered by a miniport driver must set either fNDIS_GUID_TO_OID or fNDIS_GUID_TO_STATUS (never set both). All other flags may be combined by using the OR operator as applicable.

In the following example, an NDIS_GUID structure maps a GUID to OID_GEN_CO_RCV_PDUS_NO_BUFFER:

```cpp 
NDIS_GUID NdisGuid =  {{0x0a214809, 0xe35f, 0x11d0, 0x96, 0x92, 0x00,
 0xc0, 0x4f, 0xc3, 0x35, 0x8c},
 GUID_NDIS_GEN_CO_RCV_PDUS_NO_BUFFER,
 OID_GEN_CO_RCV_PDUS_NO_BUFFER,
 4,
 fNDIS_GUID_TO_OID};
```
A GUID is an identifier used by Windows Management Instrumentation (WMI) to obtain or set information. NDIS intercepts a GUID sent by WMI to an NDIS driver, maps the GUID to an OID, and sends the OID to the driver. The driver returns the data item(s) to NDIS, which then returns the data to WMI.

NDIS also translates changes in NIC status into GUIDs recognized by WMI. When a miniport driver reports a change in NIC status with [NdisMCoIndicateStatusEx](https://msdn.microsoft.com/library/windows/hardware/ff563562), NDIS translates the NDIS_STATUS indicated by the miniport driver into a GUID that NDIS sends to WMI.

If a connection-oriented miniport driver supports customs GUIDs, it must support OID_GEN_CO_SUPPORTED_GUIDS, which returns to NDIS the mapping of custom GUIDs to custom OIDs or NDIS_STATUS strings. After querying the miniport driver with OID_GEN_CO_SUPPORTED_GUIDS, NDIS registers the miniport driver's custom GUIDs with WMI.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")