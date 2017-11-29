---
title: Audio Device Messages for MIDI
description: Audio Device Messages for MIDI
ms.assetid: d3b00985-6894-41ea-b493-d0aee269d5bf
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Audio Device Messages for MIDI


In Windows XP and later versions of Windows (including Windows Vista), the operating system communicates with musical instrument digital interface (MIDI) input and output drivers by using audio device messages.

Every MIDI input and output driver must have one [DriverProc](http://go.microsoft.com/fwlink/p/?linkid=142258) entry-point function to enable or disable the driver. Additionally, it must have an additional entry-point function to process messages from the Windows operating system. In the case of MIDI output drivers, the additional entry-point function is [**modMessage**](https://msdn.microsoft.com/library/windows/hardware/ff537532), which must be provided by the manufacturer of the MIDI device. This function processes messages that WINMM sends to the MIDI output driver. WINMM is a Windows dynamic link library (DLL) module that contains functions that help the operating system and the MIDI output driver communicate with each other. Specifically, WINMM helps to manage 16-bit multimedia applications that run on Windows.

Each message received by the **modMessage** function comes with two pointers to DWORD variables (DWORD\_PTR). For some messages, one of these parameters points to a structure that contains additional information from the client, or it points to an empty structure for the driver to fill with information for the client. One example of such a structure is [**MIDIOPENDESC**](https://msdn.microsoft.com/library/windows/hardware/ff537518). There are two other structures used by MIDI output device drivers and they are discussed in the Windows SDK. For more information about these structures, see [MIDIHDR](http://go.microsoft.com/fwlink/p/?linkid=142406) and [MIDIOUTCAPS](http://go.microsoft.com/fwlink/p/?linkid=142347).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Device%20Messages%20for%20MIDI%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




