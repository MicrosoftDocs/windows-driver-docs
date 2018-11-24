---
title: Operational Ports
description: Operational Ports
ms.assetid: 647EBDFD-A100-46A7-B387-BF11004415EC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Operational Ports


Starting with NDIS 6.30 in Windows Server 2012, the extensible switch interface creates an operational port to host an extensible switch network adapter connection. When an extensible switch port is created, it is assigned a port type. This port type is in effect after the port is created and before it is torn down. For ports assigned to Hyper-V child partitions, the operational port type stays in effect while the partition is running and operational.

Operational port types define the type of extensible switch network adapter that can connect to it. The extensible switch interface defines the following operational port types:

<a href="" id="ndisswitchporttypeexternal"></a>**NdisSwitchPortTypeExternal**  
This is a port that is configured to be connected to the external network adapter of the extensible switch. This adapter is exposed in the management operating system that runs in the Hyper-V parent partition.

The external network adapter provides a connection to the physical network interface that is available on the host. The external network adapter can be accessed by the Hyper-V parent partition and all child partitions.

**Note**  An extensible switch supports only one external network adapter connection.

 

<a href="" id="ndisswitchporttypeinternal"></a>**NdisSwitchPortTypeInternal**  
This is a port that is configured to be connected to the internal network adapter of the extensible switch. This adapter is exposed in the management operating system that runs in the Hyper-V parent partition.

The internal network adapter provides access to an extensible switch for processes that run in the management operating system. This allows these processes to send or receive packets over the extensible switch.

**Note**  An extensible switch supports only one internal network adapter.

 

<a href="" id="ndisswitchporttypesynthetic"></a>**NdisSwitchPortTypeSynthetic**  
This is a port that is configured to be connected to a synthetic network adapter. This adapter is exposed in a guest operating system that runs in a Hyper-V child partition.

**Note**  A synthetic network adapter is a type of virtual machine (VM) network adapter. This adapter is exposed in a guest operating system that is running Windows Vista or a later version of Windows.

 

<a href="" id="ndisswitchporttypeemulated"></a>**NdisSwitchPortTypeEmulated**  
This value specifies a port that is configured to be connected to an emulated network adapter. This adapter is exposed in a guest operating system.

**Note**  An emulated network adapter is a type of VM network adapter. This adapter can be exposed in a guest operating system that is running Windows XP or a non-Windows operating system.

 

 

 





