---
title: Identifiers for PCI Devices
description: Describes the device identification string formats that the PCI bus driver uses to report hardware IDs.
keywords:
- device identification strings WDK , PCI devices
- identification strings WDK device , PCI devices
- identifiers WDK device , PCI devices
- PCI device identifiers WDK device installations
- hardware IDs WDK device installations
- compatible IDs WDK device installations
ms.date: 04/08/2022
---

# Identifiers for PCI devices

> [!IMPORTANT]
> You can find a list of known IDs used in PCI devices at [The PCI ID Repository](https://pci-ids.ucw.cz/). To list IDs on Windows, use `pnputil /enum-devices /bus PCI /deviceids`.

The following is a list of the [device identification string](device-identification-strings.md) formats that the PCI bus driver uses to report [hardware IDs](hardware-ids.md). When the Plug and Play (PnP) manager queries the driver for the hardware IDs of a device, the PCI bus driver returns a list of hardware IDs in order of increasing generality.

```cpp
PCI\VEN_v(4)&DEV_d(4)&SUBSYS_s(4)n(4)&REV_r(2)

PCI\VEN_v(4)&DEV_d(4)&SUBSYS_s(4)n(4)

PCI\VEN_v(4)&DEV_d(4)&REV_r(2)

PCI\VEN_v(4)&DEV_d(4)

PCI\VEN_v(4)&DEV_d(4)&CC_c(2)s(2)p(2)

PCI\VEN_v(4)&DEV_d(4)&CC_c(2)s(2)
```

Where:

- v(4) is the four-character PCI SIG-assigned identifier for the vendor of the device, where the term *device*, following PCI SIG usage, refers to a specific PCI chip. As specified in [Publishing restrictions](../dashboard/publishing-restrictions.md), `0000` and `FFFF` are invalid codes for this identifier.

- d(4) is the four-character vendor-defined identifier for the device.

- s(4) is the four-character vendor-defined subsystem identifier.

- n(4) is the four-character PCI SIG-assigned identifier for the vendor of the subsystem. As specified in [Publishing restrictions](../dashboard/publishing-restrictions.md), `0000` and `FFFF` are invalid codes for this identifier.

- r(2) is the two-character revision number.

- c(2) is the two-character base class code from the configuration space.

- s(2) is the two-character subclass code.

- p(2) is the Programming Interface code.

## Examples

> [!NOTE]
> In these examples, you'll need to replace the placeholder SUBSYS values of `00000000`. As mentioned earlier, `0000` is invalid for the v(4) and n(4) identifiers.

The following is an example of a hardware ID for a display adapter on a portable computer. The format of this hardware ID is PCI\\VEN_v(4)&DEV_d(4)&SUBSYS_s(4)n(4)&REV_r(2):

`PCI\VEN_1414&DEV_00E0&SUBSYS_00000000&REV_04`

The following is the hardware ID for the display adapter in the previous example with the revision information removed. The format of this hardware ID is PCI\\VEN_<em>v(4)</em>&DEV_<em>d(4)</em>&SUBSYS_*s(4)n(4).*

`PCI\VEN_1414&DEV_00E0&SUBSYS_00000000`

> [!NOTE]
> In Windows 10, some IDs that previously appeared in the Hardware IDs list now appear in the list of Compatible IDs.

## Reporting compatible IDs

The following is a list of the device identification string formats that the PCI bus driver uses to report [compatible IDs](compatible-ids.md). The variety of these formats provides substantial flexibility to specify compatible IDs. The PCI bus driver constructs a list of compatible IDs based on the information that the driver can obtain from the device. When the PnP manager queries the driver for the compatible IDs of a device, the PCI bus driver returns a list of compatible IDs in order of decreasing compatibility.

```cpp
PCI\VEN_v(4)&DEV_d(4)&REV_r(2)

PCI\VEN_v(4)&DEV_d(4)

PCI\VEN_v(4)&CC_c(2)s(2)p(2)

PCI\VEN_v(4)&CC_c(2)s(2)

PCI\VEN_v(4)

PCI\CC_c(2)s(2)p(2)&DT_d(4) (applies only to a PCI Express device)

PCI\CC_c(2)s(2)p(2)

PCI\CC_c(2)s(2)&DT_d(4) (applies only to a PCI Express device)

PCI\CC_c(2)s(2)
```

Where:

- The definitions of the following fields in a compatible ID are identical to the definitions of the corresponding fields that used in a hardware ID: *v(4)*, *r(2)*, *c(2)*, *s(2)*, and *p(2)*.

- *d(4)* in the DEV_*d(4)* field is the four-character vendor-defined identifier for the device.

- *d(4)* in the DT_*d(4)* field is the four-character device type, as specified in the PCI Express Base specification.

For the example of a display adapter on a portable computer, any of the following compatible IDs would match the information in an INF file for that adapter:

```cpp
PCI\VEN_1414&DEV_00E0&REV_04

PCI\VEN_1414&DEV_00E0

PCI\VEN_1414&DEV_00E0&REV_04&CC_0300

PCI\VEN_1414&DEV_00E0&CC_030000

PCI\VEN_1414&DEV_00E0&CC_0300

PCI\VEN_1414&CC_030000

PCI\VEN_1414&CC_0300

PCI\VEN_1414

PCI\CC_030000

PCI\CC_0300
```
