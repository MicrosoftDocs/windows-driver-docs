---
title: Enabling DMA Remapping for device drivers
description: Enable and opt-into Direct Memory Access (DMA) remapping to ensure compatibility with Kernel DMA Protection and DMAGuard policies
ms.date: 05/16/2020
ms.localizationpriority: medium
ms.custom: 19H1
---

#  Enabling DMA Remapping for device drivers

Enable and opt PCIe device drivers into Direct Memory Access (DMA) remapping, to ensure compatibility with [Kernel DMA Protection](https://docs.microsoft.com/windows/security/information-protection/kernel-dma-protection-for-thunderbolt) and [DMAGuard Policy](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-dmaguard#dmaguard-deviceenumerationpolicy).

## Benefits of DMA Remapping

DMA Remapping for device drivers allows the OS to maintain good system memory hygiene, protect against memory corruption and malicious DMA attacks, as well as provide higher level of compatibility for devices. DMA Remapping is also used by the OS to improve the overall [user experience on Kernel DMA Protection](https://docs.microsoft.com/windows/security/information-protection/kernel-dma-protection-for-thunderbolt#user-experience) enabled systems, as devices with DMA Remapping compatible drivers are allowed to start and perform DMA, regardless of the lock screen status.

On Kernel DMA Protection enabled systems, [DMAGuard Policy](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-dmaguard#dmaguard-deviceenumerationpolicy) may fully block devices, with DMA Remapping incompatible drivers, connected to [external](https://docs.microsoft.com/windows-hardware/drivers/pci/dsd-for-pcie-root-ports#identifying-externally-exposed-pcie-root-ports)/[exposed](https://docs.microsoft.com/windows-hardware/drivers/pci/dsd-for-pcie-root-ports#identifying-internal-pcie-ports-accessible-to-users-and-requiring-dma-protection) PCIe ports (e.g. M.2, Thunderbolt™), depending on the policy value set by the system administrator. 

## Driver requirements for enabling and opting into DMA Remapping 

1. Drivers can only perform DMA using the Microsoft provided interfaces:
    * [WDF DMA interfaces](https://docs.microsoft.com/windows-hardware/drivers/wdf/introduction-to-dma-in-windows-driver-framework)
    * [WDM interfaces](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/)
    * [NDIS interfaces](https://docs.microsoft.com/windows-hardware/drivers/ddi/_netvista/)
2. Opt-into DMA Remapping using the following INF directive in the drivers .INF file: 
  ```INF
    [MyServiceInstall_AddReg]
    HKR,Parameters,DmaRemappingCompatible,0x00010001,1 
    ;1 = opt-in, 2 = opt-in only for external devices
  ```
3. Enable driver verifier with all standard settings when testing the driver.
    * Under driver verifier (for testing purposes), the value of the INF directive for opting in external devices, is promoted to '1'.
4. Fully test driver functionality on an Intel x64 and AMD64 systems , with VT-d/AMD-Vi enabled, using the latest Windows 10 build.

_Note: DMA Remapping is currently not supported for graphics device drivers._

## Validating that DMA Remapping is enabled for a specific device driver instance

To check if a specific driver is opted into DMA Remapping, check the values corresponding to the DMA Remapping Policy property in the "Details" tab of a device in Device Manager*. There are three possible values for the Policy in Device Manager:
* 2 = DMA Remapping is currently enforced for the specific device instance
* 1 = Device driver explicitly opted out of DMA Remapping
* 0 or DMA Remapping Policy property is not visible in the drop down menu = DMA Remapping INF directive is not set or speicified in the INF file. The OS will not enforce DMA Remapping for this device

_*For Windows 10 versions 1803 and 1809, the property field in Device Manager uses a GUID {83da6326-97a6-4088-9453-a1923f573b29}[18]_
