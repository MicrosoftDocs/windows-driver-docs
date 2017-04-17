---
title: WISPr authentication
description: WISPr authentication
ms.assetid: 49782d7f-c2f9-408d-971c-1af4d93d4d8d
---

# WISPr authentication


A Wireless Internet Service Provider roaming (WISPr)-capable hotspot includes a payload in its captive portal page that is similar to the following:

``` syntax
<HTML> 
<!--
    <?xml version=”1.0” encoding=”UTF-8”?>
    <WISPAccessGatewayParam xmlns:xsi=”http://www.w3.org/2001/XMLSchema-instance”
      xsi:noNamespaceSchemaLocation=”http://www.acmewisp.com/WISPAccessGatewayParam.xsd”>
      <Redirect>
        <AccessProcedure>1.0</AccessProcedure>
        <AccessLocation>Hotel Contoso Guest Network</AccessLocation>
        <LocationName>Hotel Contoso</LocationName>
        <LoginURL>https://captiveportal.com/login</LoginURL>
        <MessageType>100</MessageType>
        <ResponseCode>0</ResponseCode>
      </Redirect>
    </WISPAccessGatewayParam>
--> 
</HTML>
```

A smart client, such as Windows, interprets this XML (which is contained in an HTML comment to avoid its display to customers), to learn where the user’s credentials must be submitted.

When a customer manually connects to a WISPr-capable network, they see the following prompt:

![wispr prompt](images/fig1-mb-wispr-auth-prompt.jpg)

Customers who select **No, I need to sign up** are directed to your captive portal. Customers who select **Yes, I’ll enter my user name and password** are prompted to enter their credentials. These credentials are provided to your website, and the user is connected after successfully authentication.

A mobile broadband app can automatically supply credentials or replace the credentials prompt by using a tailored purchase or authentication flow. This requires that the network support WISPr, and that the app be installed before the user connects to the network.

If your network offers WISPr to clients by using certain UserAgent strings, the user will not see this prompt and cannot manually enter credentials. However, your app can still participate in WISPr authentication by including the appropriate UserAgent when it creates the network profile.

The following topics are included in this section:

-   [Provisioning for hotspot authentication](provisioning-for-hotspot-authentication.md)

-   [Handling large numbers of SSIDs](handling-large-numbers-of-ssids.md)

-   [Handling the hotspot authentication event](handling-the-hotspot-authentication-event.md)

## <span id="related_topics"></span>Related topics


[Hotspot authentication methods](hotspot-authentication-methods.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20WISPr%20authentication%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





