---
title: Object Bags
description: Object Bags
ms.assetid: b7ee5756-1c79-4ead-9999-d13be9a0d3d9
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
ms.localizationpriority: medium
---

# Object Bags





AVStream manages a construct referred to as an object bag for each AVStream object visible to the minidriver. An object bag is a generic container for holding dynamically allocated memory associated with a given object.

The following structures have members of type KSOBJECT\_BAG, which is equivalent to PVOID: [**KSDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff561681), [**KSFILTERFACTORY**](https://msdn.microsoft.com/library/windows/hardware/ff562530), [**KSFILTER**](https://msdn.microsoft.com/library/windows/hardware/ff562522), and [**KSPIN**](https://msdn.microsoft.com/library/windows/hardware/ff563483).

Uses of object bags include:

-   Memory management.

    Minidrivers can use object bags for memory management to reduce cleanup work. In order to do this, a minidriver must first call [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) to allocate dynamic memory and associate it with a given object. The minidriver then adds the allocated memory to the object bag by calling [**KsAddItemToObjectBag**](https://msdn.microsoft.com/library/windows/hardware/ff560941).

    When the minidriver calls **KsAddItemToObjectBag**, AVStream associates a default cleanup function (typically [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590)) with the object. Alternatively, the minidriver can include a pointer to a minidriver-provided cleanup routine in the *Free* parameter of **KsAddItemToObjectBag**. When an object is closed, AVStream removes every item from the object bag and calls the associated cleanup routines.

-   Sharing dynamically allocated data among several AVStream objects.

    A minidriver can share dynamically allocated data among several AVStream objects by placing a given item in more than one object bag. In this case, AVStream does not release the given item until it is no longer contained in any object bag. The only limitation on the number of items an object bag can contain is available memory.

-   Determining which structures can be edited with descriptors.

    If a minidriver dynamically allocates a descriptor or a descriptor substructure, the minidriver places the descriptor in the relevant object bag. The [**\_KsEdit**](https://msdn.microsoft.com/library/windows/hardware/ff568796) function then uses this information to determine whether a given structure can be edited.

AVStream automatically removes items from an object bag if the owning object is deleted.

Minidrivers can remove individual items from an object bag by calling [**KsRemoveItemFromObjectBag**](https://msdn.microsoft.com/library/windows/hardware/ff566798) or [**KsDiscard**](https://msdn.microsoft.com/library/windows/hardware/ff561695).

 

 




