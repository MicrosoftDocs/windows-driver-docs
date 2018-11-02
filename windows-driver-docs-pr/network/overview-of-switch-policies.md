---
title: Overview of Switch Policies
description: Overview of Switch Policies
ms.assetid: DB9368CE-96D4-48C9-AE18-601EE4A09001
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Switch Policies


Starting with NDIS 6.30, the following types of policies are supported for Hyper-V extensible switches:

<a href="" id="built-in-switch-policies"></a>Built-in Switch Policies  
Built-in switch policies specify properties that are enforced by the extensible switch interface. Extensions in the extensible switch driver stack are not provisioned with the properties of these policies.

Built-in switch policies include properties that affect the switch configuration in general but do not affect traffic flow over individual switch ports. For example, one such built-in policy configures the switch to allow hardware offloads to physical adapters that support the single root I/O virtualization (SR-IOV) interface. For more information about this interface, see [Single Root I/O Virtualization (SR-IOV)](overview-of-single-root-i-o-virtualization--sr-iov-.md).

<a href="" id="custom-switch-policies"></a>Custom Switch Policies  
Custom switch policies specify proprietary properties that are defined by an independent software vendor (ISV). These properties are provisioned by the protocol edge of the extensible switch and enforced by the underlying extension that manages the custom switch policy.

The ISV defines the format for the custom switch properties. The format of the custom switch property is proprietary to the ISV.

Custom switch properties are defined through managed object format (MOF) class definitions. After the MOF file is registered with the WMI management layer, the underlying extensions are provisioned with the custom switch policy.

A custom switch property is specified by the [**NDIS\_SWITCH\_PROPERTY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh598257) enumeration value of **NdisSwitchPropertyTypeCustom**. Each custom switch property is uniquely defined through a GUID value. The extension manages those custom switch properties for which it has been configured with the property's GUID value.

**Note**  The method by which the extension is configured with the property's GUID value is proprietary to the ISV.

 

Custom switch policies are provisioned through the following OID requests:

-   The protocol edge issues OID set requests of [OID\_SWITCH\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598280) to notify underlying extensions of the addition of a custom switch property.

-   The protocol edge issues OID set requests of [OID\_SWITCH\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598283) to notify underlying extensions of the update to a custom switch property.

-   The protocol edge issues OID set requests of [OID\_SWITCH\_PROPERTY\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598281) to notify underlying extensions of the deletion of a custom switch property.

A forwarding extension can block the provisioning of the new or updated switch policy by vetoing the OID request. The extension does this by completing the OID request with STATUS\_DATA\_NOT\_ACCEPTED. If the extension does not veto the OID request, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward the OID request down the extensible switch control path.

**Note**  If the extension does not veto the OID request, it monitors the status when the request is completed. The extension does this to determine whether the OID request was vetoed by underlying extensions in the extensible switch control path or by the extensible switch interface.

 

For more information on how to manage switch policies and properties, see [Managing Switch Policies](managing-switch-policies.md).

 

 





