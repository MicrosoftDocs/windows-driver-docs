---
title: Handling large numbers of SSIDs
description: Handling large numbers of SSIDs
ms.assetid: 52bcfbd4-98f6-43e3-b697-c632f6660717
---

# Handling large numbers of SSIDs


This topic describes ways to handle the requirement for large numbers of SSIDs.

Windows 8.1 and Windows 10 significantly improve support for a large number of SSIDs by increasing the amount of SSIDs that can be configured in a single WLAN profile. A WLAN profile can now contain up to 10,000 SSIDs. Additionally, WLAN profiles support SSID prefixes.

The following sections are included in this topic:

-   [Multiple SSIDs per profile](#multssidpro)

-   [Secondary SSIDs](#secssd)

-   [Prefixes](#prefixes)

-   [Example profile](#example)

## <span id="multssidpro"></span><span id="MULTSSIDPRO"></span>Multiple SSIDs per profile


If you are provisioning Windows 8, Windows 8.1, or Windows 10 to connect to several SSIDs, we recommend that you provide multiple SSIDs per profile. This greatly reduces the size of the provisioning file and improves the responsiveness of the computer.

If you intend to use APIs to mark a network that should no longer be used, be aware that these actions apply to all SSIDs that are covered by the same profile. Therefore, it is a best practice to group related SSIDs in a single profile.

You can have a maximum of ten profiles that can each have 25 primary SSIDs in Windows 8 and up to 10,000 SSIDs in Windows 8.1. In Windows 8.1, there are two separate XML namespaces for SSIDs. The v1 namespace supports up to 25 SSIDs as in Windows 8. The v2 namespace supports up to 10,000 SSIDs. A profile must have at least one SSID in the v1 namespace and can have up to 10,000 SSIDs in total.

## <span id="secssd"></span><span id="SECSSD"></span>Secondary SSIDs


Windows 8 introduced the concept of secondary SSIDs inside the HotspotAuth section of the WLAN profile to extend the amount of SSIDs that are covered by a profile. This is still supported in Windows 8.1 and Windows 10, but we recommend using the SSID section of the WLAN profile instead to support auto-connect scenarios.

To configure more than 25 SSIDs per profile in Windows 8, you can specify secondary SSIDs for each profile in the SSIDConfig note of the HotspotAuth section. This does not create additional profiles for these networks, but associates the Hotspot settings from the profile together with that SSID.

If the user manually connects in the future and creates a new profile, the hotspot settings from this profile are automatically associated with the user-created profile. Because secondary SSIDs do not auto connect unless the user manually connects to them one time, these should be less common networks that most users do not encounter.

You can have a maximum of 250 secondary SSIDs per profile.

## <span id="prefixes"></span><span id="PREFIXES"></span>Prefixes


To associate with a particularly large or dynamic set of SSIDs, the SSID list can contain prefixes in addition to static SSIDs. This allows you to associate your mobile broadband app with a broad set of SSIDs that have four or more octets in common at the beginning of the SSID.

In Windows 8, SSID prefixes are supported in the secondary SSID list only. In Windows 8.1 and Windows 10, SSID prefixes are supported in the SSIDConfig section of the WLAN profile using the v2 namespace.

## <span id="example"></span><span id="EXAMPLE"></span>Example profile


This section shows an example profile containing an SSID in the v1 and v2 namespace each as well as an SSID prefix.

``` syntax
<WLANProfile xmlns="http://www.microsoft.com/networking/CarrierControl/WLAN/v1"
             xmlns:v2="http://www.microsoft.com/networking/CarrierControl/WLAN/v2">
  <name>SampleProfile</name>
  <SSIDConfig>
    <SSID>
        <name>MySSID1</name>
    </SSID>
    <v2:SSID>
        <v2:name>MySSID2</v2:name>
    </v2:SSID>
    <v2:SSIDPrefix>
        <v2:name>MySSIDPrefix</v2:name>
    </v2:SSIDPrefix>
  </SSIDConfig>
  <MSM>
    <security>
        <authEncryption>
            <authentication>open</authentication>
            <encryption>none</encryption>
            <useOneX>false</useOneX>
        </authEncryption>
    </security>
  </MSM>
</WLANProfile>
```

## <span id="related_topics"></span>Related topics


[WISPr authentication](wispr-authentication.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Handling%20large%20numbers%20of%20SSIDs%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





