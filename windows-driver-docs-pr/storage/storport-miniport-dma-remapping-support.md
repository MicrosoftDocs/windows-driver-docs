---
title: DMA remapping support in Storport miniport drivers
description:  DMA remapping support in Storport miniport drivers
ms.date: 07/10/2020
---

# DMA remapping support in Storport miniport drivers

The [StorAhci Storport miniport driver](https://github.com/Microsoft/Windows-driver-samples/tree/main/storage/miniports/storahci) sample code shows how to support DMA remapping in a Storport miniport driver. For additional information about DMA remapping and Kernel DMA Protection, see [Enabling DMA Remapping for device drivers](../pci/enabling-dma-remapping-for-device-drivers.md).

> [!NOTE]
>
> For Storport miniport drivers, the default value of "DMA remapping policy" device property described in [Validating that DMA Remapping is enabled for a specific device driver instance](../pci/enabling-dma-remapping-for-device-drivers.md#validating-that-dma-remapping-is-enabled-for-a-specific-device-driver-instance) is 0 for Windows 10 versions 1803 and 1809, and 2 for Windows 10 version 1903 and later.

This property corresponds to [**DEVPKEY_Device_DmaRemappingPolicy**](../install/devpkey-device-dmaremappingpolicy.md).
