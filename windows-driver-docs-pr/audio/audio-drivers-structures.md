---
title: Audio Drivers Structures
description: Audio Drivers Structures
ms.date: 06/07/2021
ms.localizationpriority: medium
---

# Audio Drivers Structures

## <span id="ddk_audio_drivers_structures_ks"></span><span id="DDK_AUDIO_DRIVERS_STRUCTURES_KS"></span>

This section describes the structures that are used by WDM audio miniport drivers. The list of structures is as follows:

[**APO\_REG\_PROPERTIES**](/windows/win32/api/audioenginebaseapo/ns-audioenginebaseapo-apo_reg_properties)

[**APOInitBaseStruct**](/windows/win32/api/audioenginebaseapo/ns-audioenginebaseapo-apoinitbasestruct)

[**APOInitSystemEffects**](/windows/win32/api/audioenginebaseapo/ns-audioenginebaseapo-apoinitsystemeffects)

[**APOInitSystemEffects2**](/windows/win32/api/audioenginebaseapo/ns-audioenginebaseapo-apoinitsystemeffects2)

[**DMUS\_KERNEL\_EVENT**](/windows-hardware/drivers/ddi/dmusicks/ns-dmusicks-_dmus_kernel_event)

[**DRMFORWARD**](/windows-hardware/drivers/ddi/drmk/ns-drmk-tagdrmforward)

[**DRMRIGHTS**](/windows-hardware/drivers/ddi/drmk/ns-drmk-tagdrmrights)

[**DS3DVECTOR**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ds3dvector)

[**KSAC3\_ALTERNATE\_AUDIO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksac3_alternate_audio)

[**KSAC3\_BIT\_STREAM\_MODE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksac3_bit_stream_mode)

[**KSAC3\_DIALOGUE\_LEVEL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksac3_dialogue_level)

[**KSAC3\_DOWNMIX**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksac3_downmix)

[**KSAC3\_ERROR\_CONCEALMENT**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksac3_error_concealment)

[**KSAC3\_LANGUAGE\_CODE**](/previous-versions/windows/hardware/drivers/ff537081(v=vs.85))

[**KSAC3\_ROOM\_TYPE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksac3_room_type)

[**KSAUDIO\_CHANNEL\_CONFIG**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_channel_config)

[**KSAUDIO\_COPY\_PROTECTION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_copy_protection)

[**KSAUDIO\_DYNAMIC\_RANGE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_dynamic_range)

[**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_mic_array_geometry)

[**KSAUDIO\_MICROPHONE\_COORDINATES**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_microphone_coordinates)

[**KSAUDIO\_MIX\_CAPS**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_mix_caps)

[**KSAUDIO\_MIXCAP\_TABLE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_mixcap_table)

[**KSAUDIO\_MIXLEVEL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_mixlevel)

[**KSAUDIO\_PACKETSIZE\_CONSTRAINTS**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints)

[**KSAUDIO\_PACKETSIZE\_CONSTRAINTS2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints2)

[**KSAUDIO\_PACKETSIZE\_PROCESSINGMODE\_CONSTRAINT**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_signalprocessingmode_constraint)

[**KSAUDIO\_POSITION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_position)

[**KSAUDIO\_POSITIONEX**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_positionex)

[**KSAUDIO\_PREFERRED\_STATUS**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_preferred_status)

[**KSAUDIO\_PRESENTATION\_POSITION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_presentation_position)

[**KSAUDIOENGINE\_BUFFER\_SIZE\_RANGE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagksaudioengine_buffer_size_range)

[**KSAUDIOENGINE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagksaudioengine_descriptor)

[**KSAUDIOENGINE\_VOLUMELEVEL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagksaudioengine_volumelevel)

[**KSDATAFORMAT\_DSOUND**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_dsound)

[**KSDATAFORMAT\_WAVEFORMATEX**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_waveformatex)

[**KSDATARANGE\_AUDIO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdatarange_audio)

[**KSDATARANGE\_MUSIC**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdatarange_music)

[**KSDRMAUDIOSTREAM\_CONTENTID**](/windows-hardware/drivers/ddi/drmk/ns-drmk-ksdrmaudiostream_contentid)

[**KSDSOUND\_BUFFERDESC**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdsound_bufferdesc)

