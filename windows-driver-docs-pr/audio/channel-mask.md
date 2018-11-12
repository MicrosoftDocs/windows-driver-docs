---
title: Channel Mask
description: Channel Mask
ms.assetid: 875ed000-ac53-4365-8381-3fe08d45cbcc
keywords:
- data formats WDK audio
- formats WDK audio , data
- audio data formats WDK
- formats WDK audio , multichannel
- multichannel formats WDK audio
- home-theater systems WDK audio
- speakers WDK audio , home-threater systems
- audio drivers WDK , home-theater systems
- WDM audio drivers WDK , home-theater systems
- 7.1 home theater speakers WDK audio
- 7.1 wide configuration speakers WDK audio
- wide configuration speakers WDK audio
- LFE speakers
- subwoofers WDK audio
- recording formats WDK audio
- playback WDK audio
- channel masks WDK audio
- mask bits WDK audio
- PCM formats WDK audio
- positions WDK audio
- data formats WDK audio , channel masks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Channel Mask


In Windows, the [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) structure defines the data format for a multichannel PCM audio stream. This structure specifies parameters such as the number of bits per PCM sample, the number of channels in the stream, and the channel mask. The channel mask specifies the mapping of channels to speakers. The following figure shows the individual bits in the channel mask.

![diagram illustrating the individual bits in the channel mask](images/spkrcfg3.png)

Each bit in the channel mask represents a particular speaker position. If the mask assigns a channel to a particular speaker position, the mask bit that represents that position is set to 1; all mask bits for unassigned speaker positions are set to 0. The WAVEFORMATEXTENSIBLE structure defines additional bits in the channel mask that are not shown in the preceding figure, but these bits have no bearing on the home-theater speaker configurations under discussion and are omitted for simplicity.

The encoding of speaker positions in the channel mask in the preceding figure is similar to that used for the property value of a [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537250) property request. For more information, see [**KSAUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537083).

The following table shows the meaning of each mask bit in the preceding figure.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bit Number</th>
<th align="left">Speaker Position</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>FL</p></td>
<td align="left"><p>Front left</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>FR</p></td>
<td align="left"><p>Front right</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>FC</p></td>
<td align="left"><p>Front center</p></td>
</tr>
<tr class="even">
<td align="left"><p>3</p></td>
<td align="left"><p>LFE</p></td>
<td align="left"><p>Low-frequency effects</p></td>
</tr>
<tr class="odd">
<td align="left"><p>4</p></td>
<td align="left"><p>BL</p></td>
<td align="left"><p>Back left</p></td>
</tr>
<tr class="even">
<td align="left"><p>5</p></td>
<td align="left"><p>BR</p></td>
<td align="left"><p>Back right</p></td>
</tr>
<tr class="odd">
<td align="left"><p>6</p></td>
<td align="left"><p>FLC</p></td>
<td align="left"><p>Front left of center</p></td>
</tr>
<tr class="even">
<td align="left"><p>7</p></td>
<td align="left"><p>FRC</p></td>
<td align="left"><p>Front right of center</p></td>
</tr>
<tr class="odd">
<td align="left"><p>8</p></td>
<td align="left"><p>BC</p></td>
<td align="left"><p>Back center</p></td>
</tr>
<tr class="even">
<td align="left"><p>9</p></td>
<td align="left"><p>SL</p></td>
<td align="left"><p>Side left</p></td>
</tr>
<tr class="odd">
<td align="left"><p>10</p></td>
<td align="left"><p>SR</p></td>
<td align="left"><p>Side right</p></td>
</tr>
</tbody>
</table>

 

For example, the **7.1 home theater speakers** configuration is described by a channel mask value of 0x63F, which indicates that the eight channels in the stream are assigned to the following speaker positions (and in the following order): FL, FR, FC, LFE, BL, BR, SL, and SR. For another example, the **7.1 wide configuration speakers** configuration is described by a channel mask value of 0xFF, which indicates that the eight channels in the stream are assigned to the following speaker positions: FL, FR, FC, LFE, BL, BR, FLC, and FRC.

The following figure shows the correspondence between the channel mask 0x63F and the **7.1 home theater speakers** configuration.

![diagram illustrating the 7.1 home theater speakers recording and playback](images/spkrcfg4.png)

The left side of the preceding figure shows the recording of audio content into the **7.1 home theater speakers** stream format. The small circle at the center of the grid represents the listener's position. Each small, black rectangle represents a microphone. The eight channels are numbered from 0 to 7. The FL microphone records into channel 0, the FR microphone records into channel 1, and so on.

The right side of the preceding figure shows the same 7.1-channel stream being played back through an eight-speaker surround configuration. In this case, each small, black rectangle represents a speaker. Seven of the speakers are mapped to positions on the grid surrounding the listener. The mapping does not assign a grid position to the LFE speaker (subwoofer); this omission is based on the assumption that these speakers typically produce only low-frequency sounds, which are nondirectional.

 

 




