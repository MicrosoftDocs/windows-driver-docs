---
title: ACX Circuits
description: This topic provides a summary of ACX Circuits 
ms.date: 03/08/2024
ms.localizationpriority: medium
ms.topic: concept-article
---

# ACX circuits

This topic discusses ACX circuits. For a general overview of ACX and list of ACX terms, see [ACX audio class extensions overview](acx-audio-class-extensions-overview.md).

As described in [Summary of ACX objects](acx-summary-of-objects.md), an AcxCircuit object represents a partial or full audio path to a user perceived audio device (speakers, mic, etc.). An AcxCircuit has at least one input pin and one output pin (ACXPIN), and it may aggregate one or more AcxElements like objects. The circuit represents an existing endpoint and its capabilities.

And ACX *Stream* is a driver component that’s created to represent an audio stream, created by a Circuit. The Stream is composed of a list of Elements created based on the parent Circuit’s Elements. A *Stream Circuit* is a circuit in a multi-stack architecture (partial audio path) that directly interface with upper user-mode streaming service. A *Core Circuit* is a circuit in a multi-stack architecture (partial audio path) that gives the identity of the audio endpoint device.

## ACX circuit identification

Every ACX circuit has a circuit identifier. ACX defines the following:

- *Name (str)*, uniquely identifies this circuit audio device type. It is used to locate INF’s setting, and it is part of the symbolic link used to access this circuit from a remote device. Example: “Render0”, “Render1” or “Capture0”.

- *Symbolic link*. A symbolic link is associated with all the exposed circuits. Clients use this symbolic link to open a communication path with the device/circuit.

- *Circuit’s component ID (guid)*. Uniquely identifies the circuit instance (vendor specific). It cannot be used in the AcxCircuitTemplate bindings if the Circuit URI was specified.

- *Circuit’s component URI (str)*. Uniquely identifies the circuit instance (vendor specific). It cannot be used in the AcxCircuitTemplate bindings if the Circuit ID was specified.

- *Circuit Factory’s component ID (guid)*. Uniquely identifies the circuit factory instance (vendor specific). It cannot be used in the AcxCircuitTemplate bindings if the Circuit Factory URI was specified.

- *Circuit Factory’s component URI (str)*. Uniquely identifies the circuit factory instance (vendor specific). It cannot be used in the AcxCircuitTemplate bindings if the Circuit Factory ID was specified.

## AcxCircuitCreate

The [AcxCircuitCreate function](/windows-hardware/drivers/ddi/acxcircuit/nf-acxcircuit-acxcircuitcreate)  is used to create an ACXCIRCUIT. An opaque ACXCIRCUIT_INIT structure that is used by the AcxCircuitCreate function. [AcxCircuitInitAllocate](/windows-hardware/drivers/ddi/acxcircuit/nf-acxcircuit-acxcircuitinitallocate) is used to initialize the ACXCIRCUIT_INIT structure.

### AcxFactoryCircuit

An ACX driver can also create AcxFactoryCircuit objects (circuit providers) during power up sequence using the [AcxFactoryCircuitCreate function](/windows-hardware/drivers/ddi/acxcircuit/nf-acxcircuit-acxfactorycircuitcreate) and the [AcxDeviceAddFactoryCircuit function](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceaddfactorycircuit).

## ACX circuit composition

ACX binds circuits together until they form a complete audio path. ACX uses audio bindings to connect audio circuits together. For more information, see  [ACX multicircuit composition](acx-multi-circuit-composition.md).

### ACX circuit dynamic creation (at any time)

ACX can create a dynamic circuit on demand. To do this, the driver allocates a [WDFDEVICE_INIT structure](../wdf/wdfdevice_init.md) by calling [WdfPdoInitAllocate](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallocate). The driver then specifies any PnP/power callbacks it wants to receive and creates the device. The driver instantiates the new device/circuit by calling [AcxDeviceAddCircuitDevice](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceaddcircuitdevice). For more information, see [ACX device enumeration](acx-device-enumeration.md).

## ACX circuit dynamic removal

The driver invokes [AcxDeviceRemoveCircuitDevice](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceremovecircuitdevice) to remove the audio device from the device list. This triggers the power down sequence on the ACX circuit device/circuit entity. The circuit device/circuit is deleted asynchronously. For more information, see [ACX device enumeration](acx-device-enumeration.md).

### AcxDeviceRemoveCircuit and AcxDeviceDetachCircuit

There are two common ways to manage circuit termination. [AcxDeviceDetachCircuit](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdevicedetachcircuit) or [AcxDeviceRemoveCircuit](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceremovecircuit).

