---
title: About the Sample Storport Miniport Driver for an LSI_U3 Device
description: Sample Storport Miniport Driver for an LSI_U3 Device
ms.date: 12/15/2019
---

# About the Sample Storport Miniport Driver for an LSI_U3 Device

The [LSI_U3 Storport miniport driver sample](/samples/microsoft/windows-driver-samples/lsi_u3-storport-miniport-driver/
) is LSI's production SYM_U3 Scsiport-based miniport driver after being ported to work with Storport instead of Scsiport. The resulting Storport-based miniport driver supports LSI Ultra160 parallel SCSI host bus adapters with 53C1010-33 or 53C1010-66 chips. Some of the characteristics of these host bus adapters include:

- Older technology SCSI controller hardware with minimal intelligence

- Very simple custom 8-bit RISC processor with 8 KB internal RAM

- Hardware and scripts limited to use 256 queue tag values per adapter

- Hardware and scripts designed to match Scsiport capabilities

Adjustments were made in the LSI_U3 miniport driver to match Storport advanced functionality to the limited hardware capabilities of the host bus adapters themselves.
