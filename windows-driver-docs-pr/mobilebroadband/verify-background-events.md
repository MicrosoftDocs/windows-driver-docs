---
title: Verify background events
description: Verify background events
ms.assetid: c840f555-2e09-409d-9d4f-4d9e8bd8d5a5
---

# Verify background events


After you connect to your hotspot network, check that the background event is launched. If not, check the following:

-   **Did Windows detect your hotspot?** If so, the network list should indicate a limited connection. If Windows detects connectivity to the Internet after connecting to the network, no hotspot authentication actions are taken.

-   **Did Windows detect WISPr on your hotspot?** If so, the background event will fire or the user will be prompted for credentials. If Windows opens the browser instead, WISPr was not detected. Check that the XML message is present in the browser’s redirect page and that it conforms to the WISPr specification.

-   **Is your app correctly associated with the profile?** If so, the background event will fire. If not, the user will be prompted for credentials upon manually connecting to the network. Check that the application family name specified as the ExtensionId matches your application and that provisioning was successful.

Next, check that you can successfully authenticate to the network. In particular, you should cover the following cases:

-   **Successful authentication** In the ideal case, your app can provide credentials and connect the user to the network.

-   **User interaction** If you need to interact with the user in certain cases, ensure that your app launches to the correct context to perform the interaction, and not simply to your app’s home page.

-   **Unsuccessful authentication** Particularly when using prefixes, you should handle the possibility that a network matches your prefix, but that you cannot generate credentials for it. In this case, you should stop authentication.

-   **Access denied** In certain cases, your app will receive the background event, but might not be able to retrieve the details of the authentication attempt. In this case, your background event should stop cleanly as soon as possible.

## <span id="related_topics"></span>Related topics


[Get started with a hotspot authentication app](get-started-with-a-hotspot-authentication-app.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Verify%20background%20events%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





