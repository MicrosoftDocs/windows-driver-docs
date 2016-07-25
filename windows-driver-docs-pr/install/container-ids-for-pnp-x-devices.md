---
title: Container IDs for PnP-X Devices
description: Container IDs for PnP-X Devices
ms.assetid: 6a1ea4e9-e672-4f37-ab26-932591fe4da4
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Container%20IDs%20for%20PnP-X%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




