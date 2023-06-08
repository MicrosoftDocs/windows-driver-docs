---
title: PKEY_AudioEngine_OEMPeriod
description: PKEY_AudioEngine_OEMPeriod
ms.date: 05/05/2023
ms.topic: reference
---

# PKEY_AudioEngine_OEMPeriod

The Windows audio engine runs at predetermined intervals that are referred to as the *periodicity* of the audio engine. In Windows 7 and later versions of Windows, the audio engine runs with a periodicity of 10 ms by default. In Windows 7, you can use an INF file and a new registry key, **PKEY_AudioEngine_OEMPeriod**, to customize the periodicity for your audio device driver. This is a per endpoint setting.

The following excerpt from an INF file shows how to use the [**INF AddReg directive**](../install/inf-addreg-directive.md) to customize the periodicity for an audio device driver.

```inf
[Version]
Signature="$Windows NT$"
Class=MEDIA
ClassGuid={4d36e96c-e325-11ce-bfc1-08002be10318}
Provider=%ExampleProvider%
CatalogFile=ExampleCatalog.cat
PnpLockdown=1

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
ExampleProvider = "Example Provider"
PKEY_AudioEndpoint_Association = "{1DA5D803-D492-4EDD-8C23-E0C0FFEE7F0E},2"
PKEY_AudioEngine_OEMPeriod = "{E4870E26-3CC5-4CD2-BA46-CA0A9A70ED04},6"
REG_BINARY          = "0x00000001"
```

Periodicity is specified as VT_BLOB. And the valid periodicity range is 50000-90000 (5-9 ms) on even 10000 HNSTIME unit boundaries (for example, 50000, 60000, 70000, 80000 or 90000).

In the preceding excerpt from an INF file, the following REG_BINARY data is provided for customization:

The periodicity of 8 ms is represented in HNSTIME units as 80000. In hexadecimal notation this value is represented as 0x013880. When this hexadecimal value is written four bits (nibbles) at a time, with least significant bits first, the result is 80,38,01. This is the value that is provided as a REG_BINARY data type.

Periodicity is specified as a VT_BLOB data type. This is represented by a decimal value of 65. In hexadecimal format 65 is represented by the value 41 and the preceding INF file excerpt shows the REG_BINARY data sequence with its first value of 41.
