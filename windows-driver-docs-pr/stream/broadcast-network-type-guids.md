---
title: Broadcast Network Type GUIDs
description: An AVStream minidriver uses network-type GUIDs to specify the broadcast network types that it supports for scanning operations.
ms.date: 10/08/2021
ms.localizationpriority: medium
---

# Broadcast Network Type GUIDs

An AVStream minidriver uses network-type GUIDs to specify the broadcast network types that it supports for scanning operations. The *Bdamedia.h* header file defines these GUIDs. For more information about obtaining the scanning capabilities of supported network types, see the [**KSPROPERTY_TUNER_SCAN_CAPS**](ksproperty-tuner-scan-caps.md) and [**KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS**](ksproperty-tuner-networktype-scan-caps.md) properties.

The following network-type GUIDs are available in BDA:

| GUID | Description |
|--|--|
| ANALOG_AUXIN_NETWORK_TYPE | A network type that broadcasts analog auxiliary signals. |
| ANALOG_FM_NETWORK_TYPE | A network type that broadcasts frequency-modulated (FM) radio signals. |
| ANALOG_TV_NETWORK_TYPE | A network type that broadcasts analog television signals. |
| DIGITAL_CABLE_NETWORK_TYPE | A network type that broadcasts digital signals over cable. |
