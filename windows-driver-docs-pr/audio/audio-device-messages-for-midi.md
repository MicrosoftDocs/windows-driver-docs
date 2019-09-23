---
title: Audio Device Messages for MIDI
description: Audio Device Messages for MIDI
ms.assetid: d3b00985-6894-41ea-b493-d0aee269d5bf
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Audio Device Messages for MIDI


In Windows XP and later versions of Windows (including Windows Vista), the operating system communicates with musical instrument digital interface (MIDI) input and output drivers by using audio device messages.

Every MIDI input and output driver must have one [DriverProc](https://go.microsoft.com/fwlink/p/?linkid=142258) entry-point function to enable or disable the driver. Additionally, it must have an additional entry-point function to process messages from the Windows operating system. In the case of MIDI output drivers, the additional entry-point function is [**modMessage**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537532(v=vs.85)), which must be provided by the manufacturer of the MIDI device. This function processes messages that WINMM sends to the MIDI output driver. WINMM is a Windows dynamic link library (DLL) module that contains functions that help the operating system and the MIDI output driver communicate with each other. Specifically, WINMM helps to manage 16-bit multimedia applications that run on Windows.

Each message received by the **modMessage** function comes with two pointers to DWORD variables (DWORD\_PTR). For some messages, one of these parameters points to a structure that contains additional information from the client, or it points to an empty structure for the driver to fill with information for the client. One example of such a structure is [**MIDIOPENDESC**](https://docs.microsoft.com/windows/desktop/api/mmddk/ns-mmddk-midiopendesc_tag). There are two other structures used by MIDI output device drivers and they are discussed in the Windows SDK. For more information about these structures, see [MIDIHDR](https://go.microsoft.com/fwlink/p/?linkid=142406) and [MIDIOUTCAPS](https://go.microsoft.com/fwlink/p/?linkid=142347).

The following is a list of the audio device messages and the **modMessage** entry-point function that processes them for a MIDI output driver:

[**modMessage**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537532(v=vs.85))

[**MODM\_CACHEDRUMPATCHES**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537533(v=vs.85))

[**MODM\_CACHEPATCHES**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537534(v=vs.85))

[**MODM\_DATA**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537535(v=vs.85))

[**MODM\_GETDEVCAPS**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537536(v=vs.85))

[**MODM\_GETNUMDEVS**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537537(v=vs.85))

[**MODM\_GETPOS**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537538(v=vs.85))

[**MODM\_GETVOLUME**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537539(v=vs.85))

[**MODM\_LONGDATA**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537540(v=vs.85))

[**MODM\_OPEN**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537541(v=vs.85))

[**MODM\_PAUSE**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537542(v=vs.85))

[**MODM\_PREPARE**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537543(v=vs.85))

[**MODM\_PROPERTIES**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537544(v=vs.85))

[**MODM\_RESET**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537545(v=vs.85))

[**MODM\_RESTART**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537546(v=vs.85))

[**MODM\_SETVOLUME**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537547(v=vs.85))

[**MODM\_STOP**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537548(v=vs.85))

[**MODM\_STRMDATA**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537549(v=vs.85))

[**MODM\_UNPREPARE**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537550(v=vs.85))

[**MOM\_CLOSE**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537551(v=vs.85))

[**MOM\_DONE**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537552(v=vs.85))

[**MOM\_OPEN**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff537553(v=vs.85))

 

 





