---
Description: IMXF Interfaces
MS-HAID: 'audio.imxf\_interfaces'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: IMXF Interfaces
---

# IMXF Interfaces


## <span id="imxf_interfaces"></span><span id="IMXF_INTERFACES"></span>


All MIDI transport in the DirectMusic port and miniport driver is carried out using the same interface: [IMXF](audio.imxf).

**IMXF** is the COM interface for a DirectMusic MIDI transform filter. The miniport driver, the sequencer, and other entities in the port driver that handle MIDI data use **IMXF** as their common COM interface. When the miniport driver implements this interface, it can participate in MIDI transport. [IPortDMus](audio.iportdmus), which resides in PortCls, manages **IMXF**. The interface from the capture device to capture sink is also an **IMXF** interface.

MIDI data is transported between user mode and kernel mode in buffers of packed time-stamped data. The kernel port driver breaks these buffers into individual events (see [**DMUS\_KERNEL\_EVENT**](audio.dmus_kernel_event)). The high-resolution MIDI sequencer passes these events to the miniport driver when the trigger time occurs.

On the input side, the kernel port driver extracts individual input messages from the miniport driver and builds packed buffers to pass up to user mode. Accordingly, the data transport model for DirectMusic miniport drivers consists of [**IMXF::PutMessage**](audio.imxf_putmessage) and [**IAllocatorMXF::GetMessage**](audio.iallocatormxf_getmessage).

The **IMXF** interface supports the following methods:

[**IMXF::ConnectOutput**](audio.imxf_connectoutput)

[**IMXF::DisconnectOutput**](audio.imxf_disconnectoutput)

[**IMXF::PutMessage**](audio.imxf_putmessage)

[**IMXF::SetState**](audio.imxf_setstate)

The [IAllocatorMXF](audio.iallocatormxf) interface extends **IMXF** by adding the following methods:

[**IAllocatorMXF::GetMessage**](audio.iallocatormxf_getmessage)

[**IAllocatorMXF::GetBufferSize**](audio.iallocatormxf_getbuffersize)

[**IAllocatorMXF::GetBuffer**](audio.iallocatormxf_getbuffer)

[**IAllocatorMXF::PutBuffer**](audio.iallocatormxf_putbuffer)

For more information about the use of these interfaces, see [Allocator](allocator.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20IMXF%20Interfaces%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


