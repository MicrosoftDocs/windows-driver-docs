---
title: User-Mode WDM Audio Components
description: User-Mode WDM Audio Components
ms.assetid: 067944fb-6854-4ae8-81ca-9b8f2eed939e
keywords: ["user-mode components WDK audio", "WinMM system components WDK audio", "WDMAud system driver WDK audio", "DirectSound system component WDK audio", "DirectMusic system component WDK audio", "Windows Audio Services WDK audio", "waveOut API WDK audio", "audio services WDK", "WDMAud system driver", "WDMAud system driver, user mode (wdmaud.drv)"]
---

# User-Mode WDM Audio Components


## <span id="user_mode_wdm_audio_components"></span><span id="USER_MODE_WDM_AUDIO_COMPONENTS"></span>


The user-mode Microsoft Windows Driver Model (WDM) audio components are:

-   WinMM System Component

-   WDMAud System Driver

-   DirectSound System Component

-   DirectMusic System Component

-   Windows Audio Services

### <span id="winmm_system_component"></span><span id="WINMM_SYSTEM_COMPONENT"></span>WinMM System Component

The WinMM system components (Winmm.dll and its 16-bit counterpart, Mmsystem.dll) implement the Microsoft Windows multimedia APIs wave*Xxx*, midi*Xxx*, mixer*Xxx*, and aux*Xxx* (see Microsoft Windows SDK documentation). The WinMM components use the WDMAud system driver to translate the WinMM API calls into kernel-streaming I/O requests.

### <span id="wdmaud_system_driver"></span><span id="WDMAUD_SYSTEM_DRIVER"></span>WDMAud System Driver

The user-mode WDMAud system driver (Wdmaud.drv) is paired with the kernel-mode WDMAud system driver (Wdmaud.sys). Together, the WDMAud system drivers translate between WinMM API calls and kernel-streaming I/O requests. The kernel-mode mode WDMAud driver is a client of the SysAudio system driver.

### <span id="directsound_system_component"></span><span id="DIRECTSOUND_SYSTEM_COMPONENT"></span>DirectSound System Component

The DirectSound system component (Dsound.dll) supports the DirectSound API (see Microsoft Windows SDK documentation). The DirectSound component is a client of the SysAudio driver. If hardware mixing is available, the SysAudio driver connects DirectSound hardware buffers directly to the rendering device. Otherwise, the SysAudio driver connects DirectSound software buffers to the KMixer system driver. For more information, see [Rendering Wave Content Using DirectSound Software and Hardware Buffers](rendering-wave-content-using-directsound-software-and-hardware-buffers.md).

### <span id="directmusic_system_component"></span><span id="DIRECTMUSIC_SYSTEM_COMPONENT"></span>DirectMusic System Component

The DirectMusic system component (DMusic.dll) supports the DirectMusic API (see Microsoft Windows SDK documentation). This component converts calls made to the DirectMusic API into I/O requests to WDM audio devices. The DirectMusic component is a client of the SysAudio system driver.

### <span id="windows_audio_services"></span><span id="WINDOWS_AUDIO_SERVICES"></span>Windows Audio Services

In Windows XP and later, the Windows Audio Services component (Audiosrv.dll) manages audio devices for Windows-based programs. Stopping Windows Audio Services prevents audio devices and effects from functioning properly. If audio services are disabled, any other services (including WDM audio drivers) that explicitly depend on them will fail to start. In the Home Edition, Professional, and Server versions of Windows XP and later, audio services are by default configured to start automatically. However, in the Advanced Server, Data Center, and Web Server versions of Windows Server 2003 and later, audio services are disabled by default. When audio services are disabled, installing an audio device does not enable them -- audio services are enabled to run automatically only if an administrator explicitly configures them to do so. For information about starting and stopping Windows services, see the help file in the **Services** dialog box (look in the Windows Control Panel under **Administrative Tools**).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20User-Mode%20WDM%20Audio%20Components%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


