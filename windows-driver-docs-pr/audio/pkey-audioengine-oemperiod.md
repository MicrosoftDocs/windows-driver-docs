---
title: PKEY\_AudioEngine\_OEMPeriod
description: PKEY\_AudioEngine\_OEMPeriod
ms.assetid: e0cefdbf-7016-4609-a898-592a40b5d430
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PKEY\_AudioEngine\_OEMPeriod


The Windows audio engine runs at predetermined intervals that are referred to as the *periodicity* of the audio engine. In Windows 7 and later versions of Windows, the audio engine runs with a periodicity of 10ms by default. In Windows 7, you can use an INF file and a new registry key, **PKEY\_AudioEngine\_OEMPeriod**, to customize the periodicity for your audio device driver. This is a per endpoint setting.

The following excerpt from an INF file shows how to use the [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) to customize the periodicity for an audio device driver.

```
[Version]
Signature="$CHICAGO$"
Class=MEDIA
Provider=%MSFT%
...
[USBAudio]
Include=ks.inf, wdmaudio.inf, wdma_usb.inf
Needs=KS.Registration, WDMAUDIO.Registration, USBAudio.CopyList, USBAudioOEM.AddReg

[USBAudio.Interfaces]
AddInterface=%KSCATEGORY_AUDIO%,"GLOBAL",USBAudio.Interface
AddInterface=%KSCATEGORY_RENDER%,"GLOBAL",USBAudio.Interface

[USBAudio.Interface]
AddReg=USBAudio.Interface.AddReg, OEMSettingsOverride.AddReg
...
;;
;; All EP\\0 entries in the same grouping
;;
;; Set default periodicity to 8ms
;;
;; 0x013880 == 80000 (HNSTIME) == 8ms
;;
[OEMSettingsOverride.AddReg]
HKR,"EP\\0", %PKEY_AudioEndpoint_Association%,,%KSNODETYPE_ANY%
HKR,"EP\\0", %PKEY_AudioEngine_OEMPeriod%, %REG_BINARY%, 41,00,63,00,08,00,00,00,80,38,01,00,00,00,00,00

[Strings]
PKEY_AudioEndpoint_Association = "{1DA5D803-D492-4EDD-8C23-E0C0FFEE7F0E},2"
PKEY_AudioEngine_OEMPeriod = "{E4870E26-3CC5-4CD2-BA46-CA0A9A70ED04},6"
REG_BINARY          = "0x00000001"
```

Periodicity is specified as VT\_BLOB. And the valid periodicity range is 50000-90000 (5-9ms) on even 10000 HNSTIME unit boundaries (for example, 50000, 60000, 70000, 80000 or 90000).

In the preceding excerpt from an INF file, the following REG\_BINARY data is provided for customization:

The periodicity of 8ms is represented in HNSTIME units as 80000. In hexadecimal notation this value is represented as 0x013880. When this hexadecimal value is written four bits (nibbles) at a time, with least significant bits first, the result is 80,38,01. This is the value that is provided as a REG\_BINARY data type.

Periodicity is specified as a VT\_BLOB data type. This is represented by a decimal value of 65. In hexadecimal format 65 is represented by the value 41 and the preceding INF file excerpt shows the REG\_BINARY data sequence with its first value of 41.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20PKEY_AudioEngine_OEMPeriod%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




