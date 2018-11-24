---
title: Audio Device Messages for MIDI
description: Audio Device Messages for MIDI
ms.assetid: d3b00985-6894-41ea-b493-d0aee269d5bf
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Audio Device Messages for MIDI


In Windows XP and later versions of Windows (including Windows Vista), the operating system communicates with musical instrument digital interface (MIDI) input and output drivers by using audio device messages.

Every MIDI input and output driver must have one [DriverProc](https://go.microsoft.com/fwlink/p/?linkid=142258) entry-point function to enable or disable the driver. Additionally, it must have an additional entry-point function to process messages from the Windows operating system. In the case of MIDI output drivers, the additional entry-point function is [**modMessage**](https://msdn.microsoft.com/library/windows/hardware/ff537532), which must be provided by the manufacturer of the MIDI device. This function processes messages that WINMM sends to the MIDI output driver. WINMM is a Windows dynamic link library (DLL) module that contains functions that help the operating system and the MIDI output driver communicate with each other. Specifically, WINMM helps to manage 16-bit multimedia applications that run on Windows.

Each message received by the **modMessage** function comes with two pointers to DWORD variables (DWORD\_PTR). For some messages, one of these parameters points to a structure that contains additional information from the client, or it points to an empty structure for the driver to fill with information for the client. One example of such a structure is [**MIDIOPENDESC**](https://msdn.microsoft.com/library/windows/hardware/ff537518). There are two other structures used by MIDI output device drivers and they are discussed in the Windows SDK. For more information about these structures, see [MIDIHDR](https://go.microsoft.com/fwlink/p/?linkid=142406) and [MIDIOUTCAPS](https://go.microsoft.com/fwlink/p/?linkid=142347).

The following is a list of the audio device messages and the **modMessage** entry-point function that processes them for a MIDI output driver:

[**modMessage**](https://msdn.microsoft.com/library/windows/hardware/ff537532)

[**MODM\_CACHEDRUMPATCHES**](https://msdn.microsoft.com/library/windows/hardware/ff537533)

[**MODM\_CACHEPATCHES**](https://msdn.microsoft.com/library/windows/hardware/ff537534)

[**MODM\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff537535)

[**MODM\_GETDEVCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff537536)

[**MODM\_GETNUMDEVS**](https://msdn.microsoft.com/library/windows/hardware/ff537537)

[**MODM\_GETPOS**](https://msdn.microsoft.com/library/windows/hardware/ff537538)

[**MODM\_GETVOLUME**](https://msdn.microsoft.com/library/windows/hardware/ff537539)

[**MODM\_LONGDATA**](https://msdn.microsoft.com/library/windows/hardware/ff537540)

[**MODM\_OPEN**](https://msdn.microsoft.com/library/windows/hardware/ff537541)

[**MODM\_PAUSE**](https://msdn.microsoft.com/library/windows/hardware/ff537542)

[**MODM\_PREPARE**](https://msdn.microsoft.com/library/windows/hardware/ff537543)

[**MODM\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/ff537544)

[**MODM\_RESET**](https://msdn.microsoft.com/library/windows/hardware/ff537545)

[**MODM\_RESTART**](https://msdn.microsoft.com/library/windows/hardware/ff537546)

[**MODM\_SETVOLUME**](https://msdn.microsoft.com/library/windows/hardware/ff537547)

[**MODM\_STOP**](https://msdn.microsoft.com/library/windows/hardware/ff537548)

[**MODM\_STRMDATA**](https://msdn.microsoft.com/library/windows/hardware/ff537549)

[**MODM\_UNPREPARE**](https://msdn.microsoft.com/library/windows/hardware/ff537550)

[**MOM\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff537551)

[**MOM\_DONE**](https://msdn.microsoft.com/library/windows/hardware/ff537552)

[**MOM\_OPEN**](https://msdn.microsoft.com/library/windows/hardware/ff537553)

 

 





