---
title: Indicating Changes to the Remote NDIS QoS Parameters
description: Indicating Changes to the Remote NDIS QoS Parameters
ms.assetid: E09EBF25-96B6-417F-9538-D0BEBE5B9E19
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating Changes to the Remote NDIS QoS Parameters


The miniport driver that supports NDIS Quality of Service (QoS) issues an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication when its remote NDIS QoS parameters are either received from a peer for the first time or change later. The miniport driver receives these QoS parameters from a remote peer through the IEEE 802.1Qaz Data Center Bridging Exchange (DCBX) protocol.

The miniport driver must follow these guidelines for issuing an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication:

-   If the miniport driver has not received a DCBX frame from a remote peer, it must not issue an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication.

-   The miniport driver must issue an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication after it has first received the QoS settings from a remote peer.

    **Note**  The miniport driver must issue this status indication if the network adapter receives remote QoS parameter settings from a peer before the driver's local QoS parameters are set. For more information, see [Setting Local NDIS QoS Parameters](setting-local-ndis-qos-parameters.md).

-   After this initial status indication, the miniport driver should only issue an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication when it determines a change in the QoS settings on the remote peer.

    **Note**  Miniport drivers should not issue an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication if there have been no changes to the remote NDIS QoS parameters. If the driver does make this type of status indication, NDIS may not pass the indication to overlying drivers.

