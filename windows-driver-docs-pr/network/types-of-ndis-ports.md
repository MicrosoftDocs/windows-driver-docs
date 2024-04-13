---
title: Types of NDIS Ports
description: Types of NDIS Ports
keywords:
- ports WDK NDIS , types
- NDIS ports WDK , types
ms.date: 03/02/2023
---

# Types of NDIS Ports





NDIS ports can be one of the following types:

<a href="" id="ndisporttypeundefined"></a>**NdisPortTypeUndefined**  
The default port type. Use this type for general port applications that do not fit into one of the following types.

<a href="" id="ndisporttypebridge"></a>**NdisPortTypeBridge**  
Reserved for system use.

<a href="" id="ndisporttyperasconnection"></a>**NdisPortTypeRasConnection**  
A Remote Access Service (RAS) connection.

<a href="" id="ndisporttype8021xsupplicant"></a>**NdisPortType8021xSupplicant**  
A remote wireless station that is associated with an access point on this host computer.

<a href="" id="ndisporttypendisimplatform"></a>**NdisPortTypeNdisImPlatform**  
Reserved for system use.

**Note**  This value is supported only in NDIS 6.30 and later.

 

The characteristics of an NDIS port vary from one port application to another. For example, for a bridge interface, the miniport driver upper edge of an intermediate driver creates an **NdisPortTypeBridge** port when the protocol edge of the intermediate driver binds to a physical miniport adapter that requires a bridge at layer three.

## Related topics


[Overview of NDIS Ports](overview-of-ndis-ports.md)

 

 






