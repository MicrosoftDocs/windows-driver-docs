---
title: SerCx2 Object Handles
author: windows-driver-content
description: This topic describes object handle types that are specifically defined for version 2 of the serial framework extension (SerCx2). 
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SerCx2 Object Handles

This topic describes object handle types that are specifically defined for version 2 of the serial framework extension (SerCx2). 
The SerCx2 device driver interface (DDI) uses these handle types to refer to objects that have features and capabilities that are specific to SerCx2.

Additionally, the SerCx2 DDI uses two of the generic object handle types, WDFDEVICE and WDFREQUEST, that are defined by the Kernel-Mode Driver Framework (KMDF). 
For more information about framework handle types, see [Summary of Framework Objects](https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/summary-of-framework-objects).

This topic describes the following object handles:

* [SERCX2CUSTOMRECEIVE Object Handle](#SERCX2CUSTOMRECEIVE)
* [SERCX2CUSTOMRECEIVETRANSACTION Object Handle](#SERCX2CUSTOMRECEIVETRANSACTION)
* [SERCX2CUSTOMTRANSMIT Object Handle](#SERCX2CUSTOMTRANSMIT)
* [SERCX2CUSTOMTRANSMITTRANSACTION Object Handle](#SERCX2CUSTOMTRANSMITTRANSACTION)
* [SERCX2PIORECEIVE Object Handle](#SERCX2PIORECEIVE)
* [SERCX2PIOTRANSMIT Object Handle](#SERCX2PIOTRANSMIT)
* [SERCX2SYSTEMDMARECEIVE Object Handle](#SERCX2SYSTEMDMARECEIVE)
* [SERCX2SYSTEMDMATRANSMIT Object Handle](#SERCX2SYSTEMDMATRANSMIT)

Header: 2.0\Sercx.h

## <a href="" id="SERCX2CUSTOMRECEIVE"></a> SERCX2CUSTOMRECEIVE Object Handle
A **SERCX2CUSTOMRECEIVE** object handle is an opaque reference to a custom-receive object in version 2 of the serial framework extension (SerCx2).

The **SerCx2CustomReceiveCreate** method creates a custom-receive object. 
SerCx2 uses this object to manage I/O transactions that use a custom data-transfer mechanism to read data from the serial controller. 
This object is opaque to serial controller drivers. 
**SerCx2CustomReceiveCreate** supplies, as an output parameter, a SERCX2CUSTOMRECEIVE handle to the newly created custom-receive object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent calls to SerCx2 methods and event callback functions.

After **SerCx2CustomReceiveCreate** creates the custom-receive object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The custom-receive object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the custom-receive object by calling a method such as [WdfObjectDelete](https://msdn.microsoft.com/library/windows/hardware/ff548734).

A serial controller driver can, as an option, create a custom-receive object, but can create no more than one such object. 
The driver can create this object only under the following conditions:

* The driver previously created a PIO-receive object.
* The driver has *not* created a system-DMA-receive object.

For more information about PIO-receive objects, see [SERCX2PIORECEIVE Object Handle](#SERCX2PIORECEIVE). 
For more information about system-DMA-receive objects, see [SERCX2SYSTEMDMARECEIVE Object Handle](#SERCX2SYSTEMDMARECEIVE).


## <a href="" id="SERCX2CUSTOMRECEIVETRANSACTION"></a> SERCX2CUSTOMRECEIVETRANSACTION Object Handle
A **SERCX2CUSTOMRECEIVETRANSACTION** object handle is an opaque reference to a custom-receive-transaction object in version 2 of the serial framework extension (SerCx2).

The [SerCx2CustomReceiveTransactionCreate](https://msdn.microsoft.com/library/windows/hardware/dn265251) method creates a custom-receive-transaction object. 
SerCx2 uses this object to manage I/O transactions that use a custom data-transfer mechanism to read data received by the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2CustomReceiveTransactionCreate](https://msdn.microsoft.com/library/windows/hardware/dn265251) supplies, as an output parameter, a SERCX2CUSTOMRECEIVETRANSACTION handle to the newly created custom-receive-transaction object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent custom-receive transactions. 
For more information, see [SerCx2 Custom-Receive Transactions](https://docs.microsoft.com/en-us/windows-hardware/drivers/serports/sercx2-custom-receive-transactions).

After [SerCx2CustomReceiveTransactionCreate](https://msdn.microsoft.com/library/windows/hardware/dn265251) creates the custom-receive-transaction object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The custom-receive-transaction object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the custom-receive-transaction object by calling a method such as [WdfObjectDelete](https://msdn.microsoft.com/library/windows/hardware/ff548734).

A serial controller driver can, as an option, create a custom-receive-transaction object, but can create no more than one such object. 
The driver can create this object only under the following conditions:</wdcml:p>

* The driver previously created a PIO-receive object.
* The driver previously created a custom-receive object.

For more information about PIO-receive objects, see [SERCX2PIORECEIVE Object Handle](#SERCX2PIORECEIVE). 
For more information about custom-receive objects, see [SERCX2CUSTOMRECEIVE Object Handle](#SERCX2CUSTOMRECEIVE).

Despite the similar lifetimes of custom-receive and custom-receive-transaction objects, these are defined as separate object types (and not combined into one type) to support the possible future expansion of the SerCx2 device driver interface.

## <a href="" id="SERCX2CUSTOMTRANSMIT"></a> SERCX2CUSTOMTRANSMIT Object Handle
A SERCX2CUSTOMTRANSMIT object handle is an opaque reference to a custom-transmit object in version 2 of the serial framework extension (SerCx2).

The [SerCx2CustomTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265256) method creates a custom-transmit object.h SerCx2 uses this object to manage I/O transactions that write data to the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2CustomTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265256) supplies, as an output parameter, a SERCX2CUSTOMTRANSMIT handle to the newly created custom-transmit object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent calls to SerCx2 methods and event callback functions.

After [SerCx2CustomTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265256) creates the custom-transmit object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The custom-transmit object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the custom-transmit object by calling a method such as [WdfObjectDelete](https://msdn.microsoft.com/library/windows/hardware/ff548734).

A serial controller driver can, as an option, create a custom-transmit object, but can create no more than one such object. 
The driver can create this object only under the following conditions:

* The driver previously created a PIO-transmit object.
* The driver has _not_ created a system-DMA-transmit object.

For more information about PIO-transmit objects, see [SERCX2PIOTRANSMIT Object Handle](#SERCX2PIOTRANSMIT). 
For more information about system-DMA-transmit objects, see [SERCX2SYSTEMDMATRANSMIT Object Handle](#SERCX2SYSTEMDMATRANSMIT).

## <a href="" id="SERCX2CUSTOMTRANSMITTRANSACTION"></a> SERCX2CUSTOMTRANSMITTRANSACTION Object Handle
A SERCX2CUSTOMTRANSMITTRANSACTION object handle is an opaque reference to a custom-transmit-transaction object in version 2 of the serial framework extension (SerCx2).

The [SerCx2CustomTransmitTransactionCreate](https://msdn.microsoft.com/library/windows/hardware/dn265259) method creates a custom-transmit-transaction object. 
SerCx2 uses this object to manage I/O transactions that use a custom data-transfer mechanism to write data to the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2CustomTransmitTransactionCreate](https://msdn.microsoft.com/library/windows/hardware/dn265259) supplies, as an output parameter, a SERCX2CUSTOMTRANSMITTRANSACTION handle to the newly created custom-transmit-transaction object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent custom-transmit transactions. 
For more information, see [SerCx2 Custom-Transmit Transactions](https://msdn.microsoft.com/en-us/library/windows/hardware/dn265320).

After [SerCx2CustomTransmitTransactionCreate](https://msdn.microsoft.com/library/windows/hardware/dn265259) creates the custom-transmit-transaction object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The custom-transmit-transaction object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the custom-transmit-transaction object by calling a method such as [WdfObjectDelete](https://msdn.microsoft.com/library/windows/hardware/ff548734).

A serial controller driver can, as an option, create a custom-transmit object, but can create no more than one such object. 
The driver can create this object only under the following conditions:

* The driver previously created a PIO-transmit object.
* The driver has _not_ created a system-DMA-transmit object.

For more information about PIO-transmit objects, see [SERCX2PIOTRANSMIT Object Handle](#SERCX2PIOTRANSMIT). 
For more information about custom-transmit objects, see [SERCX2CUSTOMTRANSMIT Object Handle](#SERCX2CUSTOMTRANSMIT).

Despite the similar lifetimes of custom-transmit and custom-transmit-transaction objects, these are defined as separate object types (and not combined into one type) to support the possible future expansion of the SerCx2 device driver interface.

## <a href="" id="SERCX2PIORECEIVE"></a> SERCX2PIORECEIVE Object Handle
A SERCX2PIORECEIVE object handle is an opaque reference to a PIO-receive object in version 2 of the serial framework extension (SerCx2).

The [SerCx2PioReceiveCreate](https://msdn.microsoft.com/en-us/library/windows/hardware/dn265264) method creates a PIO-receive object. 
SerCx2 uses object to manage programmed I/O (PIO) transactions that read data from the serial controller. 
This object is opaque to serial controller drivers. 
 supplies, as an output parameter, a SERCX2PIORECEIVE handle to the newly created PIO-receive object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent PIO-receive transactions. 

For more information, see [SerCx2 PIO-Receive Transactions](https://msdn.microsoft.com/en-us/library/windows/hardware/dn265332).
After [SerCx2PioReceiveCreate](https://msdn.microsoft.com/en-us/library/windows/hardware/dn265264) creates the PIO-receive object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The PIO-receive object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the PIO-receive object by calling a method such as [WdfObjectDelete](https://msdn.microsoft.com/library/windows/hardware/ff548734).

A serial controller driver must create one and only one PIO-receive object. 
The driver must create this object before creating either a system-DMA-receive object or a custom-receive object. 
For more information about system-DMA-receive objects, see [SERCX2SYSTEMDMARECEIVE Object Handle](#SERCX2SYSTEMDMARECEIVE). 
For more information about custom-receive objects, see [SERCX2CUSTOMRECEIVE Object Handle](#SERCX2CUSTOMRECEIVE).

## <a href="" id="SERCX2PIOTRANSMIT"></a> SERCX2PIOTRANSMIT Object Handle
A SERCX2PIOTRANSMIT object handle is an opaque reference to a PIO-transmit object in version 2 of the serial framework extension (SerCx2).

The [SerCx2PioTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265269) method creates a PIO-transmit object. 
SerCx2 uses this object to manage I/O transactions that use programmed I/O (PIO) to write data to the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2PioTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265269) supplies, as an output parameter, a SERCX2PIOTRANSMIT handle to the newly created PIO-transmit object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent PIO-transmit transactions. 
For more information, see [SerCx2 PIO-Transmit Transactions](https://msdn.microsoft.com/library/windows/hardware/dn265336).


After [SerCx2PioTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265269) creates the PIO-transmit object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The PIO-transmit object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the PIO-transmit object by calling a method such as [WdfObjectDelete](https://msdn.microsoft.com/library/windows/hardware/ff548734).

A serial controller driver must create one and only one PIO-transmit object. 
The driver must create this object before creating either a system-DMA-transmit object or a custom-transmit object. 
For more information about system-DMA-transmit objects, see [SERCX2SYSTEMDMATRANSMIT Object Handle](#SERCX2SYSTEMDMATRANSMIT). 
For more information about custom-transmit objects, see [SERCX2CUSTOMTRANSMIT Object Handle](#SERCX2CUSTOMTRANSMIT).

## <a href="" id="SERCX2SYSTEMDMARECEIVE"></a> SERCX2SYSTEMDMARECEIVE Object Handle
A SERCX2SYSTEMDMARECEIVE object handle is an opaque reference to a system-DMA-receive object in version 2 of the serial framework extension (SerCx2).

The [SerCx2SystemDmaReceiveCreate] (https://msdn.microsoft.com/library/windows/hardware/dn265279) method creates a system-DMA-receive object. 
SerCx2 uses this object to manage system DMA transactions that read data from the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2SystemDmaReceiveCreate] (https://msdn.microsoft.com/library/windows/hardware/dn265279) supplies, as an output parameter, a SERCX2SYSTEMDMARECEIVE handle to the newly created system-DMA-receive object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent system-DMA-receive transactions. 
For more information, see [SerCx2 System-DMA-Receive Transactions](https://msdn.microsoft.com/library/windows/hardware/dn265343).

After [SerCx2SystemDmaReceiveCreate](https://msdn.microsoft.com/library/windows/hardware/dn265279) creates the system-DMA-receive object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The system-DMA-receive object is automatically deleted when the device object is deleted. 
A serial controller driver can, as an option, create a system-DMA-receive object, but can create no more than one such object. 
The driver can create this object only under the following conditions:

* The driver previously created a PIO-receive object.
* The driver has _not_ created a custom-receive object.

For more information about PIO-receive objects, see [SERCX2PIORECEIVE Object Handle](#SERCX2PIORECEIVE). 
For more information about custom-receive objects, see [SERCX2CUSTOMRECEIVE Object Handle](#SERCX2CUSTOMRECEIVE).

## <a href="" id="SERCX2SYSTEMDMATRANSMIT"></a> SERCX2SYSTEMDMATRANSMIT Object Handle
A SERCX2SYSTEMDMATRANSMIT object handle is an opaque reference to a system-DMA-transmit object in version 2 of the serial framework extension (SerCx2).

The [SerCx2SystemDmaTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265288) method creates a system-DMA-transmit object. 
SerCx2 uses this object to manage system DMA transactions that write data to the serial controller. 
This object is opaque to serial controller drivers. 
[SerCx2SystemDmaTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265288) supplies, as an output parameter, a SERCX2SYSTEMDMATRANSMIT handle to the newly created system-DMA-transmit object. 
SerCx2 and the serial controller driver use this handle to refer to the object in subsequent system-DMA-transmit transactions. 
For more information, see [SerCx2 System-DMA-Transmit Transactions](https://msdn.microsoft.com/en-us/library/windows/hardware/dn265338).

After [SerCx2SystemDmaTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265288) creates the system-DMA-transmit object, this object exists for the lifetime of the framework device object that represents the serial controller device. 
The system-DMA-transmit object is automatically deleted when the device object is deleted. 
The serial controller driver must _not_ try to delete the system-DMA-transmit object by calling a method such as [WdfObjectDelete](https://msdn.microsoft.com/library/windows/hardware/ff548734).

A serial controller driver can, as an option, create a system-DMA-transmit object, but can create no more than one such object. 
The driver can create this object only under the following conditions:</wdcml:p>

* The driver previously created a PIO-transmit object.
* The driver has _not_ created a custom-transmit object.

For more information about PIO-transmit objects, see [SERCX2PIOTRANSMIT Object Handle](#SERCX2PIOTRANSMIT). 
For more information about custom-transmit objects, see [SERCX2CUSTOMTRANSMIT Object Handle](#SERCX2CUSTOMTRANSMIT).

## Related topics

[SerCx2 Custom-Receive Transactions](https://docs.microsoft.com/en-us/windows-hardware/drivers/serports/sercx2-custom-receive-transactions)

[SerCx2 Custom-Transmit Transactions](https://msdn.microsoft.com/en-us/library/windows/hardware/dn265320)

[SerCx2 PIO-Receive Transactions](https://msdn.microsoft.com/en-us/library/windows/hardware/dn265332)

[SerCx2 PIO-Transmit Transactions](https://msdn.microsoft.com/library/windows/hardware/dn265336)

[SerCx2 System-DMA-Receive Transactions](https://msdn.microsoft.com/library/windows/hardware/dn265343)

[SerCx2 System-DMA-Transmit Transactions](https://msdn.microsoft.com/en-us/library/windows/hardware/dn265338)

[SerCx2CustomReceiveTransactionCreate](https://msdn.microsoft.com/library/windows/hardware/dn265251)

[SerCx2CustomTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265256)

[SerCx2CustomTransmitTransactionCreate](https://msdn.microsoft.com/library/windows/hardware/dn265259)

[SerCx2PioReceiveCreate](https://msdn.microsoft.com/en-us/library/windows/hardware/dn265264)

[SerCx2PioReceiveCreate](https://msdn.microsoft.com/en-us/library/windows/hardware/dn265264)

[SerCx2PioTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265269)

[SerCx2SystemDmaReceiveCreate](https://msdn.microsoft.com/library/windows/hardware/dn265279)

[SerCx2SystemDmaTransmitCreate](https://msdn.microsoft.com/library/windows/hardware/dn265288)

[Summary of Framework Objects](https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/summary-of-framework-objects)

[WdfObjectDelete](https://msdn.microsoft.com/library/windows/hardware/ff548734)



--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20SerCx2%20Object%20Handles%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


