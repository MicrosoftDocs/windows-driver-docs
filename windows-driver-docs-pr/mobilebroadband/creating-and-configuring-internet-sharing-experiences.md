---
title: Creating and configuring Internet Sharing experiences
description: Creating and configuring Internet Sharing experiences
ms.assetid: 11906ee4-68f5-4be6-a3ab-6af3253c8a11
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating and configuring Internet Sharing experiences


Internet Sharing, commonly referred to as tethering, has been added in Windows 8.1 to enable users to share their mobile broadband network connection with one or more other devices that are not mobile broadband-capable. Traditional tethering mechanisms include Bluetooth and USB. However, Wi-Fi can provide the fast and easy mobile broadband connection sharing mechanism, such as personal hotspots, mobile hotspots, and so on, since it requires little configuration, enables high-speed data transmission, and relies on the familiar Wi-Fi connection process.

Windows 8.1 and Windows 10 extend the Internet sharing capability further by enabling customers to turn on and connect to PCs that have Internet Sharing configured, known as a tethering access point, just as if it was a standard Wi-Fi network.

## <span id="Turn_on_Internet_Sharing"></span><span id="turn_on_internet_sharing"></span><span id="TURN_ON_INTERNET_SHARING"></span>Turn on Internet Sharing


Internet Sharing can be turned on by using the Settings charm on the mobile broadband-capable device. Once Internet Sharing is turned on, any device that can connect to a Wi-Fi network can connect to it.

**To turn on Internet Sharing**

1.  From the **Settings** charm, click **Change PC settings**, and then click **Network**.

2.  Under the **Mobile Broadband** heading, click the network name.

3.  On the **Mobile Broadband** page, enable Internet Sharing for the network. If the mobile broadband network is disconnected, the device will automatically connect to the mobile broadband network before setting up the Wi-Fi network.

4.  If you have created the necessary service metadata package, the PC triggers an event telling the Microsoft Store mobile broadband app to run an entitlement check. The PC waits for the mobile broadband app to respond before Internet Sharing is turned on. For more info on creating service metadata packages, see [Developer guide for creating service metadata](developer-guide-for-creating-service-metadata.md).

5.  After the mobile broadband network is turned on and any required entitlement checks have passed, the mobile broadband connection is shared by using a private Wi-Fi network that uses Wi-Fi Direct Autonomous Group Owner mode with a customized network name. This ensures that any Wi-Fi device can connect to the network.

    **Note**  
    The icon for the mobile broadband network is automatically updated throughout Windows to help customers remember that the network is being shared by other people.

     

6.  After Internet Sharing is turned on, from the **Mobile Broadband** page, click **Edit** to change the network name and password.

    -   The Wi-Fi network must use WPA2-PSK.

    -   The network name is set to a default of *&lt;Device Name&gt; &lt;4 digits&gt;*. The default network name is optimized to ensure that the name is recognizable to the user by being short enough to fully fit in the Networks list and unique enough to distinguish among multiple devices.

    -   The password is set to a default of 12 random digits.

    -   The password must be at least 8 characters in length.

    -   The Wi-Fi network will restart when the network name or password is changed.

When Internet Sharing is turned on, the following things happen:

-   The network on the client device is automatically set as a metered connection to reduce unnecessary bandwidth consumption on the mobile broadband network. This is done by using a Windows 8 vendor-specific information element in the Wi-Fi beacon/probe response frame that defines the network cost. In Windows 8.1 another vendor-specific information element in the Wi-Fi beacon/probe response frame was added that notifies the client device if the network is a tethering network. This addition affects both Windows 8.1 and Windows 10.

-   When Internet Sharing is turned on, the PC cannot go into Connected Standby or sleep to ensure that client devices do not lose their internet connection.

-   You can see how much data has been used by client devices by using the mobile broadband app.

-   After the last client device has disconnected from the tethered network, Internet Sharing will wait for five minutes. If no other client devices connect, Internet Sharing is turned off and the PC returns to the normal power state.

-   Enterprise administrators can disable Internet Sharing by using Group Policy.

## <span id="Connect_to_a_tethered_network"></span><span id="connect_to_a_tethered_network"></span><span id="CONNECT_TO_A_TETHERED_NETWORK"></span>Connect to a tethered network


