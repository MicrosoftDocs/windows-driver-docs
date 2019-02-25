---
title: Managing Switch Policies
description: Managing Switch Policies
ms.assetid: F2261CA6-2D7A-4499-82F9-7E2D7C9C908D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Switch Policies


Hyper-V extensible switch filtering and forwarding extensions can be provisioned with the properties of custom switch properties. Once provisioned, these extensions enforce the policies when they filter packets obtained on the extensible switch ingress data path. For more information about these policies, see [Switch Policies](switch-policies.md).

The Hyper-V extensible switch interface uses the following object identifiers (OIDs) to provision filtering and forwarding extensions with the properties of custom switch policies:

<a href="" id="oid-switch-property-add"></a>[OID\_SWITCH\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598280)  
This OID set request is issued by the protocol edge of the extensible switch to notify underlying extensions of the addition of a property at the WMI management layer. The **InformationBuffer** of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255) structure.

**Note**  Custom switch properties are specified by an [**NDIS\_SWITCH\_PROPERTY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh598257) enumeration value of **NdisSwitchPropertyTypeCustom**.

 

<a href="" id="oid-switch-property-update"></a>[OID\_SWITCH\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598283)  
This OID set request is issued by the protocol edge of the extensible switch to notify underlying extensions of the update of a property at the WMI management layer. The **InformationBuffer** of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255) structure.

<a href="" id="oid-switch-property-delete"></a>[OID\_SWITCH\_PROPERTY\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598281)  
This OID set request is issued by the protocol edge of the extensible switch to notify underlying extensions of the deletion of a property at the WMI management layer. The **InformationBuffer** of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_PROPERTY\_DELETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598249) structure.

<a href="" id="oid-switch-property-enum"></a>[OID\_SWITCH\_PROPERTY\_ENUM](https://msdn.microsoft.com/library/windows/hardware/hh598282)  
This OID method request is sent by the extension to query the underlying miniport edge of the extensible switch about the currently configured switch properties on the extensible switch. The **InformationBuffer** of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598253) structure that specifies the parameters for the property enumeration of a switch policy.

-   An array of [**NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598250) structures. Each of these structures contains information about the properties of a switch policy.

    **Note**  If the **NumProperties** member of the [**NDIS\_SWITCH\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598253) structure is set to zero, no [**NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598250) structures are returned.

     

**Note**  The extension must not originate OID set requests of [OID\_SWITCH\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598280). [OID\_SWITCH\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598283), or [OID\_SWITCH\_PROPERTY\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598281).

 

The extensible switch extension must follow these guidelines when it handles an OID set request of [OID\_SWITCH\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598280), [OID\_SWITCH\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598283), or [OID\_SWITCH\_PROPERTY\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598281):

-   The extension must not modify the [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255) or [**NDIS\_SWITCH\_PROPERTY\_DELETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598249) structure that is associated with the OID request.

-   The extension must handle an [OID\_SWITCH\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598283) or [OID\_SWITCH\_PROPERTY\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598281) set request if the extension has been previously provisioned with a switch property that matches the following members of the [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238) or [**NDIS\_SWITCH\_PROPERTY\_DELETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598249) structure:

    -   The **PropertyType** member that specifies the type of switch property.

        **Note**  Starting with NDIS 6.30, only switch properties of **NdisSwitchPropertyTypeCustom** are specified by the [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238) or [**NDIS\_SWITCH\_PROPERTY\_DELETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598249) structures.

         

    -   The **PropertyId** member that specifies a proprietary GUID value that the extension recognizes. This GUID value is created by the independent software vendor (ISV) who also defines the format of the custom extensible switch policy property.

        **Note**  A custom extensible switch policy property is contained within an [**NDIS\_SWITCH\_PROPERTY\_CUSTOM**](https://msdn.microsoft.com/library/windows/hardware/hh598247) structure.

         

-   If the extension handles these OID set requests, the extension must update or delete the switch policy that matches the following members of the [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255) structure:

    -   The **PropertyVersion** member that specifies the version of the extensible switch policy.

    -   The **PropertyInstanceId** member that specifies the instance of the extensible switch policy.

    If the values of these members do not match a switch policy property for which the extension has been previously provisioned, the extension must fail the OID set request with NDIS\_STATUS\_INVALID\_PARAMETER. Otherwise, the extension must complete the OID set request and return NDIS\_STATUS\_SUCCESS.

-   The filtering or forwarding extension can veto the addition, deletion, or update of a switch policy. The extension does this by completing the OID request with STATUS\_DATA\_NOT\_ACCEPTED.

    **Note**  Capturing extensions must not veto the addition or update of a switch policy. Instead, it must forward the OID request down the extensible switch control path.

     

-   If the capturing or filtering extension successfully handles the OID set request for a custom switch policy, it must not complete the OID request and must forward it down the extensible switch control path.

    If the forwarding extension successfully handles the OID set request for a custom switch policy, it must complete the OID request and return the appropriate NDIS\_STATUS\_*Xxx* value.

-   If the extension does not complete the OID set request, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward the OID request down the extensible switch driver stack. In this case, the extensions should monitor the completion status of the OID to detect whether an underlying extension has failed the OID request.

 

 





