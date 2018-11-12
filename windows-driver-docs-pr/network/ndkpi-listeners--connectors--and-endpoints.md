---
title: NDKPI listeners, connectors, and endpoints
description: This section describes NDKPI listeners, connectors, and endpoints, and reference counting for connectors and endpoints
ms.assetid: 956D3550-11C8-48D0-BCF4-9027515C7C0E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDKPI Listeners, Connectors, and Endpoints


An NDK consumer connects an NDK connector by calling the *NdkConnect* ([*NDK\_FN\_CONNECT*](https://msdn.microsoft.com/library/windows/hardware/hh439865)) or *NdkConnectWithSharedEndpoint* ([*NDK\_FN\_CONNECT\_WITH\_SHARED\_ENDPOINT*](https://msdn.microsoft.com/library/windows/hardware/hh439868)) function.

Each connector that is in a connected state also has an underlying endpoint that represents the local end of the established NDK connection:

-   A connector that is established by accepting an incoming connection over an NDK listener automatically inherits the listener's implicit endpoint as its local implicit endpoint.
-   A connector that is connected via the *NdkConnect* function has its own dedicated implicit local endpoint.
-   A connector that is connected via the *NdkConnectWithSharedEndpoint* function has an explicit local endpoint that can be shared with other connectors that are also connected via the *NdkConnectWithSharedEndpoint* function.

The NDK provider must keep some sort of reference count for each implicit or explicit endpoint, and release the endpoint (i.e., mark the address/port as available to be used again) when the reference count reaches zero:

### Reference Counting for (Non-Shared) Endpoints

When the consumer calls the *NdkListen* ([*NDK\_FN\_LISTEN*](https://msdn.microsoft.com/library/windows/hardware/hh439902)) function, the provider creates an implicit endpoint. For this implicit endpoint, the provider must maintain a reference count as follows:

-   Add a reference for the listener itself to the endpoint's reference count.
-   Add a reference for each connector that is accepted over that listener.
-   Remove a reference when a connector that was previously accepted over the listener is closed.
-   Remove a reference when the listener itself is closed.
    **Note**  You can't close the listener until all the connectors are closed.

     

-   Release the endpoint when its reference count returns to zero. (This is the case only when the listener and all the connectors accepted over the listener have been closed.)
-   Simply closing the listener does not release the endpoint as long as there are previously accepted connectors that are not yet closed. This means that new *NdkListen*, *NdkConnect*, and *NdkConnectWithSharedEndpoint* requests for the same local address and port will fail until all such connections are closed. Note that the close request on the listener will also remain pending until all such connections are closed (due to the antecedent/successor rules outlined in [NDKPI Object Lifetime Requirements](ndkpi-object-lifetime-requirements.md)). The provider must reject further incoming connections on the listener as soon as a close request is issued (so that no new connections are accepted while the close request is pending).

### Reference Counting for Connectors

When the consumer calls *NdkConnect*, the provider creates and implicit endpoint. For this implicit endpoint, the provider must:

-   Add a reference by the connector. There is only one connector, hence only one reference.
-   Remove the connector's reference to the endpoint when the connector is closed.
-   Release the endpoint when that reference is gone.

### Reference Counting for Shared Endpoints

When the consumer calls *NdkConnectWithSharedEndpoint*, the provider creates an explicit shared endpoint. For this explicit shared endpoint, the provider must:

-   Add a reference for the shared endpoint itself to the shared endpoint's reference count.
-   Add a reference for each connector that is connected over that shared endpoint.
-   Remove a reference when a connector that was previously connected over the shared endpoint is closed.
-   Release the endpoint the reference count returns to zero. (This is the case when the shared endpoint and all the connectors connected over the shared endpoint have been closed.)
-   Simply closing the shared endpoint does not release the endpoint as long as there are previously connected connectors that are not yet closed. This means that new *NdkListen*, *NdkConnect*, and *NdkConnectWithSharedEndpoint* requests for the same local address and port will fail until all such connections are closed. Note that the close request on the shared endpoint will also remain pending until all such connections are closed (due to the antecedent/successor rules outlined in [NDKPI Object Lifetime Requirements](ndkpi-object-lifetime-requirements.md)).

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






