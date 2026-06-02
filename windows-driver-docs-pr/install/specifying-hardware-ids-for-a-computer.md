---
title: Specifying Hardware IDs for a Computer
description: Specifying Hardware IDs for a computer
ms.date: 06/19/2025
ms.topic: concept-article
---

# Specifying Hardware IDs for a computer

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](driver-package-container-metadata.md)**.

Devices and Printers recognizes the computer as a [device container](container-ids.md). As a result, the computer can be identified within a device metadata package by using a **[HardwareID](/previous-versions/windows/hardware/metadata/ff546114(v=vs.85))** XML element that specifies a unique [hardware ID](hardware-ids.md) value. This hardware ID value for the computer is known as a computer hardware ID, or CHID. For more information about CHIDs, see [Computer Hardware ID (CHID)](computer-hardware-ids.md).

## Using Computer HardwareIDs with PC Device Metadata packages

Each computer has a ranked set of CHIDs (referred to as HardwareID-0 through HardwareID-14), where lower numbers are more specific and higher numbers are more general. Each CHID is a GUID formed by hashing a different combination of SMBIOS fields. For the full list of CHID definitions by Windows version, see [Computer Hardware ID (CHID)](computer-hardware-ids.md).

For Windows 7 systems, we highly recommend that vendors do the following when selecting a [hardware ID](hardware-ids.md) value to use as the **[HardwareID](/previous-versions/windows/hardware/metadata/ff546114(v=vs.85))** XML element value for the computer.

- Use **HardwareID-3** or **HardwareID-4** as the first choice if the device metadata package matches a computer that has a specific make, family, and model. This allows a metadata package to match the specified computer, which provides the most precise metadata for the computer.

- Use **HardwareID-5**, as the second choice if the device metadata package covers the entire family of computers. In this case, the computer family is unique and is not branded with more than one product line.

- Use **HardwareID-6** or **HardwareID-7** as the third choice if the device metadata package covers all of your computers or those computers with a specific enclosure type.

> [!NOTE]
> For Windows 7 PC device metadata, **HardwareID-1** and **HardwareID-2** are reserved for future use. Don't use them for the computer's hardware ID.

> [!NOTE]
> For Windows 8 PC device metadata, don't use **HardwareID-1**, **HardwareID-2**, **HardwareID-3** for the computer's hardware ID. **HardwareID-1**, **HardwareID-2**, **HardwareID-3** are reserved for future use. Instead, use **HardwareID-4**, **HardwareID-5**, **HardwareID-6**, **HardwareID-7**, **HardwareID-8**, **HardwareID-9**, and **HardwareID-10**.

To specify that the hardware ID is for a computer device container, use the following rules:

- Delimit the hardware ID string with '{' and '}' characters.
- Add the prefix 'ComputerMetadata\\' in front of the hardware ID string.

Here is an example of a **[HardwareID](/previous-versions/windows/hardware/metadata/ff546114(v=vs.85))** XML element for the computer:

```cpp
DOID:ComputerMetadata\{c20d5449-511e-4cb5-902a-a541239322aa}
```

For more information about the format requirements of the **HardwareID** XML element, see **[HardwareID](/previous-versions/windows/hardware/metadata/ff546114(v=vs.85))**.

## Related articles

- [Windows 10 Driver Publishing Workflow](https://go.microsoft.com/fwlink/p/?LinkId=617374 )
