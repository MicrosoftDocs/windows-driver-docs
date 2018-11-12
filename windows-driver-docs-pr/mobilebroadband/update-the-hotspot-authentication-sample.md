---
title: Update the hotspot authentication sample
description: Update the hotspot authentication sample
ms.assetid: 68ebcdee-7b21-4177-b032-ba725ad2aee4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Update the hotspot authentication sample


The [Hotspot Authentication Sample](http://go.microsoft.com/fwlink/p/?linkid=313215) project uses a default carrier ID and application family name. To use the sample in your own test environment, you must change the following items:

-   **Update your Carrier ID** If you are publishing a mobile broadband app, this should be the Experience ID that is associated with your app and service metadata. If you are a Wi-Fi-only operator, generate a new GUID to use as your company’s ID.

-   **Update the SSID** The SSID that you use for test should match the SSID in the provisioning file and must offer captive portal and WISPr challenge to connecting clients.

-   **Sign the provisioning file** If you are a Wi-Fi-only operator, you must sign the provisioning file. In the Windows 8 SDK or the Windows 8.1 SDK, find the tool **ProvisioningTestHelper.psd1**. Import this into a PowerShell session to add the following four additional cmdlets:

    -   **Install-TestEVCert** Generates a new CA certificate, registers it on your test machine as a trusted EV SSL provider, and uses it to generate and sign an EV certificate for use in signing.

    -   **ConvertTo-SignedXml** Uses an EV certificate (generated for test, or issued by a third-party provider) to apply an XML-DSig signature to a Provisioning Metadata XML file. This signature from a trusted certificate causes Windows to accept the provisioning file as valid from a mobile broadband app that has no affiliated hardware.

    -   **Test-SignedXml** Checks a provisioning file to ensure schema conformance and valid signature.

    -   **Install-RootCertFromFile** Applies the test root certificate on a different PC, to test the client experience on a machine other than the development PC.

## <span id="related_topics"></span>Related topics


[Get started with a hotspot authentication app](get-started-with-a-hotspot-authentication-app.md)

 

 






