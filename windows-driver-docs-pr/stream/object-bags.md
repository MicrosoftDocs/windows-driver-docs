---
title: Object Bags
author: windows-driver-content
description: Object Bags
MS-HAID:
- 'avsover\_77963301-d8c4-41ab-9933-3e63a911942a.xml'
- 'stream.object\_bags'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b7ee5756-1c79-4ead-9999-d13be9a0d3d9
keywords: ["AVStream object bags WDK", "object bags WDK AVStream", "objects WDK AVStream", "memory management WDK AVStream", "sharing dynamically allocated data for AVStream WDK", "dynamically allocated data WDK AVStream", "AVStream descriptors WDK", "descriptors WDK AVStream"]
---

# Object Bags


## <a href="" id="ddk-object-bags-ksg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Object%20Bags%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


