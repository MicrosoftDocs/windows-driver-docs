---
title: Obtaining and Updating VM Queue Parameters
description: Obtaining and Updating VM Queue Parameters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining and Updating VM Queue Parameters





An overlying driver can set the configuration parameters of a VM queue after it is allocated. Also, an overlying driver or application can obtain the current parameters for a queue and parameters for the filters that are set on a queue.

To change the current configuration parameters of a queue, overlying drivers can use the [OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](./oid-receive-filter-queue-parameters.md) set OID request. The overlying driver provides a pointer to an [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_parameters) structure in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure.

The NDIS\_RECEIVE\_QUEUE\_PARAMETERS structure is used in the [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](./oid-receive-filter-allocate-queue.md) OID and the [OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](./oid-receive-filter-queue-parameters.md) OID. For more information about allocating queues, see [Allocating a VM Queue](allocating-a-vm-queue.md).

To get the current configuration parameters of a queue, overlying drivers can use the OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS method OID request. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure initially contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_parameters) structure with a queue identifier of type NDIS\_RECEIVE\_QUEUE\_ID. After a successful return from the OID method request, the **InformationBuffer** member of the NDIS\_OID\_REQUEST structure contains a pointer to an **NDIS\_RECEIVE\_QUEUE\_PARAMETERS** structure.

NDIS handles the method request for miniport drivers. Therefore, the OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS method OID request is not requested for miniport drivers. NDIS obtained the information from an internal cache of the data that it received from the OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE and OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS OID requests.

To get the current configuration parameters of a filter on a receive queue, overlying drivers can use the [OID\_RECEIVE\_FILTER\_PARAMETERS](./oid-receive-filter-parameters.md) method OID request. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure initially contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters) structure. NDIS uses the **FilterId** member in the input structure to identify the filter. After a successful return from the method request, the **InformationBuffer** member of the NDIS\_OID\_REQUEST structure contains a pointer to an updated NDIS\_RECEIVE\_FILTER\_PARAMETERS structure.

NDIS handles the OID\_RECEIVE\_FILTER\_PARAMETERS method OID request for miniport drivers. NDIS obtained the information from an internal cache of the data that it received from the [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) OID request.

Overlying drivers can use the OID\_RECEIVE\_FILTER\_PARAMETERS method OID request to get the configuration parameters for a filter on a receive queue.

The overlying driver obtained the filter identifier from an earlier OID\_RECEIVE\_FILTER\_SET\_FILTER method OID request or from the [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md) OID request. Only drivers can use the OID\_RECEIVE\_FILTER\_SET\_FILTER request.

An application obtained the filter identifier from the [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md) OID request.

 

