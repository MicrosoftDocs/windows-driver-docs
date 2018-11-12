---
title: Verify background events
description: Verify background events
ms.assetid: c840f555-2e09-409d-9d4f-4d9e8bd8d5a5
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 






