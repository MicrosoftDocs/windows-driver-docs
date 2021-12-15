---
title: Initializing an NDK-Capable Miniport Driver
description: A miniport driver that supports Network Direct kernel (NDK) is initialized in the same way as other miniport drivers. However, it must also register additional NDKPI entry points.
ms.date: 04/20/2017
---

# Initializing an NDK-Capable Miniport Driver


A miniport driver that supports Network Direct kernel (NDK) is initialized in the same way as other miniport drivers. However, it must also register additional NDKPI entry points.

-   [DriverEntry function](#driverentry-function)
-   [MiniportSetOptions function](#miniportsetoptions-function)
-   [Related topics](#related-topics)

## DriverEntry function


Every miniport driver's [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function initializes an [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure and passes it to [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) as described in the following pages:

-   [Initializing a Miniport Driver](initializing-a-miniport-driver.md)
-   [**DriverEntry of NDIS Miniport Drivers function**](./initializing-a-miniport-driver.md)

The NDK-capable miniport driver must do the following when initializing the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure:

-   In the **OidRequestHandler** member, the miniport driver must register a [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function that supports:

    -   All [NDKPI OIDs](/windows-hardware/drivers/ddi/ntddndis/index).

    -   Any OIDs that are mandatory for NDIS miniport drivers in general.

        **Note**  For a list of these mandatory OIDs, see [Mandatory OIDs for Miniport Drivers](./mandatory-oids-for-miniport-drivers.md).

         

-   In the **SetOptionsHandler** member, the miniport driver must register a [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function as described in [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md) and the following MiniportSetOptions function section.

## MiniportSetOptions function


NDIS calls the [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function immediately after the miniport driver's [**DriverEntry**](./initializing-a-miniport-driver.md) function returns. The *MiniportSetOptions* function is called in the context of the miniport driver's call to [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver).

In its [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function, the NDK-capable miniport driver registers its NDK capability and registers the following required NDKPI function entry points as described in [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md):

-   *OpenNDKAdapterHandler* ([*OPEN\_NDK\_ADAPTER\_HANDLER*](/windows-hardware/drivers/ddi/ndisndk/nc-ndisndk-open_ndk_adapter_handler))

-   *CloseNDKAdapterHandler* ([*CLOSE\_NDK\_ADAPTER\_HANDLER*](/windows-hardware/drivers/ddi/ndisndk/nc-ndisndk-close_ndk_adapter_handler))

To register NDKPI entry points for these functions, the miniport driver's [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function must do the following:

1.  Initialize an [**NDIS\_NDK\_PROVIDER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndisndk/ns-ndisndk-_ndis_ndk_provider_characteristics) structure.

    **Note**  Pay particular attention to the **Header** member description. The miniport driver must set this member correctly to identify itself as an NDK-capable miniport driver.

     

2.  Store the function entry points in the **OpenNDKAdapterHandler** and **CloseNDKAdapterHandler** members of the structure.

3.  Call the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function, passing the structure in the *OptionalHandlers* parameter.

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](./overview-of-network-direct-kernel-provider-interface--ndkpi-.md)

 

