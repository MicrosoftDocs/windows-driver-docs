---
title: MSFT\_TargetPortal class
description: Represents a target portal.
ms.assetid: 27412123-730E-4AD4-9899-049CB9528CCB
keywords:
- MSFT_TargetPortal class Windows Storage Management API
- MSFT_TargetPortal class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_TargetPortal
- MSFT_TargetPortal.IPv4Address
- MSFT_TargetPortal.IPv6Address
- MSFT_TargetPortal.SubnetMask
- MSFT_TargetPortal.PortNumber
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_TargetPortal class

Represents a target portal.

A target portal is an endpoint that is used by IP-based storage networks, such as iSCSI. It provides to initiators the IP addresses where they can discover target ports.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_TargetPortal : MSFT_StorageObject
{
  String IPv4Address;
  String IPv6Address;
  String SubnetMask;
  UInt32 PortNumber;
};
```

## Members

The **MSFT\_TargetPortal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_TargetPortal** class has these properties.

 

**IPv4Address**
   

Data type: **String**
 

Access type: Read-only
 

The IPv4 address that the target portal uses.

 

**IPv6Address**
   

Data type: **String**
 

Access type: Read-only
 

The IPv6 address that the target portal uses.

 

**PortNumber**
   

Data type: **UInt32**
 

Access type: Read-only
 

The port number that is used by the target portal.

 

**SubnetMask**
   

Data type: **String**
 

Access type: Read-only
 

The subnet mask for the IPv4 address of the target portal, if a subnet mask is defined.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

 





