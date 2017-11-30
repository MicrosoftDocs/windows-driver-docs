---
title: OID_GEN_SUPPORTED_GUIDS
author: windows-driver-content
description: As a query, the OID_GEN_SUPPORTED_GUIDS OID requests the miniport driver to return an array of structures of the type NDIS_GUID.
ms.assetid: 6985727e-50f8-4dbf-b8cd-ce31d49e8294
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_SUPPORTED_GUIDS Network Drivers Starting with Windows Vista
---

# OID\_GEN\_SUPPORTED\_GUIDS


As a query, the OID\_GEN\_SUPPORTED\_GUIDS OID requests the miniport driver to return an array of structures of the type NDIS\_GUID.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Optional.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

Remarks
-------

Each structure in the array specifies the mapping of a custom GUID (globally unique identifier) to either a custom OID or to an NDIS\_STATUS that the miniport driver sends through the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function.

The NDIS\_GUID structure is defined as follows:

```
typedef struct _NDIS_GUID {
    GUID             Guid;
    union {
        NDIS_OID     Oid;
        NDIS_STATUS  Status;
    };
    ULONG            Size;
    ULONG            Flags;
} NDIS_GUID, *PNDIS_GUID;
```

The members of this structure contain the following information:

<a href="" id="guid"></a>**Guid**  
Specifies the custom GUID defined for the miniport driver.

<a href="" id="oid"></a>**Oid**  
Specifies the custom OID to which **Guid** maps.

<a href="" id="status"></a>**Status**  
Specifies the NDIS\_STATUS to which **Guid** maps.

<a href="" id="size"></a>**Size**  
Specifies the size in bytes of each data item in the array returned by the miniport driver. If the fNDIS\_GUID\_ANSI\_STRING or fNDIS\_GUID\_NDIS\_STRING flag is set, **Size** is set to -1. Otherwise, **Size** specifies the size in bytes of the data item that the GUID represents. This member is specified only when the fNDIS\_GUID\_ARRAY flag is set.

<a href="" id="flags"></a>**Flags**  
The following flags can be combined by the OR operator to indicate whether the GUID maps to an OID or to an NDIS\_STATUS string and to indicate the type of data that is supplied for the GUID:

<a href="" id="fndis-guid-to-oid"></a>fNDIS\_GUID\_TO\_OID  
Indicates that the NDIS\_GUID structure maps a GUID to an OID.

<a href="" id="fndis-guid-to-status"></a>fNDIS\_GUID\_TO\_STATUS  
Indicates that the NDIS\_GUID structure maps a GUID to an NDIS\_STATUS string.

<a href="" id="fndis-guid-ansi-string"></a>fNDIS\_GUID\_ANSI\_STRING  
Indicates that a null-terminated ANSI string is supplied for the GUID.

<a href="" id="fndis-guid-unicode-string"></a>fNDIS\_GUID\_UNICODE\_STRING  
Indicates that a Unicode string is supplied for the GUID.

<a href="" id="fndis-guid-array"></a>fNDIS\_GUID\_ARRAY  
Indicates that an array of data items is supplied for the GUID. The specified **Size** indicates the length of each data item in the array.

<a href="" id="fndis-guid-allow-read"></a>fNDIS\_GUID\_ALLOW\_READ  
When set, indicates that all users are allowed to use this GUID to obtain information.

<a href="" id="fndis-guid-allow-write"></a>fNDIS\_GUID\_ALLOW\_WRITE  
When set, indicates that all users are allowed to use this GUID to set information.

**Note**  
By default, custom WMI GUIDs supplied by a miniport driver are only accessible to users with administrator privileges. A user with administrator privileges can always read or write to a custom GUID if the miniport driver supports the read or write operation for that GUID. Set the fNDIS\_GUID\_ALLOW\_READ and fNDIS\_GUID\_ALLOW\_WRITE flags to allow all users to access a custom GUID.

 

Note that all custom GUIDs registered by a miniport driver must set either fNDIS\_GUID\_TO\_OID or fNDIS\_GUID\_TO\_STATUS (never set both). All other flags may be combined by using the OR operator as applicable.

In the following example, an NDIS\_GUID structure maps a GUID to OID\_802\_3\_MULTICAST\_LIST:

```
NDIS_GUID    NdisGuid = {{0x44795701, 0xa61b, 0x11d0, 0x8d, 0xd4,
                          0x00, 0xc0, 0x4f, 0xc3,
                          0x35, 0x8c},
                          OID_802_3_MULTICAST_LIST,
                          6,
                          fNDIS_GUID_TO_OID | fNDIS_GUID_ARRAY};
```

A GUID is an identifier used by Windows Management Instrumentation (WMI) to obtain or set information. NDIS intercepts a GUID sent by WMI to an NDIS driver, it maps the GUID to an OID, and sends the OID to the driver. The driver returns the data items to NDIS, which then returns the data to WMI.

NDIS also translates changes in NIC status into GUIDs that are recognized by WMI. When a miniport driver reports a change in NIC status using the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function, NDIS translates the NDIS\_STATUS indicated by the miniport driver into a GUID that NDIS sends to WMI.

If a miniport driver supports customs GUIDs, it must support OID\_GEN\_SUPPORTED\_GUIDS. This OID returns to NDIS the mapping of custom GUIDs to custom OIDs or NDIS\_STATUS strings. After querying the miniport driver using OID\_GEN\_SUPPORTED\_GUIDS, NDIS registers the miniport driver's custom GUIDs with WMI.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_SUPPORTED_GUIDS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


