---
title: Full-Duplex Mode
author: windows-driver-content
description: Full-Duplex Mode
ms.assetid: 01e3388d-d568-4476-9ff0-2125acafb841
---

# Full-Duplex Mode


## <span id="ddk_full_duplex_mode_kg"></span><span id="DDK_FULL_DUPLEX_MODE_KG"></span>


The Storport driver supports an I/O model tailored specifically for high-performance buses. This I/O model allows miniport drivers to operate in full-duplex mode, which means that a miniport driver can add new requests to its queue even while it is in the process of completing others. Moreover, in full-duplex mode, the miniport driver does not have to synchronize the execution of its [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) and interrupt service routines. This can lead to significant performance enhancements. However, miniport drivers must be designed to take advantage of full-duplex mode, because Storport operates in half-duplex mode by default.

A miniport driver must configure Storport to operate in full-duplex mode while executing its [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine. It does this by initializing the **SynchronizationModel** member of the miniport driver's [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure to **StorSynchronizeFullDuplex**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Full-Duplex%20Mode%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


