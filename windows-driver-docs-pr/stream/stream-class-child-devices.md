---
title: Stream Class Child Devices
author: windows-driver-content
description: Stream Class Child Devices
ms.assetid: 2885a77d-5e39-4730-b715-99f0a426f273
keywords: ["Stream.sys class driver WDK Windows 2000 Kernel , child devices", "streaming minidrivers WDK Windows 2000 Kernel , child devices", "minidrivers WDK Windows 2000 Kernel Streaming , child devices", "child devices WDK streaming minidriver"]
---

# Stream Class Child Devices


## <a href="" id="ddk-stream-class-child-devices-ksg"></a>


This section applies to Microsoft Windows Server 2003 and earlier operating systems only if DirectX 9.0 or later is installed on that platform.

If your stream class device places an **Enum** branch in the registry under its device key, stream class behaves as a bus enumerator for the device, creating a child device for each key in the **Enum** branch.

In the **AddReg** section of the driver's INF file, the vendor supplies a value *pnpid* of type REG\_SZ for each entry under **Enum**. Stream class uses this string value to construct a Plug and Play (PnP) hardware ID for each individual child device.

In releases earlier than DirectX 9.0, stream class creates a child device hardware ID of the form "AVStream\\*&lt;pnpid&gt;*" (where &lt;pnpid&gt; is the value of *pnpid* for the specific device).

For example, the vendor specifies the following in the **AddReg** section of the INF file:

```
[MyTVDevice.AddReg]
HKR,"ENUM\CrossbarDevice",pnpid,,"MyCrossbar"
HKR,"ENUM\TunerDevice",pnpid,,"MyTuner"
```

Accordingly, stream class creates two child devices with the following device IDs:

Stream\\MyCrossbar

Stream\\MyTuner

To resolve possible ambiguity from two different child devices specifying the same *pnpid* value, DirectX 9.0 and later change the IDs reported for each of the child devices. For each hardware ID reported by the parent device, stream class creates an ID for the child device of the following form:

Stream\\*&lt;pnpid&gt;*\#*&lt;modified parent hardware ID&gt;*

The modified parent hardware ID is the parent hardware ID with each backslash (**\\**) character replaced by the number sign (**\#**).

If the resulting string is too long, stream class terminates the ID string at MAX\_DEVICE\_ID\_LEN characters, including the **NULL** terminator. In Windows Server 2003, this limit is set to 200 characters in *cfgmgr32.h*.

For example, a parent device reports the following hardware IDs:

PCI\\VEN\_XXXX&DEV\_YYYY&SUBSYS\_ZZZZZZZZ&REV\_VV

PCI\\VEN\_XXXX&DEV\_YYYY&SUBSYS\_ZZZZZZZZ

For a device with a *pnpid* key of **MyCrossbar**, stream class creates the following child device hardware IDs:

Stream\\MyCrossbar\#PCI\#VEN\_XXXX&DEV\_YYYY&SUBSYS\_ZZZZZZZZ&REV\_VV

Stream\\MyCrossbar\#PCI\#VEN\_XXXX&DEV\_YYYY&SUBSYS\_ZZZZZZZZ

Stream class uses the same process for compatible IDs reported by the parent device. Stream class creates a compatible ID for the child device of the form:

Stream\\*&lt;pnpid&gt;*\#*&lt;modified parent compatible ID&gt;*

The name modification and length rules for compatible IDs are identical to those for hardware IDs.

For example, if the parent device described previously reports the following compatible IDs:

PCI\\VEN\_XXXX&DEV\_YYYY&REV\_VV

PCI\\VEN\_XXXX&DEV\_YYYY

PCI\\VEN\_XXXX&CC\_ZZZZZZ

PCI\\VEN\_XXXX&CC\_ZZZZ

PCI\\VEN\_XXXX

PCI\\CC\_ZZZZZZ

PCI\\CC\_ZZZZ

The **MyCrossbar** child device would report through stream class the following compatible IDs:

Stream\\MyCrossbar\#PCI\#VEN\_XXXX&DEV\_YYYY&REV\_VV

Stream\\MyCrossbar\#PCI\#VEN\_XXXX&DEV\_YYYY

Stream\\MyCrossbar\#PCI\#VEN\_XXXX&CC\_ZZZZZZ

Stream\\MyCrossbar\#PCI\#VEN\_XXXX&CC\_ZZZZ

Stream\\MyCrossbar\#PCI\#VEN\_XXXX

Stream\\MyCrossbar\#PCI\#CC\_ZZZZZZ

Stream\\MyCrossbar\#PCI\#CC\_ZZZZ

Stream\\MyCrossbar

**Note**   In DirectX 9.0 and later, the legacy hardware ID, Stream\\*&lt;pnpid&gt;*, is still reported as the lowest rank compatible ID. As a result, legacy drivers continue to work unmodified on these platforms.
However, as of the DirectX 9.0 release, Microsoft recommends that vendors writing *new or revised drivers that leverage the stream class bus enumerator use the new hardware ID formats*. Drivers can support platforms running earlier versions of stream class by including the old ID in the compatible IDs list in the INF file.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Stream%20Class%20Child%20Devices%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


