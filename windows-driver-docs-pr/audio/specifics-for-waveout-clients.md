---
Description: Specifics for waveOut Clients
MS-HAID: 'audio.specifics\_for\_waveout\_clients'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Specifics for waveOut Clients
---

# Specifics for waveOut Clients


## <span id="specifics_for_waveout_clients"></span><span id="SPECIFICS_FOR_WAVEOUT_CLIENTS"></span>


A call to [**waveOutOpen**](multimedia.waveoutopen) returns WAVERR\_BADFORMAT if a driver does not support the specified wave format.

Microsoft Windows does not currently support the looping of a wave header with a non-PCM format. An attempt to loop a non-PCM format will fail, but the system does not detect the failure until the header-submittal (not header-preparation) stage because of architectural constraints. Specifically, a call to [**waveOutPrepareHeader**](multimedia.waveoutprepareheader) might accept a non-PCM wave header with WHDR\_BEGINLOOP and/or WHDR\_ENDLOOP set in **dwFlags**, but a subsequent call to [**waveOutWrite**](multimedia.waveoutwrite) fails and returns MMSYSERR\_INVALPARAM. If WHDR\_BEGINLOOP and WHDR\_ENDLOOP are not set in **dwFlags**, however, specifying **dwLoops**&gt;1 does not cause **waveOutWrite** to fail.

When non-PCM data is playing, a call to [**waveOutBreakLoop**](multimedia.waveoutbreakloop) fails with return code MMSYSERR\_INVALPARAM.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Specifics%20for%20waveOut%20Clients%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



