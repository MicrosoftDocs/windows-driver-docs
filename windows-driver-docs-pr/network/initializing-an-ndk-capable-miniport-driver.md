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


Every miniport driver's [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) function initializes an [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure and passes it to [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) as described in the following pages:

-   [Initializing a Miniport Driver](initializing-a-miniport-driver.md)
-   [**DriverEntry of NDIS Miniport Drivers function**](https://msdn.microsoft.com/library/windows/hardware/ff548818)

The NDK-capable miniport driver must do the following when initializing the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure:

-   In the **OidRequestHandler** member, the miniport driver must register a [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function that supports:

    -   All [NDKPI OIDs](https://msdn.microsoft.com/library/windows/hardware/jj206455).

    -   Any OIDs that are mandatory for NDIS miniport drivers in general.

        **Note**  For a list of these mandatory OIDs, see [Mandatory OIDs for Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff557139).

         

-   In the **SetOptionsHandler** member, the miniport driver must register a [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function as described in [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md) and the following MiniportSetOptions function section.

## MiniportSetOptions function


NDIS calls the [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function immediately after the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548818) function returns. The *MiniportSetOptions* function is called in the context of the miniport driver's call to [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654).

In its [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function, the NDK-capable miniport driver registers its NDK capability and registers the following required NDKPI function entry points as described in [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md):

-   *OpenNDKAdapterHandler* ([*OPEN\_NDK\_ADAPTER\_HANDLER*](https://msdn.microsoft.com/library/windows/hardware/hh440105))

-   *CloseNDKAdapterHandler* ([*CLOSE\_NDK\_ADAPTER\_HANDLER*](https://msdn.microsoft.com/library/windows/hardware/hh439355))

To register NDKPI entry points for these functions, the miniport driver's [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function must do the following:

1.  Initialize an [**NDIS\_NDK\_PROVIDER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/hh451566) structure.

    **Note**  Pay particular attention to the **Header** member description. The miniport driver must set this member correctly to identify itself as an NDK-capable miniport driver.

     

2.  Store the function entry points in the **OpenNDKAdapterHandler** and **CloseNDKAdapterHandler** members of the structure.

3.  Call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function, passing the structure in the *OptionalHandlers* parameter.

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






