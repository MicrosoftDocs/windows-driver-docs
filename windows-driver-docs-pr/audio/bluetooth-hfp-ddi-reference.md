---
title: Bluetooth HFP DDI Reference
description: Windows 8 has introduced the GUID\_DEVINTERFACE\_BLUETOOTH\_HFP\_SCO\_HCIBYPASS class, with interfaces that implement I/O control codes (IOCTLs) and structures for the Hands-free profile (HFP) bypass audio driver.
ms.assetid: 980B7283-56C5-44FA-8992-6DA5BE263FCD
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Bluetooth HFP DDI Reference


Windows 8 has introduced the GUID\_DEVINTERFACE\_BLUETOOTH\_HFP\_SCO\_HCIBYPASS class, with interfaces that implement I/O control codes (IOCTLs) and structures for the Hands-free profile (HFP) bypass audio driver.

For each HFP on a paired Bluetooth device the HFP driver registers an interface in this class. The interface is registered and enabled after the device is paired and the HFP driver is running. When the driver stops, the interface is disabled and unregistered.

When you develop a driver for bypass audio connections on a Bluetooth controller, your driver can use these interfaces to fully implement Bluetooth audio support. The HFP device allows only a single file object on the GUID\_DEVINTERFACE\_BLUETOOTH\_HFP\_SCO\_HCIBYPASS device interface.

The following topics describe the structures and IOCTLs that are defined for this class.

[Bluetooth HFP DDI Structures](bluetooth-hfp-ddi-structures.md)

[Bluetooth HFP DDI IOCTLs](bluetooth-hfp-ddi-ioctls.md)

 

 





