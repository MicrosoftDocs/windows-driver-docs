---
title: Setting Local NDIS QoS Parameters
description: Setting Local NDIS QoS Parameters
ms.assetid: 7AB30829-16A0-46BF-8066-506E01E718A4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Local NDIS QoS Parameters


Local NDIS Quality of Service (QoS) parameters specify the locally provisioned QoS settings for a miniport driver and its network adapter. Miniport drivers obtain the local NDIS QoS parameters in the following ways:

-   Through an object identifier (OID) method request of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835) that is issued by the Data Center Bridging (DCB) component (Msdcb.sys). This OID request contains an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure that specifies the local NDIS QoS parameters.

    For more information on the DCB component, see [NDIS QoS Architecture for Data Center Bridging](ndis-qos-architecture-for-data-center-bridging.md).

    **Note**  Starting with Windows Server 2012, the DCB component is installed and enabled with the Microsoft Data Center Bridging (DCB) server feature. This feature is not installed by default.

     

-   Through proprietary settings that are stored in the system registry and defined by the independent hardware vendor (IHV) for the network adapter. The miniport driver reads these settings when its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called by NDIS.

-   Through proprietary settings issued to the miniport driver through a management application developed by the IHV.

When the DCB component issues an OID method request of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835), the **NDIS\_QOS\_PARAMETERS\_WILLING** flag of the **NDIS\_QOS\_PARAMETERS.Flags** member specifies how the miniport driver resolves its operational QoS parameters from the local NDIS QoS parameters. Based on this flag, the driver resolves the local QoS parameters in the following ways:

-   If the **NDIS\_QOS\_PARAMETERS\_WILLING** flag is set, the miniport driver must enable the local DCB Exchange (DCBX) Willing state. This allows the driver to be remotely configured with QoS parameters. In this case, the driver resolves its operational QoS parameters based on the remote QoS parameters.

    The miniport driver can also resolve its operational QoS parameters based on any proprietary QoS settings that are defined by the IHV. The driver can only do this for QoS parameters that are not configured remotely by the peer or locally by the operating system.

    For more information about this procedure, see [Receiving Remote NDIS QoS Parameters](receiving-remote-ndis-qos-parameters.md).

-   If the **NDIS\_QOS\_PARAMETERS\_WILLING** flag is not set, the miniport driver must disable the local DCBX Willing state. This allows the driver to resolve its operational QoS parameters from its local QoS parameters instead of remote QoS parameters.

    **Note**  If the local DCBX Willing state is disabled, the miniport driver can still accept the remote QoS parameters but cannot use them to resolve its operational QoS parameters.

     

If the local DCBX Willing state is disabled, the miniport driver must follow these guidelines when it manages its local QoS parameters:

-   The miniport driver must disable or override any local QoS parameter for which the related **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CONFIGURED** flag is not set in the **NDIS\_QOS\_PARAMETERS.Flags** member.

    For example, the miniport driver can override an unconfigured local QoS parameter with its proprietary settings for the QoS parameter that are defined by the IHV. If there are no proprietary settings for local QoS parameters that are not specified with an **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CONFIGURED** flag, the driver must disable the use of these QoS parameters on the network adapter.

    **Note**  NDIS guarantees that both the **NDIS\_QOS\_PARAMETERS\_ETS\_CONFIGURED** and **NDIS\_QOS\_PARAMETERS\_PFC\_CONFIGURED** flags are set or cleared together.

     

-   The miniport driver should *apply* the local QoS parameters that are contained in the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure when it resolves its operational NDIS QoS parameters. If the driver applies these local QoS parameters, it must not use any remote QoS parameters that it received from the remote peer.

    For more information on this procedure, see [Resolving Operational NDIS QoS Parameters](resolving-operational-ndis-qos-parameters.md).

For more information about the local DCBX Willing state, see [Managing the Local DCBX Willing State](managing-the-local-dcbx-willing-state.md).

 

 





