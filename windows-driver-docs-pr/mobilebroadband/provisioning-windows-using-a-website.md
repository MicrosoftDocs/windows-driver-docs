---
title: Provisioning Windows using a website
description: Provisioning Windows using a website
ms.assetid: ba60fddd-a248-4afb-9390-f9277ef1f094
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Provisioning Windows using a website


This topic describes how to use a web site to let customers purchase and set up a mobile broadband plan on a computer that is running Windows 8, Windows 8.1, or Windows 10.

For more info about mobile broadband in Windows 8, Windows 8.1, and Windows 10, see [Overview of mobile broadband](overview-of-mobile-broadband.md).

We recommend that you develop and use a mobile broadband app as it provides the most flexibility and creates the most integrated experience. However, in a few plan purchase and setup scenarios, a mobile broadband app might not always be installed and available for use. For these scenarios, Windows 8, Windows 8.1, and Windows 10 include support to automatically open a mobile broadband web site that is hosted by you and provides the experiences that are required to complete these scenarios.

## <span id="keyscen"></span><span id="KEYSCEN"></span>Key scenarios that require a mobile broadband web site


The following scenarios require a mobile broadband web site:

-   [First use of a USB modem](#firstusb)

-   [First use of a SIM together with an embedded modem](#firstsimusb)

-   [Plan renewal when the app has been uninstalled](#renewunin)

### <span id="firstusb"></span><span id="FIRSTUSB"></span>First use of a USB modem

A user starts with a Windows 8, Windows 8.1, or Windows 10-certified mobile broadband USB modem that does not have an active associated data plan. The user connects the USB modem to a Windows 8, Windows 8.1, or Windows 10 computer for the first time, and the mobile broadband class driver is automatically installed for the device. The user opens Windows Connection Manager and chooses to connect to the mobile broadband network.

As part of the connection process, Windows determines that the mobile broadband network does not provide Internet access because no active data plan is associated with the device. Normally, Windows opens the mobile broadband app so that the app can provide an option to purchase a data plan or otherwise enable Internet access. However, because the USB modem was just installed, the mobile broadband app is not yet installed on the computer.

In this case, Windows opens a web site provided by you. This web site provides the ability to purchase a data plan or otherwise enable Internet access. After the experience is complete, a data plan is associated with the USB modem and the computer is granted Internet access on the mobile broadband network.

### <span id="firstsimusb"></span><span id="FIRSTSIMUSB"></span>First use of a SIM with an embedded modem

A user starts with a SIM that does not have an active associated data plan. The user inserts the SIM into a Windows 8, Windows 8.1, or Windows 10 computer that has an embedded mobile broadband modem. The user opens Windows Connection Manager and chooses to connect to the mobile broadband network.

As part of the connection process, Windows determines that the mobile broadband network does not provide Internet access because no active data plan is associated with the SIM. Normally, Windows opens the mobile broadband app so that the app can provide an option to purchase a data plan or otherwise enable Internet access. However, because the SIM was just inserted, the mobile broadband app is not yet installed on the computer.

In this case, Windows opens a web site provided by you. This web site provides the ability to purchase a data plan or otherwise enable Internet access. After the experience is complete, a data plan is associated with the SIM and the computer is granted Internet access on the mobile broadband network.

### <span id="renewunin"></span><span id="RENEWUNIN"></span>Plan renewal when the app has been uninstalled

A user has been regularly using mobile broadband on a Windows 8, Windows 8.1, or Windows 10 computer. At some point, the user uninstalled the mobile broadband app and the data plan expired because of an expiration date or data usage. The user opens Windows Connection Manager and chooses to connect to the mobile broadband network.

As part of the connection process, Windows determines that the mobile broadband network does not provide Internet access because an active data plan is no longer associated with the device.

Because Windows cannot start the uninstalled app, Windows opens a web site that is provided by you. On this web site, provide an experience to renew the user’s data plan or otherwise enable Internet access. After the experience is complete, a data plan is again associated with the user’s device and the computer is granted Internet access on the mobile broadband network.

## <span id="How_to_enable_key_scenarios"></span><span id="how_to_enable_key_scenarios"></span><span id="HOW_TO_ENABLE_KEY_SCENARIOS"></span>How to enable key scenarios


Use the following guidelines to help you enable these key scenarios.

### <span id="enablesimp"></span><span id="ENABLESIMP"></span>Enable a simple connect experience

You must provide a minimal amount of data to include in the Windows 8, Windows 8.1, or Windows 10 APN database. For more info about the Windows APN database, see [APN database overview](apn-database-overview.md).

You must provide the following information to include in the APN database:

-   For Windows to connect to a mobile broadband network without requiring the user to input an APN or access string, you must provide the APNs and/or access strings.

-   For Windows to automatically open a mobile broadband web site when it detects no Internet connectivity, you must provide the URL of the web site.

### <span id="detect"></span><span id="DETECT"></span>Detect Internet access

When Windows first connects to a network to determine Internet connectivity, it performs various network tests. The destination site for these tests is msftncsi.com, which is a reserved domain that is used exclusively for connectivity testing.

To avoid false positives or false negatives, your network must allow access to www.msftncsi.com only when a user has general Internet access. A user who is connected to your network without having an active data plan must not have access to www.msftncsi.com.

### <span id="webaccess"></span><span id="WEBACCESS"></span>Web site access

A mobile operator typically restricts the network access of a user who does not have active data plan by using one of two methods:

-   Keep the user on the same APN, but block access to all network destinations except for the minimal set of servers that are required for plan purchase and activation. This implementation is also known as a “walled garden.”

-   Transition the user to a purchase APN that never provides Internet access, but provides access to the set of servers that are required for plan purchase and activation.

A user who does not have an active data plan must be able to access the mobile broadband web site by using one of these methods. Additionally, the user must be able to access the web site through the Internet by using an HTTPS connection.

### <span id="devinf"></span><span id="DEVINF"></span>Device information

When Windows uses the mobile operator’s URL (AccountExperienceURL attribute in the [Operator](operator.md) element) from the APN Database, Windows provides the device information that is required to complete activation to the mobile broadband web site. This device information is passed to the web site as parameters of the HTTPS request.

The format of the URL is **https://Operator URL\[?propN=valN\[&propN=valN\]\*\]**, where:

-   **Operator URL** URL provided by you and stored in the APN Database

-   **propN** A property name.

-   **valN** The corresponding value to the propery name.

The following table lists the properties that can be included. If a property value is not provided by the mobile broadband device, that property is not included.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property name</th>
<th>Property value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SubId</p></td>
<td><p>Subscriber ID</p>
<ul>
<li><p>For GSM devices: IMSI (up to 15 digits)</p></li>
<li><p>For CDMA devices: MIN or MIN(IRM) (10 digits)</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>DevId</p></td>
<td><p>Device ID</p>
<ul>
<li><p>For GSM devices: IMEI (up to 15 digits)</p></li>
<li><p>For CDMA devices: ESN (11 digits) or MEID (17 digits)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>IccId</p></td>
<td><p>SIM ICCID (19-20 digits)</p></td>
</tr>
</tbody>
</table>

 

### <span id="Configure_the_computer"></span><span id="configure_the_computer"></span><span id="CONFIGURE_THE_COMPUTER"></span>Configure the computer

After a user has purchased a data plan or otherwise activated the mobile broadband device by using a web site, it might be useful to make the following configuration changes to the computer:

-   Define mobile broadband connection profiles

-   Provide account data

-   Define Wi-Fi hotspot connection profiles

-   Instruct the computer to reconnect the mobile broadband device

The same account provisioning metadata that can be applied to a computer by using a mobile broadband app can also be applied by a mobile broadband website. In the web page’s JavaScript, check for the availability of the [**window.external.msProvisionNetworks**](https://msdn.microsoft.com/library/dn529170) method. If it is present, the browser can transfer account provisioning metadata to Windows.

For more info about account provisioning metadata, see [Account provisioning](account-provisioning.md).

**Note**  
Account provisioning metadata must be signed with an extended validation (EV) certificate when provided by the web site.

 

 

 





