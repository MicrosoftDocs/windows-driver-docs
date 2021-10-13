---
title: Introduction to NDIS 6.40
description: This section introduces NDIS 6.40 and describes its major design additions. NDIS 6.40 is included in the Windows 8.1 and Windows Server 2012 R2 and later.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to NDIS 6.40


This section introduces Network Driver Interface Specification (NDIS) 6.40 and describes its major design additions. NDIS 6.40 is included in the Windows 8.1 and Windows Server 2012 R2 and later operating systems.

## Feature Updates


Windows 8.1 and Windows Server 2012 R2 introduce minor updates to the following features:

### NDKPI

NDKPI 1.2 adds the following new elements to the NDKPI DDI:

- *NdkSendAndInvalidate* ([*NDK\_FN\_SEND\_AND\_INVALIDATE*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_send_and_invalidate)) function
- *NdkGetCqResultsEx* ([*NDK\_FN\_GET\_CQ\_RESULTS\_EX*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_get_cq_results_ex)) function
- [**NDK\_RESULT\_EX**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_result_ex) structure
- New request callback *Flags* value: **NDK\_OP\_FLAG\_DEFER**
- New [**NDK\_ADAPTER\_INFO**](/windows/win32/api/ndkinfo/ns-ndkinfo-ndk_adapter_info)**AdapterFlags** value: **NDK\_ADAPTER\_FLAG\_RDMA\_READ\_LOCAL\_INVALIDATE\_SUPPORTED**

### Native 802.11 Wireless LAN

IEEE 802.11ac very-high throughput (VHT) PHY is now supported. The following DDI elements have been updated:

- [**DOT11\_PHY\_TYPE**](/windows-hardware/drivers/ddi/windot11/ne-windot11-_dot11_phy_type) enumeration
- [OID\_DOT11\_CURRENT\_CHANNEL](/previous-versions/windows/hardware/wireless/oid-dot11-current-channel)
- [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](/previous-versions/windows/hardware/wireless/oid-dot11-supported-phy-types)
- [OID\_DOT11\_SUPPORTED\_OFDM\_FREQUENCY\_LIST](/previous-versions/windows/hardware/wireless/oid-dot11-supported-ofdm-frequency-list)

## Sample and Documentation Updates

The [Hyper-V Extensible Switch forwarding extension sample](https://go.microsoft.com/fwlink/p/?LinkId=617913) has been updated to implement Hybrid Forwarding.

The following documentation sections have been added or significantly expanded:

-   [Porting NDIS 6.x Drivers to NDIS 6.30](porting-ndis-6-x-drivers-to-ndis-6-30.md)
-   [Network Direct Kernel Provider Interface (NDKPI)](./overview-of-network-direct-kernel-provider-interface--ndkpi-.md) Design Guide
-   [Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md)
-   [Receive Segment Coalescing (RSC)](overview-of-receive-segment-coalescing.md) Design Guide
-   [Getting Started Writing a Hyper-V Extensible Switch Extension](getting-started-writing-a-hyper-v-extensible-switch-extension.md)
-   [NVGRE Task Offload Reference](/windows-hardware/drivers/ddi/_netvista/)

The NetDMA interface is not supported in Windows 8 and Windows Server 2012 and later. The documentation has now been updated to reflect this.

This section includes the following topics:

- [Implementing an NDIS 6.40 Driver](implementing-an-ndis-6-40-driver.md)
- [Using NDIS 6.40 Data Structures](using-ndis-6-40-data-structures.md)
- [Compiling an NDIS 6.40 Driver](compiling-an-ndis-6-40-driver.md)

 

