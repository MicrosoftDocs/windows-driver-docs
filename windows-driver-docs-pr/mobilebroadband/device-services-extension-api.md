---
title: Device Services Extension API
description: Device Services Extension API
ms.assetid: e1539ae1-78fd-4d79-81bf-4030e69e191c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Services Extension API


Windows-compliant mobile broadband devices project each supported feature as a device service. Examples of services are IP Connectivity (ability to connect to or disconnect from a mobile broadband network), Phonebook, SIM Toolkit, SMS, and USSD. Each device service has a corresponding GUID. All control messages and non-IP packets that are exchanged between the mobile broadband generic driver and the device carry the GUID to identify the service that is associated with the request. Command identifiers (CIDs) and status indication codes are defined under a service’s GUID namespace. For example, Phonebook and SIM Toolkit might both share the same CID code, but they are distinguished by the device service GUID that is exchanged in the request.

Any device services that are not natively implemented by the Windows wireless platform can be accessed by the Device Services Extension API. This API provides a direct pipe for the independent hardware vendor (IHV) software to access functionality on the device. This pipe provides a conduit through the WWAN service and mobile broadband generic driver to the device, as shown in the following diagram:

![device services](images/mb-fig1-deviceservices.png)

The Windows wireless platform supports APIs for the following app functions:

-   Enumerate device services

-   Open/close device services

-   Send control commands to a specific device service

-   Send data to (or receive data from) a specific device service

-   Register for “unsolicited” device events from a specific device service

## <span id="related_topics"></span>Related topics


[List of mobile broadband Windows Runtime APIs](list-of-mobile-broadband-windows-runtime-apis.md)

 

 






