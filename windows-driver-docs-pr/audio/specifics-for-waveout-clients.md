---
title: Specifics for waveOut Clients
description: Specifics for waveOut Clients
ms.assetid: e2cfc59a-0c36-4b57-99e2-b7bed503bc12
keywords:
- waveOut non-PCM wave formats WDK audio
- non-PCM audio formats WDK , waveOut
- looping non-PCM formats
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifics for waveOut Clients


## <span id="specifics_for_waveout_clients"></span><span id="SPECIFICS_FOR_WAVEOUT_CLIENTS"></span>


A call to [**waveOutOpen**](https://msdn.microsoft.com/library/windows/desktop/dd743866) returns WAVERR\_BADFORMAT if a driver does not support the specified wave format.

Microsoft Windows does not currently support the looping of a wave header with a non-PCM format. An attempt to loop a non-PCM format will fail, but the system does not detect the failure until the header-submittal (not header-preparation) stage because of architectural constraints. Specifically, a call to [**waveOutPrepareHeader**](https://msdn.microsoft.com/library/windows/desktop/dd743868) might accept a non-PCM wave header with WHDR\_BEGINLOOP and/or WHDR\_ENDLOOP set in **dwFlags**, but a subsequent call to [**waveOutWrite**](https://msdn.microsoft.com/library/windows/desktop/dd743876) fails and returns MMSYSERR\_INVALPARAM. If WHDR\_BEGINLOOP and WHDR\_ENDLOOP are not set in **dwFlags**, however, specifying **dwLoops**&gt;1 does not cause **waveOutWrite** to fail.

When non-PCM data is playing, a call to [**waveOutBreakLoop**](https://msdn.microsoft.com/library/windows/desktop/dd743854) fails with return code MMSYSERR\_INVALPARAM.

 

 




