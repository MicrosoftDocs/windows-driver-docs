---
title: Querying the Hyper-V Extensible Switch Configuration
description: Querying the Hyper-V Extensible Switch Configuration
ms.assetid: AF646860-01AB-4F4B-84F8-B570054B10FC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying the Hyper-V Extensible Switch Configuration


The Hyper-V extensible switch interface includes object identifier (OID) requests that are issued by an extensible switch extension to query the current configuration of the extensible switch, its ports, and its network adapter connections. These requests include the following OIDs:

<a href="" id="oid-switch-nic-array"></a>[OID\_SWITCH\_NIC\_ARRAY](https://msdn.microsoft.com/library/windows/hardware/hh598261)  
This OID query request returns an array. Each element in the array specifies the configuration parameters of a network adapter that is associated with an extensible switch port.

<a href="" id="oid-switch-parameters"></a>[OID\_SWITCH\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh598270)  
This OID query request returns the current configuration of the extensible switch.

<a href="" id="oid-switch-port-array"></a>[OID\_SWITCH\_PORT\_ARRAY](https://msdn.microsoft.com/library/windows/hardware/hh598271)  
This OID query request returns an array. Each element in the array specifies the configuration parameters for an extensible switch port.

<a href="" id="oid-switch-port-property-enum"></a>[OID\_SWITCH\_PORT\_PROPERTY\_ENUM](https://msdn.microsoft.com/library/windows/hardware/hh598277)  
This OID method request returns an array. Each element in the array specifies the properties of a policy for a specified extensible switch port.

<a href="" id="oid-switch-property-enum"></a>[OID\_SWITCH\_PROPERTY\_ENUM](https://msdn.microsoft.com/library/windows/hardware/hh598282)  
This OID method request returns an array. Each element in the array specifies the properties of an extensible switch policy.

**Note**  When a switch extension binds for a Hyper-v Extensible Switch, it must first issue the [OID\_SWITCH\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh598270) OID to obtain the basic switch information. If the **IsActive** member of the [**NDIS\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598220) structure is FALSE, the extension must not issue the other query OIDs until the switch has finished activation. In this case, the **NetEventSwitchActivate** [**NET\_PNP\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff568751) notification specifies the switch activation event. If the **IsActive** member is TRUE at bind, the extension can safely issue the other query OIDs. Querying for the configuration while the Hyper-v Extensible Switch has not completed activation will result in the extension having an incomplete initial view of the switch configuration.

 

**Note**  When an extension generates its own OID requests, it does this in the same way as any NDIS filter driver. For more information on how this is done, see [Generating OID Requests from an NDIS Filter Driver](generating-oid-requests-from-an-ndis-filter-driver.md).

 

For more information on the control path for extensible switch OID requests, see [Hyper-V Extensible Switch Control Path for OID Requests](hyper-v-extensible-switch-control-path-for-oid-requests.md).

 

 





