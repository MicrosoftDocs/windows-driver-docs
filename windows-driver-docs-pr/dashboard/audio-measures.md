---
title: Audio measures
description: Audio measure definitions
ms.topic: article
ms.date: 05/20/2019
---

# Audio measures

## Audio stream initialization

Whenever an application (or Windows component) wants to play or record audio, it uses one of various audio APIs.

All of the audio APIs eventually invoke the core audio API call [IAudioClient::Initialize](/windows/win32/api/audioclient/nf-audioclient-iaudioclient-initialize). This creates the connection between the application and the Windows audio engine, and a connection between the Windows audio engine and the audio driver.

If the IAudioClient::Initialize call fails, then the application is, with some exceptions, unable to use audio. Some IAudioClient::Initialize errors are benign and are ignored; a list of these errors is provided in the [appendix](measure-appendix.md).

The result of the call is logged in an **AudioClientInitialize** telemetry event in the **Microsoft.Windows.Audio.Client** provider. The **HResult** field is 0 if the call succeeded, and a negative number if the call failed.

The following audio measures track IAudioClient::Initialize success:
* [Percent of machines with at least one audio stream initialization failure](pct-machines-with-at-least-one-audio-stream-initialization-failure.md)
* [Percent of Machines with Subpar Stream Initialization Success Rate](pct-machines-with-subpar-stream-initialization-success-rate.md)

## Audio user-mode reliability

Kernel Streaming audio drivers run in kernel mode. If an audio driver hits an exception, it results in a Blue Screen of Death (BSOD) or Green Screen of Death (GSOD).

There are no measures specifically for audio kernel-mode reliability issues, but there are measures for kernel-mode reliability issues in general.

The Windows shared-mode audio engine runs in user mode. In particular, the "Windows Audio" service AudioSrv.dll (AudioSrv) runs in a dedicated svchost.exe process. It also launches a helper "Windows Audio Device Graph Isolation" process audiodg.exe (AudioDg).

Audio IHVs can include plugins to the user-mode audio engine called Audio Processing Objects (APOs).

If an APO hits an exception, there is no blue screen of death, but the Windows audio engine crashes. There is also a watchdog timer which verifies that calls from applications are completing quickly. If a call gets stuck, the watchdog notices and forces a crash of the Windows audio engine.

Either way, all audio on the system is lost until the audio engine can be restarted.

If AudioDg crashes, and AudioSrv is around to notice, an **AudioDgCrash** telemetry event is logged from the **Microsoft.Windows.Audio.Service** provider. (In some older versions of Windows 10, the event was **AudioDg-Crash**.)

If AudioSrv crashes, and AudioDg is around to notice, an **AudioSrvSvchostCrash** telemetry event is logged from the **Microsoft.Windows.Audio.DeviceGraph** provider. (In some older versions of Windows 10, the event was **AudioSrv-Svchost-Crash**.)

If the audio service hangs, a **Hang** telemetry event is logged from the **Microsoft.Windows.Audio.Service** provider. (In some older versions of Windows 10, for certain kinds of hangs, a **Hang** event would also be logged from the **Microsoft.Windows.Audio.DeviceGraph** provider.)

The following audio measures track the reliability of the Windows audio engine:
* [Percent of machines with at least one audio crash](pct-machines-with-at-least-one-audio-crash.md)
* [Percent of machines with at least one audio hang](pct-machines-with-at-least-one-audio-hang.md)