You can connect to a tethered network using a Wi-Fi device in the same way you connect to any other Wi-Fi network. However, if a user connects to a tethered network with the same Microsoft account credentials on both devices running Windows 8.1 or Windows 10, the following things happen:

-   If Internet Sharing is not turned on when the Windows 8.1 or Windows 10 device connects, the two devices create a Bluetooth connection and Internet Sharing is turned on.

-   The connection is automatically configured (network name and SSID) by automatically retrieving the credentials from the tethered network.

**Note**  
Users can also connect to a tethering access point if they have paired their devices by using Bluetooth.

 

## <span id="Configure_Internet_Sharing"></span><span id="configure_internet_sharing"></span><span id="CONFIGURE_INTERNET_SHARING"></span>Configure Internet Sharing


Some mobile network operators (MNOs) or mobile virtual network operators (MVNOs) do not support Internet Sharing on their network, or they require an entitlement check prior to setting up Internet Sharing. Windows provides the necessary controls to ensure that Windows devices comply with network policies. 

To do this in Windows 8, Windows 8.1, or Windows 10 prior to version 1803, you must author a service metadata package and configure the [AllowTethering](allowtethering.md) element in the schema ([Service metadata package schema reference](service-metadata-package-schema-reference.md)). For more info about creating a service metadata package, see [Developer guide for creating service metadata](developer-guide-for-creating-service-metadata.md). There are three options:

-   Allow Internet Sharing for all customers. (default value if not specified in the service metadata package)

-   Block Internet Sharing for all customers

-   Allow Internet Sharing for customers after an entitlement check

To do this in Windows 10, version 1803 and later, you must set the [**Hotspot** setting in the COSA database](desktop-cosa-apn-database-settings.md#desktop-cosa-only-settings) to the appropriate value.

If you decide that an entitlement check is not required, no additional information or capabilities are needed. If an entitlement check is required, you must also provide a background notification event handler that is part of your UWP mobile broadband app. In Windows 10, version 1803 and later, use the methods in the [TetheringEntitlementCheckTriggerDetails](https://docs.microsoft.com/uwp/api/windows.networking.networkoperators.tetheringentitlementchecktriggerdetails) class to handle Windows notification events for checking tethering entitlement. For earlier versions of Windows, use the [**NetworkOperatorNotificationEventDetails**](https://msdn.microsoft.com/library/windows/apps/br207377) class. For more info on creating the background notification event handler, see [Enabling mobile operator notifications and system events](enabling-mobile-operator-notifications-and-system-events.md).

MOs and MVNOs have different requirements on what PDP context should be used for Internet Sharing. Windows has updated the existing [provisioning XML schema](https://msdn.microsoft.com/library/windows/apps/hh868398) to enable you to provision the system with the correct Internet Sharing PDP context information. For more information about multiple PDP contexts, see [Developing apps using multiple PDP contexts](developing-apps-using-multiple-pdp-contexts.md).

You can also configure the maximum number of concurrent connected client devices is 10. You can change this number to anything between 3 and 10 by using [Account provisioning](account-provisioning.md).

To help ensure that your users don’t accidentally run over their data, you can show data usage statistics to your customers for shared and non-shared traffic in your mobile broadband app by using the [**GetNetworkUsageAsync**](https://msdn.microsoft.com/library/windows/apps/dn266073) method of the [**ConnectionProfile**](https://msdn.microsoft.com/library/windows/apps/br207249) class.

## <span id="Create_a_custom_Internet_Sharing_app"></span><span id="create_a_custom_internet_sharing_app"></span><span id="CREATE_A_CUSTOM_INTERNET_SHARING_APP"></span>Create a custom Internet Sharing app


For most operators, the Windows user interface will provide the best experience for Internet Sharing. However, in order to create a consistent experience across all their devices and hardware, you may choose to include your own Internet Sharing user experience in your mobile broadband app or other app that has been given privileged access to the mobile broadband device. Windows provides several new APIs in the [**Windows.Networking.NetworkOperators namespace**](https://msdn.microsoft.com/library/windows/apps/br241148) to enable your app to do the following:

-   Ensure the system is capable of Internet Sharing

-   Turn on and off Internet Sharing

-   Query and configure the Wi-Fi SSID and passphrase for the network

-   Run an entitlement check

-   Query the number of connected devices, as well as the maximum number of connected devices allowed

-   Receive and react to notifications about a change in the Internet Sharing status or number of connected devices

 

 





