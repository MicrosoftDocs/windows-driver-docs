---
title: Audio Device Messages for MIDI
description: Audio Device Messages for MIDI
ms.date: 04/22/2020
---

# Audio Device Messages for MIDI


In Windows XP and later versions of Windows (including Windows Vista), the operating system communicates with musical instrument digital interface (MIDI) input and output drivers by using audio device messages.

Every MIDI input and output driver must have one [DriverProc](/windows/win32/api/mmiscapi/nc-mmiscapi-driverproc) entry-point function to enable or disable the driver. Additionally, it must have an additional entry-point function to process messages from the Windows operating system. In the case of MIDI output drivers, the additional entry-point function is [**modMessage**](/previous-versions/windows/hardware/drivers/ff537532(v=vs.85)), which must be provided by the manufacturer of the MIDI device. This function processes messages that WINMM sends to the MIDI output driver. WINMM is a Windows dynamic link library (DLL) module that contains functions that help the operating system and the MIDI output driver communicate with each other. Specifically, WINMM helps to manage 16-bit multimedia applications that run on Windows.

Each message received by the **modMessage** function comes with two pointers to DWORD variables (DWORD\_PTR). For some messages, one of these parameters points to a structure that contains additional information from the client, or it points to an empty structure for the driver to fill with information for the client. One example of such a structure is [**MIDIOPENDESC**](/windows/win32/api/mmddk/ns-mmddk-midiopendesc). There are two other structures used by MIDI output device drivers and they are discussed in the Windows SDK. For more information about these structures, see [MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) and [MIDIOUTCAPS](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps).

The following is a list of the audio device messages and the **modMessage** entry-point function that processes them for a MIDI output driver:

[**modMessage**](/previous-versions/windows/hardware/drivers/ff537532(v=vs.85))

[**MODM\_CACHEDRUMPATCHES**](/previous-versions/windows/hardware/drivers/ff537533(v=vs.85))

[**MODM\_CACHEPATCHES**](/previous-versions/windows/hardware/drivers/ff537534(v=vs.85))

[**MODM\_DATA**](/previous-versions/windows/hardware/drivers/ff537535(v=vs.85))

[**MODM\_GETDEVCAPS**](/previous-versions/windows/hardware/drivers/ff537536(v=vs.85))

[**MODM\_GETNUMDEVS**](/previous-versions/windows/hardware/drivers/ff537537(v=vs.85))

[**MODM\_GETPOS**](/previous-versions/windows/hardware/drivers/ff537538(v=vs.85))

[**MODM\_GETVOLUME**](/previous-versions/windows/hardware/drivers/ff537539(v=vs.85))

[**MODM\_LONGDATA**](/previous-versions/windows/hardware/drivers/ff537540(v=vs.85))

[**MODM\_OPEN**](/previous-versions/windows/hardware/drivers/ff537541(v=vs.85))

[**MODM\_PAUSE**](/previous-versions/windows/hardware/drivers/ff537542(v=vs.85))

[**MODM\_PREPARE**](/previous-versions/windows/hardware/drivers/ff537543(v=vs.85))

[**MODM\_PROPERTIES**](/previous-versions/windows/hardware/drivers/ff537544(v=vs.85))

[**MODM\_RESET**](/previous-versions/windows/hardware/drivers/ff537545(v=vs.85))

[**MODM\_RESTART**](/previous-versions/windows/hardware/drivers/ff537546(v=vs.85))

[**MODM\_SETVOLUME**](/previous-versions/windows/hardware/drivers/ff537547(v=vs.85))

[**MODM\_STOP**](/previous-versions/windows/hardware/drivers/ff537548(v=vs.85))

[**MODM\_STRMDATA**](/previous-versions/windows/hardware/drivers/ff537549(v=vs.85))

[**MODM\_UNPREPARE**](/previous-versions/windows/hardware/drivers/ff537550(v=vs.85))

[**MOM\_CLOSE**](/previous-versions/windows/hardware/drivers/ff537551(v=vs.85))

[**MOM\_DONE**](/previous-versions/windows/hardware/drivers/ff537552(v=vs.85))

[**MOM\_OPEN**](/previous-versions/windows/hardware/drivers/ff537553(v=vs.85))

 

