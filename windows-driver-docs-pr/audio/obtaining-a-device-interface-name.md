---
title: Obtaining a Device Interface Name
description: Obtaining a Device Interface Name
ms.assetid: 2ad0bafa-c836-4dca-9287-72cdbddec7d0
keywords:
- WDM audio extensions WDK , device interface names
- device interface names WDK audio
- interface names WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining a Device Interface Name


## <span id="obtaining_a_device_interface_name"></span><span id="OBTAINING_A_DEVICE_INTERFACE_NAME"></span>


In Windows Me, and Windows 2000 and later, the Windows multimedia functions **waveInMessage**, **waveOutMessage**, **midiInMessage**, **midiOutMessage**, and **mixerMessage** can retrieve the device interface name of a device. This information is useful to application programs that need to identify the device outside of the waveIn, waveOut, midiIn, midiOut, or mixer API. Within one of these APIs, a device ID is sufficient.

The Plug and Play manager generates a device interface name to uniquely identify each device that it enumerates. An application should treat the string containing a device interface name as opaque. For more information about device interfaces, see [Introduction to Device Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff549460).

The header file Mmddk.h defines two message constants for the purpose of obtaining device interface names:

[**DRV\_QUERYDEVICEINTERFACESIZE**](https://msdn.microsoft.com/library/windows/hardware/ff536364)

[**DRV\_QUERYDEVICEINTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536363)

The first message obtains the size in bytes of the buffer needed to hold the string containing the device interface name. The second message retrieves the name string in a buffer of the required size.

The system intercepts and handles the DRV\_QUERYDEVICEINTERFACESIZE and DRV\_QUERYDEVICEINTERFACE messages without sending the messages to the device driver.

The first parameter to the *xxx*Message function is the device ID, which the caller must cast to the appropriate handle type: HWAVEIN, HWAVEOUT, HMIDIIN, HMIDIOUT, or HMIXER. For more information about the *xxx*Message functions, see [System-Intercepted Device Messages](system-intercepted-device-messages.md).

 

 




