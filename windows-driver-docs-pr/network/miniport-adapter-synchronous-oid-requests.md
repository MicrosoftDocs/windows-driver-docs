---
title: Miniport Adapter Synchronous OID Requests
description: This topic describes miniport adapter Synchronous OID requests
ms.assetid: E169972C-2EFF-4005-B279-9EFC53B431E2
keywords: Miniport Adapter Synchronous OID Requests Interface, Miniport Adapter Synchronous OID call, WDK Miniport Adapter Synchronous OIDs, Miniport Adapter Synchronous OID request
ms.author: windowsdriverdev
ms.date: 09/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Miniport Adapter Synchronous OID Requests

To support the Synchronous OID request path, miniport drivers provide a [*MiniportSynchronousOidRequest*](TBD) function entry point in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure when they call the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function.

For miniport drivers, the *Synchronous OID request interface* differs from the Regular and Direct OID request interfaces in that miniport drivers do not have to register an asynchronous *complete* callback function. This is because of the synchronous nature of the path. For more info about the differences between Regular, Direct, and Synchronous OIDs in general, see [Synchronous OID Request Interface in NDIS 6.80](synchronous-oid-request-interface-in-ndis-6-80.md).

> [!NOTE]
> NDIS 6.80 supports specific OIDs for use with the Synchronous OID request interface. OIDs that existed before NDIS 6.80 and some NDIS 6.80 OIDs are not supported. To determine if an OID can be used in the Synchronous OID request interface, see the OID reference page.

To support the Synchronous OID request interface, use the documentation for the standard OID request interface. The following table shows the relationship between the functions in the Synchronous OID request interface and the standard OID request interface.

| Synchronous OID function | Standard OID function |
| --- | --- |
| [*MiniportSynchronousOidRequest*](TBD) | [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")