---
title: CGMS-A Standards
description: CGMS-A Standards
ms.assetid: e41de08f-4dfa-42fc-8ddb-f27385c5780a
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CGMS-A Standards


Multiple standards define the Content Generation Management System Analog (CGMS-A) protection type. Various countries and regions use various versions of CGMS-A. A hardware vendor must ensure that his or her display miniport driver supports the appropriate CGMS-A version. For example, a driver for a graphics adapter to be used in Japan should probably support the Association of Radio Industries and Businesses (ARIB) TR-B15 standard, which is the operational guideline for digital satellite broadcasting. However, a driver for a graphics adapter to be used in the United States should support the International Electrotechnical Commission (IEC) 61880 standard or the Consumer Electronics Association (CEA) CEA-608-B standard. The standard that a graphics adapter's display miniport driver supports depends on the type of signal that the adapter transmits. The following list describes various standards that define CGMS-A. Currently, redistribution control is defined only in the CEA-805-A standard.

<span id="CEA-805-A"></span><span id="cea-805-a"></span>CEA-805-A  
Data on Component Video Interfaces

Defines how CGMS-A and redistribution control information should be encoded in an analog 480p, 720p, or 1080i signal that is transmitted from a component video output (Y/Pb/Pr output).

This standard is published by CEA. For more information about CEA, see the [Consumer Electronics Association](http://go.microsoft.com/fwlink/p/?linkid=71276) website.

<span id="CEA-608-B_and_EIA-608-B"></span><span id="cea-608-b_and_eia-608-b"></span><span id="CEA-608-B_AND_EIA-608-B"></span>CEA-608-B and EIA-608-B  
Line 21 Data Services

Defines how CGMS-A information should be encoded in a 480i signal that is transmitted from an RF, composite, or S-Video output.

This standard is published by CEA and Electronic Components Industry Association (ECIA). For more information about ECIA, see the [Electronic Components Industry Association](http://go.microsoft.com/fwlink/p/?linkid=71278) website.

<span id="EN_300_294_V1.3.2__1998-04_"></span><span id="en_300_294_v1.3.2__1998-04_"></span>EN 300 294 V1.3.2 (1998-04)  
Television systems; 625-line television - Wide Screen Signaling (WSS)

Defines how CGMS-A should be encoded in a 576i Phase Alternation Line (PAL) or Sequential Color with Memory (SECAM) signal.

This standard is published by the European Telecommunications Standards Institute (ETSI). For more information about this standard, see the [ETSI](http://go.microsoft.com/fwlink/p/?linkid=26364) website.

<span id="IEC_-_61880_-_First_edition_-_Video_systems__525_60_"></span><span id="iec_-_61880_-_first_edition_-_video_systems__525_60_"></span><span id="IEC_-_61880_-_FIRST_EDITION_-_VIDEO_SYSTEMS__525_60_"></span>IEC - 61880 - First edition - Video systems (525/60)  
Video and accompanied data using the vertical blanking interval - Analog interface

A method of encoding CGMS-A information in a 480i video signal that is transmitted from an analog or digital video output.

This method is published by IEC. For more information about the IEC, see the [IEC](http://go.microsoft.com/fwlink/p/?linkid=8732) website.

<span id="IEC_-_61880-2_-_First_edition_-_Video_systems__525_60__"></span><span id="iec_-_61880-2_-_first_edition_-_video_systems__525_60__"></span><span id="IEC_-_61880-2_-_FIRST_EDITION_-_VIDEO_SYSTEMS__525_60__"></span>IEC - 61880-2 - First edition - Video systems (525/60)   
Video and accompanied data using the vertical blanking interval - Analog interface - Part 2: 525 progressive scan system

A method of encoding CGMS-A information in a 480p video signal that is transmitted from an analog or digital video output.

<span id="IEC_-_62375_-_Video_systems__625_50_progressive_"></span><span id="iec_-_62375_-_video_systems__625_50_progressive_"></span><span id="IEC_-_62375_-_VIDEO_SYSTEMS__625_50_PROGRESSIVE_"></span>IEC - 62375 - Video systems (625/50 progressive)  
Video and accompanied data using the vertical blanking interval - Analog interface

A method of encoding CGMS-A information in a 576p video signal that is transmitted from an analog or digital video output.

<span id="ARIB_TR-B15"></span><span id="arib_tr-b15"></span>ARIB TR-B15  
Operational Guideline for Digital Satellite Broadcasting

Defines how CGMS-A information should be encoded in an analog 480i, 480p, 720p, or 1080i signal that is transmitted from a video output.

This standard applies only to Japan.

This standard is published by ARIB. For more information about ARIB, see the [ARIB English](http://go.microsoft.com/fwlink/p/?linkid=71283) website.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20CGMS-A%20Standards%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




