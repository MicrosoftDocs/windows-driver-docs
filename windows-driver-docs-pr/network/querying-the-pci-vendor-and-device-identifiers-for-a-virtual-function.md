---
title: Querying the PCI vendor and device IDs for a virtual function
description: Querying the PCI Vendor and Device Identifiers for a Virtual Function
ms.date: 04/20/2017
---

# Querying the PCI Vendor and Device Identifiers for a Virtual Function

**Note** This method can only be used by overlying drivers that run in the management operating system of the Hyper-V parent partition.

An overlying driver issues an object identifier (OID) method request of [OID\_SRIOV\_VF\_VENDOR\_DEVICE\_ID](./oid-sriov-vf-vendor-device-id.md) to query the PCI Express (PCIe) vendor identifier (*VendorID*) and device identifier (*DeviceID*). This data is read from the PCIe configuration space for the PCIe Virtual Function (VF) on the physical network adapter.

Overlying drivers issue this OID method request to the miniport driver of the PCI Express (PCIe) Physical Function (PF) of the network adapter. This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The guest operating system, which runs in a Hyper-V child partition, uses the VendorID and the DeviceID of the VF for generic Plug and Play (PnP) IDs for device enumeration. Starting with Windows Server 2012, the PF miniport driver can provide the following set of identifiers for the VF network adapter that is exposed in the child partition:

-   The VendorID and DeviceID of the physical network adapter. This allows compatible drivers to be loaded in the guest operating system, which runs in the Hyper-V child partition, and the management operating system, which runs in the Hyper-V parent partition.

-   A VendorID and DeviceID that differ from the identifiers of the physical network adapter. This allows a driver to be loaded in the guest operating system that is more appropriate for its use. For example, the PF miniport driver may return a VendorID and DeviceID for a VF network adapter so that a driver is loaded that disables certain feature sets, such as power management or protocol task offloads.

Before it issues this OID method request, the overlying driver must initialize an [**NDIS\_SRIOV\_VF\_VENDOR\_DEVICE\_ID\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_vendor_device_id_info) structure. The driver must set the **VFId** member to the identifier of the VF from which the information is to be read.

When it handles this OID request, the PF miniport driver must verify that the specified VF has resources that have been previously allocated. The PF miniport driver allocates resources for a VF during an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](./oid-nic-switch-allocate-vf.md). If resources for the specified VF have not been allocated, the driver must fail the OID request.

 

