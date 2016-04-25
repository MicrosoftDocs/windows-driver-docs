---
title: System and device firmware updates via a firmware driver package
description: Deploying a firmware update using a firmware driver package follows a relatively simple process that can be divided into three phases
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: D649234A-B757-41A6-B2C1-6D43775FF999
---

# System and device firmware updates via a firmware driver package


Deploying a firmware update using a firmware driver package follows a relatively simple process that can be divided into three phases:

1.  Author a firmware update package.
2.  Certify and sign the update package.
3.  Install the update.

The following diagram shows this process in greater detail.

![system and device firmware update process](images/systemanddevicefirmwareupdateprocess.png)

This process assumes that the UEFI firmware update payload has already been developed, tested, and signed.

1.  The firmware driver package simply contains the payload for a firmware update and allows the firmware update payload to be distributed in the same manner as all Windows drivers.
2.  After the driver package has been deployed to a system, the firmware update payload is passed to platform firmware via the UEFI UpdateCapsule service.
3.  Upon receipt of the firmware update payload, platform firmware recognizes the payload and applies the update.
4.  The implementation of the platform firmware update code is proprietary, as is the format of the firmware update payload.

A device driver package contains an INF file describing the devices to which the package applies. A firmware driver package is the same. Devices and system firmware resources supporting this update mechanism must uniquely identify themselves to bind to a firmware driver package. The next section describes the identification mechanism.

## In this section


-   [Populating the ESRT table](populating-the-esrt-table.md)
-   [Customizing firmware for different geographic regions](customizing-firmware-for-different-geographic-regions.md)
-   [Authoring a firmware update package](authoring-a-firmware-update-package.md)
-   [Certifying and signing the update package](certifying-and-signing-the-update-package.md)
-   [Installing the update](installing-the-update.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20System%20and%20device%20firmware%20updates%20via%20a%20firmware%20driver%20package%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




