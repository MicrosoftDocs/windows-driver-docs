---
title: SpbCx Object Handles
description: This topic describes object handles that are defined for the SPB framework extension (SpbCx) library.
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SpbCx Object Handles
This topic describes object handles that are defined for the SPB framework extension (SpbCx) library. 

Additionally, the SerCx2 DDI uses two of the generic object handle types, WDFDEVICE and WDFREQUEST, that are defined by the Kernel-Mode Driver Framework (KMDF). 
For more information about framework handle types, see [Summary of Framework Objects](https://docs.microsoft.com/windows-hardware/drivers/wdf/summary-of-framework-objects).

This topic describes the following object handles:

* [SPBREQUEST Object Handle](#SPBREQUEST)
* [SPBTARGET Object Handle](#SPBTARGET)

Header: Spbcx.h

##  SPBREQUEST Object Handle
An **SPBREQUEST** object handle represents an I/O request that is issued to a target device on the bus.

```cpp
DECLARE_HANDLE(SPBREQUEST)
```

The **SPBREQUEST** object class is derived from the **WDFREQUEST** object class, which represents an I/O request that is dispatched by the I/O manager. 
Thus, **WdfRequestXxx** methods that take **WDFREQUEST** handle values as parameters accept **SPBREQUEST** handle values as valid parameter values. 
For more information about these methods, see [Framework Request Objects](https://docs.microsoft.com/windows-hardware/drivers/wdf/framework-request-objects).

However, some SpbCx methods and callback functions specifically require **SPBREQUEST** handles as parameters. 
For such a parameter, substituting a **WDFREQUEST** handle that is not also an **SPBREQUEST** handle is an error.

For example, the [SpbRequestGetTransferParameters](https://msdn.microsoft.com/library/windows/hardware/hh450924) method takes an **SPBREQUEST** handle as a parameter. 
To supply, for this parameter, a **WDFREQUEST** handle that is not also an **SPBREQUEST** handle is an error. 
The reason for this requirement is that an **SPBREQUEST** object must store additional, SPB-specific state information to support [I/O transfer sequences](https://docs.microsoft.com/windows-hardware/drivers/spb/i-o-transfer-sequences). 
The **WDFREQUEST** base object class does not provide this support.

During device initialization, your SPB controller driver can assign a per-request context to an **SPBREQUEST** handle by calling the [SpbControllerSetRequestAttributes](https://msdn.microsoft.com/library/windows/hardware/hh450908) method.
  
##  SPBTARGET Object Handle
An **SPBTARGET** object handle identifies a logical connection from a client (peripheral driver) to an addressable port or peripheral device on the bus.
   
   ```cpp
   DECLARE_HANDLE(SPBTARGET)
   ```
For an I<sup>2</sup>C bus, an **SPBTARGET** handle corresponds to a specific device address.  
For an SPI bus, an **SPBTARGET** handle corresponds to a device-select line.

Typically, an **SPBTARGET** object exists from the start of the [EvtSpbTargetConnect](https://msdn.microsoft.com/library/windows/hardware/hh450818) event callback through the end of the corresponding [EvtSpbTargetDisconnect](https://msdn.microsoft.com/library/windows/hardware/hh450820) event callback. However, the lifetime of the **SPBTARGET** object might extend beyond the second callback if the SPB controller driver takes an additional reference on the **SPBTARGET** object to prevent the object from unexpectedly disappearing during the processing of an I/O request for the target.

The SPB controller driver performs all hardware-specific operations for an SPB controller device. 
When a client sends an [IRP_MJ_CREATE](https://msdn.microsoft.com/library/windows/hardware/ff548630) request to open a connection to a target on the bus, the SPB framework extension (SpbCx), which manages the I/O queue for the controller driver, passes this request to the SPB controller driver by calling this driver's [EvtSpbTargetConnect](https://msdn.microsoft.com/library/windows/hardware/hh450818) callback function. 
This _Target_ parameter of this function is an **SPBTARGET** handle. 
The function can use this handle to retrieve connection-specific resource information (for example, the device address) from the PnP manager. 
When the client sends an [IRP_MJ_CLOSE](https://msdn.microsoft.com/library/windows/hardware/ff550720) request to close the connection, SpbCx passes this request to the SPB controller driver's [EvtSpbTargetDisconnect](https://msdn.microsoft.com/library/windows/hardware/hh450820) callback function, which releases these resources.

### Exclusive-Mode Access
Clients have exclusive-mode to access target devices. Only one client can have a connection to a particular target device at a time. 
SpbCx ensures that only one **SPBTARGET** handle exists for a target device address on the bus. 
This restriction is necessary because SpbCx does not support the interleaving of I/O requests that are sent by two or more clients to a target device. 
If a target device must be able to receive requests from several clients, this device requires a MUX driver—separate from the controller driver—that can properly interleave the requested operations.

### Interoperability with KMDF
The [SerCx2 Driver Support Methods](https://msdn.microsoft.com/library/windows/hardware/dn265323) and [SpbCx Event Callback Functions](https://msdn.microsoft.com/library/windows/hardware/hh450911) that are defined by SpbCx use **SPBTARGET** handles to represent open connections to target devices on the bus. 
However, a controller driver must typically call KMDF methods that require WDFFILEOBJECT handles, instead of **SPBTARGET** handles, to designate target devices.

An **SPBTARGET** object is similar to a WDFFILEOBJECT object. However, an **SPBTARGET** object contains additional, SPB-specific information. 
For example, during the processing of an [IOCTL_SPB_EXECUTE_SEQUENCE](https://msdn.microsoft.com/library/windows/hardware/hh450857) I/O control request, the **SPBTARGET** object for the target device tracks the state of the transfers in the [I/O transfer sequence](https://docs.microsoft.com/windows-hardware/drivers/spb/i-o-transfer-sequences).

To obtain the WDFFILEOBJECT handle to a target, the SPB controller driver calls the [SpbTargetGetFileObject](https://msdn.microsoft.com/library/windows/hardware/hh450927) method. 
This method accepts, as an input parameter, an **SPBTARGET** handle to an open target device, and returns the corresponding WDFFILEOBJECT handle to this target.

In accordance with KMDF conventions, the SPB controller driver can attach its own context to the **SPBTARGET** object for a target device, and this context can include associated [EvtCleanupCallback](https://msdn.microsoft.com/library/windows/hardware/ff540840) and [EvtDestroyCallback](https://msdn.microsoft.com/library/windows/hardware/ff540841) callback functions. 
The SPB controller driver uses this context to track information that is specific to the controller driver and to the target device. 
In addition, this driver can create child objects of the **SPBTARGET** object, such as timers, DPCs, or, if needed, I/O requests and I/O queues.
 
## Related topics

[EvtCleanupCallback](https://msdn.microsoft.com/library/windows/hardware/ff540840)

[EvtDestroyCallback](https://msdn.microsoft.com/library/windows/hardware/ff540841)

[EvtSpbTargetConnect](https://msdn.microsoft.com/library/windows/hardware/hh450818)

[EvtSpbTargetDisconnect](https://msdn.microsoft.com/library/windows/hardware/hh450820)

[Framework Request Objects](https://docs.microsoft.com/windows-hardware/drivers/wdf/framework-request-objects)

[I/O transfer sequence](https://docs.microsoft.com/windows-hardware/drivers/spb/i-o-transfer-sequences)

[IOCTL_SPB_EXECUTE_SEQUENCE](https://msdn.microsoft.com/library/windows/hardware/hh450857)

[IRP_MJ_CLOSE](https://msdn.microsoft.com/library/windows/hardware/ff550720)

[IRP_MJ_CREATE](https://msdn.microsoft.com/library/windows/hardware/ff548630)

[SerCx2 Driver Support Methods](https://msdn.microsoft.com/library/windows/hardware/dn265323)

[SpbControllerSetRequestAttributes](https://msdn.microsoft.com/library/windows/hardware/hh450908)

[SpbCx Event Callback Functions](https://msdn.microsoft.com/library/windows/hardware/hh450911)

[SpbRequestGetTransferParameters](https://msdn.microsoft.com/library/windows/hardware/hh450924)

[SpbTargetGetFileObject](https://msdn.microsoft.com/library/windows/hardware/hh450927)

[Summary of Framework Objects](https://docs.microsoft.com/windows-hardware/drivers/wdf/summary-of-framework-objects)



