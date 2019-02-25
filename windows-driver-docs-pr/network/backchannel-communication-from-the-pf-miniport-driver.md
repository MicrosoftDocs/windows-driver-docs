---
title: Backchannel Communication from the PF Miniport Driver
description: Backchannel Communication from the PF Miniport Driver
ms.assetid: 819FC32C-D50C-480F-AE6E-078E4ECD3400
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Backchannel Communication from the PF Miniport Driver


A miniport driver of the PCI Express (PCIe) Physical Function (PF) communicates with a miniport driver of the PCIe Virtual Function (VF) to issue notifications about changes in the data of a VF configuration block. The PF miniport driver issues these notifications to *invalidate* the data in the VF configuration block. In response to this notification, the VF miniport driver can issue a backchannel request to the PF miniport driver to read the data from an invalidated VF configuration block.

A VF configuration block is used for backchannel communication between the PF and VF miniport drivers. The IHV can define one or more VF configuration blocks for the device. Each VF configuration block has an IHV-defined format, length, and block ID.

**Note**  Data from each VF configuration block is used only by the PF and VF miniport drivers. The format and content of this data is opaque to components of the Windows operating system.

 

The following steps occur when issuing and handling notifications of invalid VF configuration data:

1.  In the guest operating system, NDIS issues an I/O control request of [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/hh439301). When this IOCTL is completed, NDIS is notified that VF configuration data has changed.

2.  In the management operating system that runs in the Hyper-V parent partition, the following steps occur:

    1.  The PF miniport driver calls the [**NdisMInvalidateConfigBlock**](https://msdn.microsoft.com/library/windows/hardware/hh451517) function to notify NDIS that VF configuration data has changed and is no longer valid. The driver sets the *BlockMask* parameter to a ULONGLONG bitmask that specifies which VF configuration blocks have changed. Each bit in the bitmask corresponds to a VF configuration block. If the bit is set to one, the data in the corresponding VF configuration block has changed.
    2.  NDIS signals the virtualization stack, which runs in the management operating system, about the change to VF configuration block data. The virtualization stack caches the *BlockMask* parameter data.

        **Note**  Each time that the PF miniport driver calls [**NdisMInvalidateConfigBlock**](https://msdn.microsoft.com/library/windows/hardware/hh451517), the virtualization stack ORs the *BlockMask* parameter data with the current value in its cache.

         

    3.  The virtualization stack notifies the virtual PCI (VPCI) driver, which runs in the guest operating system, about the invalidation of VF configuration data. The virtualization stack sends the cached *BlockMask* parameter data to the VPCI driver.

3.  In the guest operating system that runs in a Hyper-V child partition, the following steps occur:

    1.  The VPCI driver saves the cached *BlockMask* parameter data in the **BlockMask** member of the [**VPCI\_INVALIDATE\_BLOCK\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh451586) structure that is associated with the [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/hh439301) request.

    2.  The VPCI driver successfully completes the [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/hh439301) request. When this happens, NDIS issues an object identifier (OID) method request of [OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK](https://msdn.microsoft.com/library/windows/hardware/hh451903) to the VF miniport driver. An [**NDIS\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451684) is passed along in the OID request. This structure contains the cached *BlockMask* parameter data.

        NDIS also issues another [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/hh439301) request to handle successive notifications of changes to VF configuration data.

    3.  When the VF driver handles the [OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK](https://msdn.microsoft.com/library/windows/hardware/hh451903) request, it can read data from the specified VF configuration blocks by calling [**NdisMReadConfigBlock**](https://msdn.microsoft.com/library/windows/hardware/hh451523). For more information about this process, see [Backchannel Communication from a VF Miniport Driver](backchannel-communication-from-a-vf-miniport-driver.md).

 

 





