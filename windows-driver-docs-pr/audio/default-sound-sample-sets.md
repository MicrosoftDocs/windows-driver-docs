---
Description: Default Sound Sample Sets
MS-HAID: 'audio.default\_sound\_sample\_sets'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Default Sound Sample Sets
---

# Default Sound Sample Sets


## <span id="default_sound_sample_sets"></span><span id="DEFAULT_SOUND_SAMPLE_SETS"></span>


Some synthesizers ship with a default sound set that conforms to General MIDI or some extension thereof. This sound set is provided for applications that do not support sample downloading or desire a default sound set to use in conjunction with downloaded samples. There are two possible delivery mechanisms for such a sound set: as a prepackaged DLS set, or as a ROM set.

In the case of the prepackaged DLS set, management of the set is delegated to DirectMusic. Microsoft provides a default DLS set based on the Roland GS samples. Manufacturers wishing to use a different default set with their hardware should contact the DirectMusic group at Microsoft. Sample sets provided in this manner should not set the capabilities bits indicating hardware support for a sample set; only ROM sets should set these bits.

ROM sets are also managed by the system. In order to preserve maximum sample memory for use by downloadable samples, the miniport driver should not load the entire ROM set into sample RAM. (This is not an issue for hardware that can play samples directly out of ROM.) The system provides instrument download requests for needed updates before the update change itself is delivered. If an instrument download refers to an update in the ROM sample set, then the **dwDLId** member of the DMUS\_DOWNLOADINFO structure (described in the Microsoft Windows SDK documentation) contains the tag DOWNLOAD\_ID\_ROMSET (defined as 0xFFFFFFFF).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Default%20Sound%20Sample%20Sets%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


