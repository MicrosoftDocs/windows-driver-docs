---
title: ACX IO request packet IRPs
description: This topic provides a high level summary of the ACX IO request packet IRPs.
ms.date: 09/29/2023
ms.localizationpriority: medium
---

# ACX IO request packet IRPs

This topic provides a summary of the Audio Class eXtensions (ACX) IO request packet IRPs.

For general information about the ACX, see [ACX audio class extensions overview](acx-audio-class-extensions-overview.md) and [Summary of ACX Objects](acx-summary-of-objects.md). For information about ACX targets and synchronization, see [ACX targets and driver synchronization](acx-targets.md).

>[!NOTE]
> The ACX headers and libraries are not included in the  WDK 10.0.22621.2428 (released October 24, 2023), but are available in previous versions, as well as the latest (25000 series builds) Insider Preview of the WDK. For more information about preview versions of the WDK, see [Installing preview versions of the Windows Driver Kit (WDK)](../installing-preview-versions-wdk.md).


## IRP request dispatching

An ACX client specifies an action via a driver request (IRP). For general information about IRPs, see, [I/O request packets](../gettingstarted/i-o-request-packets.md) and [Packet-Driven I/O with Reusable IRPs](../kernel/packet-driven-i-o-with-reusable-irps.md).

The client sends this request to a circuit/pin/element/stream by using the circuit or stream handle. The request ID is a triplet:

- set (guid),
- id/index (ulong)
- optional pin-id/node-id (ulong) value.  

At creation time the driver can optionally associates properties/methods/events with one of more of following objects:

- pin
- circuit
- stream
- element

Each property/method/event is identified by an ID and a callback handler. By default, ACX defines all the properties/methods/events required by KS-clients (user-mode layers), thus drivers do not need to redefine them. Drivers only need to define their custom properties/methods/events.

When ACX receives an ACX/KS style IoCtrl request, it validates the request and locks the caller’s buffers in memory. This validation and buffer lock down is done in a WDM pre-process callback that ACX registered at initialization time. During this phase, the ACX adds its own completion callback to the WDM IRP before forwarding it back to WDF for normal dispatching. The completion callback gives ACX an opportunity to add/inject any compatibility workarounds as needed.

Next WDF invokes the dynamic dispatch IRP callback, in this callback ACX/driver (optionally) associates a WDF queue with the request. In this callback ACX locates the target ACX object: circuit, pin, circuit-element or stream using the handle on which this request was sent, and the optional pin-id/node-id/circuit-element within the request.

In an audio composite device it is possible that the target object (circuit-only) may be located on a different stack than the one on which the request is originally sent on. In addition, a request may need to act on multiple stacks, an example of this, is a stream change state.

After the target has been identified, ACX checks if the target circuit/stream-object specifies an override for the default processing queue, if not, ACX uses the default queue associated with current handle. The ACX/driver then instructs WDF to insert the request into the either the specified or the default queue.

Next WDF invokes the in-caller process callback if present. ACX doesn’t need/use the in-caller process callback because it already locked the buffers in memory in the pre-process callback. Thus, ACX informs WDF to not invoke the in-process callback after specifying the target queue for the request.

### Secondary queue usage

The default ACX queue is a power-managed, serial, no-locking queue. The driver should move any request taking an undetermined amount of time into a secondary queue. The driver managed queue could be a manual-passive queue, where the driver can hold on to these requests until it is ready to complete them later.

### Power reference requests

ACX automatically power up the device before dispatching a request to the driver. This is done implicitly by using a WDF power managed queues. This creates a behavior similar to portcls. That is, a power reference is taken, before dispatching the request.

### Invoking the queue’s dispatch handler

Next WDF takes a power reference and invokes the queue’s dispatch handler. The default queue which is associated with the ACX handler checks for any pre-process overrides, and if present, ACX invokes the registered driver’s pre-process callback. ACX allows the driver to specify overrides based on the type of request (property, event, and method) and (optionally) request IDs.  

If a pre-process callback was specified, after ACX invokes the callback, the request is owned by the driver. The driver may complete the request or forward it back to ACX for normal dispatching.

If a pre-process callback was not specified, or if the driver gives back the request to ACX, ACX retrieves the target ACX object and locates the declared property/event/method’s callback. It then invokes the callback passing the WDF request and the target ACX Object (circuit/stream/circuit-element).

Next ACX (or for custom properties, the driver) performs the requested action and completes the request, or if the request takes an undetermined amount of time, the driver can move the request to a secondary queue. The driver is responsible for serializing and completing any active pending requests.

This diagram illustrates the typical request dispatch workflow.

:::image type="content" source="images/audio-acx-dispatch-workflow-1.png" alt-text="Diagram illustrating dispatch workflow with audio service, WDF, ACX, and a driver.":::

This diagram illustrates the dispatch workflow when driver has an ACX preprocess callback defined, although in the end the request is handled by the ACX framework.

:::image type="content" source="images/audio-acx-dispatch-workflow-2.png" alt-text="Diagram illustrating dispatch workflow with audio service, WDF, ACX, and a driver having a preprocess callback.":::

### ACX circuit PnP internal interfaces

To facilitate the communication between ACX Endpoint Manager (EM) and the ACX driver components (kernel-mode or user-mode components), the ACX defines the following internal PnP device interfaces:

- ACXCATEGORY_CIRCUITFACTORY
- ACXCATEGORY_CIRCUIT

The EM uses the ACXCATEGORY_CIRCUITFACTORY interface to instruct a target device to create or remove a specific circuit of this type. This interface is active while the underline device is able to create circuits, otherwise it is disabled (example: remove, surprise-removal, stop or manual remove).

The Audio subsystem uses ACXCATEGORY_CIRCUIT (which may be created on a different device stack than the circuit-manager stack), to track and communicate with the ACX circuit. This interface is active when the circuit has been created and ready to process commands.

For information about other power and PnP processes, see [ACX device enumeration](acx-device-enumeration.md) and [ACX power management](acx-power-management.md).

## See also

[ACX audio class extensions overview](acx-audio-class-extensions-overview.md)

[ACX reference documentation](acx-reference.md)

[Summary of ACX Objects](acx-summary-of-objects.md)

[ACX version information](acx-version-overview.md)

[ACX multi stack cross driver communications](acx-multi-stack.md)
