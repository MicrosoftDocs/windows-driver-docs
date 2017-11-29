---
title: Bluetooth HFP DDI Reference
description: Windows 8 has introduced the GUID\_DEVINTERFACE\_BLUETOOTH\_HFP\_SCO\_HCIBYPASS class, with interfaces that implement I/O control codes (IOCTLs) and structures for the Hands-free profile (HFP) bypass audio driver.
ms.assetid: 980B7283-56C5-44FA-8992-6DA5BE263FCD
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bluetooth HFP DDI Reference


Windows 8 has introduced the GUID\_DEVINTERFACE\_BLUETOOTH\_HFP\_SCO\_HCIBYPASS class, with interfaces that implement I/O control codes (IOCTLs) and structures for the Hands-free profile (HFP) bypass audio driver.

For each HFP on a paired Bluetooth device the HFP driver registers an interface in this class. The interface is registered and enabled after the device is paired and the HFP driver is running. When the driver stops, the interface is disabled and unregistered.

When you develop a driver for bypass audio connections on a Bluetooth controller, your driver can use these interfaces to fully implement Bluetooth audio support. The HFP device allows only a single file object on the GUID\_DEVINTERFACE\_BLUETOOTH\_HFP\_SCO\_HCIBYPASS device interface.

The following topics describe the structures and IOCTLs that are defined for this class.

[Bluetooth HFP DDI Structures](bluetooth-hfp-ddi-structures.md)

[Bluetooth HFP DDI IOCTLs](bluetooth-hfp-ddi-ioctls.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Bluetooth%20HFP%20DDI%20Reference%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




