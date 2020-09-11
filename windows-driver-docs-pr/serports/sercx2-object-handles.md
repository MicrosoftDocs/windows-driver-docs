---
title: SerCx2 Object Handles
description: This topic describes object handle types that are specifically defined for version 2 of the serial framework extension (SerCx2). 
ms.localizationpriority: medium
ms.date: 12/27/2018
---

# SerCx2 Object Handles

This topic describes object handle types that are specifically defined for version 2 of the serial framework extension (SerCx2). 
The SerCx2 device driver interface (DDI) uses these handle types to refer to objects that have features and capabilities that are specific to SerCx2.

Additionally, the SerCx2 DDI uses two of the generic object handle types, WDFDEVICE and WDFREQUEST, that are defined by the Kernel-Mode Driver Framework (KMDF). 
For more information about framework handle types, see [Summary of Framework Objects](../wdf/summary-of-framework-objects.md).

This topic describes the following object handles:

* [SERCX2CUSTOMRECEIVE Object Handle](#sercx2customreceive-object-handle)
* [SERCX2CUSTOMRECEIVETRANSACTION Object Handle](#sercx2customreceivetransaction-object-handle)
* [SERCX2CUSTOMTRANSMIT Object Handle](#sercx2customtransmit-object-handle)
* [SERCX2CUSTOMTRANSMITTRANSACTION Object Handle](#sercx2customtransmittransaction-object-handle)
* [SERCX2PIORECEIVE Object Handle](#sercx2pioreceive-object-handle)
* [SERCX2PIOTRANSMIT Object Handle](#sercx2piotransmit-object-handle)
* [SERCX2SYSTEMDMARECEIVE Object Handle](#sercx2systemdmareceive-object-handle)
* [SERCX2SYSTEMDMATRANSMIT Object Handle](#sercx2systemdmatransmit-object-handle)

Header: 2.0\Sercx.h

##  SERCX2CUSTOMRECEIVE Object Handle
A **SERCX2CUSTOMRECEIVE** object handle is an opaque reference to a custom-receive object in version 2 of the serial framework extension (SerCx2).

The **SerCx2CustomReceiveCreate** method creates a custom-receive object. 
SerCx2 uses this object to manage I/O transactions that use a custom data-transfer mechanism to read data from the serial controller. 
This object is opaque to serial controller drivers. 
**SerCx2CustomReceiveCreate** supplies, as an output parameter, a SERCX2CUSTOMRECEIVE handle to the newly created custom-receive object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent calls to SerCx2 methods and event callback functions.

After **SerCx2CustomReceiveCreate** creates the custom-receive object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The custom-receive object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the custom-receive object by calling a method such as [WdfObjectDelete](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

A serial controller driver can, as an option, create a custom-receive object, but can create no more than one such object. 
The driver can create this object only under the following conditions:

* The driver previously created a PIO-receive object.
* The driver has *not* created a system-DMA-receive object.

For more information about PIO-receive objects, see [SERCX2PIORECEIVE Object Handle](#sercx2pioreceive-object-handle). 
For more information about system-DMA-receive objects, see [SERCX2SYSTEMDMARECEIVE Object Handle](#sercx2systemdmareceive-object-handle).


##  SERCX2CUSTOMRECEIVETRANSACTION Object Handle
A **SERCX2CUSTOMRECEIVETRANSACTION** object handle is an opaque reference to a custom-receive-transaction object in version 2 of the serial framework extension (SerCx2).

The [SerCx2CustomReceiveTransactionCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactioncreate) method creates a custom-receive-transaction object. 
SerCx2 uses this object to manage I/O transactions that use a custom data-transfer mechanism to read data received by the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2CustomReceiveTransactionCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactioncreate) supplies, as an output parameter, a SERCX2CUSTOMRECEIVETRANSACTION handle to the newly created custom-receive-transaction object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent custom-receive transactions. 
For more information, see [SerCx2 Custom-Receive Transactions](./sercx2-custom-receive-transactions.md).

After [SerCx2CustomReceiveTransactionCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactioncreate) creates the custom-receive-transaction object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The custom-receive-transaction object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the custom-receive-transaction object by calling a method such as [WdfObjectDelete](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

A serial controller driver can, as an option, create a custom-receive-transaction object, but can create no more than one such object. 
The driver can create this object only under the following conditions:</wdcml:p>

* The driver previously created a PIO-receive object.
* The driver previously created a custom-receive object.

For more information about PIO-receive objects, see [SERCX2PIORECEIVE Object Handle](#sercx2pioreceive-object-handle). 
For more information about custom-receive objects, see [SERCX2CUSTOMRECEIVE Object Handle](#sercx2customreceive-object-handle).

Despite the similar lifetimes of custom-receive and custom-receive-transaction objects, these are defined as separate object types (and not combined into one type) to support the possible future expansion of the SerCx2 device driver interface.

##  SERCX2CUSTOMTRANSMIT Object Handle
A SERCX2CUSTOMTRANSMIT object handle is an opaque reference to a custom-transmit object in version 2 of the serial framework extension (SerCx2).

The [SerCx2CustomTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmitcreate) method creates a custom-transmit object.h SerCx2 uses this object to manage I/O transactions that write data to the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2CustomTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmitcreate) supplies, as an output parameter, a SERCX2CUSTOMTRANSMIT handle to the newly created custom-transmit object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent calls to SerCx2 methods and event callback functions.

After [SerCx2CustomTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmitcreate) creates the custom-transmit object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The custom-transmit object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the custom-transmit object by calling a method such as [WdfObjectDelete](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

A serial controller driver can, as an option, create a custom-transmit object, but can create no more than one such object. 
The driver can create this object only under the following conditions:

* The driver previously created a PIO-transmit object.
* The driver has _not_ created a system-DMA-transmit object.

For more information about PIO-transmit objects, see [SERCX2PIOTRANSMIT Object Handle](#sercx2piotransmit-object-handle). 
For more information about system-DMA-transmit objects, see [SERCX2SYSTEMDMATRANSMIT Object Handle](#sercx2systemdmatransmit-object-handle).

##  SERCX2CUSTOMTRANSMITTRANSACTION Object Handle
A SERCX2CUSTOMTRANSMITTRANSACTION object handle is an opaque reference to a custom-transmit-transaction object in version 2 of the serial framework extension (SerCx2).

The [SerCx2CustomTransmitTransactionCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmittransactioncreate) method creates a custom-transmit-transaction object. 
SerCx2 uses this object to manage I/O transactions that use a custom data-transfer mechanism to write data to the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2CustomTransmitTransactionCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmittransactioncreate) supplies, as an output parameter, a SERCX2CUSTOMTRANSMITTRANSACTION handle to the newly created custom-transmit-transaction object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent custom-transmit transactions. 
For more information, see [SerCx2 Custom-Transmit Transactions](/previous-versions/dn265320(v=vs.85)).

After [SerCx2CustomTransmitTransactionCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmittransactioncreate) creates the custom-transmit-transaction object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The custom-transmit-transaction object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the custom-transmit-transaction object by calling a method such as [WdfObjectDelete](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

A serial controller driver can, as an option, create a custom-transmit object, but can create no more than one such object. 
The driver can create this object only under the following conditions:

* The driver previously created a PIO-transmit object.
* The driver has _not_ created a system-DMA-transmit object.

For more information about PIO-transmit objects, see [SERCX2PIOTRANSMIT Object Handle](#sercx2piotransmit-object-handle). 
For more information about custom-transmit objects, see [SERCX2CUSTOMTRANSMIT Object Handle](#sercx2customtransmit-object-handle).

Despite the similar lifetimes of custom-transmit and custom-transmit-transaction objects, these are defined as separate object types (and not combined into one type) to support the possible future expansion of the SerCx2 device driver interface.

##  SERCX2PIORECEIVE Object Handle
A SERCX2PIORECEIVE object handle is an opaque reference to a PIO-receive object in version 2 of the serial framework extension (SerCx2).

The [SerCx2PioReceiveCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceivecreate) method creates a PIO-receive object. 
SerCx2 uses object to manage programmed I/O (PIO) transactions that read data from the serial controller. 
This object is opaque to serial controller drivers. 
 supplies, as an output parameter, a SERCX2PIORECEIVE handle to the newly created PIO-receive object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent PIO-receive transactions. 

For more information, see [SerCx2 PIO-Receive Transactions](/previous-versions/dn265332(v=vs.85)).
After [SerCx2PioReceiveCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceivecreate) creates the PIO-receive object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The PIO-receive object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the PIO-receive object by calling a method such as [WdfObjectDelete](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

A serial controller driver must create one and only one PIO-receive object. 
The driver must create this object before creating either a system-DMA-receive object or a custom-receive object. 
For more information about system-DMA-receive objects, see [SERCX2SYSTEMDMARECEIVE Object Handle](#sercx2systemdmareceive-object-handle). 
For more information about custom-receive objects, see [SERCX2CUSTOMRECEIVE Object Handle](#sercx2customreceive-object-handle).

##  SERCX2PIOTRANSMIT Object Handle
A SERCX2PIOTRANSMIT object handle is an opaque reference to a PIO-transmit object in version 2 of the serial framework extension (SerCx2).

The [SerCx2PioTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitcreate) method creates a PIO-transmit object. 
SerCx2 uses this object to manage I/O transactions that use programmed I/O (PIO) to write data to the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2PioTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitcreate) supplies, as an output parameter, a SERCX2PIOTRANSMIT handle to the newly created PIO-transmit object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent PIO-transmit transactions. 
For more information, see [SerCx2 PIO-Transmit Transactions](/previous-versions/dn265336(v=vs.85)).


After [SerCx2PioTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitcreate) creates the PIO-transmit object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The PIO-transmit object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the PIO-transmit object by calling a method such as [WdfObjectDelete](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

A serial controller driver must create one and only one PIO-transmit object. 
The driver must create this object before creating either a system-DMA-transmit object or a custom-transmit object. 
For more information about system-DMA-transmit objects, see [SERCX2SYSTEMDMATRANSMIT Object Handle](#sercx2systemdmatransmit-object-handle). 
For more information about custom-transmit objects, see [SERCX2CUSTOMTRANSMIT Object Handle](#sercx2customtransmit-object-handle).

##  SERCX2SYSTEMDMARECEIVE Object Handle
A SERCX2SYSTEMDMARECEIVE object handle is an opaque reference to a system-DMA-receive object in version 2 of the serial framework extension (SerCx2).

The [SerCx2SystemDmaReceiveCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivecreate) method creates a system-DMA-receive object. 
SerCx2 uses this object to manage system DMA transactions that read data from the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2SystemDmaReceiveCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivecreate) supplies, as an output parameter, a SERCX2SYSTEMDMARECEIVE handle to the newly created system-DMA-receive object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent system-DMA-receive transactions. 
For more information, see [SerCx2 System-DMA-Receive Transactions](/previous-versions/dn265343(v=vs.85)).

After [SerCx2SystemDmaReceiveCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivecreate) creates the system-DMA-receive object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The system-DMA-receive object is automatically deleted when the device object is deleted. 
A serial controller driver can, as an option, create a system-DMA-receive object, but can create no more than one such object. 
The driver can create this object only under the following conditions:

* The driver previously created a PIO-receive object.
* The driver has _not_ created a custom-receive object.

For more information about PIO-receive objects, see [SERCX2PIORECEIVE Object Handle](#sercx2pioreceive-object-handle). 
For more information about custom-receive objects, see [SERCX2CUSTOMRECEIVE Object Handle](#sercx2customreceive-object-handle).

##  SERCX2SYSTEMDMATRANSMIT Object Handle
A SERCX2SYSTEMDMATRANSMIT object handle is an opaque reference to a system-DMA-transmit object in version 2 of the serial framework extension (SerCx2).

The [SerCx2SystemDmaTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitcreate) method creates a system-DMA-transmit object. 
SerCx2 uses this object to manage system DMA transactions that write data to the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2SystemDmaTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitcreate) supplies, as an output parameter, a SERCX2SYSTEMDMATRANSMIT handle to the newly created system-DMA-transmit object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent system-DMA-transmit transactions. 
For more information, see [SerCx2 System-DMA-Transmit Transactions](/previous-versions/dn265338(v=vs.85)).

After [SerCx2SystemDmaTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitcreate) creates the system-DMA-transmit object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The system-DMA-transmit object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the system-DMA-transmit object by calling a method such as [WdfObjectDelete](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

A serial controller driver can, as an option, create a system-DMA-transmit object, but can create no more than one such object. 
The driver can create this object only under the following conditions:</wdcml:p>

* The driver previously created a PIO-transmit object.
* The driver has _not_ created a custom-transmit object.

For more information about PIO-transmit objects, see [SERCX2PIOTRANSMIT Object Handle](#sercx2piotransmit-object-handle). 
For more information about custom-transmit objects, see [SERCX2CUSTOMTRANSMIT Object Handle](#sercx2customtransmit-object-handle).

## Related topics

[SerCx2 Custom-Receive Transactions](./sercx2-custom-receive-transactions.md)

[SerCx2 Custom-Transmit Transactions](/previous-versions/dn265320(v=vs.85))

[SerCx2 PIO-Receive Transactions](/previous-versions/dn265332(v=vs.85))

[SerCx2 PIO-Transmit Transactions](/previous-versions/dn265336(v=vs.85))

[SerCx2 System-DMA-Receive Transactions](/previous-versions/dn265343(v=vs.85))

[SerCx2 System-DMA-Transmit Transactions](/previous-versions/dn265338(v=vs.85))

[SerCx2CustomReceiveTransactionCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customreceivetransactioncreate)

[SerCx2CustomTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmitcreate)

[SerCx2CustomTransmitTransactionCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2customtransmittransactioncreate)

[SerCx2PioReceiveCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceivecreate)

[SerCx2PioReceiveCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2pioreceivecreate)

[SerCx2PioTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2piotransmitcreate)

[SerCx2SystemDmaReceiveCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmareceivecreate)

[SerCx2SystemDmaTransmitCreate](/windows-hardware/drivers/ddi/sercx/nf-sercx-sercx2systemdmatransmitcreate)

[Summary of Framework Objects](../wdf/summary-of-framework-objects.md)

[WdfObjectDelete](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete)