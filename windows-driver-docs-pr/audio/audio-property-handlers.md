---
title: Audio Property Handlers
description: Audio Property Handlers
ms.assetid: 4bf176ae-b3fd-47e6-9802-a92ef5e9904f
keywords:
- audio properties WDK , handlers
- WDM audio properties WDK , handlers
- handlers WDK audio
- property handlers WDK audio
- set-property WDK audio
- get-property WDK audio
- basic-support queries WDK audio
- automation tables WDK audio
- filters WDK audio , property handlers
- pins WDK audio , property handlers
- nodes WDK audio , property handlers
ms.date: 08/07/2018
ms.localizationpriority: medium
---

# Audio Property Handlers


## <span id="audio_property_handlers"></span><span id="AUDIO_PROPERTY_HANDLERS"></span>


A miniport driver stores information about each property that it supports in a [**PCPROPERTY\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff537722) structure. This structure contains the following information about the property:

-   The property-set GUID and property ID (or index)

-   A function pointer to the handler routine for the property

-   Flags specifying the property operations that the handler supports

The miniport driver provides an automation table (specified by a [**PCAUTOMATION\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff537685) structure) for the filter. The driver provides additional automation tables for the filter's pin types and node types - each pin or node type has its own table. Each automation table contains a (possibly empty) array of PCPROPERTY\_ITEM structures, and each of these structures describes one property of the filter, pin, or node. When a client sends a property request to a filter, pin, or node, the port driver routes the request through the automation table to the appropriate property handler.

A miniport driver can specify a unique property handler routine for each property. However, if a driver handles several similar properties, these can sometimes be consolidated into a single handler routine for convenience. Whether to provide a unique handler for each property or to consolidate several properties into a single handler is an implementation decision to be made by the driver writer and should be transparent to clients that submit property requests.

