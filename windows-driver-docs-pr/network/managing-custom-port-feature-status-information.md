---
title: Managing Custom Port Feature Status Information
description: Managing Custom Port Feature Status Information
ms.assetid: C989888B-1636-488A-80BF-13D136312417
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Custom Port Feature Status Information


The Hyper-V extensible switch interface uses the following object identifier (OID) to query custom status information for an extensible switch port. This status information is known as *port feature status* information:

<a href="" id="oid-switch-port-feature-status-query"></a>[OID\_SWITCH\_PORT\_FEATURE\_STATUS\_QUERY](https://msdn.microsoft.com/library/windows/hardware/hh598274)  
This OID method request is issued by the protocol edge of the extensible switch to obtain the custom feature status information for a specified port property.

After a successful return from this OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_PORT\_FEATURE\_STATUS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598227) structure that specifies the custom feature status information that is to be returned.

    **Note**  For a custom feature status, the **FeatureStatusType** member is set to **NdisSwitchPortPropertyTypeCustom**.

     

-   An [**NDIS\_SWITCH\_PORT\_FEATURE\_STATUS\_CUSTOM**](https://msdn.microsoft.com/library/windows/hardware/hh598226) structure that contains the status information about a custom property assigned to an extensible switch port.

    When the protocol edge of the extensible switch issues the [OID\_SWITCH\_PORT\_FEATURE\_STATUS\_QUERY](https://msdn.microsoft.com/library/windows/hardware/hh598274) request, it sets the **FeatureStatusCustomBufferLength** and **FeatureStatusCustomBufferOffset** members to a location in the **InformationBuffer** member that the extension can use to return the feature status information.

The extensible switch extension must follow these guidelines when it receives an OID method request of [OID\_SWITCH\_PORT\_FEATURE\_STATUS\_QUERY](https://msdn.microsoft.com/library/windows/hardware/hh598274):

-   The extension must handle the OID request if it manages a custom extensible switch port property that matches the **FeatureStatusId** member of the [**NDIS\_SWITCH\_PORT\_FEATURE\_STATUS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598227) structure.

-   If the extension handles the OID method request, it must return the feature status information that matches the parameters specified by the [**NDIS\_SWITCH\_PORT\_FEATURE\_STATUS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598227) structure.

    If the feature status buffer is too small, the extension must fail the OID request with NDIS\_STATUS\_INVALID\_LENGTH. The extension must set the **DATA.SET\_INFORMATION.BytesNeeded** member in the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.

    Otherwise, the extension must return the feature status information and complete the OID request with NDIS\_STATUS\_SUCCESS.

-   If the extension does not manage the custom extensible switch property, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward the OID request down the extensible switch driver stack.

    For more information about how to forward OID requests, see [Filtering OID Requests in an NDIS Filter Driver](filtering-oid-requests-in-an-ndis-filter-driver.md).

For more information about how to define and register port feature status information, see [Custom Port Feature Status](custom-port-feature-status.md).

 

 





