---
title: User-Mode WDM Audio Components
description: User-Mode WDM Audio Components
ms.assetid: 067944fb-6854-4ae8-81ca-9b8f2eed939e
keywords:
- user-mode components WDK audio
- WinMM system components WDK audio
- WDMAud system driver WDK audio
- DirectSound system component WDK audio
- DirectMusic system component WDK audio
- Windows Audio Services WDK audio
- waveOut API WDK audio
- audio services WDK
- WDMAud system driver
- WDMAud system driver, user mode (wdmaud.drv)
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




