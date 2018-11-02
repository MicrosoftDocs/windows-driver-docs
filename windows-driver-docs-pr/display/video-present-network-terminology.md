---
title: Video Present Network Terminology
description: Video Present Network Terminology
ms.assetid: a7a02522-de13-419f-8dc5-065943fd4645
keywords:
- video present networks WDK display , terminology
- VidPN WDK display , terminology
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Present Network Terminology


The VidPN manager uses the notion of a video present network (VidPN) to manage the set of display devices connected to a display adapter. For more information, see [Introduction to Video Present Networks](introduction-to-video-present-networks.md).

The following list gives definitions of the primary terms used to describe VidPNs, display adapters, and devices that connect to display adapters.

<span id="display_adapter_s_presentational_subsystem"></span><span id="DISPLAY_ADAPTER_S_PRESENTATIONAL_SUBSYSTEM"></span>**display adapter's presentational subsystem**  
All the hardware responsible for scanning rendered content from video memory and presenting it on video outputs.

<span id="video_present_network"></span><span id="VIDEO_PRESENT_NETWORK"></span>**video present network**  
A model that relates the video present sources on a display adapter to the video present targets on the adapter and specifies how those sources and targets are configured. It is an abstraction of the display adapter's presentational subsystem. A VidPN consists of the following:

<span id="video_present_sources"></span><span id="VIDEO_PRESENT_SOURCES"></span>**video present sources**  
Independent views (that is, primary surface chains) that the display adapter can present concurrently.

<span id="video_present_targets"></span><span id="VIDEO_PRESENT_TARGETS"></span>**video present targets**  
Independent physical video outputs, on each of which the display adapter can present a view.

<span id="topology"></span><span id="TOPOLOGY"></span>**topology**  
A collection of *video present paths*, where each video present path is an association between a video present source and a video present target. A video present path specifies that a particular source is connected to a particular target. The path also specifies the content transformations that are applied on the presented content. Connecting a source to a target means that the display adapter scans from the primary surface (chain) of the source and encodes the scanned content to the video signal format of the target, applying content transformations (for example, contrast/brightness gains, flicker filter, color transformation) in the process.

<span id="source_mode_sets"></span><span id="SOURCE_MODE_SETS"></span>**source mode sets**  
Each video present source in the VidPN is associated with a source mode set, which is a list of primary surface formats (source modes) that are supported on the source in the topology of the VidPN.

<span id="target_mode_sets"></span><span id="TARGET_MODE_SETS"></span>**target mode sets**  
Each video present target in the VidPN is associated with a target mode set, which is a list of video signal formats (target modes) that are supported on the target in the topology of the VidPN.

<span id="monitor_source_mode_sets"></span><span id="MONITOR_SOURCE_MODE_SETS"></span>**monitor source mode sets**  
Each target in the VidPN that is connected to a monitor (or other external display device) is associated with a monitor source mode set, which is a list of video signal formats supported on the connected monitor.

<span id="active_VidPN"></span><span id="active_vidpn"></span><span id="ACTIVE_VIDPN"></span>**active VidPN**  
The VidPN that is currently set on the display adapter.

<span id="pinned_mode"></span><span id="PINNED_MODE"></span>**pinned mode**  
A mode designated as the desired mode for a particular video present source or target. The mode that is pinned on a source (target) is not necessarily the mode currently in use by the source (target); rather it is the desired mode for that source (target) in a given VidPN (possibly to be used as the next active VidPN). A pinned mode must remain available in its mode set throughout additional constraints imposed on the VidPN. That is, no change to the VidPN is authorized unless all of the pinned modes are still supported in the modified VidPN.

<span id="functional_VidPN"></span><span id="functional_vidpn"></span><span id="FUNCTIONAL_VIDPN"></span>**functional VidPN**  
A VidPN that satisfies all of the following conditions:

-   It has a topology with at least one video present path.

-   Every video present source in the topology has a pinned mode.

-   Every video present target in the topology has a pinned mode.

<span id="modality"></span><span id="MODALITY"></span>**modality**  
The collection of mode sets for all the sources and targets in the topology of a VidPN.

<span id="cofunctional_mode_set"></span><span id="COFUNCTIONAL_MODE_SET"></span>**cofunctional mode set**  
The set of modes that are available for a particular source or target, given the constraints (for example, topology, modes pinned on other sources and targets) of a VidPN.

<span id="cofunctional_VidPN_modality"></span><span id="cofunctional_vidpn_modality"></span><span id="COFUNCTIONAL_VIDPN_MODALITY"></span>**cofunctional VidPN modality**  
The collection of cofunctional mode sets for all the sources and targets in the topology of a VidPN.

<span id="child_device_of_the_display_adapter"></span><span id="CHILD_DEVICE_OF_THE_DISPLAY_ADAPTER"></span>**child device of the display adapter**  
A device on the display adapter that the display miniport driver enumerates as a child. All child devices of the display adapter are on-board devices; monitors and other devices that connect to the display adapter are not considered child devices.

<span id="external_device"></span><span id="EXTERNAL_DEVICE"></span>**external device**  
A device that connects to a child device of the display adapter. External devices are not considered child devices of the display adapter.

<span id="video_output_device"></span><span id="VIDEO_OUTPUT_DEVICE"></span>**video output device**  
A child device of the display adapter that supplies a video output signal to an external or built-in display device.

<span id="video_output_codec"></span><span id="VIDEO_OUTPUT_CODEC"></span>**video output codec**  
A hardware encoder/decoder on the display adapter that reads from a primary surface in video memory and places a video signal representation of that surface on one or more of the display adapter's video outputs.

 

 





