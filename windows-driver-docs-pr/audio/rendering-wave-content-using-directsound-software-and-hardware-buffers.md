---
title: Rendering Wave Content Using DirectSound Software and Hardware Buffers
description: Rendering Wave Content Using DirectSound Software and Hardware Buffers
ms.assetid: df92dac3-2580-4910-8a55-bd9e9f82eb1f
keywords: ["DirectSound WDK audio , content rendering", "wave content rendering WDK audio"]
---

# Rendering Wave Content Using DirectSound Software and Hardware Buffers


## <span id="ddk_rendering_wave_content_using_directsound_software_and_hardware_buf"></span><span id="DDK_RENDERING_WAVE_CONTENT_USING_DIRECTSOUND_SOFTWARE_AND_HARDWARE_BUF"></span>


The following figure shows a configuration of Microsoft Windows Driver Model (WDM) components that renders to DirectSound software and hardware buffers.

![diagram illustrating rendering wave content using directsound software and hardware buffers](images/hwbuf.png)

See the following for a description of the WDM audio components:

[DirectSound System Component](user-mode-wdm-audio-components.md#directsound_system_component)

[SysAudio System Driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver)

[KMixer System Driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver)

[Port Class Adapter Driver and PortCls System Driver](kernel-mode-wdm-audio-components.md#port_class_adapter_driver_and_portcls_system_driver)

[USBAudio Class System Driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Rendering%20Wave%20Content%20Using%20DirectSound%20Software%20and%20Hardware%20Buffers%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


