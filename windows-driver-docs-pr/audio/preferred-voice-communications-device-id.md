---
title: Preferred Voice-Communications Device ID
description: Preferred Voice-Communications Device ID
ms.assetid: ed0fbba3-cc9e-48d6-9ab5-360f8aab3ed6
keywords:
- WDM audio extensions WDK , voice-communication device IDs
- voice-communication device IDs WDK audio
- device IDs WDK audio
- identifying audio devices
- preferred device IDs WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Preferred Voice-Communications Device ID


## <span id="preferred_voice_communications_device_id"></span><span id="PREFERRED_VOICE_COMMUNICATIONS_DEVICE_ID"></span>


In Windows Me, and Windows 2000 and later, the Windows multimedia functions **waveInMessage** and **waveOutMessage** can retrieve the device ID of the preferred device for voice communications. These two functions get the preferred voice-communication device IDs for wave input and wave output, respectively. Each device ID identifies the wave device that is preferred specifically for voice communications, in contrast to the wave device that is preferred for general wave audio usage. For information about obtaining the device ID of the preferred device for general wave audio, see [Accessing the Preferred Device ID](accessing-the-preferred-device-id.md).

Knowing the preferred voice-communications device can be helpful to application programs that, for example, allow users to select a device to open from a list of two or more devices. Such an application typically needs to indicate which among the devices in the list is the preferred device.

To retrieve the device ID of the current preferred voice-communications device, an application calls the wave *Xxx*Message function with the message parameter set to the constant [**DRVM\_MAPPER\_CONSOLEVOICECOM\_GET**](https://msdn.microsoft.com/library/windows/hardware/ff536361).

When calling the **waveInMessage** or **waveOutMessage** function with the DRVM\_MAPPER\_CONSOLEVOICECOM\_GET message, specify the value of the device handle as WAVE\_MAPPER and cast this value to the appropriate handle type, HWAVEIN or HWAVEOUT. The wave *Xxx*Message functions accept this value in place of a valid device handle so that an application can query for the default device ID without first having to open a device. For more information about the wave *Xxx*Message functions, see [System-Intercepted Device Messages](system-intercepted-device-messages.md).

The DRVM\_MAPPER\_PREFERRED\_GET message is intercepted by the mapper for the target device (waveIn or waveOut). For information about mappers for wave devices, see the Microsoft Windows SDK documentation.

 

 




