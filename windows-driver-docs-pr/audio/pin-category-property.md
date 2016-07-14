---
Description: Pin Category Property
MS-HAID: 'audio.pin\_category\_property'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Pin Category Property
---

# Pin Category Property


## <span id="pin_category_property"></span><span id="PIN_CATEGORY_PROPERTY"></span>


Microsoft Windows Driver Model (WDM) audio drivers for USB audio devices, IEEE 1394 audio devices, and audio devices on internal buses all represent their devices as KS filters with pins. A WDM audio driver maintains one [**KSPIN\_DESCRIPTOR**](stream.kspin_descriptor) structure for each pin type that it supports. Within this structure, the driver stores the [KSPROPSETID\_Pin](stream.kspropsetid_pin) properties of the pin type. Among those properties is the [**KSPROPERTY\_PIN\_CATEGORY**](stream.ksproperty_pin_category) property. A request for this property retrieves the KS pin category GUID from the **KSPIN\_DESCRIPTOR** structure's **Category** member. This GUID indicates the general category of functionality that the pin provides. For example, a particular pin category GUID, KSNODETYPE\_HEADPHONES, identifies a pin as an output jack for headphones.

In the case of a wave audio device on an internal bus (for example, PCI), the PortCls miniport driver contains an array of pin descriptors, each of which describes a pin type in the filter that represents the device. Each pin descriptor is a [**PCPIN\_DESCRIPTOR**](audio.pcpin_descriptor) structure containing an embedded [**KSPIN\_DESCRIPTOR**](stream.kspin_descriptor) structure with a pin category GUID. Upon receiving a [**KSPROPERTY\_PIN\_CATEGORY**](stream.ksproperty_pin_category) property request from a client, the port driver retrieves the pin category GUID from the miniport driver's pin descriptor for the specified pin type. For more information about pin descriptors, see [Pin Factories](pin-factories.md).

