---
title: Container IDs for PnP-X Devices
description: Container IDs for PnP-X Devices
ms.assetid: 6a1ea4e9-e672-4f37-ab26-932591fe4da4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Container IDs for PnP-X Devices


PnP extensions (PnP-X) extends Windows Plug and Play (PnP) to support devices that are connected to the computer through an IP-based network. For more information about PnP-X, refer to the [PnP-X: Plug and Play Extensions for Windows specification.](http://go.microsoft.com/fwlink/p/?linkid=142398                  )

PnP-X devices can specify a container ID as an XML element in their device metadata. Two protocols are supported:

-   Device Profile for Web Services (DPWS).

    For more information about DPWS, refer to the [DPWS specification.](http://go.microsoft.com/fwlink/p/?linkid=142400)

    For more information about supporting container IDs through DPWS, see [Container IDs for DPWS Devices](container-ids-for-dpws-devices.md).

-   Universal PnP (UPnP).

    For more information, refer to the [UPnP Device Architecture specification.](http://go.microsoft.com/fwlink/p/?linkid=142402)

    For more information about supporting container IDs through UPnP, see [Container IDs for UPnP Devices](container-ids-for-upnp-devices.md).

If a PnP-X device does not specify a container ID in the DPWS device metadata or the UPnP device description document, the PnP manager generates a container ID for the device through an algorithm specific to the protocol the device supports:

-   For DPWS devices, the generated container ID is either created from the GUID in the device’s endpoint reference address (EPR) or is a SHA-1 hash of the device's EPR (if not a GUID).

-   For UPnP devices, the generated container ID is the device's Unique Device Name (UDN).

    **Note**  In Windows 10, the PnP manager will always generate a container ID for DPWS devices by using the above algorithms, even if a container ID has been specified in the device metadata.

     

For devices which operate on a single bus or PnP-X protocol, the PnP-X generated container ID is sufficient.

Multiprotocol devices may want to specify a container ID. In a multiprotocol device, the same container ID would be shared on each protocol to allow Windows to group all instances of the device into one device container. In this manner, a container ID for the device can be specified through both DPWS and UPnP.

 

 





