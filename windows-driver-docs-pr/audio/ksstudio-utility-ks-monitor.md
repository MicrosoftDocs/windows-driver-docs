---
title: KsStudio - KS Monitor
description: KSMonitor is a device driver installed by KSStudio - KSMon.sys which can be used to examine all IRP-based communication targeted at KS Filter and Pin instances.
keywords:
- KsStudio utility WDK audio
- audio filters WDK audio , KsStudio utility
- KS filter graphs WDK audio , KsStudio utility
- filter graphs WDK audio , KsStudio utility
- testing KS filter graphs WDK audio
- audio filter graphs WDK
- graphical representation WDK audio
ms.date: 04/21/2021
ms.localizationpriority: medium
---

# KsStudio - KS Monitor 

KSMonitor is a device driver installed by KSStudio (KSMon.sys) which can be used to examine all IRP-based communication targeted at KS Filter and Pin instances.  Note that AVStream (2nd generation KS) filters can, and generally do, use other, non-IRP-base, communication types.  Therefore, KSMonitor cannot monitor on communication between two AVStream filters.

To monitor a Filter, right-click on the filter factory in the *Filter Factory* view, or on a Filter Instance in the Topology or *Object Details* view.  Choose "Monitor".  If monitoring is enabled, you will see the monitor icon on your filter instance.

## KS Monitor Features 

KSMonitor has the following features.

- Return code filtering -- This allows you to see, for example, only "STATUS_..." return codes 
- IRP filtering -- This allows you to see, for example, only IRP_MJ_DEVICECONTROL IRPs 
- Expansion of IOCTL_KS_PROPERTY IRPs 
- IRP statistics 
- IRP timing
- Breakpoint setting 
- Copy to clipboard functionality -- As with most other KSStudio views, you can copy to the clipboard

## How KS Monitor Works
 
KSMonitor works by attaching to the Device Object corresponding to a given filter.  When you chose to monitor a filter, KSStudio gives KSMonitor a handle to an instance of that filter.  Note that if the filter is not instantiated already, then KSStudio instantiates it.  KSMonitor then figures out the Device Object corresponding to this filter handle and attaches to the "top" of the that Device Object.  All IRPs targeted at the Device Object are then filtered by KSMonitor.

Note the following implications of this system:

- All IRPs including IRP_MJ_... are monitored, not just "KS IRPs" like IRP_MJ_... 
- All IRPs targeted at all instances of the filter are monitored 
- All IRPs targeted at all pin instances on the filter are monitored 

## See also

[KSStudio Utility](ksstudio-utility.md)

[KSStudio - Filters and Filter Factories](ksstudio-utility-filters-and-filter-factories.md)

[KSStudio - Pins and Nodes](ksstudio-utility-pins-and-nodes.md)

[KSStudio - KSProperties and Events](ksstudio-utility-ksproperties-and-events.md)

[KSStudio - Usage Examples](ksstudio-utility-usage-examples.md)


 




