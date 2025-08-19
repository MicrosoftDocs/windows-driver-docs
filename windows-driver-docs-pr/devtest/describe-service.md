---
title: Describe your Service in the Mobile Broadband Metadata Authoring Wizard
description: Describe your service in the Mobile Broadband Metadata Authoring Wizard
keywords:
- Describe your service in the Mobile Broadband Metadata Authoring Wizard
ms.date: 06/25/2025
ms.topic: how-to
---

# Describe your service in the Mobile Broadband Metadata Authoring Wizard

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](../install/driver-package-container-metadata.md)**.

You can provide descriptive information about your service in Windows, such as model name and manufacturer.

## To provide descriptive information about a service

1. Click the **Description** tab.
1. Fill out the following fields.
    - **Service Name**. This optional field isn't used in Windows 8.
    - **Service Provider**. The operator name that appears in Windows Connection Manager.
    - **Service Number**. Specify a GUID that uniquely identifies your service. This GUID is used to identify the operator when using operator XML provisioning. If you update the device metadata package, this GUID should remain the same. This is a different value than the Experience ID and the file name of the device metadata package. For more information on selecting a GUID for Service Number, see [Overview of Using Metadata to Configure Mobile Broadband Experiences](../mobilebroadband/using-metadata-to-configure-mobile-broadband-experiences.md).
    - **Description 1**. This optional field isn't used in Windows 8.
    - **Description 2**. This optional field isn't used in Windows 8.

For detailed information about metadata properties, see [Service Metadata Package Schema Reference](../mobilebroadband/mobilebroadbandinfo-xml-schema.md).
