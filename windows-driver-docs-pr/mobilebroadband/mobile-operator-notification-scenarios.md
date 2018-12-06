---
title: Mobile operator notification scenarios
description: Mobile operator notification scenarios
ms.assetid: 3749d9ab-3dff-4216-a23b-0e75c04d9a22
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mobile operator notification scenarios


This topic explains that scenarios when you would use a mobile operator notification with your mobile broadband app.

-   [Connect to and disconnect from mobile broadband](#conndis)

-   [Network operator messages](#netopmsg)

-   [Triggering data usage and roaming notifications locally](#trigloc)

-   [Data plan expiration and usage reset](#expire)

-   [Entitlement check for Internet Sharing](#sharing)

## <span id="conndis"></span><span id="CONNDIS"></span>Connect to and disconnect from mobile broadband


Windows Connection Manager monitors available networks across Wi-Fi, mobile broadband, and Ethernet. It makes automatic connect and disconnect decisions based on the available networks. When Windows Connection Manager connects to and disconnects from a mobile broadband profile, a [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) background event is triggered. This event enables the mobile broadband app to perform necessary logic when the user connects to their network, such as verifying account status, retrieving the most recent data usage, or displaying notifications and tile updates.

## <span id="netopmsg"></span><span id="NETOPMSG"></span>Network operator messages


The mobile broadband platform in Windows 8, Windows 8.1, and Windows 10 provides enhanced functionality that is available to a mobile broadband app only, for receiving and displaying incoming SMS and USSD administrative messages. These messages can be used for user notification, such as approaching data usage cap, international roaming, low balance, or to trigger a response from you mobile broadband app.

The app handles the incoming message as appropriate. Likely responses include any or all of the following:

-   Immediately syncing current data usage

-   Updating the mobile broadband app’s tile

-   Retrieving and applying updated operator provisioning XML

-   Displaying a notification to the user

If you want to display the message in the app, the background task that is triggered by the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event must read the message contents and store the message contents in the app’s own local data storage. The mobile broadband SMS platform does not maintain a queue of received administrative SMS notifications.

### <span id="Mobile_network_operator_SMS_notifications"></span><span id="mobile_network_operator_sms_notifications"></span><span id="MOBILE_NETWORK_OPERATOR_SMS_NOTIFICATIONS"></span>Mobile network operator SMS notifications

Incoming SMS messages are available to any app that has requested and been granted access to the SMS capabilities on the computer. However, some SMS messages come directly from the carrier and should be restricted to and handled by the mobile broadband app.

The mobile broadband SMS platform filters each new received SMS into one of two types: administrative (silent) SMS notifications from a Mobile Network Operator (MNO), and general SMS messages. Administrative SMS notifications that are received from an MNO are only accessible to the mobile broadband app and are hidden from general SMS client apps.

MNOs specify custom filtering rules for administrative SMS and USSD notifications in the account provisioning metadata. If no message filtering rules are specified, the SMS platform classifies all SMS messages as general SMS messages that are available to any app. If an incoming SMS matches the provisioned filtering rules, the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event is triggered and the background work item can handle the incoming SMS message.

### <span id="Network-initiated_USSD"></span><span id="network-initiated_ussd"></span><span id="NETWORK-INITIATED_USSD"></span>Network-initiated USSD

Windows 8, Windows 8.1, and Windows 10 provide a USSD API, which is an abstraction of the underlying USSD protocol that hides most of the details to simplify app development. Upon receiving a network-initiated USSD that matches the provisioned filtering rules, the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event is trigged and the corresponding background work item can communicate over the USSD session by using the USSD API.

For more information about USSD APIs, see [**Windows.Networking.NetworkOperators**](https://msdn.microsoft.com/library/windows/apps/br241148) namespace.

## <span id="trigloc"></span><span id="TRIGLOC"></span>Triggering data usage and roaming notifications


In many areas, MNOs are required by regulatory laws to notify a user when the user reaches their data usage limit or is roaming on a more costly network. This consumer protection mitigates the risk of excessive usage charges. In Windows, the mobile broadband app can show toast notifications and tile updates to make the user aware of the data usage and roaming states. These notifications can be initiated from your network back-end by using SMS or USSD, which trigger the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) events. Alternatively, the MobileOperatorNotification event can be triggered by using local information in the following cases.

### <span id="Data_usage_notification_by_using_local_data_counters"></span><span id="data_usage_notification_by_using_local_data_counters"></span><span id="DATA_USAGE_NOTIFICATION_BY_USING_LOCAL_DATA_COUNTERS"></span>Data usage notification by using local data counters

1.  You enable local data usage notifications by using provisioning metadata.

2.  Local data counters estimate that usage on the profile has changed by more than 5% of the user’s data limit since the last update.

3.  The Data Usage and Subscription Manager (DUSM) notifies the System Event Broker to trigger the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event.

4.  The System Event Broker invokes the mobile broadband app to handle the background event.

5.  The app handles the event by retrieving the most current usage information from your back-end infrastructure.

6.  If the current usage information exceeds a threshold (such as 80%), the app displays a toast notification to the user and updates the DUSM with the current usage. Alternatively, if the current usage does not exceed a threshold, the app does not need to display the toast notification.

### <span id="Roaming_notification_by_using_Windows_Connection_Manager"></span><span id="roaming_notification_by_using_windows_connection_manager"></span><span id="ROAMING_NOTIFICATION_BY_USING_WINDOWS_CONNECTION_MANAGER"></span>Roaming notification by using Windows Connection Manager

1.  Windows Connection Manager registers on a roaming mobile broadband network.

2.  Windows Connection Manager notifies the System Event Broker to trigger the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event.

3.  The System Event Broker invokes the mobile operator app to handle the background event.

4.  The app identifies whether the user will incur additional usage charges when roaming on this network and if necessary, displays a toast notification and tile updates to the user.

## <span id="expire"></span><span id="EXPIRE"></span>Data plan expiration and usage reset


The DUSM tracks details about the user’s account or accounts, including the plan expiration date for pre-paid data plans, or the plan usage reset date for post-paid data plans. When the user’s data plan expires, the DUSM notifies the System Event Broker to trigger the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event. The mobile broadband app can handle the event by displaying a toast notification and tile update to the user, informing them that their plan has expired or directing them to renew their service.

In the case of a post-paid data plan, the DUSM will reset the plan data usage to zero on a particular date, such as the first day of the month. When this occurs, the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event is triggered and the app can notify the user of their updated data usage.

## <span id="sharing"></span><span id="SHARING"></span>Entitlement check for Internet Sharing


In Windows 8.1, Internet Sharing, commonly referred to as tethering, has been added to enable users to share their mobile broadband network connection with one or more other devices that are not mobile broadband-capable. Traditional tethering mechanisms include Bluetooth and USB. However, Wi-Fi can provide the fast and easy mobile broadband connection sharing mechanism, such as personal hotspots, mobile hotspots, and so on, since it requires little configuration, enables high-speed data transmission, and relies on the familiar Wi-Fi connection process.

Some MNOs or MVNOs do not support Internet Sharing features on their network or they require an entitlement check prior to setting up an Internet Sharing connection. Windows provides the necessary controls to ensure that Windows devices comply with network policies. If the mobile operator has set the [AllowTethering](allowtethering.md) element to **EntitlementCheckRequired** in the service metadata package, the system will trigger the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event. The mobile broadband app then communicates with a network service to check whether or not the user is allowed to use the Internet Sharing feature and responds back to the system. If the user is allowed to use the feature, Internet Sharing will successfully start, otherwise the user will be shown either a default error message or a message defined by the mobile operator.

## <span id="related_topics"></span>Related topics


[Enabling mobile operator notifications and system events](enabling-mobile-operator-notifications-and-system-events.md)

[Creating and configuring Internet Sharing experiences](creating-and-configuring-internet-sharing-experiences.md)

 

 






