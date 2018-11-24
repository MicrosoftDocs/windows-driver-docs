---
title: Broadcast Network Type GUIDs
description: Broadcast Network Type GUIDs
ms.assetid: 3501cb1f-10f7-481b-bd2f-1f77156a676a
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Broadcast Network Type GUIDs


An AVStream minidriver uses network-type GUIDs to specify the broadcast network types that it supports for scanning operations. The *Bdamedia.h* header file defines these GUIDs. For more information about obtaining the scanning capabilities of supported network types, see the [**KSPROPERTY\_TUNER\_SCAN\_CAPS**](ksproperty-tuner-scan-caps.md) and [**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS**](ksproperty-tuner-networktype-scan-caps.md) properties.

The following network-type GUIDs are available in BDA:

<span id="ANALOG_AUXIN_NETWORK_TYPE"></span><span id="analog_auxin_network_type"></span>ANALOG\_AUXIN\_NETWORK\_TYPE  
A network type that broadcasts analog auxiliary signals.

<span id="ANALOG_FM_NETWORK_TYPE"></span><span id="analog_fm_network_type"></span>ANALOG\_FM\_NETWORK\_TYPE  
A network type that broadcasts frequency-modulated (FM) radio signals.

<span id="ANALOG_TV_NETWORK_TYPE"></span><span id="analog_tv_network_type"></span>ANALOG\_TV\_NETWORK\_TYPE  
A network type that broadcasts analog television signals.

<span id="DIGITAL_CABLE_NETWORK_TYPE"></span><span id="digital_cable_network_type"></span>DIGITAL\_CABLE\_NETWORK\_TYPE  
A network type that broadcasts digital signals over cable.

 

 





