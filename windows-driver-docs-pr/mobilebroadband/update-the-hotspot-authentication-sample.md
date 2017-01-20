---
title: Update the hotspot authentication sample
description: Update the hotspot authentication sample
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 68ebcdee-7b21-4177-b032-ba725ad2aee4
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Update%20the%20hotspot%20authentication%20sample%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





