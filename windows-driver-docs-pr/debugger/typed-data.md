---
title: Typed Data
description: Typed Data
ms.assetid: 44a84dfd-03f8-4d7b-8d71-e4b3ee23d105
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Typed Data


The EngExtCpp extension framework provides a few classes to help manipulate the target's memory. The [**ExtRemoteData**](https://msdn.microsoft.com/library/windows/hardware/ff544003) class describes a small piece of the target's memory. If the type of this memory is known, it is referred to as *typed data* and is described by [**ExtRemoteTyped**](https://msdn.microsoft.com/library/windows/hardware/ff544162) objects.

Windows lists can be iterated over by using [**ExtRemoteList**](https://msdn.microsoft.com/library/windows/hardware/ff544114) and, if the type of the objects in the list is known, [**ExtRemoteTypedList**](https://msdn.microsoft.com/library/windows/hardware/ff544173).

**Note**   Like the client objects in [**ExtExtension**](https://msdn.microsoft.com/library/windows/hardware/ff543981), instances of these classes are only valid while the extension library is used to execute an extension command or format a structure for output. In particular, they should not be cached. For more information about when client objects are valid, see [Client Objects and the Engine](client-objects-and-the-engine.md), .

 

### <span id="remote_data"></span><span id="REMOTE_DATA"></span>Remote Data

Remote data should be handled using the class [**ExtRemoteData**](https://msdn.microsoft.com/library/windows/hardware/ff544003). This class is a wrapper around a small section of a target's memory. **ExtRemoteData** automatically retrieves the memory and wraps other common requests with throwing methods.

### <span id="remote_typed_data"></span><span id="REMOTE_TYPED_DATA"></span>Remote Typed Data

If the type of the remote data is known, it should be handled using the [**ExtRemoteTyped**](https://msdn.microsoft.com/library/windows/hardware/ff544162) class. This class is an enhanced remote data object that understands data typed with type information from symbols. It is initialized to a particular object by symbol or cast, after which it can be used like an object of the given type.

### <span id="remote_lists"></span><span id="REMOTE_LISTS"></span>Remote Lists

To handle remote lists, use the [**ExtRemoteList**](https://msdn.microsoft.com/library/windows/hardware/ff544114) class. This class can be used for either a singly linked or doubly linked list. If the list is doubly linked, it is assumed that the previous pointer immediately follows the next pointer. The class contains methods that can iterate over the list and retrieve nodes both forward and backward. **ExtRemoteList** can be used with either null-terminated or circular lists also.

### <span id="remote_typed_lists"></span><span id="REMOTE_TYPED_LISTS"></span>Remote Typed Lists

To handle remote lists when the type of the nodes in the list is known, use the [**ExtRemoteTypedList**](https://msdn.microsoft.com/library/windows/hardware/ff544173) class. This is an enhanced version of [**ExtRemoteList**](https://msdn.microsoft.com/library/windows/hardware/ff544114). In addition to the basic functionality of **ExtRemoteList**, **ExtRemoteTypedList** automatically determines link offsets from type information.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Typed%20Data%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