If the caller invokes the [AcxDeviceDetachCircuit](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdevicedetachcircuit) it must not call [AcxDeviceRemoveCircuit](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceremovecircuit). If the calling driver wants to delete the circuit after AcxDeviceDetachCircuit it should use [WdfObjectDelete](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

By calling [AcxDeviceRemoveCircuit](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceremovecircuit) the calling driver tells ACX to remove this circuit and remove/delete it from the device. In this case there is no need to call WdfObjectDelete on the circuit.

In summary, [AcxDeviceDetachCircuit](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdevicedetachcircuit)  means that the driver owns the management of the circuit objects lifetime, [AcxDeviceRemoveCircuit](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceremovecircuit) means that the circuit will be removed and deleted.

For general information about WDF object lifetime management, see [Framework Object Life Cycle](/windows-hardware/drivers/wdf/framework-object-life-cycle).

#### AcxDeviceRemoveCircuitDevice

Different from the circuit termination discussed above, [AcxDeviceRemoveCircuitDevice](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceremovecircuitdevice) is used by the audio driver to remove an existing audio endpoint and can be called at any time during the driver's life cycle.

Drivers may also opt to always destroy and recreate audio devices on rebalance. This is the same scenario above when the device detects that the new settings are not compatible with the old ones.

The deletion of the circuit must be done in EvtDevicePrepareHardware/EvtDeviceReleaseHardware callbacks, and the new circuit is re-created in EvtDevicePrepareHardware. The driver deletes a circuit by un-registering the circuit (using [AcxDeviceRemoveCircuit](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceremovecircuit)).

### EvtAcxCircuitReleaseHardware (EVT_ACX_CIRCUIT_RELEASE_HARDWARE) callback function

If a driver has registered an [EvtAcxCircuitReleaseHardware callback function](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_release_hardware) the framework calls it during the following transitions:

- Resource rebalancing
- Orderly removal
- Surprise removal

The ACX framework calls the EvtAcxCircuitReleaseHardware callback function after the WDF framework has stopped sending I/O requests to the device, any interrupts assigned to the device have been disabled and disconnected, and the device has been turned off.

The ACX framework calls the EvtAcxCircuitReleaseHardware callback function before the WDF framework calls the driver's EvtDeviceReleaseHardware callback function.

When the framework calls the EvtAcxCircuitReleaseHardware the PDO for the device still exists and can be queried for device information that is available in the powered off state, for example PCI configuration state.

In addition, the translated hardware resources that the framework supplies to EvtDeviceReleaseHardware are still assigned to the device. The primary purpose of this callback function is to release those resources, and in particular to un-map any memory resources that the driver's EvtAcxCircuitPrepareHardware callback function mapped. The driver can also use this callback to perform any other ACXCIRCUIT management activity that might be required in the powered down state. Usually, all other hardware shutdown operations should take place in the driver's EvtDeviceD0Exit callback function.

The ACX framework always calls the driver's EvtAcxCircuitReleaseHardware callback function if the driver's EvtAcxCircuitPrepareHardware callback function has been called, unless the EvtAcxCircuitPrepareHardware returned a failure code.

For more information about hardware resources, see [Introduction to Hardware Resources](/windows-hardware/drivers/wdf/introduction-to-hardware-resources).

### EvtAcxFactoryCircuitReleaseHardware (EVT_ACX_FACTORY_CIRCUIT_RELEASE_HARDWARE) callback function

When the framework calls the [EvtAcxFactoryCircuitReleaseHardware](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_factory_circuit_release_hardware) the PDO for the device still exists and can be queried for device information that is available in the powered off state, for example PCI configuration state.

In addition, the translated hardware resources that the framework supplies to EvtDeviceReleaseHardware are still assigned to the device. The primary purpose of this callback function is to release those resources, and in particular to un-map any memory resources that the driver's EvtAcxCircuitPrepareHardware callback function mapped. The driver can also use this callback to perform any other ACXCIRCUIT management activity that might be required in the powered down state. Usually, all other hardware shutdown operations should take place in the driver's EvtDeviceD0Exit callback function.

The ACX framework always calls the driver's EvtAcxFactoryCircuitReleaseHardware callback function if the driver's EvtAcxFactoryCircuitPrepareHardware callback function has been called, unless the EvtAcxFactoryCircuitPrepareHardware returned a failure code.

For more information on managing WDF and circuit objects, see [ACX WDF Driver Lifetime Management](acx-wdf-driver-lifetime-management.md).

## See also

[ACX audio class extensions overview](acx-audio-class-extensions-overview.md)

[ACX multi stack cross driver communications](acx-multi-stack.md)

[ACX WDF Driver Lifetime Management](acx-wdf-driver-lifetime-management.md)

[Summary of ACX Objects](acx-summary-of-objects.md)
