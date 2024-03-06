---
title: Object Reference Tracing with Tags
description: Object Reference Tracing with Tags
keywords: ["object referencing with tags WDK"]
ms.date: 02/15/2023
---

# Object Reference Tracing with Tags


[Kernel objects](managing-kernel-objects.md) are primitive data objects that Windows kernel implements in system memory. They represent entities such as devices, drivers, files, registry keys, events, semaphores, processes, and threads.

Most kernel objects aren't permanent. To prevent Windows from deleting a nonpermanent kernel object while a kernel-mode driver is using it, the driver obtains a counted reference to the object. When the driver no longer needs the object, the driver releases its reference to the object.

If a driver doesn't release all its references to an object, the object's reference count never reaches zero, and the Object Manager never deletes it. You can't reuse leaked resources until the operating system restarts.

Another type of reference error occurs if a driver *under references* an object. In this case, the driver releases more references to an object than the driver actually holds. This error can cause the Object Manager to delete the object prematurely, while other clients are still trying to access the object.

Leaks and under-references of kernel objects can be difficult bugs to track down. For example, a process object or a device object might have tens of thousands of references. It can be difficult to identify the source of an object reference bug in these circumstances.

In Windows 7 and later versions of Windows, you can supply a tag for object references to make these bugs easier to find. The following routines associate tags with the acquisition and release of references to kernel objects:

[**ObDereferenceObjectDeferDeleteWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobjectdeferdeletewithtag)

[**ObDereferenceObjectWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobjectwithtag)

[**ObReferenceObjectByHandleWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandlewithtag)

[**ObReferenceObjectByPointerWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbypointerwithtag)

[**ObReferenceObjectWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectwithtag)

For example, **ObReferenceObjectWithTag** and **ObDereferenceObjectWithTag**, which are available in Windows 7 and later versions of Windows, are enhanced versions of the [**ObReferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obfreferenceobject) and [**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject) routines, which are available in Windows 2000 and later versions of Windows. These enhanced routines enable you to supply a four-byte, custom tag value as an input parameter. You can use the [Windows debugging tools](https://go.microsoft.com/fwlink/p/?linkid=153599) to inspect an [object reference trace](../debugger/object-reference-tracing.md) that contains the tag value for each call . **ObReferenceObject** and **ObDereferenceObject** don't enable the caller to specify custom tags, but, in Windows 7 and later versions of Windows, these routines add default tags (with tag value "Dflt") to the trace. Therefore, a call to **ObReferenceObject** or **ObDereferenceObject** has the same effect as a call to **ObReferenceObjectWithTag** or **ObDereferenceObjectWithTag** that specifies a tag value of "Dflt". (In your program, this tag value appears as 0x746c6644 or 'tlfD'.)

To track down a potential object leak or under-reference, identify a set of associated **ObReferenceObject*Xxx*WithTag** and **ObDereferenceObject*Xxx*WithTag** calls in your driver that increment and decrement the reference count of a particular object. Choose a common tag value (for example, "Lky8") to use for all the calls in this set. After your driver finishes using an object, the number of decrements should match the number of increments exactly. If these numbers don't match, your driver has an object reference bug. The debugger can compare the number of increments and decrements for each tag value and tell you if they don't match. With this capability, you can quickly pinpoint the source of the reference-count mismatch.

To view an object reference trace in the Windows debugging tools, use the [!obtrace](../debuggercmds/-obtrace.md) kernel-mode debugger extension. If object reference tracing is on, you can use the [!obtrace](../debuggercmds/-obtrace.md) extension to display object reference tags. By default, object reference tracing is off. Use the [Global Flags Editor](https://go.microsoft.com/fwlink/p/?linkid=153601) (Gflags) to enable object reference tracing. For more information about Gflags, see [Configuring Object Reference Tracing](../debugger/configuring-object-reference-tracing.md).

The output of the [!obtrace](../debuggercmds/-obtrace.md) extension includes a "Tag" column, as the following example shows:

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

If the result were instead an under-reference, the last line of the [!obtrace](../debuggercmds/-obtrace.md) output might be as follows:

```cpp
Tag: Lky8 References: 1 Dereferences: 2 Under reference by: 1
```

By default, the operating system conserves memory by deleting the object reference trace for an object after it frees the object. Keeping a trace in memory even after the system frees an object can be handy when tracking down an under-reference. For this purpose, the Gflags tool provides a "Permanent" option, which preserves the trace in memory while the computer shuts down and starts again.

Windows XP introduced object reference tracing. Because initially the trace didn't include tags, developers had to use less convenient techniques to identify object reference bugs. The debugger could track the references of groups of objects, which the developer selected by object type. The only way that the developer could identify the various sources of object references and dereferences was to compare their call stacks. Although the previous [!obtrace](../debuggercmds/-obtrace.md) example contains only five stacks, certain types of object, such as a process ([**EPROCESS**](eprocess.md)) object, might be referenced and dereferenced many thousands of times. With thousands of stacks to inspect, it might be difficult to identify the source of an object leak or under-reference without using tags.