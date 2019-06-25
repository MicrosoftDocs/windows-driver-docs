---
title: Initializing an NDK-Capable Miniport Driver
description: A miniport driver that supports Network Direct kernel (NDK) is initialized in the same way as other miniport drivers. However, it must also register additional NDKPI entry points.
ms.assetid: 9C9799AB-75A8-4E9A-8702-D389B73522DC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing an NDK-Capable Miniport Driver


A miniport driver that supports Network Direct kernel (NDK) is initialized in the same way as other miniport drivers. However, it must also register additional NDKPI entry points.

-   [DriverEntry function](#driverentry-function)
-   [MiniportSetOptions function](#miniportsetoptions-function)
-   [Related topics](#related-topics)

## DriverEntry function


Every miniport driver's [*DriverEntry*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize) function initializes an [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure and passes it to [**NdisMRegisterMiniportDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismregisterminiportdriver) as described in the following pages:

-   [Initializing a Miniport Driver](initializing-a-miniport-driver.md)
-   [**DriverEntry of NDIS Miniport Drivers function**](https://docs.microsoft.com/windows-hardware/drivers/network/initializing-a-miniport-driver)

The NDK-capable miniport driver must do the following when initializing the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure:

-   In the **OidRequestHandler** member, the miniport driver must register a [*MiniportOidRequest*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_oid_request) function that supports:

    -   All [NDKPI OIDs](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/index).

    -   Any OIDs that are mandatory for NDIS miniport drivers in general.

        **Note**  For a list of these mandatory OIDs, see [Mandatory OIDs for Miniport Drivers](https://docs.microsoft.com/windows-hardware/drivers/network/mandatory-oids-for-miniport-drivers).

         

-   In the **SetOptionsHandler** member, the miniport driver must register a [*MiniportSetOptions*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-set_options) function as described in [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md) and the following MiniportSetOptions function section.

## MiniportSetOptions function


NDIS calls the [*MiniportSetOptions*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-set_options) function immediately after the miniport driver's [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/network/initializing-a-miniport-driver) function returns. The *MiniportSetOptions* function is called in the context of the miniport driver's call to [**NdisMRegisterMiniportDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismregisterminiportdriver).

In its [*MiniportSetOptions*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-set_options) function, the NDK-capable miniport driver registers its NDK capability and registers the following required NDKPI function entry points as described in [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md):

-   *OpenNDKAdapterHandler* ([*OPEN\_NDK\_ADAPTER\_HANDLER*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndisndk/nc-ndisndk-open_ndk_adapter_handler))

-   *CloseNDKAdapterHandler* ([*CLOSE\_NDK\_ADAPTER\_HANDLER*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndisndk/nc-ndisndk-close_ndk_adapter_handler))

To register NDKPI entry points for these functions, the miniport driver's [*MiniportSetOptions*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-set_options) function must do the following:

1.  Initialize an [**NDIS\_NDK\_PROVIDER\_CHARACTERISTICS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndisndk/ns-ndisndk-_ndis_ndk_provider_characteristics) structure.

    **Note**  Pay particular attention to the **Header** member description. The miniport driver must set this member correctly to identify itself as an NDK-capable miniport driver.

     

2.  Store the function entry points in the **OpenNDKAdapterHandler** and **CloseNDKAdapterHandler** members of the structure.

3.  Call the [**NdisSetOptionalHandlers**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndissetoptionalhandlers) function, passing the structure in the *OptionalHandlers* parameter.

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






