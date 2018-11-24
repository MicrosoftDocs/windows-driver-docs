---
title: Audio Drivers Structures
description: Audio Drivers Structures
ms.assetid: 8257342f-474a-42b3-809d-96fdeede398b
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Audio Drivers Structures


## <span id="ddk_audio_drivers_structures_ks"></span><span id="DDK_AUDIO_DRIVERS_STRUCTURES_KS"></span>


This section describes the structures that are used by WDM audio miniport drivers. The list of structures is as follows:

[**APO\_REG\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/dn425140)

[**APOInitBaseStruct**](https://msdn.microsoft.com/library/windows/hardware/jj151545)

[**APOInitSystemEffects**](https://msdn.microsoft.com/library/windows/hardware/jj151546)

[**APOInitSystemEffects2**](https://msdn.microsoft.com/library/windows/hardware/dn659347)

[**AudioFXExtensionParams**](https://msdn.microsoft.com/library/windows/hardware/jj151547)

[**DMUS\_KERNEL\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff536340)

[**DRMFORWARD**](https://msdn.microsoft.com/library/windows/hardware/ff536350)

[**DRMRIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff536355)

[**DS3DVECTOR**](https://msdn.microsoft.com/library/windows/hardware/ff536367)

[**KSAC3\_ALTERNATE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537055)

[**KSAC3\_BIT\_STREAM\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff537077)

[**KSAC3\_DIALOGUE\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff537078)

[**KSAC3\_DOWNMIX**](https://msdn.microsoft.com/library/windows/hardware/ff537079)

[**KSAC3\_ERROR\_CONCEALMENT**](https://msdn.microsoft.com/library/windows/hardware/ff537080)

[**KSAC3\_LANGUAGE\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff537081)

[**KSAC3\_ROOM\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff537082)

[**KSAUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537083)

[**KSAUDIO\_COPY\_PROTECTION**](https://msdn.microsoft.com/library/windows/hardware/ff537084)

[**KSAUDIO\_DYNAMIC\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff537085)

[**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](https://msdn.microsoft.com/library/windows/hardware/ff537087)

[**KSAUDIO\_MICROPHONE\_COORDINATES**](https://msdn.microsoft.com/library/windows/hardware/ff537086)

[**KSAUDIO\_MIX\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff537090)

[**KSAUDIO\_MIXCAP\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff537088)

[**KSAUDIO\_MIXLEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff537089)

[**KSAUDIO\_PACKETSIZE\_CONSTRAINTS**](https://msdn.microsoft.com/library/windows/hardware/dn965561)

[**KSAUDIO\_PACKETSIZE\_CONSTRAINTS2**](https://msdn.microsoft.com/library/windows/hardware/mt761740)

[**KSAUDIO\_PACKETSIZE\_PROCESSINGMODE\_CONSTRAINT**](https://msdn.microsoft.com/library/windows/hardware/dn965562)

[**KSAUDIO\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/ff537091)

[**KSAUDIO\_POSITIONEX**](https://msdn.microsoft.com/library/windows/hardware/ff537092)

[**KSAUDIO\_PREFERRED\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff537093)

[**KSAUDIO\_PRESENTATION\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/hh450865)

[**KSAUDIOENGINE\_BUFFER\_SIZE\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/hh450864)

[**KSAUDIOENGINE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/hh450862)

[**KSAUDIOENGINE\_VOLUMELEVEL**](https://msdn.microsoft.com/library/windows/hardware/hh831854)

[**KSDATAFORMAT\_DSOUND**](https://msdn.microsoft.com/library/windows/hardware/ff537094)

[**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095)

[**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096)

[**KSDATARANGE\_MUSIC**](https://msdn.microsoft.com/library/windows/hardware/ff537097)

[**KSDRMAUDIOSTREAM\_CONTENTID**](https://msdn.microsoft.com/library/windows/hardware/ff537099)

[**KSDSOUND\_BUFFERDESC**](https://msdn.microsoft.com/library/windows/hardware/ff537121)

[**KSDS3D\_BUFFER\_ALL**](https://msdn.microsoft.com/library/windows/hardware/ff537101)

[**KSDS3D\_BUFFER\_CONE\_ANGLES**](https://msdn.microsoft.com/library/windows/hardware/ff537103)

[**KSDS3D\_HRTF\_FILTER\_FORMAT\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff537104)

[**KSDS3D\_HRTF\_INIT\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff537106)

[**KSDS3D\_HRTF\_PARAMS\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff537108)

[**KSDS3D\_ITD\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff537110)

[**KSDS3D\_ITD\_PARAMS\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff537114)

[**KSDS3D\_LISTENER\_ALL**](https://msdn.microsoft.com/library/windows/hardware/ff537116)

[**KSDS3D\_LISTENER\_ORIENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff537119)

[**KSJACK\_DESCRIPTION**](ksjack-description.md)

[**KSJACK\_DESCRIPTION2**](ksjack-description2.md)

[**KSJACK\_SINK\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff537140)

[**KSMUSICFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff537142)

[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

[**KSNODEPROPERTY\_AUDIO\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff537145)

[**KSP\_DRMAUDIOSTREAM\_CONTENTID**](https://msdn.microsoft.com/library/windows/hardware/ff537492)

[**KSP\_PINMODE**](https://msdn.microsoft.com/library/windows/hardware/dn457711)

[KSRTAUDIO Structures](https://msdn.microsoft.com/library/windows/hardware/ff537500)

[**KSTELEPHONY\_CALLCONTROL**](https://msdn.microsoft.com/library/windows/hardware/mt169883)

[**KSTELEPHONY\_CALLINFO**](https://msdn.microsoft.com/library/windows/hardware/mt169884)

[**KSTELEPHONY\_PROVIDERCHANGE**](https://msdn.microsoft.com/library/windows/hardware/mt169885)

[**KSTOPOLOGY\_ENDPOINTID**](https://msdn.microsoft.com/library/windows/hardware/mt169886)

[**KSTOPOLOGY\_ENDPOINTIDPAIR**](https://msdn.microsoft.com/library/windows/hardware/mt169887)

[**LOOPEDSTREAMING\_POSITION\_EVENT\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff537505)

[**MDEVICECAPSEX**](https://msdn.microsoft.com/library/windows/hardware/ff537512)

[**MIDIOPENDESC**](https://msdn.microsoft.com/library/windows/hardware/ff537518)

[**RTAUDIO\_GETREADPACKET\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt169891)

[**RTAUDIO\_SETWRITEPACKET\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt169892)

[**SOUNDDETECTOR\_PATTERNHEADER**](https://msdn.microsoft.com/library/windows/hardware/dn957513)

[**SYNTH\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff538460)

[**SYNTH\_PORTPARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff538467)

[**SYNTH\_STATS**](https://msdn.microsoft.com/library/windows/hardware/ff538473)

[**SYNTHCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff538424)

[**SYNTHDOWNLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff538429)

[**SYNTHVOICEPRIORITY\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff538452)

[**SYSAUDIO\_ATTACH\_VIRTUAL\_SOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff538480)

[**SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff538485)

[**SYSAUDIO\_INSTANCE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff538490)

[**SYSAUDIO\_SELECT\_GRAPH**](https://msdn.microsoft.com/library/windows/hardware/ff538500)

[**UNCOMPRESSEDAUDIOFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff538640)

[**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799)

[**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802)

 

 