[**KSDS3D\_BUFFER\_ALL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_buffer_all)

[**KSDS3D\_BUFFER\_CONE\_ANGLES**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_buffer_cone_angles)

[**KSDS3D\_HRTF\_FILTER\_FORMAT\_MSG**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_hrtf_filter_format_msg)

[**KSDS3D\_HRTF\_INIT\_MSG**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_hrtf_init_msg)

[**KSDS3D\_HRTF\_PARAMS\_MSG**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_hrtf_params_msg)

[**KSDS3D\_ITD\_PARAMS**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_itd_params)

[**KSDS3D\_ITD\_PARAMS\_MSG**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_itd_params_msg)

[**KSDS3D\_LISTENER\_ALL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_listener_all)

[**KSDS3D\_LISTENER\_ORIENTATION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_listener_orientation)

[**KSJACK\_DESCRIPTION**](ksjack-description.md)

[**KSJACK\_DESCRIPTION2**](ksjack-description2.md)

[**KSJACK\_SINK\_INFORMATION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagksjack_sink_information)

[**KSMUSICFORMAT**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmusicformat)

[**KSNODEPROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)

[**KSNODEPROPERTY\_AUDIO\_CHANNEL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty_audio_channel)

[**KSP\_DRMAUDIOSTREAM\_CONTENTID**](/windows-hardware/drivers/ddi/drmk/ns-drmk-ksp_drmaudiostream_contentid)

[**KSP\_PINMODE**](/windows/win32/api/msapofxproxy/ns-msapofxproxy-ksp_pinmode)

[KSRTAUDIO Structures](/windows-hardware/drivers/ddi/ksmedia/index)

[**KSTELEPHONY\_CALLCONTROL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstelephony_callcontrol)

[**KSTELEPHONY\_CALLINFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstelephony_callinfo)

[**KSTELEPHONY\_PROVIDERCHANGE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstelephony_providerchange)

[**KSTOPOLOGY\_ENDPOINTID**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstopology_endpointid)

[**KSTOPOLOGY\_ENDPOINTIDPAIR**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstopology_endpointidpair)

[**LOOPEDSTREAMING\_POSITION\_EVENT\_DATA**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-loopedstreaming_position_event_data)

[**MDEVICECAPSEX**](/windows/win32/api/mmddk/ns-mmddk-mdevicecapsex)

[**MIDIOPENDESC**](/windows/win32/api/mmddk/ns-mmddk-midiopendesc)

[**RTAUDIO\_GETREADPACKET\_INFO**](/previous-versions/windows/hardware/drivers/mt169891(v=vs.85))

[**RTAUDIO\_SETWRITEPACKET\_INFO**](/previous-versions/windows/hardware/drivers/mt169892(v=vs.85))

[**SOUNDDETECTOR\_PATTERNHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sounddetector_patternheader)

[**SYNTH\_BUFFER**](/windows-hardware/drivers/ddi/dmusprop/ns-dmusprop-_synth_buffer)

[**SYNTH\_PORTPARAMS**](/windows-hardware/drivers/ddi/dmusprop/ns-dmusprop-_synth_portparams)

[**SYNTH\_STATS**](/windows-hardware/drivers/ddi/dmusprop/ns-dmusprop-_synth_stats)

[**SYNTHCAPS**](/windows-hardware/drivers/ddi/dmusprop/ns-dmusprop-_synthcaps)

[**SYNTHDOWNLOAD**](/windows-hardware/drivers/ddi/dmusprop/ns-dmusprop-_synthdownload)

[**SYNTHVOICEPRIORITY\_INSTANCE**](/windows-hardware/drivers/ddi/dmusprop/ns-dmusprop-_synthvoicepriority_instance)

[**SYSAUDIO\_ATTACH\_VIRTUAL\_SOURCE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sysaudio_attach_virtual_source)

[**SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sysaudio_create_virtual_source)

[**SYSAUDIO\_INSTANCE\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sysaudio_instance_info)

[**SYSAUDIO\_SELECT\_GRAPH**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sysaudio_select_graph)

[**UNCOMPRESSEDAUDIOFORMAT**](/windows/win32/api/audiomediatype/ns-audiomediatype-uncompressedaudioformat)

[**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex)

[**WAVEFORMATEXTENSIBLE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-waveformatextensible)
