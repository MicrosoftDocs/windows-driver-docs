---
title: KsStudio - Filters and Filters and Factories
description: Learn how filters and filter factories can be displayed using the KsStudio Filters and Filters and Factory options.
keywords:
- KsStudio utility WDK audio
- audio filters WDK audio , KsStudio utility
- KS filter graphs WDK audio , KsStudio utility
- filter graphs WDK audio , KsStudio utility
- testing KS filter graphs WDK audio
- audio filter graphs WDK
- graphical representation WDK audio
ms.date: 04/22/2021
---

# KsStudio - Filters and Filters and Factories

This topic describes how filters and filter factories can be displayed using the [KSStudio Utility](ksstudio-utility.md).

Microsoft Windows Driver Model (WDM) audio drivers represent an audio device as a KS filter, and they represent a hardware buffer on the device as a pin on the filter. For more information, see [Filter, Pin, and Node Properties](filter--pin--and-node-properties.md).

## KS Filter Factory enumeration options
 
A session in KSStudio typically begins by enumerating the KS Filter Factories installed on the system. By default the user is presented with an enumeration options dialog on startup. This dialog may be invoked at any time after startup via the menubar (*View.Options...*). 

There are two ways by which KSStudio enumerates filters: 

- **Setup API**. This is by far the most common and useful means of filter factory enumeration. If a filter factory is correctly installed on a system, then it will be enumerable via one or more filter categories (e.g. KSCATEGORY_AUDIO, KSCATEGORY_RENDER, etc. ). You can choose which categories to enumerate, by hitting the "Classes..." button. This invokes a dialog that presents all of the categories currently declared in KSMedia.h. 

- **Explicitly by device name**. If the Setup API does not enumerate your filter factory, but the driver is installed (i.e. it shows up without error in Device Manager), you may be able to instantiate the device explicitly by name. This is done by entering the device name in the "Additional filters" edit control. This may be useful for trouble shooting enumeration problems (e.g. INF errors). 

KSStudio also provides a few "Test Filters", which exist only in the KSStudio program. These test filters can be used to stream data directly to KS filters, which may be useful for troubleshooting purposes. 

The installed filter factories that KSStudio enumerates are shown in the *Filter Factory View* discussed in [KSStudio Utility](ksstudio-utility.md). 

## Filter Factories 

Enumerated filter factories are displayed in the *Filter Factory View*. A filter factory is a facet of a WDM driver that exposes a device name that may be passed to `CreateFile` to instantiate a filter (which is a kernel object). For each filter factory enumerated, KSStudio displays an abridged list of attributes retrieved using the Windows Setup APIs, without actually instantiating the filter. 

The **Device Name** attribute is the string passed to `CreateFile` by KSStudio when the user chooses to instantiate the filter. 

## Filter Instantiation
 
To instantiate a filter, double-click on a filter factory in the *Filter Factory View* (or right-click on a factory and chose instantiate). If instantiation is successful, KSStudio interrogates the filter (via a barrage of property calls) and builds a profile using the values obtained. This profile is used to generate a graphical representation of the filter instance in the *Object Topology View*, which is deduced from the property values, and a textual representation in the *Object Details View* which shows the actual property values obtained. 

To close a filter, right-click on it and chose *Close* from the popup menu. 

## Test Filters 

KSStudio comes with several built in Test Filters or Data Pumps, so named because they submit the data buffers which are either filled or consumed by the KS Filter Graph. 

- **Wave File Pump**. This filter reads .wav files and submits the data to pins capable of consuming KSDATAFORMAT_TYPE_AUDIO data. 

- **MIDI File Pump**. This filter reads .mid or .rmi files and submits the data to pins capable of consuming KSDATAFORMAT_TYPE_MUSIC data. 

- **Wave Capture Pump**. This filter submits empty buffers to pins capable of supplying KSDATAFORMAT_AUDIO data. The data is displayed using a VU meter. 

- **MIDI Capture Pump**. This filter submits empty buffers to pins capable of supplying KSDATAFORMAT_MUSIC data. The data is displayed in the logging window as raw and translated MIDI messages. 

- **Full Duplex Stream Pump**. This filter submits empty buffers to a KSDATAFLOW_IN pin and then resubmits the data retrieved to a KSDATAFLOW_OUT pin. For example, one can use this pump to capture PCM data in from a mic pin and re-submit it to a render pin. 


## See also

[KSStudio Utility](ksstudio-utility.md)

[KSStudio - Pins and Nodes](ksstudio-utility-pins-and-nodes.md)

[KSStudio - KSProperties and Events](ksstudio-utility-ksproperties-and-events.md)

[KSStudio - KS Monitor](ksstudio-utility-ks-monitor.md)

[KSStudio - Usage Examples](ksstudio-utility-usage-examples.md)
