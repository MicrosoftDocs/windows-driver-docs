---
title: Audio measures
description: Whenever an application or Windows component wants to play or record audio, it uses one of various audio APIs.
ms.topic: article
ms.date: 08/27/2024
---

# Audio measures

Whenever an application or Windows component wants to play or record audio, it uses one of various audio APIs.

## Audio stream initialization

All of the audio APIs eventually invoke the core audio API call [IAudioClient::Initialize](/windows/win32/api/audioclient/nf-audioclient-iaudioclient-initialize). The **IAudioClient::Initialize** function creates the connection between the application and the Windows audio engine, and a connection between the Windows audio engine and the audio driver.

If the **IAudioClient::Initialize** call fails, then the application is, with some exceptions, unable to use audio. Some **IAudioClient::Initialize** errors are benign and are ignored; a list of these errors is provided in the [appendix](measure-appendix.md).

The result of the call is logged in an **AudioClientInitialize** event in the **Microsoft.Windows.Audio.Client** provider. The **HRESULT** field is 0 if the call succeeded, and a negative number if the call failed.

The following audio measures track **IAudioClient::Initialize** success:

- [Percent of machines with at least one audio stream initialization failure](pct-machines-with-at-least-one-audio-stream-initialization-failure.md)
- [Percent of Machines with Subpar Stream Initialization Success Rate](pct-machines-with-subpar-stream-initialization-success-rate.md)
- [Percent of machine endpoints with at least one audio stream initialization failure per Driver](pct-machine-endpoints-with-at-least-one-audio-stream-initialization-failure-per-driver.md)
- [Percent of machine endpoints with Subpar Stream Initialization Success Rate](pct-machine-endpoints-with-subpar-stream-initialization-success-rate.md)
- [Percent of machine endpoints with at least one audio render stream initialization failure per driver](pct-machine-endpoints-with-at-least-one-audio-render-stream-initialization-failure-per-driver.md)
- [Percent of machines with at least one audio render stream initialization failure](pct-machines-with-at-least-one-audio-render-stream-initialization-failure.md)
- [Percent of machine endpoints with at least one audio capture stream initialization failure per driver](pct-machine-endpoints-with-at-least-one-audio-capture-stream-initialization-failure-per-driver.md)
- [Percent of machines with at least one audio capture stream initialization failure](pct-machines-with-at-least-one-audio-capture-stream-initialization-failure.md)

## Audio user-mode reliability

Kernel streaming audio drivers run in kernel mode. If an audio driver hits an exception, it results in a blue screen of death (BSOD) or green screen of death (GSOD).

There are no measures specifically for audio kernel-mode reliability issues, but there are measures for kernel-mode reliability issues in general.

The Windows shared-mode audio engine runs in user mode. In particular, the Windows audio service, AudioSrv.dll (AudioSrv), runs in a dedicated svchost.exe process. It also launches a helper *Windows Audio Device Graph Isolation* process, audiodg.exe (AudioDg).

Audio IHVs can include plugins to the user-mode audio engine called audio processing objects (APOs).

If an APO hits an exception, there's no blue screen of death, but the Windows audio engine crashes. There's also a watchdog timer that verifies that calls from applications are completing quickly. If a call gets stuck, the watchdog notices and forces a crash of the Windows audio engine.

Either way, all audio on the system is lost until the audio engine can be restarted.

If AudioDg crashes, and AudioSrv is around to notice, an **AudioDgCrash** event is logged from the **Microsoft.Windows.Audio.Service** provider. In some older versions of Windows 10, the event was **AudioDg-Crash**.

If AudioSrv crashes, and AudioDg is around to notice, an **AudioSrvSvchostCrash** event is logged from the **Microsoft.Windows.Audio.DeviceGraph** provider. In some older versions of Windows 10, the event was **AudioSrv-Svchost-Crash**.

If the audio service hangs, a **Hang** event is logged from the **Microsoft.Windows.Audio.Service** provider. In some older versions of Windows 10, for certain kinds of hangs, a **Hang** event would also be logged from the **Microsoft.Windows.Audio.DeviceGraph** provider.

The following audio measures track the reliability of the Windows audio engine:

- [Percent of machines with at least one audio crash](pct-machines-with-at-least-one-audio-crash.md)
- [Percent of machines with at least one audio hang](pct-machines-with-at-least-one-audio-hang.md)
- [Percent of machine endpoints with at least one audio crash](pct-machine-endpoints-with-at-least-one-audio-crash.md)
- [Percent of machine endpoints with at least one audio hang](pct-machine-endpoints-with-at-least-one-audio-hang.md)

## Audio Processing Object disablement

This measure tracks automatic disablement of audio processing objects:

- [Percent of machines with at least one APO disablement in past seven days](pct-machines-with-at-least-one-apo-disablement-in-past-7-days.md)

## What to do if your shipping label is rejected

If your shipping label is rejected, see [Appeal a rejected audio driver](appeal-rejected-audio-driver.md)
