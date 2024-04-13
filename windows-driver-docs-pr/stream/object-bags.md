---
title: Object Bags
description: Object Bags
keywords:
- AVStream object bags WDK
- object bags WDK AVStream
- objects WDK AVStream
- memory management WDK AVStream
- sharing dynamically allocated data for AVStream WDK
- dynamically allocated data WDK AVStream
- AVStream descriptors WDK
- descriptors WDK AVStream
ms.date: 04/20/2017
---

# Object Bags





AVStream manages a construct referred to as an object bag for each AVStream object visible to the minidriver. An object bag is a generic container for holding dynamically allocated memory associated with a given object.

The following structures have members of type KSOBJECT\_BAG, which is equivalent to PVOID: [**KSDEVICE**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksdevice), [**KSFILTERFACTORY**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilterfactory), [**KSFILTER**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter), and [**KSPIN**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin).

Uses of object bags include:

-   Memory management.

    Minidrivers can use object bags for memory management to reduce cleanup work. In order to do this, a minidriver must first call [**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag) to allocate dynamic memory and associate it with a given object. The minidriver then adds the allocated memory to the object bag by calling [**KsAddItemToObjectBag**](/windows-hardware/drivers/ddi/ks/nf-ks-ksadditemtoobjectbag).

    When the minidriver calls **KsAddItemToObjectBag**, AVStream associates a default cleanup function (typically [**ExFreePool**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool)) with the object. Alternatively, the minidriver can include a pointer to a minidriver-provided cleanup routine in the *Free* parameter of **KsAddItemToObjectBag**. When an object is closed, AVStream removes every item from the object bag and calls the associated cleanup routines.

-   Sharing dynamically allocated data among several AVStream objects.

    A minidriver can share dynamically allocated data among several AVStream objects by placing a given item in more than one object bag. In this case, AVStream does not release the given item until it is no longer contained in any object bag. The only limitation on the number of items an object bag can contain is available memory.

-   Determining which structures can be edited with descriptors.

    If a minidriver dynamically allocates a descriptor or a descriptor substructure, the minidriver places the descriptor in the relevant object bag. The [**\_KsEdit**](/windows-hardware/drivers/ddi/ks/nf-ks-_ksedit) function then uses this information to determine whether a given structure can be edited.

AVStream automatically removes items from an object bag if the owning object is deleted.

Minidrivers can remove individual items from an object bag by calling [**KsRemoveItemFromObjectBag**](/windows-hardware/drivers/ddi/ks/nf-ks-ksremoveitemfromobjectbag) or [**KsDiscard**](/windows-hardware/drivers/ddi/ks/nf-ks-ksdiscard).

 

