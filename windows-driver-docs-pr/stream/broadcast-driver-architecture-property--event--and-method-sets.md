---
title: Broadcast Driver Architecture Property, Event, and Method Sets
description: This section documents the property, event, and method sets that a BDA minidriver implements.
ms.date: 10/08/2021
ms.localizationpriority: medium
---

# Broadcast Driver Architecture Property, Event, and Method Sets

This section documents the property, event, and method sets that a BDA minidriver implements. These sets are defined in *bdamedia.h*. The BDA minidriver can dispatch some of the properties and methods in these sets to default implementations in the BDA support library. For more information, see [Broadcast Driver Architecture Minidrivers](./broadcast-driver-architecture-minidrivers.md) on how the minidriver can use the BDA support library of functions to provide default handling of these sets.

The following sections provide more information about the BDA property, event, and method sets:

| Construct | Description |
|--|--|
| [KSPROPSETID_BdaAutodemodulate](kspropsetid-bdaautodemodulate.md) | The BDA autodemodulate property set controls signal demodulator nodes that can automatically determine the characteristics of the modulated signal and demodulate. |
| [KSPROPSETID_BdaCA](kspropsetid-bdaca.md) | The BDA conditional access property set queries Entitlement Control Message (ECM) map nodes for either status or user interface (UI) to display. |
| [KSEVENTSETID_BdaCAEvent](kseventsetid-bdacaevent.md) | The BDA conditional access event set notifies conditional access (CA) plugins either of changes in status or about the existence of UI to retrieve and display. |
| [KSMETHODSETID_BdaChangeSync](ksmethodsetid-bdachangesync.md) | The BDA change sync method set commits multiple changes on a filter or its pins and nodes all at once. |
| [KSMETHODSETID_BdaDeviceConfiguration](ksmethodsetid-bdadeviceconfiguration.md) | The BDA device configuration method set configures the actual topologies of connected filters. |
| [KSPROPSETID_BdaDigitalDemodulator](kspropsetid-bdadigitaldemodulator.md) | The BDA digital demodulator property set controls signal demodulator nodes that cannot automatically determine the characteristics of the modulated signal. |
| [KSPROPSETID_BdaFrequencyFilter](kspropsetid-bdafrequencyfilter.md) | The BDA frequency filter property set controls the RF tuner node in a receiver topology. |
| [KSPROPSETID_BdaLNBInfo](kspropsetid-bdalnbinfo.md) | The BDA low-noise block (LNB) property set provides an RF tuner with information about a satellite dish's LNB device. |
| [KSPROPSETID_BdaNullTransform](kspropsetid-bdanulltransform.md) | The BDA null transform property set informs a node to pass a signal through unchanged. |
| [KSPROPSETID_BdaPIDFilter](kspropsetid-bdapidfilter.md) | The BDA packet identifier (PID) filter property set controls PID filter nodes. A PID filter node filters out unwanted streams from the received broadcast stream. |
| [KSPROPSETID_BdaPinControl](kspropsetid-bdapincontrol.md) | The BDA pin control property set retrieves the properties of a pin from that pin. |
| [KSEVENTSETID_BdaPinEvent](kseventsetid-bdapinevent.md) | The BDA pin event set notifies other filters or plugins of events related to a pin. |
| [KSPROPSETID_BdaSignalStats](kspropsetid-bdasignalstats.md) | The BDA signal statistics property set retrieves signal statistics from a control node or a pin. To get signal statistics from a pin, set the **NodeId** member of the KSP_NODE structure to −1. |
| [KSPROPSETID_BdaTableSection](kspropsetid-bdatablesection.md) | The BDA table section property set provides a table section to a node to use when delivering data on the node's output. |
| [KSPROPSETID_BdaTopology](kspropsetid-bdatopology.md) | The BDA topology property set retrieves the node capabilities and connections within a filter. |
| [KSPROPSETID_BdaVoidTransform](kspropsetid-bdavoidtransform.md) | The BDA void transform property set controls when a node starts and stops operating. |
