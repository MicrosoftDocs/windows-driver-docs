---
title: Mobile operator notification event technical details
description: Mobile operator notification event technical details
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mobile operator notification event technical details

This topic explains the technical details of a mobile operator notification event.

- [Event payload](#event-payload)

- [Register for the MobileOperatorNotification event by using metadata](#register-for-the-mobileoperatornotification-event-by-using-metadata)

- [Define filtering rules in provisioning XML](#define-filtering-rules-in-provisioning-xml)

## Event payload

The MobileOperatorNotification event payload includes the following fields:

|Field|Description|
|----|----|
|**MessageType**|Enumeration of the message that triggered the event.|
|**Interface**|The GUID that corresponds to the physical interface that is associated with the event.|
|**EncodingType**|The encoding method for the message, if **MessageType** is SMS/USSD.|
|**MessageDataSize**|The size of the message, in bytes, if **MessageType** is SMS/USSD.|
|**Message**|The raw message that is received, if **MessageType** is SMS/USSD.|

The MobileOperatorNotification event enables each of the scenarios that are described in [Mobile operator notification scenarios](mobile-operator-notification-scenarios.md) by differentiating them by using the **MessageType** field in the event payload. The **MessageType**s are enumerated as follows:

|Enumeration|Type|
|----|----|
|0|GSM SMS|
|1|CDMA SMS|
|2|USSD|
|3|DataPlanThresholdReached|
|4|DataPlanReset|
|5|DataPlanDeleted|
|6|ProfileConnected|
|7|ProfileDisconnected|
|8|RegisteredRoaming|
|9|RegisteredHome|
|10|TetheringEntitlementCheck|

The work item that is associated with the MobileOperatorNotification event should start with logic that effectively differentiate the **MessageType**, and runs the appropriate code for each scenario.

### GSM/CDMA SMS and USSD

An incoming operator message, including SMS and USSD, triggers the MobileOperatorNotification event together with the appropriate corresponding **MessageType**s. Unique to these types are **EncodingType**, **MessageDataSize**, and **Message**.

### DataPlanThresholdReached

By default, this message type is disabled. You can enable it by using provisioning metadata to specify the [**DataUsageInMobileOperatorNotificationEnabled**](/uwp/schemas/mobilebroadbandschema/plans/element-datausageinmobileoperatornotificationenabled) field, as shown here.

``` syntax
<?xml version="1.0"?>
<CarrierProvisioning xmlns="http://www.microsoft.com/networking/CarrierControl/v1">
  <Global>
    <CarrierId>{2c85b76b-f859-47c4-8122-721fe8b6c25f}</CarrierId>
    <SubscriberId>012345678901234</SubscriberId>
  </Global>
  <MBNProfiles>
    <DefaultProfile xmlns="http://www.microsoft.com/networking/CarrierControl/WWAN/v1">
      <Name>Contoso</Name>
      <AssociatedPlan>SamplePlan</AssociatedPlan>
      <Context>
        <AccessString>Contoso.com</AccessString>
        <UserLogonCred>
          <UserName>User</UserName>
          <Password>[PLACEHOLDER]</Password>
        </UserLogonCred>
      </Context>
    </DefaultProfile>
  </MBNProfiles>
  <Plans>
    <Plan xmlns="http://www.microsoft.com/networking/CarrierControl/Plans/v1" Name="SamplePlan">
      <Description PlanType="Fixed">
        <DataLimitInMegabytes>500</DataLimitInMegabytes>
        <DataUsageInMobileOperatorNotificationEnabled>true</DataUsageInMobileOperatorNotificationEnabled>
      </Description>
    </Plan>
  </Plans>
</CarrierProvisioning>
```

For more info about account provisioning metadata, see [Account provisioning](account-provisioning.md).

The event is generated with this **MessageType** when the local data counters estimate that usage (bytes sent and received) on the mobile broadband interface has changed by 5% since the last occurrence, except in the following cases:

1. When connected to a home network (non-roaming), if the data plan limit has not been specified, this event is triggered at every 100 MB of local data usage.

2. When connected to a roaming network, the data plan limit does not apply and this event is triggered at every 5 MB of local data usage.

The local data counters in Windows 8 are updated every one minute; at most, this event is generated one time per minute in all described scenarios. In Windows 8.1 the event is delivered in real-time when the 5% threshold has been reached.

>[!NOTE]
>Although this information is a good first-order guide, Windows cannot account for unbilled traffic or for usage on other devices that share the same data limits (such as family plans or SIM-swapping). Mobile operator apps should use local data counters only to approximate usage since the last sync with the operator’s own billing system. For data usage that has already been processed, the billing system should be considered authoritative.

### DataPlanReset

On the plan reset date, the Data Usage and Subscription Manager (DUSM) resets the user’s current local data usage to zero.

### DataPlanDeleted

For pre-paid data plans that have a fixed expiration date, the DUSM deletes the connection profile that is associated with the account on the expiration date and the MobileOperatorNotification event is triggered by using this **MessageType**. When the connection profile is deleted, Windows Connection Manager no longer tries to automatically connect to the network that is described by the connection profile.

### ProfileConnected and ProfileDisconnected

The MobileOperatorNotification event is generated with these **MessageType**s when Windows Connection Manager connects to the network profile that is provided by the operator experience metadata. This event is triggered on every connect and disconnect, including the initial connection that follows a sleep/resume. It is also triggered if the device is already connected when the app and service metadata are downloaded and installed.

The ProfileConnected MessageType is triggered on L2 connectivity for the mobile broadband interface.

>[!NOTE]
>This trigger occurs before network identification is complete. The [**NetworkStatusChanged**](/uwp/api/Windows.Networking.Connectivity.NetworkInformation#Windows_Networking_Connectivity_NetworkInformation_NetworkStatusChanged) event (part of the [**NetworkInformation**](/uwp/api/Windows.Networking.Connectivity.NetworkInformation) API) is generated when network identification determines the connectivity level of the network. For more information about network identification, see [Quickstart: Retrieving network connection information](/previous-versions/windows/apps/hh452990(v=win.10)) and the **NetworkInformation** class.

### RegisteredRoaming and RegisteredHome

The MobileOperatorNotification event is generated with these **MessageType**s when Windows Connection Manager registers to a roaming network. This event is triggered on every registration, including the initial registration following a sleep/resume. It is also triggered if the device is already registered to the network when the app and service metadata are downloaded and installed.

The app should only notify the user one time when they register on a roaming network and one time when they return to their home network. Because this event is triggered at every registration, the app is responsible for keeping track of the previous registered state in the app’s session data.

### TetheringEntitlementCheck

The MobileOperatorNotification event is generated with this **MessageType**s when the user turns on Internet Sharing. The event is triggered every time the user tries to use Internet Sharing as long as the mobile operator has set the [AllowTethering](allowtethering.md) element in the service metadata schema to **EntitlementCheckRequired**. For more info about the service metadata schema, see [Service metadata package schema reference](mobilebroadbandinfo-xml-schema.md).

The app should run the appropriate entitlement check mechanism supported by the mobile operator network and send the outcome to the system by using the [**AuthorizeTethering**](/uwp/api/Windows.Networking.NetworkOperators.NetworkOperatorNotificationEventDetails#Windows_Networking_NetworkOperators_NetworkOperatorNotificationEventDetails_AuthorizeTethering_System_Boolean_System_String_) method of the [**NetworkOperatorNotificationEventDetails**](/uwp/api/Windows.Networking.NetworkOperators.NetworkOperatorNotificationEventDetails) class in the [**Windows.Networking.NetworkOperators**](/uwp/api/Windows.Networking.NetworkOperators) namespace. If the app does not have the capability to run the entitlement check, the mobile operator should change the Service Metadata [AllowTethering](allowtethering.md) element to **Always** or **Never**, so that the event is never generated.

## Register for the MobileOperatorNotification event by using metadata

In general, an app must be run by the user at least one time before it can register work items with the System Event broker. However, because the MobileOperatorNotification events are required to complete key mobile broadband scenarios, this event is associated with the mobile broadband app by using service metadata. In the service metadata, configure the [DeviceCompanionApplications](devicecompanionapplications.md) element.

``` syntax
<DeviceCompanionApplications>
  <Package>
    <Identity Name="MyOperatorNotification" Publisher="MyCorporation " />
    <Applications>
      <Application Id="MyOperatorNotification" />
        <DeviceNotificationHandlers>
          <DeviceNotificationHandler EventID="MobileOperatorNotificationHandler" EventAsset="backgroundtask.js" />
      </DeviceNotificationHandlers>
    </Applications>
  </Package>
</DeviceCompanionApplications>
```

The **EventID** attribute tells the system what kind of event to expect from the device. The value of the **EventAsset** attribute should point to the entry point that implements the background task. This will tell the system which task to run when that particular event has occurred.

Using this example, the system creates and registers an event that is specific to that device. It also registers the mobile broadband app for this event. The app must have a JavaScript file called backgroundtask.js that is run by the system each time that it receives an operator notification.

If the mobile broadband app is written in C#, the event asset must point to the runtime class that implements the backgroundtask interface.

``` syntax
<DeviceNotificationHandlers>
  <DeviceNotificationHandler EventID="MobileOperatorNotificationHandler" EventAsset="MNOMessageBackground.OperatorNotification" />
```

When the service metadata and app are downloaded, the Device Setup Manager registers the appropriate work item with the System Event Broker before the app is run. Immediately after the work item is registered, if the mobile broadband device is registered or connected to the network, the MobileOperatorNotification event is triggered together with the corresponding **MessageType**.

### Change background task registration in metadata

If the background task entry point is changed in an updated version of the mobile broadband app, the [DeviceNotificationHandler](devicenotificationhandler.md) element in the service metadata must also be changed.

Service metadata is updated automatically on computers running Windows 8, Windows 8.1, and Windows 10. Mobile broadband apps are updated in the Microsoft Store. You should avoid changing the [DeviceNotificationHandler](devicenotificationhandler.md) background task registration in service metadata. If a change is required, the service metadata should contain references to all the different background task entry points used in all your supported versions of the mobile broadband app to preserve functionality for users who haven’t updated the mobile broadband app.

## Define filtering rules in provisioning XML

Windows accepts an XML-based provisioning file from you. A sample version of the provisioning XML is shown here:

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<CarrierProvisioning xmlns="http://www.microsoft.com/networking/CarrierControl/v1">
    <Global>
        <!-- Adjust the Carrier ID to fit match the Service Number in service metadata. Refer to the documentation about CarrierId. -->
        <CarrierId>{11111111-1111-1111-1111-111111111111}</CarrierId>
        <!-- Adjust the Susbscriber ID. Refer to the documentation about Subscriber ID's. -->
        <SubscriberId>1234567890</SubscriberId>
    </Global>
    <MBNProfiles>
        <DefaultProfile xmlns="http://www.microsoft.com/networking/CarrierControl/WWAN/v1">
            <!-- Adjust the profile name -->
            <Name>Contoso</Name>
          <AssociatedPlan>Limited</AssociatedPlan>
            <!-- Adjust the home provider name for the given SIM/Device -->
            <HomeProviderName>Contoso</HomeProviderName>
            <Context>
                <!-- Adjust the access string to your APN. -->
                <AccessString>Contoso.Contoso</AccessString>
                <!-- Adjust the UserLogonCred to fit your UserLogonCred. Refer to the documentation about UserLogonCred's. -->
                <UserLogonCred>
                    <UserName>user</UserName>
                    <Password>[PLACEHOLDER]</Password>
                </UserLogonCred>
            </Context>
        </DefaultProfile>
      <Messages xmlns="http://www.microsoft.com/networking/CarrierControl/WWAN/v1">
        <Message RuleId="Sample1" Silent="true">
          <SMSBearer ClassZeroOnly="false" Sender="18005551212"/>
          <!-- [^]* matches all messages from this sender, regardless of content -->
          <Pattern>[^]*</Pattern>
          <!-- Because no Fields are specified, this message will be passed to the operator app without parsing. -->
        </Message>
        <Message RuleId="Sample2" Silent="false">
          <!-- Parsing a simple usage message. -->
          <USSDBearer/>
          <Pattern>(\d+\.\d+)(\w+) of (\d+)(\w+) used as of (\S+)</Pattern>
          <!-- Using these field definitions, Windows will automatically update usage data before passing the message
               to the operator app. -->
          <Units G="GB" M="MB"/>
          <Fields>
            <!-- These fields are currently unordered, but an order will be required in RC. -->
            <Usage Group="1" UnitGroup="2"/>
            <UsageTimestamp Group="5" Format="%I:%M%p on %d %b"/>
            <DataLimit Group="3" UnitGroup="4"/>
          </Fields>
        </Message>
      </Messages>
  </MBNProfiles>
  <Provisioning />
</CarrierProvisioning>
```

For more info about account provisioning metadata, see [Account provisioning](account-provisioning.md).

The rules to identify a text message as an operator message can be defined in this XML.

- **Allowed sender** The Sender attribute specifies the reserved sender address from which the notification is allowed to arrive. (This number must exactly match the sender number that is received in the SMS message, including the international format).

- **Pattern** The regular expression to identify and optionally extract the data fields from the text message. To match all messages from a sender, use pattern `[^]*`.

## Related topics

[Enabling mobile operator notifications and system events](enabling-mobile-operator-notifications-and-system-events.md)

[Creating and configuring Internet Sharing experiences](creating-and-configuring-internet-sharing-experiences.md)
