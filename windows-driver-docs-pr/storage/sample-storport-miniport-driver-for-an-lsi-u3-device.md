---
title: Sample Storport Miniport Driver for an LSI_U3 Device
description: Sample Storport Miniport Driver for an LSI_U3 Device
ms.assetid: 1ac63d07-f85c-492b-9886-f40a19d7c0b2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample Storport Miniport Driver for an LSI\_U3 Device


The LSI\_U3 Storport miniport driver sample code that is included in the WDK is LSI's production SYM\_U3 Scsiport-based miniport driver after being ported to work with Storport instead of Scsiport. The resulting Storport-based miniport driver supports LSI Ultra160 parallel SCSI host bus adapters with 53C1010-33 or 53C1010-66 chips. Some of the characteristics of these host bus adapters include:

-   Older technology SCSI controller hardware with minimal intelligence

-   Very simple custom 8-bit RISC processor with 8 KB internal RAM

-   Hardware and scripts limited to use 256 queue tag values per adapter

-   Hardware and scripts designed to match Scsiport capabilities

Adjustments were made in the LSI\_U3 miniport driver to match Storport advanced functionality to the limited hardware capabilities of the host bus adapters themselves.

 

 




