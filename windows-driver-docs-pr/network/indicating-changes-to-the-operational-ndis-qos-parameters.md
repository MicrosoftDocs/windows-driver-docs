---
title: Indicating Changes to the Operational NDIS QoS Parameters
description: Indicating Changes to the Operational NDIS QoS Parameters
ms.assetid: BAE99C83-2732-4216-BC49-23F541AA3F10
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating Changes to the Operational NDIS QoS Parameters


The miniport driver that supports NDIS Quality of Service (QoS) issues an [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication when the driver's operational NDIS QoS parameters are resolved for the first time or when they change later. The miniport driver configures the network adapter with these operational parameters to perform QoS packet transmission.

The miniport driver must follow these guidelines for issuing an [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication:

-   The miniport driver must issue an [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication after it has resolved its operational NDIS QoS parameters and configured the network adapter with them.

    **Note**  If the miniport driver is provisioned with proprietary local NDIS QoS parameters in the registry, the driver must issue an [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication during or immediately after the call to [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389). In this case, the driver initializes an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure with its proprietary local NDIS QoS parameter settings.

    For more information about how the driver resolves its operational NDIS QoS parameter settings, see [Resolving Operational NDIS QoS Parameters](resolving-operational-ndis-qos-parameters.md).

-   After this initial status indication, the miniport driver should issue an [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication when its operational NDIS QoS parameters are changed. For example, the operational NDIS QoS parameters could change under the following conditions:

    -   The operational NDIS QoS parameters change because of changes to the local NDIS QoS parameters. These parameters could change through an OID method request of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835) or through a management application developed by the independent hardware vendor (IHV).

    -   The operational NDIS QoS parameters change because of conflicts with the QoS settings from the remote peer.

        The miniport driver uses the IEEE 802.1Qaz Data Center Bridging Exchange (DCBX) protocol to discover the QoS parameters for a remote peer. If the DCBX Willing state is enabled, the driver must resolve the differences between its QoS parameters and the remote peer's QoS parameters by following the procedures that are defined for the DCBX state engine. For more information about this state engine, refer to the IEEE 802.1Qaz draft standard.

        For more information about the local DCBX Willing state, see [Managing the Local DCBX Willing State](managing-the-local-dcbx-willing-state.md).

    **Note**  When the miniport driver receives local or remote NDIS QoS parameters, it should not issue an [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication if there have been no changes to the operational NDIS QoS parameters. If the driver makes this unnecessary status indication, NDIS may not pass the indication to overlying drivers.

-   The miniport driver should issue an [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication when it needs to override the local NDIS QoS parameters that were used to resolve the operational NDIS QoS parameters.

    The miniport driver notifies NDIS and the overlying driver that it has overridden the local NDIS QoS parameters by issuing an [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication. For this type of indication, the driver must set the appropriate **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CHANGED** flags in the **Flags** member of the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure to specify the reason for overriding the local NDIS QoS parameters.

    For more information on how the miniport driver manages the local QoS parameters, see [Setting Local NDIS QoS Parameters](setting-local-ndis-qos-parameters.md).

    For more information on how the miniport driver resolves its operational QoS parameters, see [Resolving Operational NDIS QoS Parameters](resolving-operational-ndis-qos-parameters.md).

**Note**  The miniport driver must issue [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indications if its NDIS QoS capabilities are currently enabled through the **\*QOS** keyword standardized INF keyword. For more information, see [Standardized INF Keywords for NDIS QoS](standardized-inf-keywords-for-ndis-qos.md).

## Guidelines for Issuing the NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE Status Indication


The miniport driver follows these steps when it issues the [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication:

1.  The miniport driver allocates a buffer that is large enough to contain the following:

    -   An [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure that contains the NDIS QoS configuration settings as well as global operational parameters for the NDIS QoS traffic classes.

    -   An array of [**NDIS\_QOS\_CLASSIFICATION\_ELEMENT**](https://msdn.microsoft.com/library/windows/hardware/hh451631) structures. Each of these structures specifies a traffic classification as defined by a packet data pattern (*condition*) and associated IEEE 802.1p priority level (*action*). If the network adapter finds a pattern in the transmit, or *egress*, packet that matches a condition, it assigns the associated priority level to the packet. The adapter also applies the other NDIS QoS policies to the packet based on the priority level.

2.  The miniport initializes the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure with the operational NDIS QoS parameters. The driver must provide the complete set of operational parameters, including those parameters that may not be configured on the network adapter.

    When the miniport driver initializes the **Header** member, it sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_QOS\_PARAMETERS. The miniport driver sets the **Revision** member of **Header** to NDIS\_QOS\_PARAMETERS\_REVISION\_1 and the **Size** member to NDIS\_SIZEOF\_QOS\_PARAMETERS\_REVISION\_1.

    The miniport driver sets the appropriate **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CHANGED** flags in the **Flags** member if the corresponding members contain data that has changed since the miniport driverissued an [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication.

    **Note**   Setting the **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CHANGED** flags is optional. NDIS always assumes that the members of the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) are current even if they have not changed from the previous [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) status indication.

    For more information on how to set the **Flags** member, see [Guidelines for Setting the **Flags** Member](#flags).

3.  The miniport driver initializes an [**NDIS\_QOS\_CLASSIFICATION\_ELEMENT**](https://msdn.microsoft.com/library/windows/hardware/hh451631) structure for each traffic classification from the operational NDIS QoS parameters. The driver adds these elements at the end of the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure in the buffer.

    **Note**  The miniport driver must not set the NDIS\_QOS\_CLASSIFICATION\_ENFORCED\_BY\_MINIPORT flag in the **Flags** member of any [**NDIS\_QOS\_CLASSIFICATION\_ELEMENT**](https://msdn.microsoft.com/library/windows/hardware/hh451631) structures.

    The driver sets the **NumClassificationElements** member of the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure to the number of classification elements in the array. The driver sets the **FirstClassificationElementOffset** member to the byte offset of the first element from the start of the buffer. The driver also sets the **ClassificationElementSize** member to the length, in bytes, of each element in the array.

    **Note**  Starting with NDIS 6.30, the miniport driver must set the **ClassificationElementSize** member to `sizeof(NDIS_QOS_CLASSIFICATION_ELEMENT`).

4.  The miniport driver initializes an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure for the status indication in the following way:

    -   The **StatusCode** member must be set to NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE.

    -   The **StatusBuffer** member must be set to the pointer to the buffer that contains the operational NDIS QoS parameters.

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

**Note**  The **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CONFIGURED** flags must be set if the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure contains NDIS QoS parameter settings. The miniport driver must set these flags regardless of whether the settings have changed. However, the driver must set the **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CHANGED** flags only for those settings that have changed.