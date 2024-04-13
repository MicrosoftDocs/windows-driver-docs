---
title: Audio Playback Fidelity Tests in MITT
description: The audio module on the MITT board is used to detect errors that occur at the transport level of the audio device by detecting sine wave frequency accuracy (at zero cross) and counting instances where the frequency or offset is incorrect.
ms.date: 01/12/2024
---

# Audio playback fidelity tests in MITT

The audio module on the MITT board is used to detect errors that occur at the transport level of the audio device by detecting sine wave frequency accuracy (at zero cross) and counting instances where the frequency or offset is incorrect. Lack of a signal or missed packets results in a shifted waveform that is audible and detectable automatically via this mechanism.

## Before you begin

- Get a MITT board and an audio adapter. See [Buy hardware for using MITT](./multi-interface-test-tool--mitt--.md).
- [Download the MITT software package](download-the-mitt-software-package.md). Install it on the system under test.
- Install MITT firmware on the MITT board. See [Get started with MITT](./get-started-with-mitt---.md).

## Hardware setup

![mitt audio test hardware setup.](images/mitttoaudio.jpg)

1. Connect the audio adapter to **JC1** on the MITT board.
2. LineIn has the input from line out of the audio device on the system under test by using a 1/8" to 1/8" male to male cable. Other audio sources may be connected up with appropriate cabling.

## Audio playback automation tests

1. Create a folder on the system under test.
2. Copy AudiounitsimpleIO.dll from the MITT software package to the folder.
3. Run all tests by using this command:

    te.exe audiounitSimpleIO.dll

4. Run as a Simple IO plugin, use the included script SimpleIO\_MITT\_Audio\_Sample.vbs
5. To disable the Audio SimpleIO tests from running, set the following registry entry:

**HKEY\_CURRENT\_USER\\Software\\Microsoft\\MITT\\AudioUnit** \\**** = RunAudioTest

Data type  
REG\_DWORD

Description  
Set to 0.

This will play a series of test tones, from 500hz to 18khz and report the number of glitches detected. If a high number of glitches, such as 10000+, is detected, verify that the cable is connected correctly and that the volume is not muted. Any interrupted signal is detected with a glitch per expected crossing so the number can be very high.

If the tests all pass, your device is connected correctly and operating as expected.
