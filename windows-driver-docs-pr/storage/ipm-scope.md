---
title: IPM Scope
author: windows-driver-content
description: IPM Scope
ms.assetid: fa34f703-ab02-4a0d-96ae-e7cb89756992
---

# IPM Scope


Storport Idle Power Management (IPM) provides idle power management for the LUN, not the adapter. Storport IPM does not attempt to place the adapter in a low power state if all its LUNs are in a low power state. The miniport driver is responsible for managing adapter power.

Storport IPM is supported in the following system configuration only:

Systems that use a SATA adapter with a single SATA disk drive attached

Storport IPM is not supported in the following system configurations:

Systems that have non-direct attached storage (FC, iSCSI, and others)

Systems that have external storage arrays and RAID controllers

Systems that have MPIO

Systems that have non-SATA host bus adapters

Systems that have more than one disk attached to a SATA adapter

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20IPM%20Scope%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


