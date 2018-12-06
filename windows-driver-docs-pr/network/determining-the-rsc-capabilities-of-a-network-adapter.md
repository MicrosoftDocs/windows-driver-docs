---
title: Determining the RSC Capabilities of a Network Adapter
description: A receive segment coalescing (RSC)-capable miniport driver reports its RSC capability by means of the NDIS_OFFLOAD structure that it passes to NdisMSetMiniportAttributes.
ms.assetid: 043A09F9-7D5D-4401-9645-19FDBD614659
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining the RSC Capabilities of a Network Adapter


A receive segment coalescing (RSC)-capable miniport driver reports its RSC capability by means of the [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure that it passes to [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).

## Reporting RSC Capability


In the [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure, the **Header** member must be set as follows:

-   The **Revision** member must be set to **NDIS\_OFFLOAD\_REVISION\_3**.
-   The **Size** member must be set to **NDIS\_SIZEOF\_NDIS\_OFFLOAD\_REVISION\_3**.

To report its support for RSC, a miniport driver can set the following members in the [**NDIS\_TCP\_RECV\_SEG\_COALESCE\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/hh439827) structure, which is stored in the **Rsc** member of the [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure:

-   Set the **IPv4.Enabled** member to **TRUE** to indicate support for RSC for IPv4.

-   Set the **IPv6.Enabled** member to **TRUE** to indicate support for RSC for IPv6.

The miniport driver must support RSC for at least IEEE 802.3 encapsulation. In addition, it can support RSC for any other encapsulations. If it does not support RSC for some encapsulation, and it receives packets of that encapsulation, the driver must indicate the packets up the stack normally.

## Querying RSC Capability


To determine whether a miniport driver supports RSC, protocol drivers and other drivers can issue the [OID\_TCP\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569806) OID request, which will return an [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure.

 

 





