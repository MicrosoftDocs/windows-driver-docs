---
title: BDA Pin Name GUIDs
description: BDA Pin Name GUIDs
ms.assetid: 098e4c49-13dd-4c9a-8ce4-06b99b7c5fa3
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# BDA Pin Name GUIDs


## <span id="ddk_bda_pin_name_guids_ks"></span><span id="DDK_BDA_PIN_NAME_GUIDS_KS"></span>


A BDA minidriver uses BDA pin name GUIDs to specify the names and categories of pins it supports. A BDA minidriver assigns these GUIDs to the **Name** and **Category** members of a [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structure. The *Bdamedia.h* header file defines these GUIDs. Pins of filters specify their names and categories to connect to pins of other filters that also specify those names and categories.

The following pin name GUIDs are available in BDA:

<span id="PINNAME_BDA_TRANSPORT"></span><span id="pinname_bda_transport"></span>PINNAME\_BDA\_TRANSPORT  
Pin name for a BDA transport pin.

<span id="PINNAME_BDA_ANALOG_VIDEO"></span><span id="pinname_bda_analog_video"></span>PINNAME\_BDA\_ANALOG\_VIDEO  
Pin name for a BDA analog video pin.

<span id="PINNAME_BDA_ANALOG_AUDIO"></span><span id="pinname_bda_analog_audio"></span>PINNAME\_BDA\_ANALOG\_AUDIO  
Pin name for a BDA analog audio pin.

<span id="PINNAME_BDA_FM_RADIO"></span><span id="pinname_bda_fm_radio"></span>PINNAME\_BDA\_FM\_RADIO  
Pin name for a BDA FM radio pin.

<span id="PINNAME_BDA_IF_PIN"></span><span id="pinname_bda_if_pin"></span>PINNAME\_BDA\_IF\_PIN  
Pin name for a BDA intermediate frequency pin.

<span id="PINNAME_BDA_OPENCABLE_PSIP_PIN"></span><span id="pinname_bda_opencable_psip_pin"></span>PINNAME\_BDA\_OPENCABLE\_PSIP\_PIN  
Pin name for a BDA Open Cable PSIP pin.

<span id="PINNAME_IPSINK_INPUT"></span><span id="pinname_ipsink_input"></span>PINNAME\_IPSINK\_INPUT  
Pin name for an input pin to a BDA IP sink node (KSNODE\_BDA\_IP\_SINK).

<span id="PINNAME_MPE"></span><span id="pinname_mpe"></span>PINNAME\_MPE  
Pin name for a multiprotocol encapsulation (MPE) pin.

 

 





