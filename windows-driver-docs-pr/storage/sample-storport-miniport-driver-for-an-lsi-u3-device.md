---
title: Sample Storport Miniport Driver for an LSI\_U3 Device
author: windows-driver-content
description: Sample Storport Miniport Driver for an LSI\_U3 Device
ms.assetid: 1ac63d07-f85c-492b-9886-f40a19d7c0b2
---

# Sample Storport Miniport Driver for an LSI\_U3 Device


The LSI\_U3 Storport miniport driver sample code that is included in the WDK is LSI's production SYM\_U3 Scsiport-based miniport driver after being ported to work with Storport instead of Scsiport. The resulting Storport-based miniport driver supports LSI Ultra160 parallel SCSI host bus adapters with 53C1010-33 or 53C1010-66 chips. Some of the characteristics of these host bus adapters include:

-   Older technology SCSI controller hardware with minimal intelligence

-   Very simple custom 8-bit RISC processor with 8 KB internal RAM

-   Hardware and scripts limited to use 256 queue tag values per adapter

-   Hardware and scripts designed to match Scsiport capabilities

Adjustments were made in the LSI\_U3 miniport driver to match Storport advanced functionality to the limited hardware capabilities of the host bus adapters themselves.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Sample%20Storport%20Miniport%20Driver%20for%20an%20LSI_U3%20Device%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


