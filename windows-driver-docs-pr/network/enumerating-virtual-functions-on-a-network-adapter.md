---
title: Enumerating Virtual Functions on a Network Adapter
description: Enumerating Virtual Functions on a Network Adapter
ms.assetid: 3AAF2D8B-9C7A-4E5B-86B6-264ACA5EA492
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Virtual Functions on a Network Adapter


An overlying driver or user application can obtain a list of all PCI Express (PCIe) Virtual Functions (VFs) on a network adapter that supports single root I/O virtualization (SR-IOV). The driver or application issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_ENUM\_VFS](https://msdn.microsoft.com/library/windows/hardware/hh451820) to obtain this list.

Before the driver or application issues the OID request, it must initialize an [**NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451592) structure that is passed along with the request. The driver or application must follow these guidelines when initializing the **NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY** structure:

-   If the NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY\_ENUM\_ON\_SPECIFIC\_SWITCH flag is set in the **Flags** member, the overlying driver or application must set the **SwitchId** member to the identifier of a NIC switch on the SR-IOV network adapter. By setting these members in this manner, VF information is returned only for the specified NIC switch on the SR-IOV network adapter.

    **Note**  The overlying driver and user-mode application can obtain the NIC switch identifiers by issuing an OID query request of [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](https://msdn.microsoft.com/library/windows/hardware/hh451819).

-   If the **Flags** member is set to zero, the driver or application must set the **SwitchId** member to zero. By setting these members in this manner, VF information is returned for all NIC switches on the SR-IOV network adapter.

    **Note**  Starting with Windows Server 2012, Windows supports only the default NIC switch on the network adapter. Regardless of the flags set in the **Flags** member, the **SwitchId** member must be set to NDIS\_DEFAULT\_SWITCH\_ID.

After a successful return from this OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer that contains the following:

-   An [**NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451592) structure that defines the number of elements within the array.

-   An array of [**NDIS\_NIC\_SWITCH\_VF\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451591) structures. Each of these structures contains information about a single VF on a NIC switch of the network adapter. A VF is attached to a NIC switch through OID method requests of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814).

    **Note**  If no VFs are attached to a NIC switch on the network adapter, the **NumElements** member of the [**NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451592) structure is set to zero and no [**NDIS\_NIC\_SWITCH\_VF\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451591) structures are returned.

    For more information on NIC switches, see [NIC Switches](nic-switches.md).

NDIS handles the [OID\_NIC\_SWITCH\_ENUM\_VFS](https://msdn.microsoft.com/library/windows/hardware/hh451820) request for miniport drivers. NDIS returns the information from an internal cache of the data that it maintains from inspecting the following sources:

-   OID method requests of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814).

-   OID set requests of [OID\_NIC\_SWITCH\_VF\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451824).