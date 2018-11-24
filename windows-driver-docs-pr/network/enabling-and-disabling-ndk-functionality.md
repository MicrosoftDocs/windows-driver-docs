---
title: Enabling and Disabling NDK Functionality
description: To enable or disable NDK functionality, NDIS issues an OID_NDK_SET_STATE OID request. An NDK-capable miniport driver must register support for this OID in its MiniportOidRequest function.
ms.assetid: A72AD98E-FF84-48FF-B627-5534231244B0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling and Disabling NDK Functionality


To enable or disable NDK functionality, NDIS issues an [OID\_NDK\_SET\_STATE](https://msdn.microsoft.com/library/windows/hardware/hh451812) OID request. An NDK-capable miniport driver must register support for this OID in its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

## Determining whether NDK functionality can be enabled


The **\*NetworkDirect** keyword determines whether the miniport driver's NDK functionality can be enabled.

If this keyword value is set to 1 ("Enabled"), NDK functionality can be enabled.

If it is set to 0 ("Disabled"), NDK functionality cannot be enabled.

When the miniport driver is installed, its INF file sets this keyword value to 1 ("Enabled") by default. For more information, see [INF Requirements for NDKPI](inf-requirements-for-ndkpi.md).

After the miniport driver is installed, administrators can update the **\*NetworkDirect** keyword value by setting a new value in the **Advanced** property page for the adapter. For more information about advanced properties, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

**Note**   The miniport driver is automatically restarted after a change is made in the **Advanced** property page for the adapter.

 

## When to enable or disable NDK functionality


This state change can be triggered by an [OID\_NDK\_SET\_STATE](https://msdn.microsoft.com/library/windows/hardware/hh451812) OID request, or by a success or failure in the adapter itself.

## Enabling or disabling NDK functionality


To enable or disable its NDK functionality, the miniport driver must send a **NetEventNDKEnable** or **NetEventNDKDisable** Plug and Play (PnP) event to NDIS.

To send the PnP event, the miniport driver calls the [**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616) function, setting the **NetPnPEvent** member of the [**NET\_PNP\_EVENT\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff568752) structure that the *NetPnPEvent* parameter points to as follows:

-   **NetEventNDKEnable** if NDK functionality is to be enabled.

-   **NetEventNDKDisable** if NDK functionality is to be disabled.

The **NetEventNDKDisable** PnP event triggers NDIS and upper layer drivers to start closing their opened [**NDK\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/hh439848) instances over the adapter where the NDK functionality is being disabled. The PnP event will remain pending until all of the opened **NDK\_ADAPTER** instances over the adapter are closed.

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






