---
Description: Audio Property Handlers
MS-HAID: 'audio.audio\_property\_handlers'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Audio Property Handlers
---

# Audio Property Handlers


## <span id="audio_property_handlers"></span><span id="AUDIO_PROPERTY_HANDLERS"></span>


A miniport driver stores information about each property that it supports in a [**PCPROPERTY\_ITEM**](audio.pcproperty_item) structure. This structure contains the following information about the property:

-   The property-set GUID and property ID (or index)

-   A function pointer to the handler routine for the property

-   Flags specifying the property operations that the handler supports

The miniport driver provides an automation table (specified by a [**PCAUTOMATION\_TABLE**](audio.pcautomation_table) structure) for the filter. The driver provides additional automation tables for the filter's pin types and node types - each pin or node type has its own table. Each automation table contains a (possibly empty) array of PCPROPERTY\_ITEM structures, and each of these structures describes one property of the filter, pin, or node. When a client sends a property request to a filter, pin, or node, the port driver routes the request through the automation table to the appropriate property handler.

A miniport driver can specify a unique property handler routine for each property. However, if a driver handles several similar properties, these can sometimes be consolidated into a single handler routine for convenience. Whether to provide a unique handler for each property or to consolidate several properties into a single handler is an implementation decision to be made by the driver writer and should be transparent to clients that submit property requests.

A user-mode client can send a get, set, or basic-support property request by calling the Microsoft Win32 function [**DeviceIoControl**](base.deviceiocontrol) with the *dwIoControlCode* call parameter set to IOCTL\_KS\_PROPERTY. The operating system converts this call to an [**IRP**](kernel.irp), which it dispatches to the class driver. For more information, see [KS Properties](stream.ks_properties).

When a client sends a KS property request (that is, an IOCTL\_KS\_PROPERTY I/O-control IRP) to a filter handle or pin handle, the KS system driver (Ks.sys) delivers the request to the port driver for the filter object or pin object. If the miniport driver provides a handler for the property, the port driver forwards the request to the handler. Before forwarding the request, the port driver converts the information from the property request into the format specified by the [**PCPROPERTY\_REQUEST**](audio.pcproperty_request) structure. The port driver passes this structure to the miniport driver's handler.

The **MajorTarget** member of PCPROPERTY\_REQUEST points to the primary miniport driver interface for the audio device. For example, for a WavePci device, this is a pointer to the miniport driver object's [IMiniportWavePci](audio.iminiportwavepci) interface.

In the case of a KS property request sent to a filter handle, the **MinorTarget** member of PCPROPERTY\_REQUEST is **NULL**. In the case of a request sent to a pin handle, **MinorTarget** points to the stream interface for the pin. For example, for a WavePci device, this is a pointer to the stream object's [IMiniportWavePciStream](audio.iminiportwavepcistream) interface.

The **Instance** and **Value** members of PCPROPERTY\_REQUEST point to the input and output buffers, respectively, of the KS property request. (The buffers are specified by the *lpInBuffer* and *lpOutBuffer* parameters of the [**DeviceIoControl**](base.deviceiocontrol) function.) These buffers contain the property descriptor (instance data) and property value (operation data), respectively, as described in [Audio Drivers Property Sets](audio.audio_drivers_property_sets). The **Value** member points to the start of the output buffer, but the **Instance** pointer is offset from the start of the input buffer.

The input buffer begins with either a [**KSPROPERTY**](stream.ksproperty) or [**KSNODEPROPERTY**](audio.ksnodeproperty) structure. The port driver copies the information from this structure into the PCPROPERTY\_REQUEST structure's **Node**, **PropertyItem**, and **Verb** members. If any data follows the KSPROPERTY or KSNODEPROPERTY structure in the buffer, the port driver loads the **Instance** member with a pointer to this data. Otherwise, it sets **Instance** to **NULL**.

If the input buffer begins with a KSPROPERTY structure, which contains no node information, the port driver sets the PCPROPERTY\_REQUEST structure's **Node** member to ULONG(-1). In this case, the port driver calls the appropriate handler from the miniport driver's automation table for the filter or pin, depending on whether the target for the property request is specified by a filter handle or pin handle. (If the table does not specify a handler for the property, the port driver handles the request instead.)

If the input buffer begins with a KSNODEPROPERTY structure, the port driver copies the node ID from this structure into the PCPROPERTY\_REQUEST structure's **Node** member and calls the appropriate handler from the miniport driver's automation table for the node. (Again, if the table does not specify a handler for the property, the port driver handles the request instead.)

The port driver checks the KSPROPERTY\_TYPE\_TOPOLOGY bit in the operation flags of the property request to determine which of the two structures, KSPROPERTY or KSNODEPROPERTY, resides at the beginning of the input buffer:

-   If this bit is set, the request is for a node property, and the input buffer begins with a KSNODEPROPERTY structure.

-   Otherwise, the input buffer begins with a KSPROPERTY structure.

For more information about KSPROPERTY\_TYPE\_TOPOLOGY, see [**KSPROPERTY**](stream.ksproperty).

The PCPROPERTY\_REQUEST structure's **InstanceSize** and **ValueSize** members specify the sizes of the buffers pointed to by the **Instance** and **Value** members. **ValueSize** is equal to the size of the output buffer of the property request, but **InstanceSize** is the size of the data that follows the KSPROPERTY or KSNODEPROPERTY structure in the input buffer. That is, **InstanceSize** is the size of the input buffer minus the size of the KSPROPERTY or KSNODEPROPERTY structure. If no additional data follows this structure, the port driver sets **InstanceSize** to zero (and **Instance** to **NULL**).

For example, if the client specifies a [**KSNODEPROPERTY\_AUDIO\_CHANNEL**](audio.ksnodeproperty_audio_channel) structure as the instance data in the input buffer, the port driver passes the handler a PCPROPERTY\_REQUEST structure whose **Instance** member points to the KSNODEPROPERTY\_AUDIO\_CHANNEL structure's **Channel** member, and whose **InstanceSize** member contains the value

**sizeof**(KSNODEPROPERTY\_AUDIO\_CHANNEL) - **sizeof**(KSNODEPROPERTY)

Before submitting a get-property request to retrieve a property value, the client should allocate an output buffer into which the miniport driver's property handler can write the property value. For some properties, the size of the output buffer is device-dependent and the client must query the property handler for the required buffer size. In these cases, the client submits an initial property request with a zero-length output buffer. The handler responds by returning the required buffer size along with the status code STATUS\_BUFFER\_OVERFLOW. (The handler writes the required size into the **ValueSize** member of the PCPROPERTY\_REQUEST structure.) The client then retrieves the property value by allocating an output buffer of the specified size and sending this buffer in a second get-property request.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Property%20Handlers%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



