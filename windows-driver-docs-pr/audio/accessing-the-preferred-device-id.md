---
title: Accessing the Preferred Device ID
description: Accessing the Preferred Device ID
ms.assetid: ef964ce5-8bcc-4ab0-9522-b05a8a6bdf74
keywords:
- preferred device IDs WDK audio
- WDM audio extensions WDK , preferred device IDs
- device IDs WDK audio
- identifying audio devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing the Preferred Device ID


## <span id="accessing_the_preferred_device_id"></span><span id="ACCESSING_THE_PREFERRED_DEVICE_ID"></span>


In Windows Me, and Windows 2000 and later, the Windows multimedia functions **waveInMessage**, **waveOutMessage**, and **midiOutMessage** can retrieve the device ID of the preferred device. These three functions get the preferred device IDs for wave input, wave output, and MIDI output, respectively. This information is useful to application programs that, for example, allow users to select a device to open from a list of two or more devices. Such an application typically needs to indicate which among the devices in the list is the preferred device.

The preferred device is the device that the user selects through the multimedia control panel, mmsys.cpl. If a Windows multimedia or DirectSound application does not explicitly specify a device, the preferred device is selected by default.

To retrieve the device ID of the current preferred audio device, an application calls the *xxx***Message** function with the message parameter set to the constant [**DRVM\_MAPPER\_PREFERRED\_GET**](https://msdn.microsoft.com/library/windows/hardware/ff536362).

When calling the **waveInMessage**, **waveOutMessage**, or **midiOutMessage** function with the DRVM\_MAPPER\_PREFERRED\_GET message, specify the value of the device handle as WAVE\_MAPPER (for **waveInMessage** or **waveOutMessage**) or MIDI\_MAPPER (for **midiOutMessage**) and cast this value to the appropriate handle type: HWAVEIN, HWAVEOUT, or HMIDIOUT. The *xxx***Message** functions accept this value in place of a valid device handle so that an application can query for the default device ID without first having to open a device. For more information about the *xxx***Message** functions, see [System-Intercepted Device Messages](system-intercepted-device-messages.md).

The DRVM\_MAPPER\_PREFERRED\_GET message is intercepted by the mapper for the target device (waveIn, waveOut, or midiOut). For information about mappers for wave and MIDI devices, see the Microsoft Windows SDK documentation.

 

 




