---
title: Installing Device Interfaces for an Audio Adapter
description: Installing Device Interfaces for an Audio Adapter
ms.assetid: 824cc6a2-702a-4e51-91b1-ab776b1babf1
keywords:
- audio adapters WDK , device interfaces
- adapter drivers WDK audio , device interfaces
- Port Class audio adapters WDK , device interfaces
- device interfaces WDK audio
- subdevices WDK audio
- audio device interfaces WDK
ms.date: 10/27/2017
ms.localizationpriority: medium
---

# Installing Device Interfaces for an Audio Adapter


## <span id="installing_device_interfaces_for_an_audio_adapter"></span><span id="INSTALLING_DEVICE_INTERFACES_FOR_AN_AUDIO_ADAPTER"></span>


A client accesses an audio device through a set of [*device interfaces*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss_device_interface) that a vendor specifies in the adapter's INF file. The device interfaces specified in the INF file have a one-to-one correspondence with the subdevices that the adapter driver creates when it initializes the device (see [Subdevice Creation](subdevice-creation.md)). For each device interface, the INF file specifies a **FriendlyName** entry value, which is accessible in user mode, under the interface's registry key.

In the kernel-streaming architecture, topology categories (see [**KSPROPERTY\_TOPOLOGY\_CATEGORIES**](https://msdn.microsoft.com/library/windows/hardware/ff565799)) represent device interface classes.

The following table lists the topology categories that audio adapters are most likely to use to describe the capabilities of their subdevices.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Category</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>KSCATEGORY_ACOUSTIC_ECHO_CANCEL</p></td>
<td align="left"><p>An audio device that can perform acoustic echo cancellation (see [DirectSound Capture Effects](directsound-capture-effects.md)) registers itself under this category.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSCATEGORY_AUDIO</p></td>
<td align="left"><p>All audio devices register themselves under this category.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSCATEGORY_CAPTURE</p></td>
<td align="left"><p>An audio device that can capture a data stream registers itself under this category.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSCATEGORY_DATATRANSFORM</p></td>
<td align="left"><p>An audio device that performs a data transformation on a stream registers itself under this category.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSCATEGORY_MIXER</p></td>
<td align="left"><p>An audio device that can mix data streams registers itself under this category.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSCATEGORY_RENDER</p></td>
<td align="left"><p>An audio device that can render a data stream registers itself under this category.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSCATEGORY_SYNTHESIZER</p></td>
<td align="left"><p>An audio device that can convert MIDI messages to either wave audio samples or an analog output signal registers itself under this category (see [Synthesizers and Wave Sinks](synthesizers-and-wave-sinks.md)).</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSCATEGORY_TOPOLOGY</p></td>
<td align="left"><p>A device's [Topology miniport driver](topology-miniport-driver.md) registers itself under this category.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSCATEGORY_DRM_DESCRAMBLE</p></td>
<td align="left"><p>An audio device that can unscramble a DRM-protected wave stream registers itself under this category (see [Digital Rights Management](digital-rights-management.md)).</p></td>
</tr>
</tbody>
</table>

 

For a complete list of topology categories, see the KSCATEGORY\_*XXX* GUIDs that are defined in the header files Ks.h and Ksmedia.h.

All audio devices are classified under KSCATEGORY\_AUDIO, but an audio device might also be classified under additional categories such as KSCATEGORY\_RENDER (for an audio rendering device) or KSCATEGORY\_SYNTHESIZER (for a synthesizer). For each category that the INF file specifies for a device, the Windows Installer builds a set of registry entries for that device under the category name (see [Filter Factories](filter-factories.md)).

Only a device that contains a built-in synthesizer should register itself under the category KSCATEGORY\_SYNTHESIZER. Note that this category excludes a pure MPU-401 device. A pure MPU-401 device, which can output or input raw MIDI to or from a UART, should register itself under these categories:

-   KSCATEGORY\_AUDIO

-   KSCATEGORY\_RENDER

-   KSCATEGORY\_CAPTURE

Note that the [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver) reserves the registry category KSCATEGORY\_AUDIO\_DEVICE exclusively for its [virtual audio devices](virtual-audio-devices.md). Adapter drivers should not register themselves in this category.

The following example installs four common system-defined device interfaces that an adapter typically supports for an audio device.

### <span id="example__installing_audio_device_interfaces"></span><span id="EXAMPLE__INSTALLING_AUDIO_DEVICE_INTERFACES"></span>Example: Installing Audio Device Interfaces

In this example, the device-install section for the XYZ Audio Device uses the [**INF AddInterface directive**](https://msdn.microsoft.com/library/windows/hardware/ff546310) to install four audio adapter interfaces. In the following, each of the four directives assigns a unique reference string to an interface, which the adapter driver can use to distinguish between instances of each interface class.

```inf
  [XYZ-Audio-Device.Interfaces]
  AddInterface=%KSCATEGORY_AUDIO%,%KSName_Wave%,XYZ-Audio-Device.Wave
  AddInterface=%KSCATEGORY_RENDER%,%KSName_Wave%,XYZ-Audio-Device.Wave
  AddInterface=%KSCATEGORY_CAPTURE%,%KSName_Wave%,XYZ-Audio-Device.Wave
  AddInterface=%KSCATEGORY_TOPOLOGY%,%KSName_Topology%,XYZ-Audio-Device.Topology
```

The first three **AddInterface** directives specify an add-interface section named XYZ-Audio-Device.Wave. The last specifies an add-interface section named XYZ-Audio-Device.Topology. Each add-interface section adds the following registry entries to a device interface subkey, which is accessible in user mode under the \\DeviceClasses\\&lt;*InterfaceGUID*&gt; registry key:

-   A FriendlyName registry entry specifies a friendly name for each device interface.

-   Microsoft DirectShow requires a CLSID registry entry, set to a proxy GUID value, which indicates that the adapter can be accessed and controlled by the KSProxy system driver.

The two add-interface sections appear in the following example, which contains INF file entries that add each interface's FriendlyName and CLSID to the registry:

```inf
  [XYZ-Audio-Device.Wave]
  AddReg=XYZ-Audio-Device.Wave.AddReg
  [XYZ-Audio-Device.Wave.AddReg]
  HKR,,FriendlyName,,%WaveDeviceName%
  HKR,,CLSID,,%Proxy.CLSID%

  [XYZ-Audio-Device.Topology]
  AddReg=XYZ-Audio-Device.Topology.AddReg
  [XYZ-Audio-Device.Topology.AddReg]
  HKR,,FriendlyName,,%WaveDeviceMixerName%
  HKR,,CLSID,,%Proxy.CLSID%
```

The keyword HKR in this example denotes the system-supplied registry path for the device. For more information, see [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

The following is the Strings section for this example.

```inf
  [Strings]
  KSCATEGORY_AUDIO="{6994AD04-93EF-11D0-A3CC-00A0C9223196}"
  KSCATEGORY_RENDER="{65E8773E-8F56-11D0-A3B9-00A0C9223196}"
  KSCATEGORY_CAPTURE="{65E8773D-8F56-11D0-A3B9-00A0C9223196}"
  KSCATEGORY_TOPOLOGY="{DDA54A40-1E4C-11D1-A050-405705C10000}"
  Proxy.CLSID="{17CCA71B-ECD7-11D0-B908-00A0C9223196}"
  WaveDeviceName="XYZ Audio Device"
  WaveDeviceMixerName="XYZ Audio Device Super Mixer"
```

The string name that an **AddInterface** directive specifies for a KSCATEGORY\_*XXX* device interface cannot be localized because the adapter driver uses the same name internally as a string constant. The sample adapter drivers in the Windows Driver Kit (WDK) use the following string names for their audio device interfaces:

```inf
  KSNAME_Wave="Wave"
  KSNAME_UART="UART"
  KSNAME_FMSynth="FMSynth"
  KSNAME_Topology="Topology"
  KSNAME_Wavetable="Wavetable"
  KSNAME_DMusic="DMusic"
```

For the sake of uniformity, your proprietary driver should assign these same names to its corresponding device interfaces. If your driver supports additional device interfaces that are proprietary, you can invent your own proprietary names for these interfaces. Make sure that the names that the driver uses match those in your INF file. If the strings do not match, system setup will not load the driver.

 

 




