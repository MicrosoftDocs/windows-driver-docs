---
title: Service identifier ownership updates
description: Service identifier ownership updates
ms.assetid: 6cb03631-def6-44d4-a73a-0e6124e3b1f2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Service identifier ownership updates

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]


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

 

 





