---
title: ACX targets and driver synchronization
description: This topic provides a high level summary of the ACX targets and driver synchronization.
ms.date: 04/19/2023
ms.localizationpriority: medium
---

# ACX targets and driver synchronization

>[!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This topic provides a summary of the Audio Class eXtensions (ACX) targets and driver synchronization.

For general information about the ACX, see [ACX audio class extensions overview](acx-audio-class-extensions-overview.md) and [Summary of ACX Objects](acx-summary-of-objects.md). For information about IRPs, see [ACX IO request packet IRPs](acx-irps.md).

## ACX targets

ACX uses [WdfIoTarget](/windows-hardware/drivers/ddi/wdfiotarget/) to facilitate communications between ACX objects, circuits, pins, streams, elements and circuit factories. WdfIoTarget is an existing WDF abstraction to facilitate the communication between two different stacks.

Drivers use [AcxTargetCircuit](/windows-hardware/drivers/ddi/acxtargets/) to communicate with a remote circuit exposed by a different stack. AcxTargetCircuit is implemented using a WdfIoTarget.

Drivers use [AcxTargetPin](/windows-hardware/drivers/ddi/acxpin/) to communicate with a remote circuit’s pin exposed by a different stack. AcxTargetPin is implemented using a WdfIoTarget to send messages to the remote pin entity.

Drivers use [AcxTargetStream](/windows-hardware/drivers/ddi/acxstreams/) to communicate with a remote circuit’s stream exposed by a different stack. AcxTargetStream is implemented using a WdfIoTarget to create a remote stream and change the state of the remote stream.

Drivers use [AcxTargetElement](/windows-hardware/drivers/ddi/acxtargets/) to communicate with a remote circuit’s element exposed by a different stack. AcxTargetElement is implemented using a WdfIoTarget to send messages to the remote element entity.

Drivers use [AcxTargetFactoryCircuit](/windows-hardware/drivers/ddi/acxtargets/) to communicate with a remote circuit factory instance. AcxTargetFactoryCircuit is implemented using a WdfTarget to send messages to the remote circuit factory.

To interact with the remote circuit, each of the ACX types listed above supports:

- properties
- methods
- events

All these types are built on top of the [WdfIoTarget](/windows-hardware/drivers/ddi/wdfiotarget/) object types.

This diagram shows the ACX target architecture and the inheritance from the WDF Driver and Device objects.  

![diagram illustrating the acx target architecture showing WDFDRIVER, WDFDEVICE, and under that ACXTARGET, ACXSTREAM ACXSTREAMFACTORY with the lowest layer showing ACXTARGETELEMENT and ACXTARGETPIN](images/audio-acx-multi-stack-acxtarget-objects.png)

## ACX driver synchronization and serialization

The term synchronization is a general term, and it is used to reference the operations needed to share resources (memory, I/O, etc.) between multiple concurrent clients.

The term serialization is used to reference one type of synchronization for one type of object (I/O requests, callbacks, etc.).

ACX Drivers are WDF Drivers, which means that the synchronization of ACX Drivers is based on the synchronization capabilities of WDF:

- The use of reference counts and the hierarchical object model.
- Driver-configurable flow control for I/O queues.
- Object presentation lock for device objects and I/O queues.
- Automatic serialization of Plug and Play and power callbacks.

For an in-depth description of Synchronization and Serialization, see [Using Automatic Synchronization](../wdf/using-automatic-synchronization.md). For a more complete explanation, see the [Developing Drivers with Windows Driver Foundation](../wdf/developing-drivers-with-wdf.md) Microsoft Press Book.  

WDF supports the following synchronization scopes:

- No scope (default in KMDF).  
- Device scope, WDF acquires the device object presentation lock to serialize operations.

The default ACX queue is a passive, serial queue with no locking. The driver must complete the I/O operation before the next one is delivered.

ACX doesn’t support the queue scope option. With this option the driver serializes I/O on a specific queue. Different queues may have different synchronization scopes.

ACX doesn’t support device scope serialization. By default, ACX serializes requests using a serial I/O queue with no locking. Every circuit and stream object have its own dedicated queue. For more info about streaming I/Os please see the ACX Streaming topic.

If a driver holds a lock, it should never call (explicitly or implicitly) code outside its control until the lock is released.

For historical reference, the original PortCls uses a synchronization scope like the WDF device scope synchronization, where all I/O for any audio sub-devices created on this device go through the same serialization lock. This type of serialization was, and still is, the cause of various glitches. In later versions of Windows 10 (Version 1511 - TH2) PortCls was updated to use a different lock for stream position I/O requests.

## See also

[ACX audio class extensions overview](acx-audio-class-extensions-overview.md)

[Summary of ACX Objects](acx-summary-of-objects.md)

[ACX version information](acx-version-overview.md)

[ACX reference documentation](acx-reference.md)

[ACX multi stack cross driver communications](acx-multi-stack.md)
