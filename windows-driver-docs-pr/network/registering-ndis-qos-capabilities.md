---
title: Registering NDIS QoS Capabilities
description: Registering NDIS QoS Capabilities
ms.assetid: 03D70079-37A4-4FAA-BF18-ACED3A9E8267
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering NDIS QoS Capabilities


Miniport drivers regsiter the following Quality of Service (QoS) capabilities with NDIS during network adapter initialization:

- The NDIS QoS hardware capabilities that the network adapter supports.

  **Note**  Starting with NDIS 6.30, the miniport driver must register the NDIS QoS hardware capabilities that the adapter supports only if the<strong>\*QOS</strong> INF keyword setting is present in the registry. In this case, the driver must register its NDIS QoS hardware capabilities regardless of whether those capabilities are enabled or disabled on the adapter.

     

- The NDIS QoS hardware capabilities that are currently enabled on the network adapter.

  **Note**  A miniport driver's NDIS QoS hardware capabilities can be enabled or disabled through the **\*QOS** INF keyword setting in the registry. This setting is displayed on the **Advanced** property page for the network adapter.

     

For more information about the NDIS QoS INF keyword settings, see [Standardized INF Keywords for NDIS QoS](standardized-inf-keywords-for-ndis-qos.md).

The miniport driver reports the hardware NDIS QoS capabilities of the underlying network adapter through an [**NDIS\_QOS\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451629) structure that is initialized in the following way:

1.  The miniport driver initializes the **Header** member. The driver sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_QOS\_CAPABILITIES.

    Starting with NDIS 6.30, the miniport driver sets the **Revision** member of **Header** to NDIS\_QOS\_CAPABILITIES\_REVISION\_1 and the **Size** member to NDIS\_SIZEOF\_QOS\_CAPABILITIES\_REVISION\_1.

2.  If the network adapter supports the strict priority transmission selection algorithm (TSA), the miniport driver sets the NDIS\_QOS\_CAPABILITIES\_STRICT\_TSA\_SUPPORTED flag in the **Flags** member. For more information on this algorithm, see [Strict Priority Algorithm](strict-priority-algorithm.md).

    **Note**  Starting with NDIS 6.30, the miniport driver and network adapter that support NDIS QoS for IEEE Data Center Bridging (DCB) must support the strict priority TSA.

     

3.  If the network adapter supports the ability to bypass media access control security (MACsec) processing, the miniport driver sets the NDIS\_QOS\_CAPABILITIES\_MACSEC\_BYPASS\_SUPPORTED flag in the **Flags** member. For more information about MACsec, refer to the IEEE 802.1AE-2006 standard.

    **Note**  Starting with NDIS 6.30, the network adapter does not need to support the bypass of MACsec processing.

     

4.  The miniport driver sets the **MaxNumTrafficClasses** member to the maximum number of NDIS QoS traffic classes that the network adapter supports. A traffic class defines the transmit, or *egress* policies for QoS, such as IEEE 802.1p priority level and bandwidth allocation. For more information about traffic classes, see [NDIS QoS Traffic Classes](ndis-qos-traffic-classes.md).

    **Note**  Starting with NDIS 6.30, the network adapter must support a minimum of three traffic classes.

     

5.  The miniport driver sets the **MaxNumEtsCapableTrafficClasses** member to the maximum number of NDIS QoS traffic classes that the network adapter can use with the Enhanced Transmission Selection (ETS) algorithm. This value must be less than or equal to the value of the **MaxNumTrafficClasses** member.

    For more information on ETS, see [Enhanced Transmission Selection (ETS) Algorithm](enhanced-transmission-selection--ets--algorithm.md).

    **Note**  For the network adapter to support NDIS QoS, it must support a minimum of two ETS-capable traffic classes.

     

6.  The miniport driver sets the **MaxNumPfcEnabledTrafficClasses** member to the maximum number of NDIS QoS traffic classes that the network adapter can use with the Priority-based Flow Control (PFC) algorithm. This value must be less than or equal to the value of the **MaxNumTrafficClasses** member.

    For more information on PFC, see [Priority-based Flow Control (PFC)](priority-based-flow-control--pfc.md).

    **Note**  For the network adapter to support NDIS QoS, it must support at least one PFC-capable traffic class.

     

When NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the driver registers the NDIS QoS attributes of the network adapter by following these steps:

1.  The miniport driver initializes an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

    The miniport driver sets the **HardwareQOSCapabilities** member to a pointer to the previouslyinitialized [**NDIS\_QOS\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451629) structure.

    If the registry setting for the **\*QOS** INF keyword has a value of one, the NDIS QoS capabilities are enabled on the network adapter. The miniport driver sets the **CurrentQOSCapabilities** members to a pointer to the same [**NDIS\_QOS\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451629) structure.

    If the registry setting for the **\*QOS** INF keyword has a value of zero, the NDIS QoS capabilities are disabled on the network adapter. The miniport driver must set the **CurrentQOSCapabilities** member to NULL.

2.  The driver calls [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) and sets the *MiniportAttributes* parameter to a pointer to the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

For more information about the adapter initialization process, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

 

 





