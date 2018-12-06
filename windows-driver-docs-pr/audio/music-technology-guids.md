---
title: Music Technology GUIDs
description: Music Technology GUIDs
ms.assetid: 3b7c2907-e67f-458e-809d-080dcc30be1a
keywords:
- WDM audio extensions WDK , music technology GUIDs
- music technology GUIDs WDK audio
- KSDATARANGE_MUSIC structure
- synthesizers WDK audio , technology GUIDs
- MIDI stream data formats WDK audio
- DirectMusic WDK audio , stream data formats
- DMus stream data formats WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Music Technology GUIDs


## <span id="music_technology_guids"></span><span id="MUSIC_TECHNOLOGY_GUIDS"></span>


A MIDI or DMus miniport driver must specify the range of stream formats that each of its pins is capable of handling. As described in [Pin Factories](pin-factories.md), the driver specifies this information as an array of one or more data range descriptors, each of which is a structure of type [**KSDATARANGE\_MUSIC**](https://msdn.microsoft.com/library/windows/hardware/ff537097). This structure's **Technology** member indicates what type of synthesizer technology the MIDI or DirectMusic device uses. A miniport driver can set the **Technology** member to one of the GUID values shown in the following table (left column).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">KSDATARANGE_MUSIC Technology GUID</th>
<th align="left">MIDIOUTCAPS wTechnology Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>KSMUSIC_TECHNOLOGY_PORT</p></td>
<td align="left"><p>MOD_MIDIPORT</p></td>
<td align="left"><p>The device is an MPU-401 device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSMUSIC_TECHNOLOGY_SYNTH</p></td>
<td align="left"><p>MOD_SYNTH</p></td>
<td align="left"><p>The device is a synthesizer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSMUSIC_TECHNOLOGY_SQSYNTH</p></td>
<td align="left"><p>MOD_SQSYNTH</p></td>
<td align="left"><p>The device is a square-wave synthesizer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSMUSIC_TECHNOLOGY_FMSYNTH</p></td>
<td align="left"><p>MOD_FMSYNTH</p></td>
<td align="left"><p>The device is an FM synthesizer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSMUSIC_TECHNOLOGY_MAPPER</p></td>
<td align="left"><p>MOD_MAPPER</p></td>
<td align="left"><p>The device is the Microsoft MIDI mapper.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSMUSIC_TECHNOLOGY_WAVETABLE</p></td>
<td align="left"><p>MOD_WAVETABLE</p></td>
<td align="left"><p>The device is a hardware wavetable synthesizer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSMUSIC_TECHNOLOGY_SWSYNTH</p></td>
<td align="left"><p>MOD_SWSYNTH</p></td>
<td align="left"><p>The device is a software synthesizer.</p></td>
</tr>
</tbody>
</table>

 

The **midiOutGetDevCaps** function translates the technology GUID that it receives from the driver to an index that it writes to the **wTechnology** member of the MIDIOUTCAPS structure that it outputs to the caller. The preceding table shows the **wTechnology** value (center column) corresponding to each technology GUID. For more information about **midiOutGetDevCaps** and MIDIOUTCAPS, see the Microsoft Windows SDK documentation.

When enumerating devices, a MIDI application that uses the Windows multimedia midiOut or midiIn API can see MIDI pins, but not DirectMusic pins. A DirectMusic application can see both MIDI and DirectMusic pins. A MIDI or DMus miniport driver identifies a MIDI pin by setting the subtype GUID in the pin's data ranges to KSDATAFORMAT\_SUBTYPE\_MIDI. A DMus miniport driver identifies a DirectMusic pin by setting the subtype GUID to KSDATAFORMAT\_SUBTYPE\_DIRECTMUSIC. For examples of data ranges for MIDI and DirectMusic pins, see [MIDI Stream Data Range](midi-stream-data-range.md) and [DirectMusic Stream Data Range](directmusic-stream-data-range.md).

As explained in [MIDI and DirectMusic Filters](midi-and-directmusic-filters.md), an adapter driver calls the [**PcNewMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff537714) function to create an instance of one of the system-supplied miniport drivers in Portcls.sys. The caller specifies one of the driver GUIDs in the following table to specify which miniport driver to instantiate.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Driver GUID</th>
<th align="left">Technology GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>CLSID_MiniportDriverDMusUART</strong></p></td>
<td align="left"><p>KSMUSIC_TECHNOLOGY_PORT</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CLSID_MiniportDriverDMusUARTCapture</strong></p></td>
<td align="left"><p>KSMUSIC_TECHNOLOGY_PORT</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CLSID_MiniportDriverFmSynth</strong></p></td>
<td align="left"><p>KSMUSIC_TECHNOLOGY_FMSYNTH</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CLSID_MiniportDriverFmSynthWithVol</strong></p></td>
<td align="left"><p>KSMUSIC_TECHNOLOGY_FMSYNTH</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CLSID_MiniportDriverUart</strong></p></td>
<td align="left"><p>KSMUSIC_TECHNOLOGY_PORT</p></td>
</tr>
</tbody>
</table>

 

The right column of the preceding table indicates the technology GUID that the corresponding miniport driver specifies in its pins' data ranges. For example, the FmSynth miniport driver assigns the technology GUID KSMUSIC\_TECHNOLOGY\_FMSYNTH to its pins.

Some wavetable synthesizer devices expose themselves to applications as MPU-401 devices (with technology GUID KSMUSIC\_TECHNOLOGY\_PORT). In the absence of an external synthesizer, they are able to play a raw MIDI byte stream through the wavetable synthesizer.

However, the midiOut API prefers wavetable synthesizer devices (with technology GUID KSMUSIC\_TECHNOLOGY\_WAVETABLE) when selecting the default (preferred) MIDI playback device. It explicitly avoids selecting an MPU-401 device to be the default device.

To make itself eligible to be the default device, a wavetable device that can play raw MIDI should expose itself as a wavetable device, not an MPU-401 device. However, if an adapter driver is using the system-supplied MPU-401 miniport driver, DMusUART, to manage its wavetable synthesizer device, that miniport driver statically assigns the technology GUID KSMUSIC\_TECHNOLOGY\_PORT to its pins.

By calling the [**IMusicTechnology::SetTechnology**](https://msdn.microsoft.com/library/windows/hardware/ff536780) method, an adapter driver can overwrite the technology GUIDs in a miniport driver's data ranges. In the following code example, an adapter driver changes the technology GUID in the DMusUART miniport driver's data ranges from its default value, KSMUSIC\_TECHNOLOGY\_PORT, to the value KSMUSIC\_TECHNOLOGY\_WAVETABLE. With this new setting, the MPU-like wavetable device is eligible to be selected by the midiOut API as the default MIDI device.

```cpp
  // Create the miniport object.
  PUNKNOWN miniport;

  ntStatus = PcNewMiniport((PMINIPORT*)&miniport, CLSID_MiniportDriverDMusUART);

  // Query the miniport driver for the IMusicTechnology interface.
  IMusicTechnology* pMusicTechnology;

  if (NT_SUCCESS(ntStatus))
  {
      ntStatus = miniport->QueryInterface(IID_IMusicTechnology, (PVOID*)&pMusicTechnology);
  }

  // Set the Technology members in the DirectMusic data-range entries
  // for all the pins that are exposed by this miniport.
  // SetTechnology should be called before initializing the miniport.
  if (NT_SUCCESS(ntStatus))
  {
      ntStatus = pMusicTechnology->SetTechnology(&KSMUSIC_TECHNOLOGY_WAVETABLE);
  }
```

As indicated in the comment in the preceding code example, the adapter driver should call [**SetTechnology**](https://msdn.microsoft.com/library/windows/hardware/ff536780) before calling the port driver's `Init` method (which, in turn, calls the miniport driver's `Init` method). The system-supplied DMusUART and UART miniport drivers both support the [IMusicTechnology](https://msdn.microsoft.com/library/windows/hardware/ff536778) interface. For other miniport drivers, support for IMusicTechnology is optional. For more information, see the implementation of the **SetTechnology** method in the DMusUART sample audio driver in the Microsoft Windows Driver Kit (WDK).

 

 




