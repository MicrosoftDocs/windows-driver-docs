---
title: SetupPreferredAudioDevices
description: SetupPreferredAudioDevices
ms.assetid: cc6b7da4-335d-4629-ba54-32aa32a1eb09
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SetupPreferredAudioDevices


## <span id="ddk_setuppreferredaudiodevices_ks"></span><span id="DDK_SETUPPREFERREDAUDIODEVICES_KS"></span>


The SetupPreferredAudioDevices keyword denotes the preferred audio device, which is the device that the audio system enables by default when the system contains one or more audio devices. This keyword is media-class specific and is supported by Microsoft Windows Millennium Edition/Windows 98, Microsoft Windows 2000, Windows XP, and Windows Vista. SetupPreferredAudioDevicesis not supported in Windows 7.

When creating an audio device, an application program can elect to use the default (or preferred) device instead of explicitly specifying a device. (For example, see the descriptions of the [**waveOutOpen**](https://msdn.microsoft.com/library/windows/desktop/dd743866) and **DirectSoundCreate** functions in the Microsoft Windows SDK documentation.)

The audio system keeps track of the current preferred audio device in the system registry. When a user upgrades a system by installing a new audio device, the proprietary INF file that installs the device typically updates the registry to designate the new device as the preferred audio device.

The SetupPreferredAudioDevices keyword can appear within a registry-update directive in the **add-registry-section** (see [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320)) of an INF file for an audio device. This directive has the following format:

*reg-rootkey*, \[*reg-subkey*\]SetupPreferredAudioDevices \[*flags*\], \[*dword-value*\]

The directive instructs the audio system to use the device's audio functions as the defaults for sound playback, sound recording, and MIDI music playback. Following installation, these three defaults appear in the Sounds and Multimedia control panel under the **Audio** tab. The user can use Control Panel to change the default devices.

The directive's *dword-value* parameter specifies a DWORD value that should be nonzero in order to enable the directive. If this value is zero, the directive has no effect. Because Windows Me/98 do not support the REG\_DWORD registry data type, however, *dword-value* is typically expressed as a 4-byte REG\_BINARY type instead of as a DWORD (for example, as "01,00,00,00" instead of "0x00000001"). The *dword-value* parameter can be specified in raw binary format by setting the directive's *flags* parameter to "1" (FLG\_ADDREG\_BINVALUETYPE).

The directive takes effect at the time that the driver for the device is installed. If another device occupies the role of preferred device at the time that the new device is installed, the directive causes the new device to assume the role of preferred device, thus displacing the other device from this role.

When upgrading or reinstalling the driver for a device that has already been installed, you may want to avoid altering the user's current preferred-device selections for sound playback, sound recording, and MIDI music playback. If so, set the FLG\_ADDREG\_NOCLOBBER bit in the *flags* parameter, which causes the directive to take effect only if this is the device's initial installation.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following example is a part of an INF file that shows how to use the SetupPreferredAudioDevices keyword:

```inf
  AddReg = XYZ-Audio-Device.AddReg
  ...
  [XYZ-Audio-Device.AddReg]
  HKR,,SetupPreferredAudioDevices,3,01,00,00,00
```

The directive at the end of the example specifies that the device named "XYZ-Audio-Device" is now the preferred audio device. HKR is the audio device's root key in the registry. The *flags* parameter is set to 3, which is the bitwise OR of FLG\_ADDREG\_BINVALUETYPE and FLG\_ADDREG\_NOCLOBBER. The latter prevents the device's existing preferred-device registry entries from getting overwritten in the event that the device is already installed and its driver is merely being upgraded. The four bytes at the end of the directive specify a nonzero value, which is necessary to enable the directive.

With the current implementation of the SetupPreferredAudioDevices keyword in Windows Vista, any audio endpoint with its *dword-value* set to an odd number can be set as the default device. To make sure that the correct endpoint is set as the default device, make sure that the KS filter that contains the relevant endpoint is exposed last. You have to do this because of the algorithm that the AudioEndpointBuilder service uses to populate property stores and setting default devices.

 

 





