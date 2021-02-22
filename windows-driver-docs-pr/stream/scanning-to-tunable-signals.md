---
title: Scanning to Tunable Signals
description: Scanning to Tunable Signals
keywords:
- signal scanning WDK video capture
- scanning tunable signals WDK video capture
- tunable signals WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Scanning to Tunable Signals


**This section applies only to operating systems starting with Microsoft Windows Vista.**

Signal scanning is the process of locking to the next tunable signal (up or down) that is broadcast along a range of frequency values on a cable or antenna system. For operating systems earlier than Windows Vista, signal scanning is driven largely by software (the *KsTvTune.ax* module) and is based on scanning a known map of channels as opposed to a frequency-based scan of the broadcast spectrum. If an AVStream minidriver that runs on Windows Vista reports back signal-scanning capabilities through a new-for-Windows Vista property in the [PROPSETID\_TUNER](./propsetid-tuner.md) property set, the tuner filter (*KsTvTune.ax*) and the applications above can use those capabilities for scanning. If the driver does not support the new frequency-based scanning functionality, *KsTvTune.ax* falls back to the former channel-based scanning functionality.

The tuner filter and an AVStream minidriver can handle the new frequency-based scanning functionality by using a [hardware-assisted scanning algorithm](hardware-assisted-scanning-algorithm.md).

When scanning completes, the minidriver must signal an event handle. For information about the event operation flow, see [Event Mechanism and Flow](event-mechanism-and-flow.md).

To support the new frequency-based scanning functionality, the minidriver must implement the required property in the following list and optionally implement the remaining properties and the event:

[**KSPROPERTY\_TUNER\_SCAN\_CAPS**](./ksproperty-tuner-scan-caps.md) (Required)

[**KSPROPERTY\_TUNER\_SCAN\_STATUS**](./ksproperty-tuner-scan-status.md) (Optional)

[**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS**](./ksproperty-tuner-networktype-scan-caps.md) (Optional)

[**KSEVENT\_TUNER\_INITIATE\_SCAN**](./ksevent-tuner-initiate-scan.md) (Optional)

 

