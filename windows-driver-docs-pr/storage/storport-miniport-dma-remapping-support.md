---
title: DMA remapping support in Storport miniport drivers
description:  DMA remapping support in Storport miniport drivers
ms.assetid: 9d1e1549-8b11-4a9a-b068-7b1d75c58e52
ms.date: 07/01/2020
ms.localizationpriority: medium
---

# DMA remapping support in Storport miniport drivers

The [StorAhci Storport miniport driver](https://github.com/microsoft/Windows-driver-samples/tree/master/storage/miniports/storahci) sample code shows how to support DMA remapping in a Storport miniport driver. For additional information about DMA remapping and Kernel DMA Protection, see [Enabling DMA Remapping for device drivers](https://docs.microsoft.com/windows-hardware/drivers/pci/enabling-dma-remapping-for-device-drivers).

> [!NOTE]
>
> The default value of "DMA remapping policy" device property described in [Validating that DMA Remapping is enabled for a specific device driver instance](https://docs.microsoft.com/windows-hardware/drivers/pci/enabling-dma-remapping-for-device-drivers#validating-that-dma-remapping-is-enabled-for-a-specific-device-driver-instance) is 0 for Windows 10 versions 1803 and 1809, and 2 for Windows 10 version 1903 and later.

This property corresponds to **DEVPKEY_Device_DmaRemappingPolicy**.
