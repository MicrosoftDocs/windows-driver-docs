---
title: DirectSound Hardware Acceleration in 64-Bit Versions of Windows XP
description: DirectSound Hardware Acceleration in 64-Bit Versions of Windows XP
ms.assetid: 0497acff-1e7f-45b9-b5ec-f1783ea7e900
keywords: ["hardware acceleration WDK DirectSound , 64-bit systems", "64-bit WDK audio"]
---

# DirectSound Hardware Acceleration in 64-Bit Versions of Windows XP


## <span id="ddk_directsound_hardware_acceleration_in_64_bit_versions_of_windows_xp"></span><span id="DDK_DIRECTSOUND_HARDWARE_ACCELERATION_IN_64_BIT_VERSIONS_OF_WINDOWS_XP"></span>


In Windows Me/98 and in 32-bit versions of Windows 2000, Windows XP, and Windows Server 2003, if an audio device has the hardware features needed to support DirectSound hardware acceleration, then both WavePci and WaveCyclic miniport drivers can provide hardware-accelerated pins for use by DirectSound output streams. The same is true of WaveCyclic miniport drivers in 64-bit versions of Windows XP and Windows Server 2003.

In 64-bit versions of Windows XP and Windows Server 2003, the WavePci port driver enables a WavePci miniport driver to provide DirectSound hardware acceleration only if the audio device's DMA engine can address all locations in physical memory. The port driver permits hardware acceleration under either of the following conditions:

-   The device generates 64-bit DMA addresses.

-   The device generates 32-bit DMA addresses and all physical memory addresses are in the 4-gigabyte address range, 0 to 0xFFFFFFFF.

When the adapter driver creates the WavePci port object and calls [**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943) (see [Subdevice Creation](subdevice-creation.md)), the port driver calls the miniport driver's [**IMiniportWavePci::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536734) method. In order to make DirectSound hardware acceleration available to clients, the miniport driver must call the [**IPortWavePci::NewMasterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff536916) method before returning from the **IMiniportWavePci::Init** call. During the call to **NewMasterDmaChannel**, the port driver determines whether the audio device has the DMA addressing capabilities required for hardware acceleration. Acceleration is disabled if the WavePci device can address only 32 bits and any portion of physical memory lies outside the device's 4-gigabyte address range.

In 64-bit versions of Windows XP and Windows Server 2003, a WavePci miniport driver can provide hardware acceleration only if it calls the **IPortWavePci::NewMasterDmaChannel** method to create a new DMA channel object. If the driver calls [**PcNewDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff537712) instead, hardware acceleration is automatically disabled.

The preceding restriction does not apply to WaveCyclic miniport drivers in 64-bit versions of Windows XP and Windows Server 2003. It also does not apply to WavePci or WaveCyclic miniport drivers in any 32-bit versions of Windows.

Although use of the **PcNewDmaChannel** function does not disable hardware acceleration in 32-bit versions of Windows, driver writers should consider **PcNewDmaChannel** to be obsolete. For all new audio drivers, use one of the following **IPortWave*Xxx*::New*Xxx*DmaChannel** methods in place of **PcNewDmaChannel**:

[**IPortWavePci::NewMasterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff536916)

[**IPortWaveCyclic::NewMasterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff536900)

[**IPortWaveCyclic::NewSlaveDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff536902)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DirectSound%20Hardware%20Acceleration%20in%2064-Bit%20Versions%20of%20Windows%20XP%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




