---
title: KS Properties
description: KS Properties
keywords:
- kernel streaming WDK , properties
- KS properties WDK kernel streaming
- properties WDK kernel streaming
ms.date: 04/20/2017
---

# KS Properties





A *Property* represents a capability or control-state setting that belongs to a kernel streaming object, such as a filter or pin. Clients of a kernel streaming minidriver can send get and set property requests (KSPROPERTY\_TYPE\_GET and KSPROPERTY\_TYPE\_SET) to the filters and pins that the minidriver has instantiated. A group of related properties is referred to as a *property set*.

To get or set individual properties, user-mode clients call the Win32 function **DeviceIoControl** with the *dwIoControlCode* parameter set to IOCTL\_KS\_PROPERTY. **DeviceIoControl** is described in the Microsoft Windows SDK documentation. Kernel-mode clients should call [**KsSynchronousDeviceControl**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-kssynchronousdevicecontrol).

The input buffer is either a [**KSPROPERTY**](ksproperty-structure.md) structure or a wrapper containing a KSPROPERTY structure and other information relevant to the request. In response to this call, the operating system dispatches an IRP to the class driver.

When the class driver receives the resulting IRP, it calls [**KsPropertyHandler**](/windows-hardware/drivers/ddi/ks/nf-ks-kspropertyhandler). The class driver includes as a call parameter the address of the KSPROPERTY structure that identifies the specifics of the property request. The property request is either handled automatically at the class driver level or by a minidriver-provided handler. See [Kernel Streaming Property Sets](./avstream-property-sets.md) for reference information including which property sets are handled by the class driver and which require minidriver-provided handlers. A minidriver can override or augment the class driver handler by providing callbacks for a property that is by default handled by the class driver.

If the minidriver has provided handlers for this property, **KsPropertyHandler** in turn hands off the request to the appropriate minidriver-supplied callback.

A minidriver provides pointers to its property support callbacks in a structure of type [**KSPROPERTY\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item). A minidriver groups an array of related KSPROPERTY\_ITEM structures in a [**KSPROPERTY\_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_set) structure. Different class driver models have slightly different methods for the minidriver to make property set data available to the class driver. You can find class driver-specific information by following the links in [Kernel Streaming](kernel-streaming.md).

The minidriver also provides a pointer to a [**KSPROPERTY\_VALUES**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_values) structure in a KSPROPERTY\_ITEM structure. The KSPROPERTY\_VALUES structure in turn contains an array of [**KSPROPERTY\_MEMBERSLIST**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_memberslist) structures. This is where the minidriver specifies the size and type of acceptable values for the property. Each KSPROPERTY\_MEMBERSLIST structure contains a header member: see [**KSPROPERTY\_MEMBERSHEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_membersheader) For information about how to specify legal ranges or values for a property that your minidriver supports. You can also find an implementation of this mechanism in the *Testcap* sample in the Microsoft Windows Driver Kit (WDK).

To report the size and type of acceptable values for a property, the class driver returns a [**KSPROPERTY\_DESCRIPTION**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_description) structure in response to a KSPROPERTY\_TYPE\_BASICSUPPORT request from the client.

The class driver may append a list of KSPROPERTY\_MEMBERSHEADER structures to the KSPROPERTY\_DESCRIPTION structure.

 

