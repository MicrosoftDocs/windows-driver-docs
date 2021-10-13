---
title: Managing Custom Switch Feature Status Information
description: Managing Custom Switch Feature Status Information
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Custom Switch Feature Status Information


The Hyper-V extensible switch interface uses the following object identifier (OID) to query custom status information for the extensible switch. This status information is known as *switch feature status* information:

<a href="" id="oid-switch-feature-status-query"></a>[OID\_SWITCH\_FEATURE\_STATUS\_QUERY](./oid-switch-feature-status-query.md)  
This OID method request is issued by the protocol edge of the extensible switch to obtain the custom feature status information for a specified switch property.

After a successful return from this OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_FEATURE\_STATUS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_feature_status_parameters) structure that specifies the custom feature status information that is to be returned.

    **Note**  For a custom feature status, the **FeatureStatusType** member is set to **NdisSwitchPropertyTypeCustom**.

     

-   An [**NDIS\_SWITCH\_FEATURE\_STATUS\_CUSTOM**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_feature_status_custom) structure that contains the status information about a custom property assigned to an extensible switch port.

    When the protocol edge of the extensible switch issues the [OID\_SWITCH\_FEATURE\_STATUS\_QUERY](./oid-switch-feature-status-query.md) request, it sets the **FeatureStatusCustomBufferLength** and **FeatureStatusCustomBufferOffset** members to a location in the **InformationBuffer** member that the extension can use to return the feature status information.

The extensible switch extension must follow these guidelines when it receives an OID method request of [OID\_SWITCH\_FEATURE\_STATUS\_QUERY](./oid-switch-feature-status-query.md):

-   The extension must handle the OID request if it manages a custom extensible switch feature status that matches the **FeatureStatusId** member of the [**NDIS\_SWITCH\_FEATURE\_STATUS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_feature_status_parameters) structure.

-   If the extension handles the OID method request, it must return the feature status information that matches the parameters specified by the [**NDIS\_SWITCH\_FEATURE\_STATUS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_feature_status_parameters) structure.

    If the feature status buffer is too small, the extension must fail the OID request with NDIS\_STATUS\_INVALID\_LENGTH. The extension must set the **DATA.SET\_INFORMATION.BytesNeeded** member in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure to the minimum buffer size that is required.

    Otherwise, the extension must return the feature status information and complete the OID request with NDIS\_STATUS\_SUCCESS.

-   If the extension does not manage the custom extensible switch feature status, it must call [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) to forward the OID request down the extensible switch driver stack.

    For more information about how to forward OID requests, see [Filtering OID Requests in an NDIS Filter Driver](filtering-oid-requests-in-an-ndis-filter-driver.md).

For more information about how to define and register switch feature status information, see [Custom Switch Feature Status](custom-switch-feature-status.md).

 

