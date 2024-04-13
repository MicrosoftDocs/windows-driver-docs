---
title: Event Handling in AVStream
description: Event Handling in AVStream
keywords:
- events WDK AVStream
- AVStream events WDK
- automation tables WDK AVStream
ms.date: 04/20/2017
---

# Event Handling in AVStream





AVStream filters and pins describe properties, events, and methods that they support by supplying a [**KSAUTOMATION\_TABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksautomation_table_) structure in the **AutomationTable** member of either a [**KSFILTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter_descriptor) structure or a [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structure. For more information, see [AVStream Descriptors](avstream-descriptors.md).

To support events, an AVStream minidriver provides an array of [**KSEVENT\_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksevent_set) structures in an automation table. Each KSEVENT\_SET structure contains an array of [**KSEVENT\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksevent_item) structures. Each KSEVENT\_ITEM structure describes how the minidriver supports a specific event.

The minidriver can customize event behavior by supplying [*AVStrMiniAddEvent*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnksaddevent) and [*AVStrMiniRemoveEvent*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnksremoveevent) handlers in the KSEVENT\_ITEM structures.

When AVStream receives an event enable request, it generates a KSEVENT\_ENTRY structure. If the minidriver has provided an *AVStrAddEvent* handler, AVStream passes a pointer to the KSEVENT\_ENTRY structure in the call to *AVStrAddEvent*.

If you do not provide an *AVStrAddEvent* handler, then by default AVStream adds the event to the object list. Your minidriver does not receive a [**KSEVENT\_ENTRY**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksevent_entry) pointer. Your minidriver can trigger the event by calling [**KsFilterGenerateEvents**](/windows-hardware/drivers/ddi/ks/nf-ks-ksfiltergenerateevents) or [**KsPinGenerateEvents**](/windows-hardware/drivers/ddi/ks/nf-ks-kspingenerateevents).

 

