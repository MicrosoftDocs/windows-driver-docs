---
title: Miniport adapter OID request serialization
description: Miniport adapter OID request serialization
keywords: ["OIDs WDK networking , miniport adapter requests", "miniport adapters WDK networking , OID requests", "adapters WDK networking , OID requests", "object identifiers WDK networking", "OID serialization"]
---

# Miniport adapter OID request serialization

All OID requests to a miniport adapter are serialized by NDIS except for [direct OID requests](miniport-adapter-direct-oid-requests.md), which were designed not be serialized. A miniport adapter will not receive a new OID request until any pending request is completed. Therefore, miniport adapters must complete OIDs promptly.

>[!NOTE]
> We recommend completing an OID request in less than 1000ms, or 1 second, so the user will not notice any delay in performance. For specific information about timing OID requests, see the [NdisTimedOidComplete](https://msdn.microsoft.com/library/windows/hardware/dn305120) Driver Verifier rule.

One exception to this OID serialization rule is for Wi-Fi miniport adapters that use WDI, which may see a second OID request if they take too long to complete the previous OID. The following example explains what happens in this situation:

1. The first OID request is passed to the WDI miniport adapter.
2. The NIC does not respond to the OID within the time limit specified by the driver.
3. WDI calls the driver's [MINIPORT_WDI_ADAPTER_HANG_DIAGNOSE](https://msdn.microsoft.com/library/windows/hardware/mt297558) callback function to collect diagnostic data about the NIC.
4. The first OID is no longer considered to block serialization. This means the WDI miniport adapter can now receive other OID requests, even though the first OID is serialized. However, these other OIDS are also serialized, which means the WDI miniport adapter will not pend more than 2 OIDs simultaneously (the first OID that is still hung and a second OID).

## Related topics

For more information about WDI UE hang detection, see [UE hang detection: Steps 1-14](https://msdn.microsoft.com/windows/hardware/drivers/network/wdi-ue-hang-detection--step-1-to-step-14).

For more information about OID requests in NDIS, see [Simplifying your OID request handler](https://go.microsoft.com/fwlink/p/?linkid=846658) on the NDIS blog.

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")