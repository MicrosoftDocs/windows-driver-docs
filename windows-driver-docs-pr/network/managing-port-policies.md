---
title: Managing Port Policies
description: Managing Port Policies
ms.assetid: 46394916-6558-4BDA-8920-E3C5378823BE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Port Policies


Hyper-V extensible switch filtering and forwarding extensions can be provisioned with the properties of standard and custom port properties. Once provisioned, these extensions enforce the policies when they filter packets obtained on the extensible switch ingress data path. For more information about these policies, see [Port Policies](port-policies.md).

The Hyper-V extensible switch interface uses the following object identifiers (OIDs) to provision filtering and forwarding extensions with the properties of standard and custom port policies:

<a href="" id="oid-switch-port-property-add"></a>[OID\_SWITCH\_PORT\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598275)  
This OID set request is issued by the protocol edge of the extensible switch to notify underlying extensions of the addition of a property at the WMI management layer. The **InformationBuffer** of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238) structure.

**Note**  Custom port properties are specified by an [**NDIS\_SWITCH\_PORT\_PROPERTY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh598242) enumeration value of **NdisSwitchPortPropertyTypeCustom**. Standard port properties are specified by an **NDIS\_SWITCH\_PORT\_PROPERTY\_TYPE** enumeration value of **NdisSwitchPortPropertyTypeSecurity**, **NdisSwitchPortPropertyTypeVlan**, and **NdisSwitchPortPropertyTypeProfile**.

 

<a href="" id="oid-switch-port-property-update"></a>[OID\_SWITCH\_PORT\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598278)  
This OID set request is issued by the protocol edge of the extensible switch to inform underlying extensions of the update of a property at the WMI management layer. The **InformationBuffer** of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238) structure.

<a href="" id="oid-switch-port-property-delete"></a>[OID\_SWITCH\_PORT\_PROPERTY\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598276)  
This OID set request is issued by the protocol edge of the extensible switch to inform underlying extensions of the deletion of a property at the WMI management layer. The **InformationBuffer** of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_PORT\_PROPERTY\_DELETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598232) structure.

<a href="" id="oid-switch-port-property-enum"></a>[OID\_SWITCH\_PORT\_PROPERTY\_ENUM](https://msdn.microsoft.com/library/windows/hardware/hh598277)  
This OID method request is sent by the extension to query the underlying miniport edge of the extensible switch about the currently configured properties for a specified port on the extensible switch. The **InformationBuffer** of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598236) structure that specifies the parameters for the policy enumeration of a specified port.

-   An array of [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598233) structures. Each of these structures contains information about the properties of an extensible switch port policy.

    **Note**  If the **NumProperties** member of the [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598236) structure is set to zero, no [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598233) structures are returned.

     

**Note**  The extension must not originate OID set requests of [OID\_SWITCH\_PORT\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598275). [OID\_SWITCH\_PORT\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598278), or [OID\_SWITCH\_PORT\_PROPERTY\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598276).

 

The extensible switch extension must follow these guidelines when it handles an OID set request of [OID\_SWITCH\_PORT\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598275), [OID\_SWITCH\_PORT\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598278), or [OID\_SWITCH\_PORT\_PROPERTY\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598276):

-   The extension must not modify the [**NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238) or [**NDIS\_SWITCH\_PORT\_PROPERTY\_DELETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598232) structure that is associated with the OID request.

-   The extension must handle these OID requests if the extension manages the property. Depending on the OID request, the extension must inspect the following members of the [**NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238) or [**NDIS\_SWITCH\_PORT\_PROPERTY\_DELETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598232) structures to determine whether it manages the port property:

    -   The **PropertyType** member. This member specifies the type of the port property. Custom port properties have a **PropertyType** member value of **NdisSwitchPortPropertyTypeCustom**. Standard port properties have other property type values. For example, standard VLAN port policies have a property type value of **NdisSwitchPortPropertyTypeVlan**.

    -   The **PropertyId** member. This member specifies a proprietary GUID value for a custom port property. This GUID value is created by the independent software vendor (ISV) who also defines the format of the custom extensible switch property.

        **Note**  The extension must ignore this member for standard port policies.

         

-   The extension must handle an [OID\_SWITCH\_PORT\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598278) set request if the extension was previously provisioned with a port property that matches the following members of the [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255) structure:

    -   The **PropertyType** member.

    -   The **PropertyId** member.

        **Note**  The extension must ignore this member for standard port policies.

         

    -   The **PropertyVersion** member. This member specifies the version of the port property that the extension was provisioned with.

    -   The **PropertyInstanceId** member. This member specifies the instance of the port property that the extension was provisioned with.

-   The filtering or forwarding extension can veto the addition or update of a port policy that it manages. The extension does this by completing the OID request with STATUS\_DATA\_NOT\_ACCEPTED.

    **Note**  Capturing extensions must not veto the addition or update of a port policy. Instead, it must forward the OID request down the extensible switch control path.

     

-   A forwarding extension can fail the OID request for standard port properties that it does not support or if the property conflicts with its own policy configuration. In this case, the extension must complete the OID request and return the appropriate NDIS status code to report the failure.

-   If the extension successfully handles the OID set request for a standard port policy, it must not complete the OID request and must forward it down the extensible switch control path.

-   If the capturing or filtering extension successfully handles the OID set request for a custom port policy, it must not complete the OID request and must forward it down the extensible switch control path.

    If the forwarding extension successfully handles the OID set request for a custom port policy, it must complete the OID request and return the appropriate NDIS\_STATUS\_*Xxx* value.

-   If the extension does not complete the OID set request, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward the OID request down the extensible switch driver stack. In this case, the extensions should monitor the completion status of the OID to detect whether an underlying extension has failed the OID request.

 

 





