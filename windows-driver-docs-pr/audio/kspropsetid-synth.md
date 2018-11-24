---
title: KSPROPSETID\_Synth
description: KSPROPSETID\_Synth
ms.assetid: ff5efd85-0b4d-4625-b029-fecf325bcacb
keywords: ["KSPROPSETID_Synth"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_Synth


## <span id="ddk_kspropsetid_synth_ks"></span><span id="DDK_KSPROPSETID_SYNTH_KS"></span>


The `KSPROPSETID_Synth` property set contains properties that are global to the configuration of a synth node ([**KSNODETYPE\_SYNTHESIZER**](ksnodetype-synthesizer.md)).

Property items in this set are specified by KSPROPERTY\_SYNTH enumeration values, as defined in header file Dmusprop.h.

## <span id="ddk_ksproperty_synth_caps_ks"></span><span id="DDK_KSPROPERTY_SYNTH_CAPS_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_CAPS property is used by the system to determine the capabilities of a synthesizer.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538424" data-raw-source="[&lt;strong&gt;SYNTHCAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538424)"><strong>SYNTHCAPS</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type SYNTHCAPS and specifies the synthesizer's capabilities. These capabilities include:

-   Amount of sample memory available

-   Maximum number of channel groups

-   Maximum number of voices

-   Maximum number of audio channels

-   Rendering effects

For more information, see [**SYNTHCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff538424).

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_CAPS property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

For more information about synthesizer capabilities, see the **IDirectMusicPort::GetCaps** method and the DMUS\_PORTCAPS structure in the Microsoft Windows SDK documentation.

## <span id="ddk_ksproperty_synth_channelgroups_ks"></span><span id="DDK_KSPROPERTY_SYNTH_CHANNELGROUPS_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_CHANNELGROUPS property is used by the system to set or get the number of active channel groups on the pin instance. Channel groups are numbered, beginning with zero, on each pin instance.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and specifies how many channel groups the pin supports. If a pin supports *n* channel groups, the channel groups on the pin are numbered from 0 to *n*-1.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_CAPS property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible failure codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_BUFFER_TOO_SMALL</p></td>
<td align="left"><p>The buffer was too small to complete the operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
</tbody>
</table>

 

For more information about channel groups, see the descriptions of the **IDirectMusicPort::GetNumChannelGroups** and **IDirectMusicPort::SetNumChannelGroups** methods in the Microsoft Windows SDK documentation.

## <span id="ddk_ksproperty_synth_latencyclock_ks"></span><span id="DDK_KSPROPERTY_SYNTH_LATENCYCLOCK_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_LATENCYCLOCK property is used to query the miniport driver for the stream's current latency-clock time, which is always greater than the master-clock time.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>ULONGLONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONGLONG and represents the synthesizer's current latency time. This time is specified relative to the master clock and expressed in 100-nanosecond units.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_LATENCYCLOCK property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible failure codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_BUFFER_TOO_SMALL</p></td>
<td align="left"><p>The buffer was too small to complete the operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_INVALID_DEVICE_REQUEST</p></td>
<td align="left"><p>The operation is invalid for this device.</p></td>
</tr>
</tbody>
</table>

 

Latency clocks are typically used to synchronize audio output streams among multiple devices.

A KSPROPERTY\_SYNTH\_LATENCYCLOCK get-property request should return a latency-clock time that equals the current master-clock time, plus the minimum guaranteed latency of the audio filter that the stream passes through. An application program that schedules audio data to be played earlier than the current latency-clock time risks having the data played late.

For more information about latency clocks, see the following:

-   The discussion of the KSPROPERTY\_SYNTH\_LATENCYCLOCK property in [Latency Clocks](https://msdn.microsoft.com/library/windows/hardware/ff537503).

-   The descriptions of the **IDirectMusicPort::GetLatencyClock** and **IReferenceClock::GetTime** methods in the Microsoft Windows SDK documentation.

## <span id="ddk_ksproperty_synth_portparameters_ks"></span><span id="DDK_KSPROPERTY_SYNTH_PORTPARAMETERS_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_PORTPARAMETERS property is used to get the configuration parameters for a DirectMusic *port*, which is a DirectMusic term for a device that sends or receives music data. (In KS terminology, DirectMusic port does not correspond to a DMus port driver. It corresponds to a render or capture pin on a DirectMusic filter.)

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a> + <a href="https://msdn.microsoft.com/library/windows/hardware/ff538467" data-raw-source="[&lt;strong&gt;SYNTH_PORTPARAMS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538467)"><strong>SYNTH_PORTPARAMS</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538467" data-raw-source="[&lt;strong&gt;SYNTH_PORTPARAMS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538467)"><strong>SYNTH_PORTPARAMS</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) consists of a KSNODEPROPERTY structure that is immediately followed by a SYNTH\_PORTPARAMS structure. Before sending the property request, the client specifies its requested parameter values by writing them into the SYNTH\_PORTPARAMS structure.

The property value (operation data) is also of type SYNTH\_PORTPARAMS. The miniport driver loads this structure with the parameter values that it actually uses to configure the port.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

If the miniport driver succeeds in configuring the DirectMusic port exactly as specified by the caller, it returns the STATUS\_SUCCESS code. Otherwise, it returns an appropriate error code. The following table indicates some of the possible error status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_NOT_ALL_ASSIGNED</p></td>
<td align="left"><p>The operation succeeded, but the miniport driver had to modify one or more of the parameter values that the caller marked as valid in the property value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
</tbody>
</table>

 

This is the most complicated of the DirectMusic property items to handle. Although this property supports only the get request, the get request also sets the port parameters. The port passes a SYNTH\_PORTPARAMS structure as the property descriptor for the property request. A property-value buffer accompanies the property request, but because this is a get request, the buffer is only used to retrieve information from the miniport driver.

The miniport driver should first copy the SYNTH\_PORTPARAMS structure from the property descriptor to the property-value buffer. Next, it should check to see if it is capable of supporting all the parameter values that the caller has requested (marked as valid). If the miniport driver is unable to support one or more of the requested parameter values, it should overwrite (in the SYNTH\_PORTPARAMS structure in the property-value buffer) the requested values for these particular parameters with the values that it can support.

If the miniport driver makes no changes to the caller's SYNTH\_PORTPARAMS, the caller should get back a property value that exactly matches the parameters in the property descriptor that the caller originally sent down to the miniport driver.

By convention, the driver also fills in values for parameters that do not have corresponding bits set in the **dwValidParams** member of SYNTH\_PORTPARAMS. This allows the caller to see what default values the miniport driver used for these parameters. The miniport driver outputs the actual parameter values that it used to build the wave-interface device.

The miniport driver's KSPROPERTY\_SYNTH\_PORTPARAMETERS handler should be prepared to correctly handle requests for sample-rate changes.

## <span id="ddk_ksproperty_synth_runningstats_ks"></span><span id="DDK_KSPROPERTY_SYNTH_RUNNINGSTATS_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_RUNNINGSTATS property is used to query the miniport driver for the synthesizer's performance statistics.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538473" data-raw-source="[&lt;strong&gt;SYNTH_STATS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538473)"><strong>SYNTH_STATS</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type SYNTH\_STATS. The miniport driver's property handler writes the following statistics into this structure:

-   The average number of voices playing

-   CPU usage

-   Number of notes lost

-   Amount of free memory

-   Peak volume level

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_RUNNINGSTATS property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible error codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_BUFFER_TOO_SMALL</p></td>
<td align="left"><p>The buffer was too small to complete the operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_INVALID_DEVICE_REQUEST</p></td>
<td align="left"><p>The operation is invalid for this device.</p></td>
</tr>
</tbody>
</table>

 

The synthesizer's performance statistics are continuously updated while the device remains in the KSSTATE\_RUN state. Each time the device enters this state, it resets the statistics, which zeros cumulative values such as the peak volume and number of notes lost.

For additional information, see the description of the **IDirectMusicPort::GetRunningStats** method and the DMUS\_SYNTHSTATS structure in the Microsoft Windows SDK documentation.

## <span id="ddk_ksproperty_synth_voicepriority_ks"></span><span id="DDK_KSPROPERTY_SYNTH_VOICEPRIORITY_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_VOICEPRIORITY property specifies what priority a particular voice in a MIDI synthesizer should have when the miniport driver needs to bump voices from its voice cache.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a> + <a href="https://msdn.microsoft.com/library/windows/hardware/ff538452" data-raw-source="[&lt;strong&gt;SYNTHVOICEPRIORITY_INSTANCE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538452)"><strong>SYNTHVOICEPRIORITY_INSTANCE</strong></a></p></td>
<td align="left"><p>DWORD</p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) consists of a KSNODEPROPERTY structure that is immediately followed by a SYNTHVOICEPRIORITY\_INSTANCE structure, which specifies the voice's channel group (set of 16 MIDI channels) and channel number (within the group).

The property value (operation data) is a DWORD that specifies the priority. The client uses a KSPROPERTY\_SYNTH\_VOICEPRIORITY set-property request to send the voice's new priority to the miniport driver, and it uses a KSPROPERTY\_SYNTH\_VOICEPRIORITY get-property request to retrieve the voice's current priority from the miniport driver.

**Voice Priorities**

The following channel-group priorities are defined in header file Dmusprop.h:

```cpp
  DAUD_CRITICAL_VOICE_PRIORITY
  DAUD_HIGH_VOICE_PRIORITY
  DAUD_STANDARD_VOICE_PRIORITY
  DAUD_LOW_VOICE_PRIORITY
  DAUD_PERSIST_VOICE_PRIORITY
```

The preceding list is ordered with the highest priority at the top of the list and the lowest at the bottom. These priorities are ORed with the channel priority offsets to arrive at the voice priority for each channel within a channel group. The resulting priorities are passed in the get- and set-property requests.

The preceding channel-group priority values are large compared to the channel priority offsets. The result is that changing the channel-group priority raises or lowers the priority of the entire channel group relative to other channel groups without altering the relative priorities of the channels within the channel group.

### <span id="default_priorities"></span><span id="DEFAULT_PRIORITIES"></span> Default Priorities

When a synthesizer miniport driver is created, it assigns a default priority to each of its voices. The defaults are defined as follows:

-   By default, priorities are equal across channel groups. This means, for example, that channel 5 on channel group 1 has the same priority as channel 5 on channel group 2.

-   In accordance with DLS Level-1 specifications, channel 10 (the MIDI percussion channel) has the highest priority, followed by 1 through 9 and 11 through 16.

Header file Dmusprop.h defines the following priority offsets:

```cpp
  DAUD_CHAN10_VOICE_PRIORITY_OFFSET
  DAUD_CHAN1_VOICE_PRIORITY_OFFSET
  DAUD_CHAN2_VOICE_PRIORITY_OFFSET
  DAUD_CHAN3_VOICE_PRIORITY_OFFSET
  DAUD_CHAN4_VOICE_PRIORITY_OFFSET
  DAUD_CHAN5_VOICE_PRIORITY_OFFSET
  DAUD_CHAN6_VOICE_PRIORITY_OFFSET
  DAUD_CHAN7_VOICE_PRIORITY_OFFSET
  DAUD_CHAN8_VOICE_PRIORITY_OFFSET
  DAUD_CHAN9_VOICE_PRIORITY_OFFSET
  DAUD_CHAN11_VOICE_PRIORITY_OFFSET
  DAUD_CHAN12_VOICE_PRIORITY_OFFSET
  DAUD_CHAN13_VOICE_PRIORITY_OFFSET
  DAUD_CHAN14_VOICE_PRIORITY_OFFSET
  DAUD_CHAN15_VOICE_PRIORITY_OFFSET
  DAUD_CHAN16_VOICE_PRIORITY_OFFSET
```

The preceding list of offsets is ordered with the highest priority at the top of the list. Header file Dmusprop.h also defines the default priorities of the channels in each channel group by bitwise ORing each of these offsets with DAUD\_STANDARD\_VOICE\_PRIORITY. For example, the following definition gives the default priority for channel 1 in each channel group:

```cpp
  #define DAUD_CHAN1_DEF_VOICE_PRIORITY \
    (DAUD_STANDARD_VOICE_PRIORITY | DAUD_CHAN1_VOICE_PRIORITY_OFFSET)
```

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_VOICEPRIORITY property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible error codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_BUFFER_TOO_SMALL</p></td>
<td align="left"><p>The buffer was too small to complete the operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
</tbody>
</table>

 

For more information about voice priorities, see the descriptions of the **IDirectMusicPort::GetChannelPriority** and **IDirectMusicPort::SetChannelPriority** methods in the Microsoft Windows SDK documentation.

## <span id="ddk_ksproperty_synth_volume_ks"></span><span id="DDK_KSPROPERTY_SYNTH_VOLUME_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_VOLUME property gets or sets the volume level of a synthesizer device.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type LONG and specifies the volume level of the synthesizer device. The volume setting is specified in units of 1/100ths of a decibel. The miniport driver should either change its volume or report its volume, depending on whether the request is to get or set the property.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_VOLUME property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible error codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_BUFFER_TOO_SMALL</p></td>
<td align="left"><p>The buffer was too small to complete the operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
</tbody>
</table>

 

## <span id="ddk_ksproperty_synth_volumeboost_ks"></span><span id="DDK_KSPROPERTY_SYNTH_VOLUMEBOOST_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_VOLUMEBOOST property specifies the amount by which a synthesizer device's volume is boosted.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type LONG and specifies by how much to boost the audio signal after the mix stage. This is the amount of volume to add to the final output of the synthesizer after all voice articulation and mixing have been completed. The volume boost amount is specified in 1/100ths of a decibel. This value can be positive or negative.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_VOLUMEBOOST property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible error codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_BUFFER_TOO_SMALL</p></td>
<td align="left"><p>The buffer was too small to complete the operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
</tbody>
</table>

 

No other boost should be added to the output. The synthesizer should follow strict DLS Level-1 conventions for articulation.

This property is used to equalize the volume of the synthesizer with other audio output in the system, and boost amounts should therefore be interpreted in a consistent manner across all devices.

 

 





