---
title: Introduction to NDIS 6.50
description: This section introduces NDIS 6.50 and describes changes from NDIS 6.40. NDIS 6.50 is included in Windows 10, version 1507 and later.
ms.date: 09/30/2020
ms.localizationpriority: medium
---

# Introduction to NDIS 6.50

This topic introduces Network Driver Interface Specification (NDIS) 6.50 and describes its major design additions. NDIS 6.50 is included in Windows 10, version 1507 and later.

NDIS 6.50 is a minor version update to NDIS 6.40. For more information about porting NDIS 6.x drivers to NDIS 6.50, see [Porting NDIS 6.x drivers to NDIS 6.50](porting-ndis-6-x-drivers-to-ndis-6-50.md).

## Feature updates

NDIS 6.50 is an incremental update to NDIS 6.40 and does not contain any major new features.

## Implementing an NDIS 6.50 driver

An NDIS 6.50 driver must follow the requirements that are defined in [Implementing an NDIS 6.30 driver](implementing-an-ndis-6-30-driver.md).

In addition, an NDIS 6.50 driver must be compliant with the following requirements:

- An NDIS 6.50 driver must report the correct NDIS version when it registers with NDIS.
   
   You must update the major and minor NDIS version number in the NDIS_Xxx_DRIVER_CHARACTERISTICS structure to support NDIS 6.50. The MajorNdisVersion member must contain 6 and the MinorNdisVersion member must contain 50. This requirement applies to miniport, protocol, and filter drivers. You must also update the version information for the compiler (see [Compiling an NDIS 6.50 driver](#compiling-an-ndis-650-driver)).

- NDIS 6.50 miniport drivers for Windows 10, version 1507 and later must use the NDIS 6.50 versions of data structures. For more information, see [Using NDIS 6.50 data structures](#using-ndis-650-data-structures).

## Compiling an NDIS 6.50 driver

The WDK for Windows 10, version 1507 supports header versioning. Header versioning makes sure that NDIS 6.50 drivers use the appropriate NDIS 6.50 data structures at compile time.

Add the following compiler settings to the Visual Studio project for your driver:

- For a miniport driver, add ```NDIS650_MINIPORT=1```.
- For a filter or protocol driver, add ```NDIS650=1```.

For information on building a driver with the Windows 10, version 1507 release of the WDK, see [Building a Driver](../develop/building-a-driver.md).

## Using NDIS 6.50 data structures

### New data structures

The following data structures are new in NDIS 6.50.

- [OID_WWAN_SYS_CAPS](./oid-wwan-sys-caps.md)
- [OID_WWAN_DEVICE_CAPS_EX](./oid-wwan-device-caps-ex.md)
- [OID_WWAN_SLOT_INFO_STATUS](./oid-wwan-slot-info-status.md)
- [OID_WWAN_NETWORK_IDLE_HINT](./oid-wwan-network-idle-hint.md) 
- [NDIS_STATUS_PD_CURRENT_CONFIG](./ndis-status-pd-current-config.md)
- [NDIS_PD_CAPABILITIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pd_capabilities)
- [NDIS_PD_CLOSE_PROVIDER_PARAMETERS](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_close_provider_parameters)
- [NDIS_PD_CONFIG](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pd_config)
- [NDIS_PD_COUNTER_PARAMETERS](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_counter_parameters)
- [NDIS_PD_COUNTER_VALUE](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_counter_value)
- [NDIS_PD_FILTER_COUNTER](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_filter_counter)
- [NDIS_PD_FILTER_PARAMETERS](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_filter_parameters)
- [NDIS_PD_ON_RSS_QUEUE_PARAMETERS](/windows-hardware/drivers/ddi/_netvista/)
- [NDIS_PD_OPEN_PROVIDER_PARAMETERS](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_open_provider_parameters)
- [NDIS_PD_PROVIDER_DISPATCH](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_provider_dispatch)
- [NDIS_PD_QUEUE](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_queue)
- [NDIS_PD_QUEUE_DISPATCH](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_queue_dispatch)
- [NDIS_PD_QUEUE_PARAMETERS](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_queue_parameters)
- [NDIS_PD_RECEIVE_QUEUE_COUNTER](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_receive_queue_counter)
- [NDIS_PD_TRANSMIT_QUEUE_COUNTER](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_transmit_queue_counter)
- [PD_BUFFER](/windows-hardware/drivers/ddi/ndis/ns-ndis-_pd_buffer)
- [PD_BUFFER_8021Q_INFO](/windows-hardware/drivers/ddi/ndis/ns-ndis-_pd_buffer_8021q_info)
- [PD_BUFFER_VIRTUAL_SUBNET_INFO](/windows-hardware/drivers/ddi/ndis/ns-ndis-_pd_buffer_virtual_subnet_info)

### Updated data structures

The following data structures were updated in NDIS 6.50.

- [NET_PNP_EVENT_NOTIFICATION](/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_pnp_event_notification)
- [NDIS_OID_REQUEST](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)
- [NDIS_NET_BUFFER_LIST_INFO](/windows-hardware/drivers/ddi/nblinfo/ne-nblinfo-ndis_net_buffer_list_info)
- [NdisMGetDeviceProperty](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetdeviceproperty)
- [NDIS_SWITCH_OPTIONAL_HANDLERS](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_optional_handlers)
- [NDIS_SWITCH_NIC_SAVE_STATE](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state)
- [NDIS_RECEIVE_FILTER_PARAMETERS](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters)

## NDIS 6.51

NDIS 6.51 is a very minor version update to NDIS 6.50. NDIS 6.51 is included in Windows 10, version 1511 and later. All information for NDIS 6.50 also applies to NDIS 6.51 with the following exceptions:

- The MinorNdisVersion changes from 50 to 51 when registering your driver with NDIS.
- The compiler settings change from ```NDIS650_MINIPORT=1``` for miniport drivers and ```NDIS650=1``` for filter or protocol drivers, to ```NDIS651_MINIPORT=1``` and ```NDIS651=1``` respectively.
