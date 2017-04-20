---
title: Provisioning API
description: Provisioning API
ms.assetid: bcb17631-a13c-416c-ac10-97f6c0d12cb0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Provisioning API


By using the Provisioning API, you can provision the Windows-based computer with required connection profiles for mobile broadband and Wi-Fi, and can configure the cost that is associated with the mobile broadband profiles. Provisioning information is contained in an XML document, as described in [Using metadata to configure mobile broadband experiences](using-metadata-to-configure-mobile-broadband-experiences.md). You typically call this API after subscription purchase or to update provisioning information on the computer.

You can also call the Provisioning API at any time to update the information that is provided to Windows. This is usually done when the mobile broadband app retrieves updated cost and plan status from the operator’s server, but it can also be done when Wi-Fi hotspot networks or the mobile broadband network configuration must be updated.

For more information about the Provisioning API, see [**ProvisioningAgent class**](https://msdn.microsoft.com/library/windows/apps/br207397).

## <span id="related_topics"></span>Related topics


[List of mobile broadband Windows Runtime APIs](list-of-mobile-broadband-windows-runtime-apis.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Provisioning%20API%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





