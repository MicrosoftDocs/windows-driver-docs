---
title: Object Reference Tracing
description: Object Reference Tracing
ms.assetid: b5af0ab0-954b-4da1-a074-df88d2d039f8
keywords: ["Object Reference Tracing", "Object Reference Tracing, overview", "GFlags, Object Reference Tracing"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Object Reference Tracing


The **Object Reference Tracing** feature records sequential stack traces each time that an object reference counter is incremented or decremented. The traces can help you to detect object reference errors, including double-dereferencing, failure to reference, and failure to dereference objects. This feature is supported only in Windows Vista and later versions of Windows.

For information about configuring the Object Reference Tracing feature in the **Global Flags** dialog box, see [Configuring Object Reference Tracing](configuring-object-reference-tracing.md). For information about configuring the Object Reference Tracing feature at the command prompt, see [**GFlags Commands**](gflags-commands.md). For an example, see [Example 15: Using Object Reference Tracing](example-15--using-object-reference-tracing.md).

Object reference traces are most useful when you suspect that a particular object is not being referenced or dereferenced properly, typically because increased pool usage indicates that an object is leaking, or a process or session cannot be ended, even though its handle count is zero. Unlike traces that are recorded in logs for later review, object reference traces are designed to be used in real time, while the process is running and the object is being referenced and dereferenced. You view an object reference trace in the debugger by using the [**!obtrace debugger extension**](-obtrace.md). Because this extension requires a specified object address, you must know in advance which object is the likely source of the error.

The following rules apply to Object Reference Tracing:

-   You can run only one object reference trace at a time.

-   Because a kernel-wide trace is not practical, you must limit the trace to objects that are created with specified pool tags, or to objects that are created by a specified process (indicated by an image file name), or both.

-   You can specify only one image file for each trace. If you specify an image file, the trace is limited to objects that are created by the processes that the image represents. Objects that are referenced by the process, but are created by a different process, are not traced.

-   You can specify a maximum of 16 pool tags for each trace. Objects with any of the specified pool tags are traced.

-   If you specify both an image file and one or more pool tags, the trace is limited to objects that are created by the process and have any of the specified pool tags.

-   Object Reference Tracing cannot trace processes that are already running when a trace is started. The trace includes only the objects of processes that start after the trace begins.

-   Objects marked for tracing are traced until the object is destroyed or tracing is disabled. By default, the traces for an object are maintained only until the object is destroyed, but you can specify a "permanent" trace (**/p**) where the trace is retained until tracing is disabled.

-   You can store the Object Reference Tracing configuration as a registry setting or a kernel flag (run-time) setting. If you have both registry and kernel flag settings, the run-time settings take precedence, but are lost when you shut down or restart the computer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Object%20Reference%20Tracing%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




