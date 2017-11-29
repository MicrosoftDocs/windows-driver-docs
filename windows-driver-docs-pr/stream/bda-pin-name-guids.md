---
title: BDA Pin Name GUIDs
description: BDA Pin Name GUIDs
ms.assetid: 098e4c49-13dd-4c9a-8ce4-06b99b7c5fa3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20BDA%20Pin%20Name%20GUIDs%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




