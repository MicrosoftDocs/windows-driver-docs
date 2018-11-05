---
title: Broadcast Driver Architecture Property, Event, and Method Sets
description: Broadcast Driver Architecture Property, Event, and Method Sets
ms.assetid: 4323c19a-e47d-4ec6-a39c-3f2e95c526e4
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Broadcast Driver Architecture Property, Event, and Method Sets


## <span id="ddk_broadcast_driver_architecture_property_event_and_method_sets_ks"></span><span id="DDK_BROADCAST_DRIVER_ARCHITECTURE_PROPERTY_EVENT_AND_METHOD_SETS_KS"></span>


This section documents the property, event, and method sets that a BDA minidriver implements. These sets are defined in *bdamedia.h*. The BDA minidriver can dispatch some of the properties and methods in these sets to default implementations in the BDA support library. For more information, see [Broadcast Driver Architecture Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff556588) on how the minidriver can use the BDA support library of functions to provide default handling of these sets.

The following sections provide more information about the BDA property, event, and method sets:

<span id="KSPROPSETID_BdaAutodemodulate"></span><span id="kspropsetid_bdaautodemodulate"></span><span id="KSPROPSETID_BDAAUTODEMODULATE"></span>[KSPROPSETID\_BdaAutodemodulate](kspropsetid-bdaautodemodulate.md)  
The BDA autodemodulate property set controls signal demodulator nodes that can automatically determine the characteristics of the modulated signal and demodulate.

<span id="KSPROPSETID_BdaCA"></span><span id="kspropsetid_bdaca"></span><span id="KSPROPSETID_BDACA"></span>[KSPROPSETID\_BdaCA](kspropsetid-bdaca.md)  
The BDA conditional access property set queries Entitlement Control Message (ECM) map nodes for either status or user interface (UI) to display.

<span id="KSEVENTSETID_BdaCAEvent"></span><span id="kseventsetid_bdacaevent"></span><span id="KSEVENTSETID_BDACAEVENT"></span>[KSEVENTSETID\_BdaCAEvent](kseventsetid-bdacaevent.md)  
The BDA conditional access event set notifies conditional access (CA) plugins either of changes in status or about the existence of UI to retrieve and display.

<span id="KSMETHODSETID_BdaChangeSync"></span><span id="ksmethodsetid_bdachangesync"></span><span id="KSMETHODSETID_BDACHANGESYNC"></span>[KSMETHODSETID\_BdaChangeSync](ksmethodsetid-bdachangesync.md)  
The BDA change sync method set commits multiple changes on a filter or its pins and nodes all at once.

<span id="KSMETHODSETID_BdaDeviceConfiguration"></span><span id="ksmethodsetid_bdadeviceconfiguration"></span><span id="KSMETHODSETID_BDADEVICECONFIGURATION"></span>[KSMETHODSETID\_BdaDeviceConfiguration](ksmethodsetid-bdadeviceconfiguration.md)  
The BDA device configuration method set configures the actual topologies of connected filters.

<span id="KSPROPSETID_BdaDigitalDemodulator"></span><span id="kspropsetid_bdadigitaldemodulator"></span><span id="KSPROPSETID_BDADIGITALDEMODULATOR"></span>[KSPROPSETID\_BdaDigitalDemodulator](kspropsetid-bdadigitaldemodulator.md)  
The BDA digital demodulator property set controls signal demodulator nodes that cannot automatically determine the characteristics of the modulated signal.

<span id="KSPROPSETID_BdaFrequencyFilter"></span><span id="kspropsetid_bdafrequencyfilter"></span><span id="KSPROPSETID_BDAFREQUENCYFILTER"></span>[KSPROPSETID\_BdaFrequencyFilter](kspropsetid-bdafrequencyfilter.md)  
The BDA frequency filter property set controls the RF tuner node in a receiver topology.

<span id="KSPROPSETID_BdaLNBInfo"></span><span id="kspropsetid_bdalnbinfo"></span><span id="KSPROPSETID_BDALNBINFO"></span>[KSPROPSETID\_BdaLNBInfo](kspropsetid-bdalnbinfo.md)  
The BDA low-noise block (LNB) property set provides an RF tuner with information about a satellite dish's LNB device.

<span id="KSPROPSETID_BdaNullTransform"></span><span id="kspropsetid_bdanulltransform"></span><span id="KSPROPSETID_BDANULLTRANSFORM"></span>[KSPROPSETID\_BdaNullTransform](kspropsetid-bdanulltransform.md)  
The BDA null transform property set informs a node to pass a signal through unchanged.

<span id="KSPROPSETID_BdaPIDFilter"></span><span id="kspropsetid_bdapidfilter"></span><span id="KSPROPSETID_BDAPIDFILTER"></span>[KSPROPSETID\_BdaPIDFilter](kspropsetid-bdapidfilter.md)  
The BDA packet identifier (PID) filter property set controls PID filter nodes. A PID filter node filters out unwanted streams from the received broadcast stream.

<span id="KSPROPSETID_BdaPinControl"></span><span id="kspropsetid_bdapincontrol"></span><span id="KSPROPSETID_BDAPINCONTROL"></span>[KSPROPSETID\_BdaPinControl](kspropsetid-bdapincontrol.md)  
The BDA pin control property set retrieves the properties of a pin from that pin.

<span id="KSEVENTSETID_BdaPinEvent"></span><span id="kseventsetid_bdapinevent"></span><span id="KSEVENTSETID_BDAPINEVENT"></span>[KSEVENTSETID\_BdaPinEvent](kseventsetid-bdapinevent.md)  
The BDA pin event set notifies other filters or plugins of events related to a pin.

<span id="KSPROPSETID_BdaSignalStats"></span><span id="kspropsetid_bdasignalstats"></span><span id="KSPROPSETID_BDASIGNALSTATS"></span>[KSPROPSETID\_BdaSignalStats](kspropsetid-bdasignalstats.md)  
The BDA signal statistics property set retrieves signal statistics from a control node or a pin. To get signal statistics from a pin, set the **NodeId** member of the KSP\_NODE structure to −1.

<span id="KSPROPSETID_BdaTableSection"></span><span id="kspropsetid_bdatablesection"></span><span id="KSPROPSETID_BDATABLESECTION"></span>[KSPROPSETID\_BdaTableSection](kspropsetid-bdatablesection.md)  
The BDA table section property set provides a table section to a node to use when delivering data on the node's output.

<span id="KSPROPSETID_BdaTopology"></span><span id="kspropsetid_bdatopology"></span><span id="KSPROPSETID_BDATOPOLOGY"></span>[KSPROPSETID\_BdaTopology](kspropsetid-bdatopology.md)  
The BDA topology property set retrieves the node capabilities and connections within a filter.

<span id="KSPROPSETID_BdaVoidTransform"></span><span id="kspropsetid_bdavoidtransform"></span><span id="KSPROPSETID_BDAVOIDTRANSFORM"></span>[KSPROPSETID\_BdaVoidTransform](kspropsetid-bdavoidtransform.md)  
The BDA void transform property set controls when a node starts and stops operating.

**Note**   The BDA property, event, and method sets are available on Windows XP and later. These sets are available on the Windows 2000 platform only if DirectX 9.0 and later is installed on that platform.

 

 

 





