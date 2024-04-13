---
title: Audio Device Messages for MIDI
description: Audio Device Messages for MIDI
ms.date: 04/22/2020
---

# Audio Device Messages for MIDI


In Windows XP and later versions of Windows (including Windows Vista), the operating system communicates with musical instrument digital interface (MIDI) input and output drivers by using audio device messages.

Every MIDI input and output driver must have one [DriverProc](/windows/win32/api/mmiscapi/nc-mmiscapi-driverproc) entry-point function to enable or disable the driver. Additionally, it must have an additional entry-point function to process messages from the Windows operating system. In the case of MIDI output drivers, the additional entry-point function is [**modMessage**](mod-message.md), which must be provided by the manufacturer of the MIDI device. This function processes messages that WINMM sends to the MIDI output driver. WINMM is a Windows dynamic link library (DLL) module that contains functions that help the operating system and the MIDI output driver communicate with each other. Specifically, WINMM helps to manage 16-bit multimedia applications that run on Windows.

Each message received by the **modMessage** function comes with two pointers to DWORD variables (DWORD\_PTR). For some messages, one of these parameters points to a structure that contains additional information from the client, or it points to an empty structure for the driver to fill with information for the client. One example of such a structure is [**MIDIOPENDESC**](/windows/win32/api/mmddk/ns-mmddk-midiopendesc). There are two other structures used by MIDI output device drivers and they are discussed in the Windows SDK. For more information about these structures, see [MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) and [MIDIOUTCAPS](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps).

The following is a list of the audio device messages and the **modMessage** entry-point function that processes them for a MIDI output driver:

[**modMessage**](mod-message.md)

[**MODM\_CACHEDRUMPATCHES**](modm-cachedrumpatches.md)

[**MODM\_CACHEPATCHES**](modm-cachepatches.md)

[**MODM\_DATA**](modm-data.md)

[**MODM\_GETDEVCAPS**](modm-getdevcaps.md)

[**MODM\_GETNUMDEVS**](modm-getnumdevs.md)

[**MODM\_GETPOS**](modm-getpos.md)

[**MODM\_GETVOLUME**](modm-getvolume.md)

[**MODM\_LONGDATA**](modm-longdata.md)

[**MODM\_OPEN**](modm-open.md)

[**MODM\_PAUSE**](modm-pause.md)

[**MODM\_PREPARE**](modm-prepare.md)

[**MODM\_PROPERTIES**](modm-properties.md)

[**MODM\_RESET**](modm-reset.md)

[**MODM\_RESTART**](modm-restart.md)

[**MODM\_SETVOLUME**](modm-setvolume.md)

[**MODM\_STOP**](modm-stop.md)

[**MODM\_STRMDATA**](modm-strmdata.md)

[**MODM\_UNPREPARE**](modm-unprepare.md)

[**MOM\_CLOSE**](mom-close.md)

[**MOM\_DONE**](mom-done.md)

[**MOM\_OPEN**](mom-open.md)
