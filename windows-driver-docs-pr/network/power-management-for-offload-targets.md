---
title: Power Management for Offload Targets
description: Power Management for Offload Targets
ms.assetid: 3d32d617-cf6d-4fe7-9feb-be2e36fd3006
keywords:
- TCP chimney offload WDK networking , power management
- chimney offload WDK networking , power management
- power management WDK networking , TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power Management for Offload Targets


\[The TCP chimney offload feature is deprecated and should not be used.\]

For an offload target, a device power state other than D0 (the fully powered state) might not be suitable for processing offloaded TCP connections. In this situation, the host stack initiates a terminate offload operation for all offloaded TCP connections before an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) request is sent to the offload target.

An offload target should not return a value of NDIS\_STATUS\_SUCCESS for [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) until the terminate offload operation has completed for all offloaded TCP connections. The offload target can return a value of NDIS\_STATUS\_PENDING to complete the OID\_PNP\_SET\_POWER request asynchronously. After the terminate offload operation has completed for all offloaded TCP connections, the offload target must call the [**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622) function and return a value of NDIS\_STATUS\_SUCCESS to inform NDIS that the OID\_PNP\_SET\_POWER request is complete.

 

 





