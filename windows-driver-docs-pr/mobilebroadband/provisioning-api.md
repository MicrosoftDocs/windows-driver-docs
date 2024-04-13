---
title: Provisioning API
description: Provisioning API
ms.date: 04/20/2017
---

# Provisioning API


By using the Provisioning API, you can provision the Windows-based computer with required connection profiles for mobile broadband and Wi-Fi, and can configure the cost that is associated with the mobile broadband profiles. Provisioning information is contained in an XML document, as described in [Using metadata to configure mobile broadband experiences](using-metadata-to-configure-mobile-broadband-experiences.md). You typically call this API after subscription purchase or to update provisioning information on the computer.

You can also call the Provisioning API at any time to update the information that is provided to Windows. This is usually done when the mobile broadband app retrieves updated cost and plan status from the operator’s server, but it can also be done when Wi-Fi hotspot networks or the mobile broadband network configuration must be updated.

For more information about the Provisioning API, see [**ProvisioningAgent class**](/uwp/api/Windows.Networking.NetworkOperators.ProvisioningAgent).

## <span id="related_topics"></span>Related topics


[List of mobile broadband Windows Runtime APIs](list-of-mobile-broadband-windows-runtime-apis.md)

 