**Note**  The miniport driver must issue [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indications if its NDIS QoS capabilities are currently enabled. Starting with Windows Server 2012, these indications allow system administrators to view NDIS QoS and Data Center Bridging (DCB) settings regardless of whether the Microsoft DCB server feature is installed.



## Guidelines for Issuing the NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE Status Indication


The miniport driver follows these steps when it issues the [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication:

1.  The miniport driver allocates a buffer that is large enough to contain the following:

    -   An [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure that contains the NDIS QoS configuration settings as well as global operational parameters for the NDIS QoS traffic classes.

    -   An array of [**NDIS\_QOS\_CLASSIFICATION\_ELEMENT**](https://msdn.microsoft.com/library/windows/hardware/hh451631) structures. Each of these structures specifies a traffic classification as defined by a packet data pattern (*condition*) and associated IEEE 802.1p priority level (*action*). If the network adapter finds a pattern in the transmit, or *egress*, packet that matches a condition, it assigns the associated priority level to the packet. The adapter also applies the other NDIS QoS policies to the packet based on the priority level.

2.  The miniport initializes the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure with the remote NDIS QoS parameters. The driver must provide the complete set of remote parameters that were received from the DCBX frame sent by the remote peer.

    When the miniport driver initializes the **Header** member, it sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_QOS\_PARAMETERS. The miniport driver sets the **Revision** member of **Header** to NDIS\_QOS\_PARAMETERS\_REVISION\_1 and the **Size** member to NDIS\_SIZEOF\_QOS\_PARAMETERS\_REVISION\_1.

    The miniport driver sets the appropriate **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CHANGED** flags if the corresponding members contain data that has changed since the miniport driver previously issued an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication.

    **Note**   Setting these **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CHANGED** flags is optional. NDIS always assumes that the members of the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) are specified even if they have not changed from the previous [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication.

    The miniport driver sets the **Flags** member to specify status information for the data that is contained in the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure members.

    For example, the miniport driver sets the appropriate **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CHANGED** flags in the **Flags** member for those members which contain data that has changed since the miniport driver previously issued an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication.

    For more information on how to set the **Flags** member, see [Guidelines for Setting the **Flags** Member](#flags).

3.  The miniport driver initializes an [**NDIS\_QOS\_CLASSIFICATION\_ELEMENT**](https://msdn.microsoft.com/library/windows/hardware/hh451631) structure for each traffic classification from the remote NDIS QoS parameters. The driver adds these elements past the end of the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure in the buffer.

    **Note**  The miniport driver must not set the NDIS\_QOS\_CLASSIFICATION\_ENFORCED\_BY\_MINIPORT flag in the **Flags** member of any [**NDIS\_QOS\_CLASSIFICATION\_ELEMENT**](https://msdn.microsoft.com/library/windows/hardware/hh451631) structures.

    The driver sets the **NumClassificationElements** member of the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure to the number of classification elements in the array. The driver sets the **FirstClassificationElementOffset** member to the byte offset of the first element from the start of the buffer. The driver also sets the **ClassificationElementSize** member to the length, in bytes, of each element in the array.

    **Note**  Starting with NDIS 6.30, the miniport driver must set the **ClassificationElementSize** member to `sizeof(NDIS_QOS_CLASSIFICATION_ELEMENT`).

4.  The miniport driver initializes an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure for the status indication in the following way:

    -   The **StatusCode** member must be set to NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE.

    -   The **StatusBuffer** member must be set to the pointer to the buffer that contains the remote NDIS QoS parameters.

    -   The **StatusBufferSize** member must be set to the length, in bytes, of the buffer.

5.  The miniport driver issues the status indication by calling [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600). The driver must pass a pointer to the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure to the *StatusIndication* parameter.

## Guidelines for Setting the Flags Member

The miniport driver sets the following flags in the **Flags** member of the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure to specify which operational NDIS QoS parameters have been configured or changed on the network adapter:

<a href="" id="ndis-qos-parameters-ets-configured"></a>**NDIS\_QOS\_PARAMETERS\_ETS\_CONFIGURED**  
If this flag is set, the miniport driver has configured the network adapter with the ETS parameters contained in the following members:

-   **NumTrafficClasses**

-   **PriorityAssignmentTable**

-   **TcBandwidthAssignmentTable**

-   **TsaAssignmentTable**

**Note**  The miniport driver must support ETS in order to support NDIS QoS for DCB. However, the setting of this flag does not specify whether the network adapter supports ETS. Instead, the setting of this flag specifies only whether ETS parameters are configured on the network adapter.

<a href="" id="ndis-qos-parameters-ets-changed"></a>**NDIS\_QOS\_PARAMETERS\_ETS\_CHANGED**  
If this flag is set, one or more ETS parameters have changed in the following members:

-   **NumTrafficClasses**

-   **PriorityAssignmentTable**

-   **TcBandwidthAssignmentTable**

-   **TsaAssignmentTable**

<a href="" id="ndis-qos-parameters-pfc-configured"></a>**NDIS\_QOS\_PARAMETERS\_PFC\_CONFIGURED**  
If this flag is set, the miniport driver has configured the network adapter with the PFC settings contained in the **PfcEnable** member.

**Note**  The miniport driver must support PFC in order to support NDIS QoS for DCB. The setting of this flag does not specify whether the network adapter supports PFC. Instead, the setting of this flag specifies only whether PFC parameters are enabled on the network adapter.

<a href="" id="ndis-qos-parameters-pfc-changed"></a>**NDIS\_QOS\_PARAMETERS\_PFC\_CHANGED**  
If this flag is set, one or more PFC settings have changed in the **PfcEnable** member.

<a href="" id="ndis-qos-parameters-classification-configured"></a>**NDIS\_QOS\_PARAMETERS\_CLASSIFICATION\_CONFIGURED**  
If this flag is set, the miniport driver has configured the network adapter with the QoS traffic classifications parameters specified in the following members:

-   **NumClassificationElements**

-   **ClassificationElementSize**

-   **FirstClassificationElementOffset**

<a href="" id="ndis-qos-parameters-classification-changed"></a>**NDIS\_QOS\_PARAMETERS\_CLASSIFICATION\_CHANGED**  
If this flag is set, one or more QoS traffic classification parameters have changed in the following members:

-   **NumClassificationElements**

-   **ClassificationElementSize**

-   **FirstClassificationElementOffset**

**Note**  The **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CONFIGURED** flags must be set if the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure contains NDIS QoS parameter settings. The miniport driver must set these flags regardless of whether the settings have changed. However, the driver must only set the **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CHANGED** flags for those settings that have changed.

## Guidelines for Indicating Invalid Remote NDIS QoS Parameters


The miniport driver must invalidate its remote QoS parameters if the following conditions are true:

-   The time-to-live (TTL) value expires for the remote QoS parameters.

    **Note**  DCBX is carried over the Link Layer Discovery Protocol (LLDP) protocol as specified in the IEEE 802.1AB-2005 standard. LLDP frames always contain a TTL field.

-   Another data-link peer sends a DCBX frame before the TTL value expires. This scenario is known as a *multi-peer* condition. DCBX requires that the miniport driver maintain only one set of remote QoS parameters that were received from a single data-link peer.

    When a multi-peer condition occurs, the miniport driver must invalidate all of the remote QoS parameters until the TTL value expires for all of the received DCBX frames.

When the miniport driver invalidates its remote NDIS QoS parameters, it must follow these steps when it issues the [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication:

1.  Because the miniport driver is not reporting any valid remote NDIS QoS parameters, it must first fill an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure with zeros.

    When the miniport driver initializes the **Header** member of this structure, it sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_QOS\_PARAMETERS. The miniport driver sets the **Revision** member of **Header** to NDIS\_QOS\_PARAMETERS\_REVISION\_1 and the **Size** member to NDIS\_SIZEOF\_QOS\_PARAMETERS\_REVISION\_1.

    The miniport driver sets the appropriate **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CHANGED** flags in the **Flags** member.

2.  The miniport driver initializes an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure for the status indication in the following way:

    -   The **StatusCode** member must be set to NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE.

    -   The **StatusBuffer** member must be set to the address of the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure.

    -   The **StatusBufferSize** member must be set to `sizeof(NDIS_QOS_PARAMETERS)`.

3.  The miniport driver issues the status indication by calling [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600). The driver must pass a pointer to the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure to the *StatusIndication* parameter.