---
title: Introduction to NDIS 6.40
description: This section introduces NDIS 6.40 and describes its major design additions. NDIS 6.40 is included in the Windows 8.1 and Windows Server 2012 R2 and later.
ms.assetid: 46DB94AA-DBAD-49E0-A1F0-FEB095E26F2C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to NDIS 6.40


This section introduces Network Driver Interface Specification (NDIS) 6.40 and describes its major design additions. NDIS 6.40 is included in the Windows 8.1 and Windows Server 2012 R2 and later operating systems.

## Feature Updates


Windows 8.1 and Windows Server 2012 R2 introduce minor updates to the following features:

### NDKPI

NDKPI 1.2 adds the following new elements to the NDKPI DDI:

- *NdkSendAndInvalidate* ([*NDK\_FN\_SEND\_AND\_INVALIDATE*](https://msdn.microsoft.com/library/windows/hardware/dn265507)) function
- *NdkGetCqResultsEx* ([*NDK\_FN\_GET\_CQ\_RESULTS\_EX*](https://msdn.microsoft.com/library/windows/hardware/dn265506)) function
- [**NDK\_RESULT\_EX**](https://msdn.microsoft.com/library/windows/hardware/dn265509) structure
- New request callback *Flags* value: **NDK\_OP\_FLAG\_DEFER**
- New [**NDK\_ADAPTER\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh439851)**AdapterFlags** value: **NDK\_ADAPTER\_FLAG\_RDMA\_READ\_LOCAL\_INVALIDATE\_SUPPORTED**

### Native 802.11 Wireless LAN

IEEE 802.11ac very-high throughput (VHT) PHY is now supported. The following DDI elements have been updated:

- [**DOT11\_PHY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff548741) enumeration
- [OID\_DOT11\_CURRENT\_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/ff569127)
- [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](https://msdn.microsoft.com/library/windows/hardware/ff569426)
- [OID\_DOT11\_SUPPORTED\_OFDM\_FREQUENCY\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569425)

## Sample and Documentation Updates

The [Hyper-V Extensible Switch forwarding extension sample](http://go.microsoft.com/fwlink/p/?LinkId=617913) has been updated to implement Hybrid Forwarding.

The following documentation sections have been added or significantly expanded:

-   [Porting NDIS 6.x Drivers to NDIS 6.30](porting-ndis-6-x-drivers-to-ndis-6-30.md)
-   [Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md) Design Guide
-   [Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md)
-   [Receive Segment Coalescing (RSC)](receive-segment-coalescing--rsc-.md) Design Guide
-   [Getting Started Writing a Hyper-V Extensible Switch Extension](getting-started-writing-a-hyper-v-extensible-switch-extension.md)
-   [NVGRE Task Offload Reference](https://msdn.microsoft.com/library/windows/hardware/dn197221)

The NetDMA interface is not supported in Windows 8 and Windows Server 2012 and later. The documentation has now been updated to reflect this.

This section includes the following topics:

- [Implementing an NDIS 6.40 Driver](implementing-an-ndis-6-40-driver.md)
- [Using NDIS 6.40 Data Structures](using-ndis-6-40-data-structures.md)
- [Compiling an NDIS 6.40 Driver](compiling-an-ndis-6-40-driver.md)

 

 





