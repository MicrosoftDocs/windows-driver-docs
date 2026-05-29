---
title: Using Computer Hardware IDs (CHIDs)
description: Learn how Computer Hardware IDs (CHIDs) are used for driver distribution in Partner Center and Windows Update.
ms.date: 05/29/2026
ms.topic: how-to
ai-usage: ai-assisted
---

# Using Computer Hardware IDs (CHIDs)

Computer Hardware IDs (CHIDs) are defined in [Computer Hardware ID (CHID)](../install/computer-hardware-ids.md). For the full CHID hierarchy and the SMBIOS field combinations used for each HardwareID value, see that article.

OEMs must provide the correct CHID information to the driver publisher. The [ComputerHardwareIds](../devtest/computerhardwareids.md) tool, included in the Windows Desktop Tools SDK, can help with reporting CHIDs from a known set of System Management BIOS (SMBIOS) values. ComputerHardwareIds performs two different tasks.

1. Default behavior: The tool reports the system's SMBIOS values and generated CHIDs.

   By default, the tool displays the system's SMBIOS values, and the CHIDs that are generated from the SMBIOS values.

1. Simulation behavior: The tool generates CHIDs from user provided SMBIOS values.

   You can run the tool with simulated SMBIOS values (such as manufacturer, family, and SKU) to get a list of generated CHIDs. The tool allows you to determine which CHIDs would be generated on a system with specific SMBIOS data values.

## Tips for consistent CHIDs

CHIDs are generated based on case sensitive SMBIOS values. Care must be taken to ensure that systems don't mix cases in SMBIOS text values. Similarly, UNICODE characters aren't specially treated. Upper and lower case versions of special characters, such as the Turkish dotted and undotted letter I, are treated uniquely: I, ı, İ and i aren't the same.

The ComputerHardwareIds tool only computes CHIDs that have the necessary SMBIOS values available. If an SMBIOS data field is missing (or it's null), then any related CHIDs aren't generated. For example, if the SMBIOS SKU field is null, then CHIDs 0, 3, 4 6 and 7 aren't available for that particular system.

For more information about CHIDs, see [Computer Hardware ID (CHID)](../install/computer-hardware-ids.md).

## How the Windows Update Service uses CHID

The Windows Update service uses CHID to "reduce the number of systems that a driver is applicable to". This reduction is the first thing that happens before PnP ranking is done.

The Windows Update service treats CHID differently depending on which Windows OS level is installed.

| Windows 10 version | Windows Update behavior |
|--|--|
| 1507 through 1703 | Windows Update ranks each CHID from CHID-0 to CHID-14 where CHID-0 outranks CHID-14 |
| 1709 and later | CHID level is no longer ranked. All applicable CHID targeted drivers from CHID-0 through CHID-14 are grouped together then PnP ranking occurs on the entire group. |

Consider the following example:

Contoso has the following two drivers published as Automatic that target the same hardware (HWID) but with different CHID.

- Distribution 1 - targeting CHID-4 (Manufacturer + Family + Product Name + SKU Number)
- Distribution 2 - targeting CHID-5 (Manufacturer + Family + Product Name)

Which one is by the Windows Update Service for systems that match CHID-5?

| Contoso System | Windows OS level | Offered Driver |
|--|--|--|
| CHID-5 match but not a CHID-4 match | Windows 10 1703 or earlier | Distribution 2 |
| CHID-5 match but not a CHID-4 match | Windows 10 1709 or later | Distribution 2 |
| CHID-5 match **and** a CHID-4 match | Windows 10 1703 or earlier | Distribution 1 |
| CHID-5 match **and** a CHID-4 match | Windows 10 1709 or later | Both are offered. PnP ranking would then select the best match of these two CHIDs for installation. |
