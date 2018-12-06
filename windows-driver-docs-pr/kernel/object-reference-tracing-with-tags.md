---
title: Object Reference Tracing with Tags
description: Object Reference Tracing with Tags
ms.assetid: f6c3d7b2-09b1-4055-b066-cce8831efab2
keywords: ["object referencing with tags WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Object Reference Tracing with Tags


[Kernel objects](managing-kernel-objects.md) are primitive data objects that the Windows kernel implements in system memory to represent the various parts of the computing environment that are managed by the operating system. Kernel objects represent features such as devices, drivers, files, registry keys, events, semaphores, processes, and threads.

Most kernel objects are not permanent. To prevent a nonpermanent kernel object from being deleted while a kernel-mode driver uses the object, the driver can obtain a counted reference to the object. When the driver no longer needs the object, the driver releases its reference to the object.

If a driver does not release all its references to an object, the object's reference count never decrements to zero and the object is never deleted. Therefore, the system resources that are used by the object (for example, system memory) are *leaked*. That is, they cannot be used until the next time that the operating system starts.

Another type of reference error occurs if a driver *under references* an object. In this case, the driver releases more references to an object than the driver actually holds. This error can cause the object to be deleted prematurely, while other clients are still trying to access the object.

Leaks and under-references of kernel objects can be difficult bugs to track down. For example, a process object or a device object might have tens of thousands of references. It can be difficult to identify the source of an object reference bug in these circumstances.

In Windows 7 and later versions of Windows, object references can be tagged to make these bugs easier to find. The following routines associate tags with the acquisition and release of references to kernel objects:

[**ObDereferenceObjectDeferDeleteWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff557732)

[**ObDereferenceObjectWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff557734)

[**ObReferenceObjectByHandleWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff558683)

[**ObReferenceObjectByPointerWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff558688)

[**ObReferenceObjectWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff558690)

For example, **ObReferenceObjectWithTag** and **ObDereferenceObjectWithTag**, which are available in Windows 7 and later versions of Windows, are enhanced versions of the [**ObReferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff558678) and [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) routines, which are available in Windows 2000 and later versions of Windows. These enhanced routines enable you to supply a four-byte, custom tag value as an input parameter. The tag value for each call is added to an [object reference trace](http://go.microsoft.com/fwlink/p/?linkid=153590) that can be accessed by the [Windows debugging tools](http://go.microsoft.com/fwlink/p/?linkid=153599). **ObReferenceObject** and **ObDereferenceObject** do not enable the caller to specify custom tags, but, in Windows 7 and later versions of Windows, these routines add default tags (with tag value "Dflt") to the trace. Therefore, a call to **ObReferenceObject** or **ObDereferenceObject** has the same effect as a call to **ObReferenceObjectWithTag** or **ObDereferenceObjectWithTag** that specifies a tag value of "Dflt". (In your program, this tag value is represented as 0x746c6644 or 'tlfD'.)

To track down a potential object leak or under-reference, identify a set of associated **ObReferenceObject*Xxx*WithTag** and **ObDereferenceObject*Xxx*WithTag** calls in your driver that increment and decrement the reference count of a particular object. Choose a common tag value (for example, "Lky8") to use for all the calls in this set. After your driver is finished using the object, the number of decrements should match the number of increments exactly. If these numbers do not match, your driver has an object reference bug. The debugger can compare the number of increments and decrements for each tag value and tell you if they do not match. With this capability, you can quickly pinpoint the source of the reference-count mismatch.

To view an object reference trace in the Windows debugging tools, use the [!obtrace](http://go.microsoft.com/fwlink/p/?linkid=153600) kernel-mode debugger extension. In Windows 7 and later versions of Windows, the [!obtrace](http://go.microsoft.com/fwlink/p/?linkid=153600) extension can display object reference tags, if object reference tracing is enabled. By default, object reference tracing is disabled. Use the [Global Flags Editor](http://go.microsoft.com/fwlink/p/?linkid=153601) (Gflags) to enable object reference tracing. For more information about Gflags, see [Configuring Object Reference Tracing](http://go.microsoft.com/fwlink/p/?linkid=153602).

After object reference tracing is enabled, the output that is produced by the [!obtrace](http://go.microsoft.com/fwlink/p/?linkid=153600) extension includes a "Tag" column, as the following example shows:

```cpp
0: kd> !obtrace 0x8a226130
Object: 8a226130
 Image: leakyapp.exe
Sequence   (+/-)   Tag    Stack
--------   -----   ----   --------------------------------------------
      36    +1     Dflt      nt!ObCreateObject+1c4
                             nt!NtCreateEvent+93
                             nt!KiFastCallEntry+12a

      37    +1     Dflt      nt!ObpCreateHandle+1c1
                             nt!ObInsertObjectEx+d8
                             nt!ObInsertObject+1e
                             nt!NtCreateEvent+ba
                             nt!KiFastCallEntry+12a

      38    -1     Dflt      nt!ObfDereferenceObjectWithTag+22
                             nt!ObInsertObject+1e
                             nt!NtCreateEvent+ba
                             nt!KiFastCallEntry+12a

      39    +1     Lky8      nt!ObReferenceObjectByHandleWithTag+254
                             leakydrv!LeakyCtlDeviceControl+6c
                             nt!IofCallDriver+63
                             nt!IopSynchronousServiceTail+1f8
                             nt!IopXxxControlFile+6aa
                             nt!NtDeviceIoControlFile+2a
                             nt!KiFastCallEntry+12a

      3a    -1     Dflt      nt!ObfDereferenceObjectWithTag+22
                             nt!ObpCloseHandle+7f
                             nt!NtClose+4e
                             nt!KiFastCallEntry+12a
 
--------   -----   ----   --------------------------------------------
References: 3, Dereferences 2
Tag: Lky8 References: 1 Dereferences: 0 Over reference by: 1
```

The last line in this example indicates that the reference and dereference counts that are associated with the "Lky8" tag do not match and that the result of this mismatch is an over-reference by one (that is, a leak).

If the result were instead an under-reference, the last line of the [!obtrace](http://go.microsoft.com/fwlink/p/?linkid=153600) output might be as follows:

```cpp
Tag: Lky8 References: 1 Dereferences: 2 Under reference by: 1
```

By default, the operating system conserves memory by deleting the object reference trace for an object after the object is freed. To track down an under-reference requires that the trace remain stored in memory even after the object is freed. For this purpose, the Gflags tool provides a "Permanent" option, which preserves the trace in memory while the computer shuts down and starts again.

Object reference tracing, without tags, was introduced in Windows XP. Because the trace did not include tags, developers had to use less convenient techniques to identify object reference bugs. The debugger could track the references of groups of objects, which the developer selected by object type. The only way that the developer could identify the various sources of object references and dereferences was to compare their call stacks. Although the previous [!obtrace](http://go.microsoft.com/fwlink/p/?linkid=153600) example contains only five stacks, certain types of object, such as a process ([**EPROCESS**](eprocess.md)) object, might be referenced and dereferenced many thousands of times. With thousands of stacks to inspect, it might be difficult to identify the source of an object leak or under-reference without using tags.

 

 




