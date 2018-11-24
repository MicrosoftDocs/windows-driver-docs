---
title: Full-Duplex Mode
description: Full-Duplex Mode
ms.assetid: 01e3388d-d568-4476-9ff0-2125acafb841
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Full-Duplex Mode


## <span id="ddk_full_duplex_mode_kg"></span><span id="DDK_FULL_DUPLEX_MODE_KG"></span>


The Storport driver supports an I/O model tailored specifically for high-performance buses. This I/O model allows miniport drivers to operate in full-duplex mode, which means that a miniport driver can add new requests to its queue even while it is in the process of completing others. Moreover, in full-duplex mode, the miniport driver does not have to synchronize the execution of its [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) and interrupt service routines. This can lead to significant performance enhancements. However, miniport drivers must be designed to take advantage of full-duplex mode, because Storport operates in half-duplex mode by default.

A miniport driver must configure Storport to operate in full-duplex mode while executing its [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine. It does this by initializing the **SynchronizationModel** member of the miniport driver's [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure to **StorSynchronizeFullDuplex**.

 

 




