---
title: Creating and Using Per-Stream Context Structures
author: windows-driver-content
description: Creating and Using Per-Stream Context Structures
ms.assetid: f34898e2-f82e-4962-89d2-e9fb077c04f9
keywords: ["filter drivers WDK file system , per-stream context tracking", "file system filter drivers WDK , per-stream context tracking", "per-stream context tracking WDK file system", "tracking per-stream context WDK file system", "FSRTL_PER_STREAM_CONTEXT"]
---

# Creating and Using Per-Stream Context Structures


## <span id="ddk_creating_and_using_per_stream_context_structures_if"></span><span id="DDK_CREATING_AND_USING_PER_STREAM_CONTEXT_STRUCTURES_IF"></span>


File system filter drivers that use a per-stream context structure containing a [**FSRTL\_PER\_STREAM\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff547357) structure can take advantage of built-in per-stream context support in Microsoft Windows XP and later. This section covers the following topics:

[Creating a Per-Stream Context](creating-a-per-stream-context.md)

[Associating a Per-Stream Context With a File Stream](associating-a-per-stream-context-with-a-file-stream.md)

[Deleting a Per-Stream Context](deleting-a-per-stream-context.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Creating%20and%20Using%20Per-Stream%20Context%20Structures%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


