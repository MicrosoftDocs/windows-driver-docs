---
title: KS Properties
author: windows-driver-content
description: KS Properties
MS-HAID:
- 'ks-overview\_1c4153d6-c153-44da-bb5a-5dab0ea4bd5c.xml'
- 'stream.ks\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a385929e-1934-4d88-aaf9-ff1ddbfd30f7
keywords: ["kernel streaming WDK , properties", "KS properties WDK kernel streaming", "properties WDK kernel streaming"]
---

# KS Properties


## <a href="" id="ddk-ks-properties-ksg"></a>


A *Property* represents a capability or control-state setting that belongs to a kernel streaming object, such as a filter or pin. Clients of a kernel streaming minidriver can send get and set property requests (KSPROPERTY\_TYPE\_GET and KSPROPERTY\_TYPE\_SET) to the filters and pins that the minidriver has instantiated. A group of related properties is referred to as a *property set*.

To get or set individual properties, user-mode clients call the Win32 function **DeviceIoControl** with the *dwIoControlCode* parameter set to IOCTL\_KS\_PROPERTY. **DeviceIoControl** is described in the Microsoft Windows SDK documentation. Kernel-mode clients should call [**KsSynchronousDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff567142).

The input buffer is either a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure or a wrapper containing a KSPROPERTY structure and other information relevant to the request. In response to this call, the operating system dispatches an IRP to the class driver.

When the class driver receives the resulting IRP, it calls [**KsPropertyHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564263). The class driver includes as a call parameter the address of the KSPROPERTY structure that identifies the specifics of the property request. The property request is either handled automatically at the class driver level or by a minidriver-provided handler. See [Kernel Streaming Property Sets](https://msdn.microsoft.com/library/windows/hardware/ff554246) for reference information including which property sets are handled by the class driver and which require minidriver-provided handlers. A minidriver can override or augment the class driver handler by providing callbacks for a property that is by default handled by the class driver.

If the minidriver has provided handlers for this property, **KsPropertyHandler** in turn hands off the request to the appropriate minidriver-supplied callback.

A minidriver provides pointers to its property support callbacks in a structure of type [**KSPROPERTY\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff565176). A minidriver groups an array of related KSPROPERTY\_ITEM structures in a [**KSPROPERTY\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff565617) structure. Different class driver models have slightly different methods for the minidriver to make property set data available to the class driver. You can find class driver-specific information by following the links in [Kernel Streaming](kernel-streaming.md).

The minidriver also provides a pointer to a [**KSPROPERTY\_VALUES**](https://msdn.microsoft.com/library/windows/hardware/ff565966) structure in a KSPROPERTY\_ITEM structure. The KSPROPERTY\_VALUES structure in turn contains an array of [**KSPROPERTY\_MEMBERSLIST**](https://msdn.microsoft.com/library/windows/hardware/ff565190) structures. This is where the minidriver specifies the size and type of acceptable values for the property. Each KSPROPERTY\_MEMBERSLIST structure contains a header member: see [**KSPROPERTY\_MEMBERSHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff565189) For information about how to specify legal ranges or values for a property that your minidriver supports. You can also find an implementation of this mechanism in the *Testcap* sample in the Microsoft Windows Driver Kit (WDK).

To report the size and type of acceptable values for a property, the class driver returns a [**KSPROPERTY\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff565132) structure in response to a KSPROPERTY\_TYPE\_BASICSUPPORT request from the client.

The class driver may append a list of KSPROPERTY\_MEMBERSHEADER structures to the KSPROPERTY\_DESCRIPTION structure.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KS%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