A USB audio device has some number of terminals through which digital streams and analog signals can enter and exit the device. When constructing a KS filter to represent a USB audio device, the [USBAudio class system driver](kernel-mode-wdm-audio-components.md#usbaudio-class-system-driver) translates the terminals on the device into pins on the filter. The header file Ksmedia.h defines a mapping for each USB terminal type identifier to a KS pin category GUID. The following six tables show the terminal type identifiers and their corresponding pin category GUIDs.

### <span id="input_terminal_types"></span><span id="INPUT_TERMINAL_TYPES"></span> Input Terminal Types

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">USB Terminal ID</th>
<th align="left">KS Pin Category GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0201</p></td>
<td align="left"><p>KSNODETYPE_MICROPHONE</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0202</p></td>
<td align="left"><p>KSNODETYPE_DESKTOP_MICROPHONE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0203</p></td>
<td align="left"><p>KSNODETYPE_PERSONAL_MICROPHONE</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0204</p></td>
<td align="left"><p>KSNODETYPE_OMNI_DIRECTIONAL_MICROPHONE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0205</p></td>
<td align="left"><p>KSNODETYPE_MICROPHONE_ARRAY</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0206</p></td>
<td align="left"><p>KSNODETYPE_PROCESSING_MICROPHONE_ARRAY</p></td>
</tr>
</tbody>
</table>

 

### <span id="output_terminal_types"></span><span id="OUTPUT_TERMINAL_TYPES"></span> Output Terminal Types

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">USB Terminal ID</th>
<th align="left">KS Pin Category GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0301</p></td>
<td align="left"><p>KSNODETYPE_SPEAKER</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0302</p></td>
<td align="left"><p>KSNODETYPE_HEADPHONES</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0303</p></td>
<td align="left"><p>KSNODETYPE_HEAD_MOUNTED_DISPLAY_AUDIO</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0304</p></td>
<td align="left"><p>KSNODETYPE_DESKTOP_SPEAKER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0305</p></td>
<td align="left"><p>KSNODETYPE_ROOM_SPEAKER</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0306</p></td>
<td align="left"><p>KSNODETYPE_COMMUNICATION_SPEAKER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0307</p></td>
<td align="left"><p>KSNODETYPE_LOW_FREQUENCY_EFFECTS_SPEAKER</p></td>
</tr>
</tbody>
</table>

 

### <span id="bidirectional_terminal_types"></span><span id="BIDIRECTIONAL_TERMINAL_TYPES"></span> Bidirectional Terminal Types

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">USB Terminal ID</th>
<th align="left">KS Pin Category GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0401</p></td>
<td align="left"><p>KSNODETYPE_HANDSET</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0402</p></td>
<td align="left"><p>KSNODETYPE_HEADSET</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0403</p></td>
<td align="left"><p>KSNODETYPE_SPEAKERPHONE_NO_ECHO_REDUCTION</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0404</p></td>
<td align="left"><p>KSNODETYPE_ECHO_SUPPRESSING_SPEAKERPHONE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0405</p></td>
<td align="left"><p>KSNODETYPE_ECHO_CANCELING_SPEAKERPHONE</p></td>
</tr>
</tbody>
</table>

 

### <span id="telephony_terminal_types"></span><span id="TELEPHONY_TERMINAL_TYPES"></span> Telephony Terminal Types

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">USB Terminal ID</th>
<th align="left">KS Pin Category GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0501</p></td>
<td align="left"><p>KSNODETYPE_PHONE_LINE</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0502</p></td>
<td align="left"><p>KSNODETYPE_TELEPHONE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0503</p></td>
<td align="left"><p>KSNODETYPE_DOWN_LINE_PHONE</p></td>
</tr>
</tbody>
</table>

 

### <span id="external_terminal_types"></span><span id="EXTERNAL_TERMINAL_TYPES"></span> External Terminal Types

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">USB Terminal ID</th>
<th align="left">KS Pin Category GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0601</p></td>
<td align="left"><p>KSNODETYPE_ANALOG_CONNECTOR</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0602</p></td>
<td align="left"><p>KSNODETYPE_DIGITAL_AUDIO_INTERFACE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0603</p></td>
<td align="left"><p>KSNODETYPE_LINE_CONNECTOR</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0604</p></td>
<td align="left"><p>KSNODETYPE_LEGACY_AUDIO_CONNECTOR</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0605</p></td>
<td align="left"><p>KSNODETYPE_SPDIF_INTERFACE</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0606</p></td>
<td align="left"><p>KSNODETYPE_1394_DA_STREAM</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0607</p></td>
<td align="left"><p>KSNODETYPE_1394_DV_STREAM_SOUNDTRACK</p></td>
</tr>
</tbody>
</table>

 

### <span id="embedded_function_terminal_types"></span><span id="EMBEDDED_FUNCTION_TERMINAL_TYPES"></span> Embedded Function Terminal Types

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">USB Terminal ID</th>
<th align="left">KS Pin Category GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0701</p></td>
<td align="left"><p>KSNODETYPE_LEVEL_CALIBRATION_NOISE_SOURCE</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0702</p></td>
<td align="left"><p>KSNODETYPE_EQUALIZATION_NOISE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0703</p></td>
<td align="left"><p>KSNODETYPE_CD_PLAYER</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0704</p></td>
<td align="left"><p>KSNODETYPE_DAT_IO_DIGITAL_AUDIO_TAPE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0705</p></td>
<td align="left"><p>KSNODETYPE_DCC_IO_DIGITAL_COMPACT_CASSETTE</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0706</p></td>
<td align="left"><p>KSNODETYPE_MINIDISK</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0707</p></td>
<td align="left"><p>KSNODETYPE_ANALOG_TAPE</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0708</p></td>
<td align="left"><p>KSNODETYPE_PHONOGRAPH</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0709</p></td>
<td align="left"><p>KSNODETYPE_VCR_AUDIO</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x070A</p></td>
<td align="left"><p>KSNODETYPE_VIDEO_DISC_AUDIO</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x070B</p></td>
<td align="left"><p>KSNODETYPE_DVD_AUDIO</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x070C</p></td>
<td align="left"><p>KSNODETYPE_TV_TUNER_AUDIO</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x070D</p></td>
<td align="left"><p>KSNODETYPE_SATELLITE_RECEIVER_AUDIO</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x070E</p></td>
<td align="left"><p>KSNODETYPE_CABLE_TUNER_AUDIO</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x070F</p></td>
<td align="left"><p>KSNODETYPE_DSS_AUDIO</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0710</p></td>
<td align="left"><p>KSNODETYPE_RADIO_RECEIVER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0711</p></td>
<td align="left"><p>KSNODETYPE_RADIO_TRANSMITTER</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0712</p></td>
<td align="left"><p>KSNODETYPE_MULTITRACK_RECORDER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0713</p></td>
<td align="left"><p>KSNODETYPE_SYNTHESIZER</p></td>
</tr>
</tbody>
</table>

 

For more information about USB terminal type identifiers, see the *Universal Serial Bus Device Class Definition for Terminal Types* (release 1.0), which is available at the [USB Implementers Forum](http://go.microsoft.com/fwlink/p/?linkid=8780) website.

All pin category GUIDs in the preceding tables have parameter names of the form KSNODETYPE\_*XXX*. Note that KS node type GUIDs also have KSNODETYPE\_*XXX* parameter names. This naming convention creates some potential for confusion between pin category GUIDs and node type GUIDs. Fortunately, nearly every KSNODETYPE\_*XXX* parameter identifies either a pin category or a node type, but not both. The one exception to the rule is [**KSNODETYPE\_SYNTHESIZER**](audio.ksnodetype_synthesizer), which can identify either a pin category or a node type, depending on the context. For a list of node type GUIDs, see [Audio Topology Nodes](audio.audio_topology_nodes).

When instantiating a USB audio device, the USBAudio class system driver queries the device for its internal topology, including its terminals. With this information, the USBAudio driver constructs a filter to represent the device and translates each terminal into a corresponding pin on the filter. During this process, the driver translates each USB terminal type identifier into the corresponding KS pin category GUID, which is one of the GUIDs in the preceding tables. The driver constructs a [**KSPIN\_DESCRIPTOR**](stream.kspin_descriptor) structure to describe the pin, and it writes the pin category GUID into the structure.

A PortCls miniport driver does not necessarily use only the category GUIDs that appear in the preceding six tables. For example, a driver might define and use a custom pin category GUID to describe a pin type whose functional category falls outside the categories in the tables. Naturally, a custom pin category GUID is useful only to clients that recognize the GUID.

The audio subsystem maintains a list of pin category GUIDs and their associated friendly names in the system registry. The GUIDs and friendly names are stored in the registry path HKLM\\SYSTEM\\CurrentControlSet\\Control\\MediaCategories. The media class installer copies the GUID-name pairs into the registry from the Ks.inf file located in the Inf subfolder of the main Windows folder (for example, C:\\Windows\\Inf\\Ks.inf).

In Windows Vista and later, the operating system uses pin categories to associate friendly names with audio endpoint devices. For more information about how to associate friendly names with audio endpoint devices, see [Friendly Names for Audio Endpoint Devices](friendly-names-for-audio-endpoint-devices.md).

In Windows XP, Windows 2000, and Windows Millennium Edition, the operating system makes only limited use of pin categories. The [WDMAud system driver](user-mode-wdm-audio-components.md#wdmaud-system-driver) acts on behalf of the mixer API to translate pin category GUIDs into MIXERLINE\_COMPONENTTYPE\_*XXX* values for use by client applications. WDMAud recognizes only a subset of the pin category GUIDs that appear in the preceding six tables. In addition, for historical reasons, WDMAud recognizes two pin category GUIDs, KSCATEGORY\_AUDIO and PINNAME\_CAPTURE, that do not appear in the tables. For more information about the translation of pin categories to mixer lines, see [Topology Pins](topology-pins.md). For information about the mixer API, see the Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Pin%20Category%20Property%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



