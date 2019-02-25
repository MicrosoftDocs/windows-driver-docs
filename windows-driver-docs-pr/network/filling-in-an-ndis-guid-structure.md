---
title: Filling in an NDIS_GUID Structure
description: Filling in an NDIS_GUID Structure
ms.assetid: 971f6f25-fd2b-4a1e-9378-6270a094f4ff
keywords:
- NDIS_GUID
- WMI WDK networking , GUIDs
- OIDs WDK networking , WMI
- GUIDs WDK networking
- Windows Management Instrumentation WDK networking , GUIDs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filling in an NDIS\_GUID Structure





An NDIS\_GUID structure is defined as follows:

```C++
typedef struct _NDIS_GUID {
  GUID  Guid;
  union {
    NDIS_OID  Oid;
    NDIS_STATUS  Status;
  };
  ULONG  Size;
  ULONG  Flags;
} NDIS_GUID, *PNDIS_GUID;
```

To obtain a GUID for the **Guid** member of the structure, you can run the Uuidgen.exe application. For more information about this application, see the Microsoft Windows SDK documentation.

The **Oid** or **Status** member is a ULONG that is an OID code. NDIS 6.0 does not map custom status indications to WMI GUIDs.

If the NDIS\_GUID structure maps an OID that returns an array of data items, the **Size** member specifies the size, in bytes, of each data item in the array. If the data is not an array, the **Size** member specifies the size of the data. If the size of the data items is variable, or if the OID does not return data, the **Size** member must be -1.

A bitwise OR of the following values for the **Flags** member indicates the type of data that is associated with the GUID:

<a href="" id="fndis-guid-to-oid"></a>fNDIS\_GUID\_TO\_OID  
When this flag is set, the NDIS\_GUID structure maps a GUID to an OID.

<a href="" id="fndis-guid-to-status"></a>fNDIS\_GUID\_TO\_STATUS  
Reserved for NDIS. Miniport drivers should not use this flag.

<a href="" id="fndis-guid-ansi-string"></a>fNDIS\_GUID\_ANSI\_STRING  
When this flag is set, a null-terminated ANSI string is supplied for the GUID.

<a href="" id="fndis-guid-unicode-string"></a>fNDIS\_GUID\_UNICODE\_STRING  
When this flag is set, a Unicode string is supplied for the GUID.

<a href="" id="fndis-guid-array"></a>fNDIS\_GUID\_ARRAY  
When this flag is set, an array of data items is supplied for the GUID. The specified **Size** value indicates the length of each data item in the array.

<a href="" id="fndis-guid-allow-read"></a>fNDIS\_GUID\_ALLOW\_READ  
When this flag is set, all users are allowed to use this GUID to obtain information.

<a href="" id="fndis-guid-allow-write"></a>fNDIS\_GUID\_ALLOW\_WRITE  
When this flag is set, all users are allowed to use this GUID to set information.

**Note**  By default, custom WMI GUIDs that a miniport driver supplies are accessible only to users with administrator privileges. A user with administrator privileges can always read or write to a custom GUID if the miniport driver supports the read or write operation for that GUID. You can set the fNDIS\_GUID\_ALLOW\_READ and fNDIS\_GUID\_ALLOW\_WRITE flags to allow all users to access a custom GUID.

 

Note that for all custom GUIDs that a driver registers, the driver must set fNDIS\_GUID\_TO\_OID. Miniport drivers should never set fNDIS\_GUID\_TO\_STATUS. All of the other flags can be combined by using a bitwise OR operation.

 

 





