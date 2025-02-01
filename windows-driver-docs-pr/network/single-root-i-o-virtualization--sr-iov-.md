---
title: Introduction to Single Root I/O Virtualization (SR-IOV)
description: Learn about the single root I/O virtualization interface and how it supports Microsoft Hyper-V performance improvements.
ms.date: 01/31/2025
---

# Introduction to single root I/O virtualization

Starting with NDIS 6.30, the single root I/O virtualization (SR-IOV) interface supports Microsoft Hyper-V performance improvements for virtualized networks on Windows Server 2012 and later versions of Windows Server.

The SR-IOV specification from PCI-SIG defines the extensions to the PCI Express (PCIe) specification suite that enable multiple virtual machines (VMs) to share the same PCIe physical hardware resources.

The following articles describe the NDIS SR-IOV interface and the techniques for writing an NDIS miniport driver for an SR-IOV capable network adapter that implements the PCIe SR-IOV specification.

- [Overview of single root I/O virtualization](overview-of-single-root-i-o-virtualization--sr-iov-.md)

- [Writing SR-IOV PF miniport drivers](writing-sr-iov-pf-miniport-drivers.md)

- [Writing SR-IOV VF miniport drivers](writing-sr-iov-vf-miniport-drivers.md)

- [SR-IOV PF/VF backchannel communication](sr-iov-pf-vf-backchannel-communication.md)

- [SR-IOV object identifiers](sr-iov-oids.md)

For more information on SR-IOV, see the [PCI-SIG single root I/O virtualization and sharing](https://pcisig.com/specifications/iov/single_root) specification.