A user-mode client can send a get, set, or basic-support property request by calling the Microsoft Win32 function [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) with the *dwIoControlCode* call parameter set to IOCTL\_KS\_PROPERTY. The operating system converts this call to an [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694), which it dispatches to the class driver. For more information, see [KS Properties](https://msdn.microsoft.com/library/windows/hardware/ff567671).

When a client sends a KS property request (that is, an IOCTL\_KS\_PROPERTY I/O-control IRP) to a filter handle or pin handle, the KS system driver (Ks.sys) delivers the request to the port driver for the filter object or pin object. If the miniport driver provides a handler for the property, the port driver forwards the request to the handler. Before forwarding the request, the port driver converts the information from the property request into the format specified by the [**PCPROPERTY\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537723) structure. The port driver passes this structure to the miniport driver's handler.

The **MajorTarget** member of PCPROPERTY\_REQUEST points to the primary miniport driver interface for the audio device. For example, for a WavePci device, this is a pointer to the miniport driver object's [IMiniportWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536724) interface.

In the case of a KS property request sent to a filter handle, the **MinorTarget** member of PCPROPERTY\_REQUEST is **NULL**. In the case of a request sent to a pin handle, **MinorTarget** points to the stream interface for the pin. For example, for a WavePci device, this is a pointer to the stream object's [IMiniportWavePciStream](https://msdn.microsoft.com/library/windows/hardware/ff536725) interface.

The **Instance** and **Value** members of PCPROPERTY\_REQUEST point to the input and output buffers, respectively, of the KS property request. (The buffers are specified by the *lpInBuffer* and *lpOutBuffer* parameters of the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function.) These buffers contain the property descriptor (instance data) and property value (operation data), respectively, as described in [Audio Drivers Property Sets](https://msdn.microsoft.com/library/windows/hardware/ff536197). The **Value** member points to the start of the output buffer, but the **Instance** pointer is offset from the start of the input buffer.

The input buffer begins with either a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) or [**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143) structure. The port driver copies the information from this structure into the PCPROPERTY\_REQUEST structure's **Node**, **PropertyItem**, and **Verb** members. If any data follows the KSPROPERTY or KSNODEPROPERTY structure in the buffer, the port driver loads the **Instance** member with a pointer to this data. Otherwise, it sets **Instance** to **NULL**.

If the input buffer begins with a KSPROPERTY structure, which contains no node information, the port driver sets the PCPROPERTY\_REQUEST structure's **Node** member to ULONG(-1). In this case, the port driver calls the appropriate handler from the miniport driver's automation table for the filter or pin, depending on whether the target for the property request is specified by a filter handle or pin handle. (If the table does not specify a handler for the property, the port driver handles the request instead.)

If the input buffer begins with a KSNODEPROPERTY structure, the port driver copies the node ID from this structure into the PCPROPERTY\_REQUEST structure's **Node** member and calls the appropriate handler from the miniport driver's automation table for the node. (Again, if the table does not specify a handler for the property, the port driver handles the request instead.)

The port driver checks the KSPROPERTY\_TYPE\_TOPOLOGY bit in the operation flags of the property request to determine which of the two structures, KSPROPERTY or KSNODEPROPERTY, resides at the beginning of the input buffer:

-   If this bit is set, the request is for a node property, and the input buffer begins with a KSNODEPROPERTY structure.

-   Otherwise, the input buffer begins with a KSPROPERTY structure.

For more information about KSPROPERTY\_TYPE\_TOPOLOGY, see [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262).

The PCPROPERTY\_REQUEST structure's **InstanceSize** and **ValueSize** members specify the sizes of the buffers pointed to by the **Instance** and **Value** members. **ValueSize** is equal to the size of the output buffer of the property request, but **InstanceSize** is the size of the data that follows the KSPROPERTY or KSNODEPROPERTY structure in the input buffer. That is, **InstanceSize** is the size of the input buffer minus the size of the KSPROPERTY or KSNODEPROPERTY structure. If no additional data follows this structure, the port driver sets **InstanceSize** to zero (and **Instance** to **NULL**).

For example, if the client specifies a [**KSNODEPROPERTY\_AUDIO\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff537145) structure as the instance data in the input buffer, the port driver passes the handler a PCPROPERTY\_REQUEST structure whose **Instance** member points to the KSNODEPROPERTY\_AUDIO\_CHANNEL structure's **Channel** member, and whose **InstanceSize** member contains the value

**sizeof**(KSNODEPROPERTY\_AUDIO\_CHANNEL) - **sizeof**(KSNODEPROPERTY)

Before submitting a get-property request to retrieve a property value, the client should allocate an output buffer into which the miniport driver's property handler can write the property value. For some properties, the size of the output buffer is device-dependent, and the client must query the property handler for the required buffer size. In these cases, the client submits an initial property request with an output buffer pointer of nullptr and an output buffer length of zero. The handler responds by returning the required buffer size along with the status code STATUS_BUFFER_OVERFLOW. The client then retrieves the property value by allocating an output buffer of the specified size and sending this buffer in a second get-property request.
 
If the specified buffer size is too small to receive any of the requested information, the method returns STATUS_BUFFER_TOO_SMALL. 
 
In some cases, PortCls port drivers return STATUS_BUFFER_TOO_SMALL instead of STATUS_BUFFER_OVERFLOW in response to a property request with a non-zero output buffer address and size. Required buffer size is not returned in such cases. 
 
For more information, see [Using NTSTATUS Values](https://docs.microsoft.com/windows-hardware/drivers/kernel/using-ntstatus-values) and these blog posts:

- [How to return the number of bytes required for a subsequent operation](https://blogs.msdn.microsoft.com/doronh/2006/12/12/how-to-return-the-number-of-bytes-required-for-a-subsequent-operation/)

- [STATUS_BUFFER_OVERFLOW really should be named STATUS_BUFFER_OVERFLOW_PREVENTED](https://blogs.msdn.microsoft.com/oldnewthing/20080404-00/?p=22863)




 

 




