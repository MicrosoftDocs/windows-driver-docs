---
title: Overview of Port Policies
description: Overview of Port Policies
ms.assetid: 9FA63E67-F5CC-4508-A36F-7A5956568D0E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Port Policies


Starting with NDIS 6.30, the following types of policies are supported for Hyper-V extensible switch ports:

<a href="" id="built-in-port-policies"></a>Built-in Port Policies  
Built-in port policies specify properties that are enforced by the extensible switch interface. Extensions in the extensible switch driver stack are not provisioned with the properties of these policies.

Built-in port policies include access control lists (ACLs) and quality of service (QoS) properties. When a packet arrives at the miniport edge of the extensible switch on the ingress data path, the switch filters the packet and enforces these policies. If the packet passes the filtering, the switch forwards the packet up the egress data path for additional handling and filtering by overlying extensions.

For more information about the extensible switch data path, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

<a href="" id="standard-port-policies"></a>Standard Port Policies  
Standard port policies specify security, profile, or virtual LAN (VLAN) properties. These properties are provisioned by object identifier (OID) requests issued by the protocol edge of the extensible switch. If a forwarding extension is not installed and enabled in the extensible switch data path, these policies are enforced by the underlying extensible switch's miniport edge. Otherwise, the forwarding extension enforces these policies if it allows the policy to be provisioned.

Standard port properties are specified by an [**NDIS\_SWITCH\_PORT\_PROPERTY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh598242) enumeration value of **NdisSwitchPortPropertyTypeSecurity**, **NdisSwitchPortPropertyTypeVlan**, and **NdisSwitchPortPropertyTypeProfile**.

**Note**  If a forwarding extension does not manage or enforce VLAN port properties, it must return STATUS\_DATA\_NOT\_ACCEPTED for the [OID\_SWITCH\_PORT\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598275) and [OID\_SWITCH\_PORT\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598278) requests that add or update the property. VLAN port properties have a property type of **NdisSwitchPortPropertyTypeVlan**.

 

<a href="" id="custom-port-policies"></a>Custom Port Policies  
Custom port policies specify proprietary properties that are defined by an independent software vendor (ISV). These properties are provisioned by OID requests issued by the extensible switch's protocol edge of the extensible switch and enforced by the underlying extension that manages the custom port policy.

Custom port properties are defined through managed object format (MOF) class definitions. The ISV defines the format of the custom port properties through the MOF class definition. After the MOF file is registered with the WMI management layer, the underlying extensions are provisioned with the custom port policy.

A custom port property is specified by [**NDIS\_SWITCH\_PORT\_PROPERTY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh598242) enumeration value of **NdisSwitchPortPropertyTypeCustom**. Each custom port property is uniquely defined through a GUID value. The extension manages those custom port properties for which it has been configured with the property's GUID value.

**Note**  The method by which the extension is configured with the property's GUID value is proprietary to the ISV.

 

Standard and custom port policies are provisioned through the following OID requests:

-   The protocol edge issues OID set requests of [OID\_SWITCH\_PORT\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598275) to notify underlying extensions of the addition of a standard or custom port property.

-   The protocol edge issues OID set requests of [OID\_SWITCH\_PORT\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598278) to notify underlying extensions of the update to a standard or custom port property.

-   The protocol edge issues OID set requests of [OID\_SWITCH\_PORT\_PROPERTY\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598276) to notify underlying extensions of the deletion of a standard or custom port property.

A forwarding extension can block the provisioning of the new or updated port policy by vetoing the OID request. The extension does this by completing the OID request with STATUS\_DATA\_NOT\_ACCEPTED. If the extension does not veto the OID request, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward the OID request down the extensible switch control path.

**Note**  If the extension does not veto the OID request, it monitors the status when the request is completed. The extension does this to determine whether the OID request was vetoed by underlying extensions in the extensible switch control path or by the extensible switch interface.

 

For more information on how to manage port policies and properties, see [Managing Port Policies](managing-port-policies.md).

 

 





