---
title: NDIS\_ISOLATION\_PARAMETERS structure
author: windows-driver-content
description: The NDIS\_ISOLATION\_PARAMETERS structure is used by the OID\_GEN\_ISOLATION\_PARAMETERS OID to return the isolation parameters that are set on a VM network adapter's port.
ms.assetid: 71A01647-3415-4F76-A67C-D1022C8A11D9
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
- NDIS_ISOLATION_PARAMETERS structure Network Drivers Starting with Windows Vista
- PNDIS_ISOLATION_PARAMETERS structure pointer Network Drivers Starting with Windows Vista
---

# NDIS\_ISOLATION\_PARAMETERS structure


The **NDIS\_ISOLATION\_PARAMETERS** structure is used by the [OID\_GEN\_ISOLATION\_PARAMETERS](oid-gen-isolation-parameters.md) OID to return the isolation parameters that are set on a VM network adapter's port.

Syntax
------

```ManagedCPlusPlus
typedef struct _NDIS_ISOLATION_PARAMETERS {
  NDIS_OBJECT_HEADER  Header;
  ULONG               Flags;
  NDIS_ISOLATION_MODE IsolationMode;
  BOOLEAN             AllowUntaggedTraffic;
  ULONG               NumRoutingDomainEntries;
  ULONG               FirstRoutingDomainEntryOffset;
} NDIS_ISOLATION_PARAMETERS, *PNDIS_ISOLATION_PARAMETERS;
```

Members
-------

**Header**  
The type, revision, and size of the **NDIS\_ISOLATION\_PARAMETERS** structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](ndis-object-header.md) structure.

The **Type** member of **Header** must be set to **NDIS\_OBJECT\_TYPE\_DEFAULT**. To specify the version of the **NDIS\_ISOLATION\_PARAMETERS** structure, the **Revision** member of **Header** must be set to the following value:

<a href="" id="ndis-isolation-parameters-revision-1"></a>NDIS\_ISOLATION\_PARAMETERS\_REVISION\_1  
Original version for NDIS 6.40 and later.

Set the **Size** member to **NDIS\_SIZEOF\_NDIS\_ISOLATION\_PARAMETERS\_REVISION\_1**.

**Flags**  
A **ULONG** value that contains a bitwise **OR** of flags. This member is reserved for NDIS.

**IsolationMode**  
An [**NDIS\_ISOLATION\_MODE**](ndis-isolation-mode.md) enumeration value that specifies the isolation mode.

**AllowUntaggedTraffic**  
Specifies whether the VM network adapter's port is allowed to send or receive untagged packets. If untagged packets are allowed, the VM network adapter miniport driver tags untagged packets with the default isolation ID. Otherwise, the miniport driver drops them.

**NumRoutingDomainEntries**  
A **ULONG** value that specifies the number of [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](ndis-routing-domain-entry.md) in the array that follows the **NDIS\_ISOLATION\_PARAMETERS** structure.

**FirstRoutingDomainEntryOffset**  
A **ULONG** value that specifies the offset, in bytes, to the first [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](ndis-routing-domain-entry.md) element in the array that follows the **NDIS\_ISOLATION\_PARAMETERS** structure. The offset is measured from the start of the **NDIS\_ISOLATION\_PARAMETERS** structure to the beginning of the first element of the array.

**Note**  If the value of **NumRoutingDomainEntries** is zero, this member is ignored.

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.40 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_ISOLATION\_MODE**](ndis-isolation-mode.md)

[**NDIS\_ISOLATION\_PARAMETERS\_GET\_FIRST\_ROUTING\_DOMAIN\_ENTRY**](ndis-isolation-parameters-get-first-routing-domain-entry.md)

[**NDIS\_OBJECT\_HEADER**](ndis-object-header.md)

[**NDIS\_ROUTING\_DOMAIN\_ENTRY**](ndis-routing-domain-entry.md)

[**NDIS\_SWITCH\_PORT\_PROPERTY\_ISOLATION**](ndis-switch-port-property-isolation.md)

[OID\_GEN\_ISOLATION\_PARAMETERS](oid-gen-isolation-parameters.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_ISOLATION_PARAMETERS%20structure%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


