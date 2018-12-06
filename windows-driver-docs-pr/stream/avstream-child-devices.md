---
title: AVStream Child Devices
description: AVStream Child Devices
ms.assetid: 4b2528d7-acc7-40eb-a351-64d8564c7a13
keywords:
- child devices WDK AVStream
- AVStream child devices WDK
- bus enumeration WDK AVStream
- hardware IDs WDK AVStream
- identifiers WDK AVStream
- compatible IDs WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AVStream Child Devices





This section applies to Microsoft Windows Server 2003 and earlier operating systems only if DirectX 9.0 or later is installed on that platform.

AVStream can function as a bus enumerator for your device, creating a child device for each key in the **Enum** branch. To do this, place an **Enum** branch in the registry under the device key.

Specifically, in the **AddReg** section of the driver's INF file, the vendor supplies a value *pnpid* of type REG\_SZ for each entry under **Enum**. AVStream uses this string value to construct a Plug and Play (PnP) hardware ID for each individual child device.

In releases earlier than DirectX 9.0, AVStream creates a child device hardware ID of the form "AVStream\\*&lt;pnpid&gt;*" (where &lt;pnpid&gt; is the value of *pnpid* for the specific device).

For example, the vendor specifies the following in the **AddReg** section of the INF file:

```INF
[MyTVDevice.AddReg]
HKR,"ENUM\CrossbarDevice",pnpid,,"MyCrossbar"
HKR,"ENUM\TunerDevice",pnpid,,"MyTuner"
```

Accordingly, AVStream creates two child devices with the following device IDs:

AVStream\\MyCrossbar

AVStream\\MyTuner

To resolve possible ambiguity from two different child devices specifying the same *pnpid* value, DirectX 9.0 and later change the IDs reported for each of the child devices. For each hardware ID reported by the parent device, AVStream creates an ID for the child device in the following form:

AVStream\\*&lt;pnpid&gt;*\#*&lt;modified parent hardware ID&gt;*

The modified parent hardware ID is the parent hardware ID with each backslash (**\\**) character replaced by the number sign (**\#**).

If the resulting string is too long, AVStream terminates the ID string at MAX\_DEVICE\_ID\_LEN characters, including the **NULL** terminator. In Windows Server 2003, this limit is set to 200 characters in *cfgmgr32.h*.

For example, a parent device reports the following hardware IDs:

PCI\\VEN\_XXXX&DEV\_YYYY&SUBSYS\_ZZZZZZZZ&REV\_VV

PCI\\VEN\_XXXX&DEV\_YYYY&SUBSYS\_ZZZZZZZZ

For a device with a *pnpid* key of **MyCrossbar**, AVStream creates the following child device hardware IDs:

AVStream\\MyCrossbar\#PCI\#VEN\_XXXX&DEV\_YYYY&SUBSYS\_ZZZZZZZZ&REV\_VV

AVStream\\MyCrossbar\#PCI\#VEN\_XXXX&DEV\_YYYY&SUBSYS\_ZZZZZZZZ

AVStream uses the same process for compatible IDs reported by the parent device. AVStream creates a compatible ID for the child device of the form:

AVStream\\*&lt;pnpid&gt;*\#*&lt;modified parent compatible ID&gt;*

The name modification and length rules for compatible IDs are identical to those for hardware IDs.

For example, if the parent device previously described reports the following compatible IDs:

PCI\\VEN\_XXXX&DEV\_YYYY&REV\_VV

PCI\\VEN\_XXXX&DEV\_YYYY

PCI\\VEN\_XXXX&CC\_ZZZZZZ

PCI\\VEN\_XXXX&CC\_ZZZZ

PCI\\VEN\_XXXX

PCI\\CC\_ZZZZZZ

PCI\\CC\_ZZZZ

The **MyCrossbar** child device would report through AVStream the following compatible IDs:

AVStream\\MyCrossbar\#PCI\#VEN\_XXXX&DEV\_YYYY&REV\_VV

AVStream\\MyCrossbar\#PCI\#VEN\_XXXX&DEV\_YYYY

AVStream\\MyCrossbar\#PCI\#VEN\_XXXX&CC\_ZZZZZZ

AVStream\\MyCrossbar\#PCI\#VEN\_XXXX&CC\_ZZZZ

AVStream\\MyCrossbar\#PCI\#VEN\_XXXX

AVStream\\MyCrossbar\#PCI\#CC\_ZZZZZZ

AVStream\\MyCrossbar\#PCI\#CC\_ZZZZ

AVStream\\MyCrossbar

**Note**   In DirectX 9.0 and later, the legacy hardware ID, AVStream\\*&lt;pnpid&gt;*, is still reported as the lowest rank compatible ID. As a result, legacy drivers continue to work unmodified on these platforms.
However, as of the DirectX 9.0 release, Microsoft recommends that vendors writing new or revised drivers that leverage the AVStream class bus enumerator use the new hardware ID formats. Drivers can support platforms running earlier versions of AVStream by including the old ID in the compatible IDs list in the INF file.

 

 

 




