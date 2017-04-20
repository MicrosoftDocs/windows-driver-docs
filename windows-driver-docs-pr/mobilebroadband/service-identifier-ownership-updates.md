---
title: Service identifier ownership updates
description: Service identifier ownership updates
ms.assetid: 6cb03631-def6-44d4-a73a-0e6124e3b1f2
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Service identifier ownership updates


Service Identifiers are a set of fields that are encoded in mobile broadband devices (SIM cards for GSM and modem for CDMA) and are used to uniquely identify the device. The service identifier is used by Windows 8, Windows 8.1, and Windows 10 to download the service metadata package for that device. Before you create your service metadata packages, you must register your service identifiers with the Windows Dev Center hardware dashboard. For info on registering new service identifiers, see [Developer guide for creating service metadata](developer-guide-for-creating-service-metadata.md).

Depending on the technology, service identifiers can consist of the following:

-   GSM

    -   **Provider ID** The combination of mobile country code and mobile network code, which is a 5 or 6 digit number.

    -   **Provider Name** The name flashed on to the device when the firmware is provisioned.

-   CDMA

    -   **SID** The System Identifier (SID) of a CDMA network.

    -   **Provider Name** The name flashed on to the device when the firmware is provisioned.

If the ownership of an IMSI changes, the new operator must send an email to sysdev@microsoft.com with the following info:

-   Organization name used by the operator during the Windows Dev Center hardware dashboard registration process

-   Name of the old mobile operator that owned the IMSI

-   List of GSM Provider IDs affected by the ownership change

You should receive an acknowledgement emails with 24 hours that your request was received. However, it could take up to 5 business days to process the request. If we have conflicts, we’ll send you an email asking for additional information.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Service%20identifier%20ownership%20updates%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




