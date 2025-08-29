---
title: PKEY\_APO\_SWFallback\_ProcessingModes
description: In Windows 10 version 1709 and later, the PKEY\_APO\_SWFallback\_ProcessingModes property key identifies the HW modes that can fallback to software processing modes supported by the driver.
ms.date: 10/22/2018
ms.topic: reference
---

# PKEY\_APO\_SWFallback\_ProcessingModes

Starting in Windows 10 version 1809, the *PKEY\_APO\_SWFallback\_ProcessingModes* property key identifies the modes that can fallback to software processing. The driver developer should list all of the mode effect processing modes that support software fallback that their driver supports. This list needs to encompass all the modes that the driver supports in hardware.

If a stream is requested for one of these modes and there are insufficient HW resources available to open a pin in that processing mode, a pin will be opened in the RAW mode and the SW APO initialized with the requested processing mode will be used instead. Because of this, drivers that would like to support software fallback of HW processing modes, must support RAW mode. For more information about audio modes, see [Audio Signal Processing Modes](audio-signal-processing-modes.md). SW fallback applies only to the HOST pin.

SW fallback is triggered when a stream is created and there aren’t available resources in the hardware. The OS does a direct query to the driver for available resources to determine if SW fallback is required. The OS uses knowledge of the driver, such as how many pin instances are supported by the driver, to determine if there are not sufficient HW resources.  If the HW resources are not available SW fallback is used to create streams on the RAW pin. The SW fallback process is managed by the OS and requires no input from the driver when SW fallback occurs. The driver does not need to return any  additional specific  error codes to use SWFallback.

If audio constraints have been specified, the OS will do an additional check against those. For more information, see  [Audio Hardware Resource Management](audio-hardware-resource-management.md).

The driver needs to have the supported fallback modes in their FxPropertyStore. Any AUDIO_SIGNALPROCESSINGMODEs for SWFallback need to be added to the FxPropertyStore for the driver under PKEY_APO_SWFallback_ProcessingModes which is {D3993A3F-99C2-4402-B5EC-A92A0367664B},13. This will allow for them to be recognized for SWFallback. 



###  PKEY\_APO\_SWFallback\_ProcessingModes Definition

*PKEY\_APO\_SWFallback\_ProcessingModes* is defined as shown here.

```inf
PKEY_APO_SWFallback_ProcessingModes (REG_MULTI_SZ) = {D3993A3F-99C2-4402-B5EC-A92A0367664B},13 
```


### <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample

The INF file property key lists the signal processing modes supported by the host connector that are available for fallback to SW APO if sufficient HW resources aren't available. 

An INF file specifies settings for in the add-registry section for that device. The following INF example shows the strings and add-registry sections that loads the APO SW fallback processing modes into the registry. In this example four modes are implemented, raw, default, movie and communications. 

```cpp
[Strings]
PKEY_APO_SWFallback_ProcessingModes  = "{D3993A3F-99C2-4402-B5EC-A92A0367664B},13"
...
AUDIO_SIGNALPROCESSINGMODE_DEFAULT = "{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}"
AUDIO_SIGNALPROCESSINGMODE_MOVIE   = "{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}"
AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS = "{98951333-B9CD-48B1-A0A3-FF40682D73F7}"
...
[PKEY.APO.SWFallback.AddReg]
;Include all supported modes:
HKR,"FX\\0",%PKEY_APO_SWFallback_ProcessingModes%,%REG_MULTI_SZ%,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%,%AUDIO_SIGNALPROCESSINGMODE_MOVIE%,%AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS%
```

## Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)




