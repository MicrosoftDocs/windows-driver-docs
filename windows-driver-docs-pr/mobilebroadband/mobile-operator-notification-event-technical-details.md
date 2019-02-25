---
title: Mobile operator notification event technical details
description: Mobile operator notification event technical details
ms.assetid: 639f238a-4bb4-4ac0-9b59-92a761dbc351
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mobile operator notification event technical details


This topic explains the technical details of a mobile operator notification event.

-   [Event payload](#eventpl)

-   [Register for the MobileOperatorNotification event by using metadata](#regmd)

-   [Define filtering rules in provisioning XML](#deffilter)

## <span id="eventpl"></span><span id="EVENTPL"></span>Event payload


The MobileOperatorNotification event payload includes the following fields:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>MessageType</strong></p></td>
<td><p>Enumeration of the message that triggered the event.</p></td>
</tr>
<tr class="even">
<td><p><strong>Interface</strong></p></td>
<td><p>The GUID that corresponds to the physical interface that is associated with the event.</p></td>
</tr>
<tr class="odd">
<td><p><strong>EncodingType</strong></p></td>
<td><p>The encoding method for the message, if <strong>MessageType</strong> is SMS/USSD.</p></td>
</tr>
<tr class="even">
<td><p><strong>MessageDataSize</strong></p></td>
<td><p>The size of the message, in bytes, if <strong>MessageType</strong> is SMS/USSD.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Message</strong></p></td>
<td><p>The raw message that is received, if <strong>MessageType</strong> is SMS/USSD.</p></td>
</tr>
</tbody>
</table>

 

The MobileOperatorNotification event enables each of the scenarios that are described in [Mobile operator notification scenarios](mobile-operator-notification-scenarios.md) by differentiating them by using the **MessageType** field in the event payload. The **MessageType**s are enumerated as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Enumeration</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>GSM SMS</p></td>
</tr>
<tr class="even">
<td><p>1</p></td>
<td><p>CDMA SMS</p></td>
</tr>
<tr class="odd">
<td><p>2</p></td>
<td><p>USSD</p></td>
</tr>
<tr class="even">
<td><p>3</p></td>
<td><p>DataPlanThresholdReached</p></td>
</tr>
<tr class="odd">
<td><p>4</p></td>
<td><p>DataPlanReset</p></td>
</tr>
<tr class="even">
<td><p>5</p></td>
<td><p>DataPlanDeleted</p></td>
</tr>
<tr class="odd">
<td><p>6</p></td>
<td><p>ProfileConnected</p></td>
</tr>
<tr class="even">
<td><p>7</p></td>
<td><p>ProfileDisconnected</p></td>
</tr>
<tr class="odd">
<td><p>8</p></td>
<td><p>RegisteredRoaming</p></td>
</tr>
<tr class="even">
<td><p>9</p></td>
<td><p>RegisteredHome</p></td>
</tr>
<tr class="odd">
<td><p>10</p></td>
<td><p>TetheringEntitlementCheck</p></td>
</tr>
</tbody>
</table>

 

The work item that is associated with the MobileOperatorNotification event should start with logic that effectively differentiate the **MessageType**, and runs the appropriate code for each scenario.

### <span id="gsmetc"></span><span id="GSMETC"></span>GSM/CDMA SMS and USSD

An incoming operator message, including SMS and USSD, triggers the MobileOperatorNotification event together with the appropriate corresponding **MessageType**s. Unique to these types are **EncodingType**, **MessageDataSize**, and **Message**.

### <span id="DataPlanThresholdReached"></span><span id="dataplanthresholdreached"></span><span id="DATAPLANTHRESHOLDREACHED"></span>DataPlanThresholdReached

By default, this message type is disabled. You can enable it by using provisioning metadata to specify the [**DataUsageInMobileOperatorNotificationEnabled**](https://msdn.microsoft.com/library/windows/apps/hh868368) field, as shown here.

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
          <Password>pass</Password>
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

1.  When connected to a home network (non-roaming), if the data plan limit has not been specified, this event is triggered at every 100 MB of local data usage.

2.  When connected to a roaming network, the data plan limit does not apply and this event is triggered at every 5 MB of local data usage.

The local data counters in Windows 8 are updated every one minute; at most, this event is generated one time per minute in all described scenarios. In Windows 8.1 the event is delivered in real-time when the 5% threshold has been reached.

**Note**  
Although this information is a good first-order guide, Windows cannot account for unbilled traffic or for usage on other devices that share the same data limits (such as family plans or SIM-swapping). Mobile operator apps should use local data counters only to approximate usage since the last sync with the operator’s own billing system. For data usage that has already been processed, the billing system should be considered authoritative.

 

### <span id="DataPlanReset"></span><span id="dataplanreset"></span><span id="DATAPLANRESET"></span>DataPlanReset

On the plan reset date, the Data Usage and Subscription Manager (DUSM) resets the user’s current local data usage to zero.

### <span id="DataPlanDeleted"></span><span id="dataplandeleted"></span><span id="DATAPLANDELETED"></span>DataPlanDeleted

For pre-paid data plans that have a fixed expiration date, the DUSM deletes the connection profile that is associated with the account on the expiration date and the MobileOperatorNotification event is triggered by using this **MessageType**. When the connection profile is deleted, Windows Connection Manager no longer tries to automatically connect to the network that is described by the connection profile.

### <span id="ProfileConnected_and_ProfileDisconnected"></span><span id="profileconnected_and_profiledisconnected"></span><span id="PROFILECONNECTED_AND_PROFILEDISCONNECTED"></span>ProfileConnected and ProfileDisconnected

The MobileOperatorNotification event is generated with these **MessageType**s when Windows Connection Manager connects to the network profile that is provided by the operator experience metadata. This event is triggered on every connect and disconnect, including the initial connection that follows a sleep/resume. It is also triggered if the device is already connected when the app and service metadata are downloaded and installed.

The ProfileConnected MessageType is triggered on L2 connectivity for the mobile broadband interface.

**Note**  
This trigger occurs before network identification is complete. The [**NetworkStatusChanged**](https://msdn.microsoft.com/library/windows/apps/br207299) event (part of the [**NetworkInformation**](https://msdn.microsoft.com/library/windows/apps/br207293) API) is generated when network identification determines the connectivity level of the network. For more information about network identification, see [Quickstart: Retrieving network connection information](https://msdn.microsoft.com/library/windows/apps/hh452990) and the **NetworkInformation** class.

 

### <span id="RegisteredRoaming_and_RegisteredHome"></span><span id="registeredroaming_and_registeredhome"></span><span id="REGISTEREDROAMING_AND_REGISTEREDHOME"></span>RegisteredRoaming and RegisteredHome

The MobileOperatorNotification event is generated with these **MessageType**s when Windows Connection Manager registers to a roaming network. This event is triggered on every registration, including the initial registration following a sleep/resume. It is also triggered if the device is already registered to the network when the app and service metadata are downloaded and installed.

The app should only notify the user one time when they register on a roaming network and one time when they return to their home network. Because this event is triggered at every registration, the app is responsible for keeping track of the previous registered state in the app’s session data.

### <span id="TetheringEntitlementCheck"></span><span id="tetheringentitlementcheck"></span><span id="TETHERINGENTITLEMENTCHECK"></span>TetheringEntitlementCheck

The MobileOperatorNotification event is generated with this **MessageType**s when the user turns on Internet Sharing. The event is triggered every time the user tries to use Internet Sharing as long as the mobile operator has set the [AllowTethering](allowtethering.md) element in the service metadata schema to **EntitlementCheckRequired**. For more info about the service metadata schema, see [Service metadata package schema reference](service-metadata-package-schema-reference.md).

The app should run the appropriate entitlement check mechanism supported by the mobile operator network and send the outcome to the system by using the [**AuthorizeTethering**](https://msdn.microsoft.com/library/windows/apps/dn266090) method of the [**NetworkOperatorNotificationEventDetails**](https://msdn.microsoft.com/library/windows/apps/br207377) class in the [**Windows.Networking.NetworkOperators**](https://msdn.microsoft.com/library/windows/apps/br241148) namespace. If the app does not have the capability to run the entitlement check, the mobile operator should change the Service Metadata [AllowTethering](allowtethering.md) element to **Always** or **Never**, so that the event is never generated.

## <span id="regmd"></span><span id="REGMD"></span>Register for the MobileOperatorNotification event by using metadata


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

### <span id="Change_background_task_registration_in_metadata"></span><span id="change_background_task_registration_in_metadata"></span><span id="CHANGE_BACKGROUND_TASK_REGISTRATION_IN_METADATA"></span>Change background task registration in metadata

If the background task entry point is changed in an updated version of the mobile broadband app, the [DeviceNotificationHandler](devicenotificationhandler.md) element in the service metadata must also be changed.

Service metadata is updated automatically on computers running Windows 8, Windows 8.1, and Windows 10. Mobile broadband apps are updated in the Microsoft Store. You should avoid changing the [DeviceNotificationHandler](devicenotificationhandler.md) background task registration in service metadata. If a change is required, the service metadata should contain references to all the different background task entry points used in all your supported versions of the mobile broadband app to preserve functionality for users who haven’t updated the mobile broadband app.

## <span id="deffilter"></span><span id="DEFFILTER"></span>Define filtering rules in provisioning XML


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
                    <Password>password</Password>
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

-   **Allowed sender** The Sender attribute specifies the reserved sender address from which the notification is allowed to arrive. (This number must exactly match the sender number that is received in the SMS message, including the international format).

-   **Pattern** The regular expression to identify and optionally extract the data fields from the text message. To match all messages from a sender, use pattern `[^]*`.

## <span id="related_topics"></span>Related topics


[Enabling mobile operator notifications and system events](enabling-mobile-operator-notifications-and-system-events.md)

[Creating and configuring Internet Sharing experiences](creating-and-configuring-internet-sharing-experiences.md)

 

 






